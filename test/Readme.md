# CAN device information

In the final implementation of the protocol, the name of each data ID can be read from the device. For now use the tables below to associate data to measurement value:

Use test.py in root folder to dump data from the CAN bus.

## BMS 

Device ID: 0x00

| Data Object ID | Data Name |
|--------|------|
| 0x4001 | vBat |
| 0x4002 | vLoad |
| 0x4003 | vCell1 |
| 0x4004 | vCell2 |
| 0x4005 | vCell3 |
| 0x4006 | vCell4 |
| 0x4007 | vCell5 |
| 0x4008 | iBat |
| 0x4009 | tempBat |
| 0x400A | SOC |


## MPPT

Device ID: 0x0A

| Data Object ID | Data Name |
|--------|-------|
| 0x4001 | vBat |
| 0x4002 | vSolar |
| 0x4003 | iBat |
| 0x4004 | iLoad |
| 0x4005 | tempExt |
| 0x4006 | tempInt |
| 0x4007 | loadEn |
| 0x4008 | eInputDay_Wh |
| 0x4009 | eOutputDay_Wh |
| 0x400A | eInputTotal_Wh |
| 0x400B | eOutputTotal_Wh |
