# gen1-hvdp-5.0.0: enum reference

Generated from canonical JSON. These are version-specific source ordinals, not a cross-firmware contract.

## CommandFromHMI

107 entries; evidence `S0255`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/CommandFromHMI.java:7`; SHA256 `916bad8fe6150c229a4a7e559800feba04ab5ee3555d2d4656299e39e60f8d82`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | No_Command |
| 1 | 0x01 | Lock_with_Steering |
| 2 | 0x02 | Lock_without_Steering |
| 3 | 0x03 | Seat_Unlock_Cmd |
| 4 | 0x04 | Reverse_mode_activated |
| 5 | 0x05 | Headlight_Turn_ON_Request |
| 6 | 0x06 | ECO_Mode_Rejected_by_User |
| 7 | 0x07 | ECO_Mode_Accepted_by_User |
| 8 | 0x08 | Vehicle_Shutdown_is_Rejected_by_User |
| 9 | 0x09 | ALARM_Turn_Off_Request |
| 10 | 0x0A | Headlight_Turn_OFF_Request |
| 11 | 0x0B | Accepted_Get_Home_Request |
| 12 | 0x0C | Rejected_Get_Home_Request |
| 13 | 0x0D | Stop_Charge |
| 14 | 0x0E | Scooter_Reboot |
| 15 | 0x0F | OTA_Installation_Started |
| 16 | 0x10 | OTA_Installation_in_Progress |
| 17 | 0x11 | OTA_Installation_Complete |
| 18 | 0x12 | MCU_Reboot |
| 19 | 0x13 | HU_Reboot |
| 20 | 0x14 | Passcode_ACK |
| 21 | 0x15 | TripoMeter_Reset_Successfull |
| 22 | 0x16 | CTA_LOCK |
| 23 | 0x17 | CTA_UNLOCK |
| 24 | 0x18 | CTA_IGNORE |
| 25 | 0x19 | PASSCODE_AUTH |
| 26 | 0x1A | High_Beam_ON |
| 27 | 0x1B | High_Beam_OFF |
| 28 | 0x1C | Low_Beam_ON |
| 29 | 0x1D | Low_Beam_OFF |
| 30 | 0x1E | Rear_Light_ON |
| 31 | 0x1F | Rear_Light_OFF |
| 32 | 0x20 | Left_Indicator_ON |
| 33 | 0x21 | Left_Indicator_OFF |
| 34 | 0x22 | Right_Indicator_ON |
| 35 | 0x23 | Right_Indicator_OFF |
| 36 | 0x24 | Front_DRL_ON |
| 37 | 0x25 | Front_DRL_OFF |
| 38 | 0x26 | AUTO_HEADLIGHT_SUNRISE_EN |
| 39 | 0x27 | Auto_HEAD_LIGHT_SUNSET_EN |
| 40 | 0x28 | Auto_Head_Light_Reserved |
| 41 | 0x29 | Regen_Type_Default_SELECTED |
| 42 | 0x2A | Regen_Type_City_Ride_En_Selected |
| 43 | 0x2B | Regen_Type_Highway_Glide_En_Selected |
| 44 | 0x2C | Smart_Head_Light_Default_Selected |
| 45 | 0x2D | Smart_Head_Light_Low_Beam_En_Selected |
| 46 | 0x2E | Smart_Head_Light_High_Beam_En_Selected |
| 47 | 0x2F | Smart_Head_Light_Smart_Light_En_Selected |
| 48 | 0x30 | Boost_Mode_Enable_Selected |
| 49 | 0x31 | Boost_Mode_Disable_Selected |
| 50 | 0x32 | Accident_Detection_Enable_Selected |
| 51 | 0x33 | Accident_Detection_Disable_Selected |
| 52 | 0x34 | Tow_Tamper_Detection_Enable_Selected |
| 53 | 0x35 | Tow_Tamper_Detection_Disable_Selected |
| 54 | 0x36 | Proximity_Lock_Unlock_Enable_Selected |
| 55 | 0x37 | Proximity_Lock_Unlock_Disable_Selected |
| 56 | 0x38 | Smart_DRL_Light_Enable_Selected |
| 57 | 0x39 | Smart_DRL_Light_Disable_Selected |
| 58 | 0x3A | Auto_Head_Light_Handling_Enable_Selected |
| 59 | 0x3B | Auto_Head_Light_Handling_Disable_Selected |
| 60 | 0x3C | Hazard_Light_Feature_Enable_Selected |
| 61 | 0x3D | Hazard_Light_Feature_Disable_Selected |
| 62 | 0x3E | Auto_Indicator_Turn_off_Feature_Enable_Selected |
| 63 | 0x3F | Auto_Indicator_Turn_off_Feature_Disable_Selected |
| 64 | 0x40 | Motor_Cutoff_Delay_Selected_Enable_Selected |
| 65 | 0x41 | Motor_Cutoff_Delay_Selected_Disable_Selected |
| 66 | 0x42 | Hill_Hold_Request_Enable_Selected |
| 67 | 0x43 | Hill_Hold_Request_Disable_Selected |
| 68 | 0x44 | VACATION_MODE_ON |
| 69 | 0x45 | VACATION_MODE_OFF |
| 70 | 0x46 | NEED_HELP |
| 71 | 0x47 | I_AM_SAFE |
| 72 | 0x48 | DELETE_PROFILE |
| 73 | 0x49 | USER_CALIBRATION_REQUEST |
| 74 | 0x4A | Hazard_Light_Turn_ON |
| 75 | 0x4B | Hazard_Light_Turn_OFF |
| 76 | 0x4C | HMI_Alarm_ignore_True |
| 77 | 0x4D | Tow_Theft_Low_Sensitivity |
| 78 | 0x4E | Tow_Theft_High_Sensitivity |
| 79 | 0x4F | HMI_Alarm_ignore_False |
| 80 | 0x50 | Exit_Diagnostic_Mode |
| 81 | 0x51 | Version_Mismatched |
| 82 | 0x52 | Smart_Head_Light_SMART_LIGHT_EN_Deselected |
| 83 | 0x53 | Ride_Now |
| 84 | 0x54 | Lock_Now |
| 85 | 0x55 | TMH_Lights_Enable |
| 86 | 0x56 | TMH_Lights_Disabled |
| 87 | 0x57 | Alarm_unlock_Now |
| 88 | 0x58 | Drive_acess_revoked_enable |
| 89 | 0x59 | Drive_acess_revoked_disable |
| 90 | 0x5A | SIDE_STAND_DISABLE |
| 91 | 0x5B | SIDE_STAND_ENABLE |
| 92 | 0x5C | Brake_Switch_Fault_Deactivate |
| 93 | 0x5D | Brake_Switch_Fault_Activate |
| 94 | 0x5E | AI_Ind_OFF |
| 95 | 0x5F | Brk_Snsr_Fail_detect_AI |
| 96 | 0x60 | Brk_Snsr_Fail_clear_AI |
| 97 | 0x61 | OTA_MCU_Reset |
| 98 | 0x62 | HMI_Wakeup_pass |
| 99 | 0x63 | Restrict_Drive |
| 100 | 0x64 | SOS_Enable |
| 101 | 0x65 | SOS_Disable |
| 102 | 0x66 | BD_Drv_Prk_Ack |
| 103 | 0x67 | Park_Assist_Enabled |
| 104 | 0x68 | Park_Assist_Disabled |
| 105 | 0x69 | DIY_mode_Enable |
| 106 | 0x6A | DIY_mode_Disable |

## CommandFromApp

22 entries; evidence `S0256`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/CommandFromApp.java:7`; SHA256 `367067e72cebfa6bbeb4bc152e456fdf6eb7f004ed6a98198bcd7a75fc9ebf8a`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | No_Command |
| 1 | 0x01 | Vehicle_UNLOCK |
| 2 | 0x02 | Vehicle_LOCK |
| 3 | 0x03 | Vehicle_HeadLamp_ON |
| 4 | 0x04 | Vehicle_HeadLamps_OFF |
| 5 | 0x05 | Trunk_Open |
| 6 | 0x06 | Vehicle_Remote_Immobilize_ON |
| 7 | 0x07 | Vehicle_Remote_Immobilize_OFF |
| 8 | 0x08 | Lock_without_Steering |
| 9 | 0x09 | Reserved |
| 10 | 0x0A | Diagnostic_Request |
| 11 | 0x0B | Find_My_Bike_Light_Turn_ON_Request |
| 12 | 0x0C | Find_My_Bike_Sound_Turn_ON_Request |
| 13 | 0x0D | PRNTCNTRL_SPORT_ACS_REVOKED |
| 14 | 0x0E | PRNTCNTRL_HYPER_ACS_REVOKED |
| 15 | 0x0F | PRNTCNTRL_ACS_RESET |
| 16 | 0x10 | Alarm_unlock_Now |
| 17 | 0x11 | Accident_Detection_Enable_Selected |
| 18 | 0x12 | Accident_Detection_Disable_Selected |
| 19 | 0x13 | Tow_Tamper_Detection_Enable_Selected |
| 20 | 0x14 | Tow_Tamper_Detection_Disable_Selected |
| 21 | 0x15 | FMB_SPEAKER_ENABLE |

## CommandFromKrutrim

14 entries; evidence `S0257`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/CommandFromKrutrim.java:7`; SHA256 `548f561080e6e7c9ca6fabafda16cd272e2da7a827f084e71944b880fa9940e0`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | SNA |
| 1 | 0x01 | LockTheScooter |
| 2 | 0x02 | HighBeamON |
| 3 | 0x03 | HighBeamOFF |
| 4 | 0x04 | RightIndicatorON |
| 5 | 0x05 | RightIndicatorOFF |
| 6 | 0x06 | LeftIndicatorON |
| 7 | 0x07 | LeftIndicatorOFF |
| 8 | 0x08 | IncreaseVolume |
| 9 | 0x09 | DecreaseVolume |
| 10 | 0x0A | TURN_ON_NORMAL_MODE |
| 11 | 0x0B | TURN_ON_SPORT_MODE |
| 12 | 0x0C | TURN_ON_HYPER_MODE |
| 13 | 0x0D | TURN_ON_ECO_MODE |

## CommandFromVehicle

217 entries; evidence `S0258`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/CommandFromVehicle.java:7`; SHA256 `b195043677c88f80ae92166e04d0dd51e983489c487df26cca9bdb3bc2c858d3`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | NO_COMMAND |
| 1 | 0x01 | ACTIVATE_PASSCODE_WINDOW |
| 2 | 0x02 | DERATE_AFE_FAULT_CCS |
| 3 | 0x03 | DERATE_PDU_COOLDOWN_WAIT |
| 4 | 0x04 | DERATE_CHARGE_TO_RIDE |
| 5 | 0x05 | DISABLED_PDU_MODE_SWITCH |
| 6 | 0x06 | DISABLED_HIGHER_MODE |
| 7 | 0x07 | DERATE_AFE_FAULT |
| 8 | 0x08 | RERATING_REVIVAL_PDU |
| 9 | 0x09 | DERATE_PDU_TEMP_ERROR_START |
| 10 | 0x0A | DERATE_PDU_TEMP_ERROR_INPGRS |
| 11 | 0x0B | DERATE_SOC_3_WARNING |
| 12 | 0x0C | DERATE_SOC_3 |
| 13 | 0x0D | DERATE_PDU_TEMP_WARN_START |
| 14 | 0x0E | DERATE_PDU_TEMP_WARN_INPGRS |
| 15 | 0x0F | RERATING_HIGHER_MODE |
| 16 | 0x10 | DERATE_SOC_15_WARNING |
| 17 | 0x11 | TYPE3_ERROR_SET |
| 18 | 0x12 | TYPE3_ERROR_CLEAR |
| 19 | 0x13 | TYPE2_ERROR_SET |
| 20 | 0x14 | TYPE2_ERROR_CLEAR |
| 21 | 0x15 | TYPE1_ERROR_SET |
| 22 | 0x16 | TYPE1_ERROR_CLEAR |
| 23 | 0x17 | TRUNK_OPEN_NOTIFICATION |
| 24 | 0x18 | TRUNK_CLOSE_NOTIFCATION |
| 25 | 0x19 | ENTERING_INTO_DEEP_SLEEP |
| 26 | 0x1A | TEST_01 |
| 27 | 0x1B | TEST_02 |
| 28 | 0x1C | TEST_03 |
| 29 | 0x1D | TEST_04 |
| 30 | 0x1E | TEST_05 |
| 31 | 0x1F | DERATE_SOC_15 |
| 32 | 0x20 | DERATE_SOC_20_WARNING |
| 33 | 0x21 | DERATE_SOC_20 |
| 34 | 0x22 | GENERAL_LOW_BATTERY |
| 35 | 0x23 | DERATE_OVER_TEMP_WARN_START |
| 36 | 0x24 | DERATE_OVER_TEMP_WARN_INPGRS |
| 37 | 0x25 | DERATE_OVER_TEMP_ERR_START |
| 38 | 0x26 | DERATE_OVER_TEMP_ERR_INPGRS |
| 39 | 0x27 | DERATE_TEMP_COOLDOWN_WAIT |
| 40 | 0x28 | DISABLED_OT_MODE_SWITCH |
| 41 | 0x29 | RERATING_REVIVAL_OT |
| 42 | 0x2A | CHARGE_NOT_HAPPENING |
| 43 | 0x2B | DERATE_MOT_TEMP_ERROR_START |
| 44 | 0x2C | DERATE_MCU_TEMP_ERROR_START |
| 45 | 0x2D | DERATE_MOT_COOLDOWN_WAIT |
| 46 | 0x2E | DERATE_MCU_COOLDOWN_WAIT |
| 47 | 0x2F | DISABLED_MOT_MODE_SWITCH |
| 48 | 0x30 | DISABLED_MCU_MODE_SWITCH |
| 49 | 0x31 | DERATE_MOT_TEMP_WARN_START |
| 50 | 0x32 | DERATE_MCU_TEMP_WARN_START |
| 51 | 0x33 | RERATING_HIGHER_MODE_OT |
| 52 | 0x34 | RERATING_HIGHER_MODE_MOT |
| 53 | 0x35 | RERATING_HIGHER_MODE_MCU |
| 54 | 0x36 | DERATE_MOT_CHILL_WARN |
| 55 | 0x37 | DERATE_MCU_CHILL_WARN |
| 56 | 0x38 | RERATING_REVIVAL_MOT |
| 57 | 0x39 | RERATING_REVIVAL_MCU |
| 58 | 0x3A | DERATE_CHRG_OVER_TEMP_WARN |
| 59 | 0x3B | CLOSE_SIDE_STAND_TO_DRIVE |
| 60 | 0x3C | SIDE_STAND_OPEN |
| 61 | 0x3D | APPLY_SIDE_STAND_TO_LOCK |
| 62 | 0x3E | HOLD_BRK_SSB_TO_DRV |
| 63 | 0x3F | BATT_TEMP_OOR |
| 64 | 0x40 | BATT_TEMP_OOR_ALL |
| 65 | 0x41 | CURR_SNSR_FAIL_OC_SC |
| 66 | 0x42 | VLT_SNSR_FAIL |
| 67 | 0x43 | VLT_SNSR_FAIL_ALL |
| 68 | 0x44 | BATT_TEMP_SNSR_FAIL |
| 69 | 0x45 | BATT_TEMP_SNSR_FAIL_ALL |
| 70 | 0x46 | OVER_CURR_CHRG_WARN |
| 71 | 0x47 | MCU_GRADE2_ECO |
| 72 | 0x48 | MCU_GRADE2_RESTART |
| 73 | 0x49 | MCU_GRADE2_CONTACT_CS |
| 74 | 0x4A | MCU_GRADE3_PARK |
| 75 | 0x4B | MCU_GRADE3_RESTART |
| 76 | 0x4C | MCU_GRADE3_CONTACT_CS |
| 77 | 0x4D | BATT_SNSR_FAIL_CONTACT_CS |
| 78 | 0x4E | BATT_TEMP_OOR_CHRG |
| 79 | 0x4F | BATT_TEMP_OOR_ALL_CHRG |
| 80 | 0x50 | VLT_SNSR_FAIL_CHRG |
| 81 | 0x51 | VLT_SNSR_FAIL_ALL_CHRG |
| 82 | 0x52 | BATT_TEMP_SNSR_FAIL_CHRG |
| 83 | 0x53 | BATT_TEMP_SNSR_FAIL_ALL_CHRG |
| 84 | 0x54 | CHARGE_BATT_LOWTEMP_WARN |
| 85 | 0x55 | DERATE_LOW_TEMP_WARN_START |
| 86 | 0x56 | DERATE_LOW_TEMP_ERR_START |
| 87 | 0x57 | PDU_WARN_CHRG |
| 88 | 0x58 | MCU_GRADE2_DISABLED_HIGHER |
| 89 | 0x59 | INITIATE_TRIPOMETER_RESET |
| 90 | 0x5A | INITIATE_NAVIGATION_PING_TEST |
| 91 | 0x5B | CELL_DIP_ERR_GRADE2 |
| 92 | 0x5C | SPIKE_ERR_GRADE2 |
| 93 | 0x5D | CAN_FAIL |
| 94 | 0x5E | RERATE_HIGHER_MODE_DRV_TEMP |
| 95 | 0x5F | RERATE_HIGHER_MODE_CHRG_TEMP |
| 96 | 0x60 | RERATE_HIGHER_MODE_CELL_DIP |
| 97 | 0x61 | RERATE_HIGHER_MODE_SPIK_ERR |
| 98 | 0x62 | RERATING_REVIVAL_CAN |
| 99 | 0x63 | SLP_TEMP_RISE_GRADE2 |
| 100 | 0x64 | RERATE_HIGHER_MODE_SLP_OT |
| 101 | 0x65 | DRV_TEMP_RISE_GRADE2 |
| 102 | 0x66 | CHRG_TEMP_RISE_GRADE2 |
| 103 | 0x67 | DISABLED_CELLDIP_MODE_SWITCH |
| 104 | 0x68 | DISABLED_SPIKE_MODE_SWITCH |
| 105 | 0x69 | DISABLED_TEMP_MODE_RISE_SWITCH |
| 106 | 0x6A | CAN_FAIL_WAIT_CONTACT_CS |
| 107 | 0x6B | BMS_GRADE4_CUTOFF |
| 108 | 0x6C | CNTCR_TOGGLING_ISSUE |
| 109 | 0x6D | OVR_CHRG_PROTECTION |
| 110 | 0x6E | LOCK_IN_PRGS |
| 111 | 0x6F | CHRG_CMPLT_UNPLG_CHRGR |
| 112 | 0x70 | STOP_CHRG_OVER_TEMP_ERR |
| 113 | 0x71 | NORMAL_MODE_AVAILABLE |
| 114 | 0x72 | VEHICLE_FALL_DETECTED |
| 115 | 0x73 | VEHICLE_FALL_RECOVERED |
| 116 | 0x74 | VEHICLE_FALL_ALARM_IGNORED |
| 117 | 0x75 | USER_CALIBRATION_SUCCESS |
| 118 | 0x76 | USER_CALIBRATION_FAIL |
| 119 | 0x77 | UNLOCK_FAIL_CTA |
| 120 | 0x78 | LOCK_FAIL_CTA |
| 121 | 0x79 | CHGR_PERMANENT_FAULT |
| 122 | 0x7A | CHGR_TEMPORARY_FAULT |
| 123 | 0x7B | CHGR_PWR_OFF |
| 124 | 0x7C | CHGR_LATCH_NOT_CONED |
| 125 | 0x7D | RID_ACCS_RVKED_PARK_IN_30S |
| 126 | 0x7E | DERATE_THROT_ERROR |
| 127 | 0x7F | DERATE_DRV_FLT |
| 128 | 0x80 | DCHRG_INHBT_ERROR |
| 129 | 0x81 | HILL_HOLD_EXIT_NUDGE |
| 130 | 0x82 | UNPLUG_CHGR_TO_RIDE |
| 131 | 0x83 | SAFE_UNPLUG_HYPER_CHARGER |
| 132 | 0x84 | INITIALIZING_HYPERCHARGER |
| 133 | 0x85 | UNPLUG_HYPER_CHGR_FAULT |
| 134 | 0x86 | HILL_HOLD_USR_DEACT_REQ |
| 135 | 0x87 | ENTERING_VACATION_MODE |
| 136 | 0x88 | EXITING_VACATION_MODE |
| 137 | 0x89 | PLEASE_RELEASE_EMERGENCY_BUTTON_TO_START_CHARGING |
| 138 | 0x8A | ACCS_RVKED_CONTACT_OWNER |
| 139 | 0x8B | CONFIG_MISMATCH |
| 140 | 0x8C | VERSION_MISMATCH |
| 141 | 0x8D | THERMAL_RUNAWAY |
| 142 | 0x8E | DISABLED_SPORTS_MODE_FAULT |
| 143 | 0x8F | DISABLED_SPORTS_MODE_SOC |
| 144 | 0x90 | DISABLED_SPORTS_MODE_TEMP |
| 145 | 0x91 | GEOFEN_ACS_REVOKED |
| 146 | 0x92 | PRNTCNTRL_SPORT_ACS_REVOKED |
| 147 | 0x93 | PRNTCNTRL_HYPER_ACS_REVOKED |
| 148 | 0x94 | PRNTCNTRL_ACS_RESET |
| 149 | 0x95 | VCU_Over_Temp_Grade1 |
| 150 | 0x96 | MCU_Temp_Rise_Grade1 |
| 151 | 0x97 | MOTOR_Temp_Rise_Grade1 |
| 152 | 0x98 | Accident_Detected |
| 153 | 0x99 | TAMPER_PASS_EXIT |
| 154 | 0x9A | LOW_BATTERY_DEACTIVATING_CRUISE |
| 155 | 0x9B | LOW_BATTERY_CANNOT_ENABLE_CRUISE |
| 156 | 0x9C | CRUISE_DEACT_BATT_CURR_SPIKE |
| 157 | 0x9D | CHARGE_BATT_LOWTEMP_ERR |
| 158 | 0x9E | DCDC_LOW_THRESH_REACHED |
| 159 | 0x9F | CHARGING_PAYMENT_DUE |
| 160 | 0xA0 | SideStand_DownWarning |
| 161 | 0xA1 | CAN_FAILURE_CANT_ENABLE_CRUISE |
| 162 | 0xA2 | CAN_COM_FAILURE |
| 163 | 0xA3 | CAN_COM_FAILURE_GRADE3_PRK |
| 164 | 0xA4 | CAN_COM_ERROR_NORMAL |
| 165 | 0xA5 | REDUCED_PERFORMANCE_CANNOT_ENABLE_CRUISE |
| 166 | 0xA6 | THROTTLE_OFFSET_DRV_ERROR |
| 167 | 0xA7 | PDU_WARN_ECO |
| 168 | 0xA8 | PDU_WARN_ECO_CRUISE_FAILURE |
| 169 | 0xA9 | PDU_WARN_ECO_START |
| 170 | 0xAA | RELEASE_THROTTLE_TO_DRIVE |
| 171 | 0xAB | BATT_WARN_ECO |
| 172 | 0xAC | BATT_WARN_ECO_CRUISE_FAILURE |
| 173 | 0xAD | BATT_WARN_ECO_START |
| 174 | 0xAE | USE_ECO_NUDGE |
| 175 | 0xAF | USE_REGEN_NUDGE |
| 176 | 0xB0 | UPGRADE_FOR_BOOSTCHARGER |
| 177 | 0xB1 | UPGRADE_FOR_FASTCHARGER |
| 178 | 0xB2 | UPGRADE_FOR_HILLHOLD |
| 179 | 0xB3 | TECHPACK_AVAILABLE |
| 180 | 0xB4 | NOT_DELIVERED_EXHAUSTED_RANGE |
| 181 | 0xB5 | SCOOTER_NOT_DELIVERED |
| 182 | 0xB6 | IN_SERVICE_RANGE_EXHAUST |
| 183 | 0xB7 | IN_SERVICE |
| 184 | 0xB8 | PARTS_MISMATCHED |
| 185 | 0xB9 | PARTS_MISMATCHED_EXHAUSTED |
| 186 | 0xBA | ACCIDENT_EMERGENCY_WINDOW |
| 187 | 0xBB | ENABLE_RIDE_TO_REVERSE |
| 188 | 0xBC | SOC_DERATION_DRIVE_TO_PARK |
| 189 | 0xBD | SOC_DERATION_UNLOCK |
| 190 | 0xBE | BBW_BRAKE_FAILURE_DRIVE |
| 191 | 0xBF | BBW_BRAKE_FAILURE_PARK |
| 192 | 0xC0 | BBW_BREAKSENSOR_FAULT |
| 193 | 0xC1 | BLE_MAC_GRADE1 |
| 194 | 0xC2 | PM_SCHEME_NOTIF_1 |
| 195 | 0xC3 | PM_SCHEME_NOTIF_2 |
| 196 | 0xC4 | PM_SCHEME_NOTIF_3 |
| 197 | 0xC5 | PM_SCHEME_NOTIF_4 |
| 198 | 0xC6 | PM_SCHEME_NOTIF_5 |
| 199 | 0xC7 | TEST_RIDE |
| 200 | 0xC8 | BRAKE_PRESSED_LMP_WARN |
| 201 | 0xC9 | ENABLE_RIDE_TO_SWITCH_MODE |
| 202 | 0xCA | COME_TO_HALT_TO_TURNOFF |
| 203 | 0xCB | TP_HYPER_NA |
| 204 | 0xCC | TP_SPORT_NA |
| 205 | 0xCD | TP_ECO_NA |
| 206 | 0xCE | TP_REVERSE_NA |
| 207 | 0xCF | TP_CRUISE_NA |
| 208 | 0xD0 | TP_CHARGING_NA |
| 209 | 0xD1 | NOT_DELIVER_PARK_TRANSITION |
| 210 | 0xD2 | JOB_OPEN_PARK_TRANSITION |
| 211 | 0xD3 | JOB_OPEN_RANGE_EXHAUST |
| 212 | 0xD4 | NOT_DELIVERED_RANGE_EXHAUST |
| 213 | 0xD5 | NOT_DELIVER_RESTRICTED_ECO |
| 214 | 0xD6 | NOT_DELIVER_RESTRICTED_NORMAL |
| 215 | 0xD7 | JOB_OPEN_RESTRICTED_ECO |
| 216 | 0xD8 | JOB_OPEN_RESTRICTED_NORMAL |

## DriveModes

12 entries; evidence `S0259`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/DriveModes.java:7`; SHA256 `7789129b8b487f87472ad8f105f33fb27b79c23dc0d6c7280cefffd33daba77e`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | PARK |
| 1 | 0x01 | ECO |
| 2 | 0x02 | NORMAL |
| 3 | 0x03 | SPORT |
| 4 | 0x04 | CUSTOM |
| 5 | 0x05 | REVERSE |
| 6 | 0x06 | LIMPHOME |
| 7 | 0x07 | HYPER |
| 8 | 0x08 | ADAPTIVE_BOOST |
| 9 | 0x09 | SERVICE |
| 10 | 0x0A | PARK_ASSIST |
| 11 | 0x0B | BOOST2 |

## VehicleStates

16 entries; evidence `S0260`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/VehicleStates.java:7`; SHA256 `658b7fd8eee301582f3f26d3a3dd9574c6b25c3cfd510150028b49ae313f2c76`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | SNA |
| 1 | 0x01 | BC_CHARGE_ACTIVE |
| 2 | 0x02 | VACATION |
| 3 | 0x03 | SLEEP |
| 4 | 0x04 | VEHICLE_IDLE |
| 5 | 0x05 | SC_CHARGE_IDLE |
| 6 | 0x06 | SC_CHARGE_FAULT |
| 7 | 0x07 | SC_CHARGE_ACTIVE |
| 8 | 0x08 | FC_CHARGE_IDLE |
| 9 | 0x09 | FC_CHARGE_FAULT |
| 10 | 0x0A | FC_CHARGE_ACTIVE |
| 11 | 0x0B | PARK |
| 12 | 0x0C | DRIVE |
| 13 | 0x0D | ALARM |
| 14 | 0x0E | BC_CHARGE_IDLE |
| 15 | 0x0F | BC_CHARGE_FAULT |

## VehicleLockStateBCM

5 entries; evidence `S0261`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/VehicleLockStateBCM.java:7`; SHA256 `fb2fe16d3e21be39d9d063da9d77401b37c126f99b0eaac65c39d60b471dacc8`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | SNA |
| 1 | 0x01 | Vehicle_Unlocked |
| 2 | 0x02 | Vehicle_Unlock_Fail |
| 3 | 0x03 | Vehicle_Locked |
| 4 | 0x04 | Vehicle_Lock_Fail |

## SomState

7 entries; evidence `S0262`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/SomState.java:7`; SHA256 `7e3f9c0a309130d6bb22cf4e6c2800e201ee98719a122ca46dfd56cc21db429c`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | OFF |
| 1 | 0x01 | BOOTING |
| 2 | 0x02 | SLEEP |
| 3 | 0x03 | STAND_BY |
| 4 | 0x04 | FASTBOOT |
| 5 | 0x05 | KEY_OFF |
| 6 | 0x06 | KEY_ON |

## PowerButtonStatus

4 entries; evidence `S0263`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/PowerButtonStatus.java:7`; SHA256 `d540c4ed1d2df16d42d5a9edbb82e361c64ada8a587c6158af007bb6b468ce29`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | Not_Pressed |
| 1 | 0x01 | Normal_Press |
| 2 | 0x02 | Long_Press |
| 3 | 0x03 | Reserver |

## VehicleSafetyAlerts

13 entries; evidence `S0264`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/VehicleSafetyAlerts.java:7`; SHA256 `bb6b28c72ac2dacb838566576e081cc29eb8eb13b43be618b3cba0d3ce3e33aa`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | No_Command |
| 1 | 0x01 | Battery_Temperature_High_Alert |
| 2 | 0x02 | Battery_Temperature_Very_High_Alert |
| 3 | 0x03 | Battery_Temperature_Low_Alert |
| 4 | 0x04 | Battery_Temperature_Very_Low_Alert |
| 5 | 0x05 | Motor_Temperature_High_Alert |
| 6 | 0x06 | Motor_Temperature_Very_High_Alert |
| 7 | 0x07 | Motor_Temperature_Low_Alert |
| 8 | 0x08 | Motor_Temperature_Very_Low_Alert |
| 9 | 0x09 | Side_Stand_Position_Alert |
| 10 | 0x0A | Steering_Lock_Unlock_Alert |
| 11 | 0x0B | Tamper_Alert |
| 12 | 0x0C | Current_Drive_Mode |

## ChargerDueStatus

4 entries; evidence `S0265`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/ChargerDueStatus.java:7`; SHA256 `2fa85c8e738910a61c72310c983c784930a78e03edd80b4db462eccc519a8759`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | SNA |
| 1 | 0x01 | DUES_PENDING |
| 2 | 0x02 | DUES_PAID |
| 3 | 0x03 | CONNECTION_FAILED |

## MapCommandAck

3 entries; evidence `S0266`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/MapCommandAck.java:7`; SHA256 `1e315f7ced1d64f978b6578e6dafbe36bbd5d25976fb48a28e7c72e9fbdd4466`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | NO_COMMAND |
| 1 | 0x01 | Success |
| 2 | 0x02 | Failure |

## ProximityCommandType

65 entries; evidence `S0267`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/ProximityCommandType.java:8`; SHA256 `3de9cf92c6760c3fbd332e90d347e32586b3763254a4810033cd44e743f204ad`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | UNKNOWN_CMD |
| 1 | 0x01 | PROXIMITY_SOFTWARE_VERSION |
| 2 | 0x02 | MAC_ADDRESS_PROXIMITY_BLE |
| 3 | 0x03 | DEVICE_DISCOVERABLE |
| 4 | 0x04 | DISCONNECT_CURRENT_PHONE |
| 5 | 0x05 | DEVICE_CONNECTABLE_BOUND_DEVICE |
| 6 | 0x06 | CLEAR_ALL_PHONE |
| 7 | 0x07 | NO_OF_PAIRED_PHONE |
| 8 | 0x08 | CURRENT_PHONE_0_MAC |
| 9 | 0x09 | CURRENT_PHONE_1_MAC |
| 10 | 0x0A | CURRENT_PHONE_2_MAC |
| 11 | 0x0B | CURRENT_PHONE_3_MAC |
| 12 | 0x0C | CURRENT_PHONE_4_MAC |
| 13 | 0x0D | SUCESSFUL_BOND_CONNECTION |
| 14 | 0x0E | UNAUTHORIZE_ACCESS_ATTEMP_NO |
| 15 | 0x0F | PROXIMITY_BLE_PAIRING_RESPONSE_FROM_USER |
| 16 | 0x10 | PARTY_MODE |
| 17 | 0x11 | OLAMAPS_ACK |
| 18 | 0x12 | PROFILE_ID |
| 19 | 0x13 | PROXIMITY_FEATURE |
| 20 | 0x14 | DELETE_PROFILE_ID |
| 21 | 0x15 | GET_CURRENT_CONNECTED_PROFILE_ID |
| 22 | 0x16 | HMI_LOGGED_IN_PROFILE_ID |
| 23 | 0x17 | LOCK_UNLOCK_REASON |
| 24 | 0x18 | PROFILEID_BLE_ACK |
| 25 | 0x19 | PAIRING_POPUP_ACK |
| 26 | 0x1A | EXPLICITE_COMMAND_PAIRING |
| 27 | 0x1B | PROXIMITY_PAIRING_ACK |
| 28 | 0x1C | HILL_HOLD_RQST_Enable_Selected |
| 29 | 0x1D | HILL_HOLD_RQST_Disable_Selected |
| 30 | 0x1E | REGEN_TYPE_DEFAULT_Selected |
| 31 | 0x1F | REGEN_TYPE_CITY_RIDE_EN_Selected |
| 32 | 0x20 | REGEN_TYPE_HIGHWAY_GLIDE_EN_Selected |
| 33 | 0x21 | SMART_HEAD_LIGHT_DEFAULT_Selected |
| 34 | 0x22 | SMART_HEAD_LIGHT_LOW_BEAM_EN_Selected |
| 35 | 0x23 | SMART_HEAD_LIGHT_HIGH_BEAM_EN_Selected |
| 36 | 0x24 | SMART_HEAD_LIGHT_SMART_LIGHT_EN_Selected |
| 37 | 0x25 | BOOST_MODE_Enable_Selected |
| 38 | 0x26 | BOOST_MODE_Disable_Selected |
| 39 | 0x27 | FALL_DETECTION_Enable_Selected |
| 40 | 0x28 | FALL_DETECTION_Disable_Selected |
| 41 | 0x29 | TOW_TAMPER_DETECTION_Enable_Selected |
| 42 | 0x2A | TOW_TAMPER_DETECTION_Disable_Selected |
| 43 | 0x2B | PROXIMITY_LOCK_UNLOCK_Enable_Selected |
| 44 | 0x2C | PROXIMITY_LOCK_UNLOCK_Disable_Selected |
| 45 | 0x2D | SMART_DRL_LIGHT_Enable_Selected |
| 46 | 0x2E | SMART_DRL_LIGHT_Disable_Selected |
| 47 | 0x2F | AUTO_HEADLIGHT_HANDLING_Enable_Selected |
| 48 | 0x30 | AUTO_HEADLIGHT_HANDLING_Disable_Selected |
| 49 | 0x31 | HAZARD_LIGHT_FEATURE_Enable_Selected |
| 50 | 0x32 | HAZARD_LIGHT_FEATURE_Disable_Selected |
| 51 | 0x33 | AUTO_INDICATOR_TURN_OFF_FEATURE_Enable_Selected |
| 52 | 0x34 | AUTO_INDICATOR_TURN_OFF_FEATURE_Disable_Selected |
| 53 | 0x35 | MOTOR_CUTOFF_DELAY_Enable_Selected |
| 54 | 0x36 | MOTOR_CUTOFF_DELAY_Disable_Selected |
| 55 | 0x37 | Hill_Hold_Request_Enable_Selected |
| 56 | 0x38 | Hill_Hold_Request_Disable_Selected |
| 57 | 0x39 | Vacation_Mode_ON |
| 58 | 0x3A | Vacation_Mode_OFF |
| 59 | 0x3B | Need_Help |
| 60 | 0x3C | I_am_Safe |
| 61 | 0x3D | Delete_Profile |
| 62 | 0x3E | User_Calibration_Request |
| 63 | 0x3F | TMH_Lights_Enable |
| 64 | 0x40 | TMH_Lights_Disabled |

## ChargingModes

7 entries; evidence `S0268`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/ChargingModes.java:7`; SHA256 `3c5d279afb0ff60f2c0da2dff4548a5fe29d9787ed1aa014bad537e49b7384bb`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | SNA |
| 1 | 0x01 | Idle |
| 2 | 0x02 | Safe |
| 3 | 0x03 | Slow_Charge |
| 4 | 0x04 | Fast_Charge |
| 5 | 0x05 | Discharge |
| 6 | 0x06 | Boost_Charge |

## ECUModes

8 entries; evidence `S0269`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/ECUModes.java:7`; SHA256 `3316a672e70aa38506e51bc48be1cc8d36103db56e15069537953d78032d8384`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | SNA |
| 1 | 0x01 | ECU_POWERUP |
| 2 | 0x02 | DIAGNOSTIC |
| 3 | 0x03 | AUX_BATTERY_CHARGE |
| 4 | 0x04 | DRIVE_NORMAL |
| 5 | 0x05 | LIMPHOME |
| 6 | 0x06 | DRIVE_FAULT |
| 7 | 0x07 | Reserved |

## FallDetection

4 entries; evidence `S0270`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/FallDetection.java:7`; SHA256 `5c0970f0e23d335d314941fce0fbc87ce0e160761f042f9543592f406380f95a`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | SNA |
| 1 | 0x01 | ACTIVE |
| 2 | 0x02 | INACTIVE |
| 3 | 0x03 | RECOVERED |

## TowTheftDetection

3 entries; evidence `S0271`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/TowTheftDetection.java:7`; SHA256 `0319e0905ed0e6824fb4edce9ac185641bce5148b2f4b19f7d7330923aec0d0b`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | SNA |
| 1 | 0x01 | ACTIVE |
| 2 | 0x02 | INACTIVE |

## RegenAvailability

4 entries; evidence `S0272`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/RegenAvailability.java:7`; SHA256 `2cde0155460237e54091c875eeba6cf8347316a590de648519f7bb065b557a49`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | REGEN_NOT_AVAILABLE |
| 1 | 0x01 | REGEN_AVAILABLE |
| 2 | 0x02 | REGEN_NOT_AVAILABLE_THROTTLE |
| 3 | 0x03 | Reserved |

## HillHoldStatus

7 entries; evidence `S0273`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/HillHoldStatus.java:7`; SHA256 `3e016d4cb475190afa34407d6e5ff62f4e792fea3113e5afcff339dfb7a1b040`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | SNA |
| 1 | 0x01 | UNAVAILABLE |
| 2 | 0x02 | ACTIVE |
| 3 | 0x03 | NOT_ACTIVE |
| 4 | 0x04 | ABT_TO_DEACTIVATE |
| 5 | 0x05 | ABT_TO_ACTIVATE |
| 6 | 0x06 | HH_ACTIVATED |

## RegenStatus

5 entries; evidence `S0274`.
Source: `HVDP/sources/com/olaelectric/vehicleinterface/RegenStatus.java:7`; SHA256 `e79e16fbed1eb566503b83633d43baa888c99f7dbbdebd560e25e142c9379964`.

| Value | Hex | Source name |
|---:|---|---|
| 0 | 0x00 | Not_Active |
| 1 | 0x01 | Coast_Regen |
| 2 | 0x02 | Coast_Forced_Regen |
| 3 | 0x03 | Coast_Brake_Regen |
| 4 | 0x04 | Coast_Forced_Brake_Regen |
