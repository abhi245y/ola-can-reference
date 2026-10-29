import copy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from catalog import decode, load
from validate import validate


class ReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = load(ROOT / "catalog/gen1/hvdp-5.0.0.json")

    def values(self, number, payload):
        return {s["name"]: s for s in decode(self.profile, number, bytes.fromhex(payload))["signals"]}

    def test_seed_integrity(self):
        self.assertEqual(validate(self.profile), [])
        self.assertEqual(len(self.profile["frames"]), 99)
        self.assertEqual(sum("headunit_rx" in f["directions"] for f in self.profile["frames"]), 77)
        self.assertEqual(sum("headunit_tx" in f["directions"] for f in self.profile["frames"]), 20)

    def test_display_values(self):
        self.assertEqual(self.values(0x354, "2F00000000000000")["displayed_speed"]["value"], 47)
        self.assertEqual(self.values(0x352, "4600000000000000")["displayed_soc"]["value"], 70)

    def test_scaled_battery_current(self):
        self.assertEqual(self.values(0x140, "0000000030750000")["battery_current"]["value"], 0)

    def test_unit_interpretation_is_separate_from_layout(self):
        speed = self.values(0x354, "2F00000000000000")["displayed_speed"]
        self.assertEqual(speed["confidence"], "static_source")
        self.assertEqual(speed["unit_confidence"], "inferred")
        odometer = self.values(0x356, "E803000000000000")["odometer_meters"]
        self.assertEqual(odometer["value"], 1000)
        self.assertEqual(odometer["unit_confidence"], "static_source")

    def test_power_button_not_voltage(self):
        result = self.values(0x153, "0001000000000000")["power_button_status"]
        self.assertEqual(result["label"], "Normal_Press")
        self.assertIsNone(result["unit"])

    def test_lock_and_drive_enums(self):
        self.assertEqual(self.values(0x144, "0100000000000000")["bcm_lock_state"]["label"], "Vehicle_Unlocked")
        self.assertEqual(self.values(0x15B, "0200000000000000")["requested_drive_mode"]["label"], "NORMAL")
        self.assertIsNone(self.values(0x144, "0700000000000000")["bcm_lock_state"]["label"])

    def test_terminal_enum_entries_not_dropped(self):
        for name, count, last in [("CommandFromHMI", 107, "DIY_mode_Disable"),
                                  ("CommandFromApp", 22, "FMB_SPEAKER_ENABLE"),
                                  ("CommandFromKrutrim", 14, "TURN_ON_ECO_MODE"),
                                  ("CommandFromVehicle", 217, None)]:
            values = self.profile["enums"][name]["values"]
            self.assertEqual(len(values), count)
            if last:
                self.assertEqual(values[-1], {"value": count - 1, "name": last})
        self.assertEqual(self.values(0x6BC, "6A00000000000000")["hmi_command"]["label"], "DIY_mode_Disable")
        self.assertEqual(self.values(0x65A, "0D00000000000000")["voice_command"]["label"], "TURN_ON_ECO_MODE")

    def test_imu_is_integer_not_ieee754(self):
        values = self.values(0x64D, "2A080000D0070000")
        self.assertEqual(values["accelerometer_z_raw"]["value"], 90)
        self.assertEqual(values["gyrometer_z_raw"]["value"], 0)
        self.assertIsNone(values["accelerometer_z_raw"]["unit"])

    def test_unknown_short_and_unsupported_frames(self):
        for number, payload in [(0x143, bytes(8)), (0x313, bytes(2)), (0x6BC, bytes(1)),
                                (0x800, bytes(8)), (0x354, bytes(9)), (0x354, b""), (0x7FF, bytes(8))]:
            with self.assertRaises(ValueError):
                decode(self.profile, number, payload)

    def test_duplicate_or_mismatched_ids_rejected(self):
        bad = copy.deepcopy(self.profile)
        bad["frames"].append(copy.deepcopy(bad["frames"][0]))
        self.assertTrue(any("duplicate frame" in e for e in validate(bad)))
        bad = copy.deepcopy(self.profile)
        bad["frames"][0]["decimal_id"] += 1
        self.assertTrue(any("must agree" in e for e in validate(bad)))

    def test_overlapping_and_unsupported_fields_rejected(self):
        bad = copy.deepcopy(self.profile)
        frame = next(f for f in bad["frames"] if f["signals"])
        duplicate = copy.deepcopy(frame["signals"][0])
        duplicate["name"] += "_duplicate"
        frame["signals"].append(duplicate)
        self.assertTrue(any("overlapping" in e for e in validate(bad)))
        frame["signals"][0]["byte_order"] = "big_endian"
        self.assertTrue(any("little endian" in e for e in validate(bad)))

    def test_callback_summary_cannot_validate_raw_frames(self):
        bad = copy.deepcopy(self.profile)
        frame = bad["frames"][0]
        frame["raw_runtime_validation"] = "correlated"
        frame["runtime_observations"] = ["observations/gen1/2026-10-30-unlock-drive.json"]
        self.assertTrue(any("raw-frame evidence" in e for e in validate(bad)))

    def test_source_identity_and_bounds_required(self):
        bad = copy.deepcopy(self.profile)
        first = next(iter(bad["evidence"].values()))
        first["source_sha256"] = "missing"
        first["path"] = "/private/decompiled/source.java"
        frame = next(f for f in bad["frames"] if f["signals"])
        frame["signals"][0]["start_bit"] = 64
        errors = validate(bad)
        self.assertTrue(any("SHA256" in e for e in errors))
        self.assertTrue(any("portable" in e for e in errors))
        self.assertTrue(any("bits must fit" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
