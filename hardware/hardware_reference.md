# FPV Hardware Reference — Dimensions, Pinouts, Fitment Data
**Generated:** 2025-12-12

---

## FRAME SPECIFICATIONS

| Frame | Wheelbase | Stack | Arm | Weight | Camera Mount | Notes |
|-------|-----------|-------|-----|--------|--------------|-------|
| **Source One V5** (need) | 220mm | 30.5×30.5 | 5mm | ~90g | 20×20 / 19×19 | Standard 5" |
| **Mark5 HD** (3D printed) | 230mm | 30.5×30.5 | 5mm | ~120g | 20×20 | **Replace with carbon** |
| **Mario 5 O4 XH** | 226mm | 30.5×30.5 | 4mm | ~85g | DJI O4 specific | Cinematic |
| **GX140** | 140mm | 20×20 | 3mm | ~45g | Runcam Split / Turtle V2 | 3" |
| **Mobula8** | 85mm | 16×16 (AIO) | 2mm | ~18g | Built-in | 2" whoop |
| **Mobula7 V3** | 75mm | 16×16 (AIO) | 2mm | ~15g | Built-in | 2" whoop spare |
| **FPVDrone 295mm** | 295mm | 30.5×30.5 | 5mm | ~140g | 20×20 | 7" long range |
| **YoungRC F450** | 450mm | 30.5×30.5 | 4mm | ~280g | 30×30 | 450 class |
| **HAWK'S WORK F450** | 450mm | 30.5×30.5 | 4mm | ~280g | 30×30 | 450 class |

### Frame Mounting Patterns
| Pattern | Hole Spacing | Hole Dia | Typical Use |
|---------|--------------|----------|-------------|
| 16×16 | 16mm | 2.0mm | Whoop AIO |
| 20×20 | 20mm | 2.5mm | 3-4" 20×20 stack |
| 30.5×30.5 | 30.5mm | 3.2mm (M3) | 5-7" standard |
| 30×30 | 30mm | 3.2mm | 450mm platform |

---

## FLIGHT CONTROLLER SPECS

| FC | MCU | IMU | Baro | OSD | UARTs | I2C | Mount | Dim (mm) | Weight |
|----|-----|-----|------|-----|-------|-----|-------|----------|--------|
| **Radiolink F405** | STM32F405 | ICM42688 | DPS310 | Yes | 6 | 2 | 30.5 | 36×36 | 6g |
| **SpeedyBee F405 Mini** | STM32F405 | ICM42688 | DPS310 | Yes | 4 | 1 | 20×20 | 25×25 | 4g |
| **SpeedyBee F405 Mini Stack** | F405 + BLS 35A | ICM42688 | DPS310 | Yes | 4 | 1 | 20×20 | 25×25 | 12g |
| **GoolRC GF30F722** | STM32F722 | ICM42688 | DPS310 | Yes | 6 | 2 | 30.5 | 36×36 | 6g |
| **SoloGood F722 Stack** | STM32F722 | ICM42688 | DPS310 | Yes | 4 | 1 | 30.5 | 36×36 | 15g |
| **Matek H743-WLITE** | STM32H743 | ICM42688-P | DPS310 | Yes | 6 | 2 | **25×25 M2** | 36×36 | 7g |
| **MicoAir H743V2 AIO** | STM32H743 | ICM42688×2 | DPS310 | Yes | 6 | 2 | 30.5 | 45×45 | 25g |

---

## ESC SPECIFICATIONS

| ESC | Current | Protocol | Mount | Dim (mm) | Weight | BEC |
|-----|---------|----------|-------|----------|--------|-----|
| **Radiolink FLYCOLOR 55A** | 55A | DShot600 | 30.5 | 36×36 | 8g | 5V 2A |
| **SpeedyBee BLS 35A** | 35A | DShot600 | 20×20 | 25×25 | 5g | 5V 3A |
| **SoloGood BLS8 60A** | 60A | DShot600 | 30.5 | 36×36 | 10g | 5V 3A |
| **HGLRC Specter 60A** | 60A | DShot600 | 30.5×30.5 4in1 | 36×36 | 8g | 5V 2A |
| **Readytosky 40A** | 40A | DShot600 | Single | 24×18 | 4g | 5V 3A |
| **AERO SELFIE 30A** | 30A | DShot600 | 30.5 | 36×36 | 5.4g | None |

---

## MOTOR SPECIFICATIONS

| Motor | Size | KV | Stator | Shaft | Mount | Weight | Prop | Cell |
|-------|------|-----|--------|-------|-------|--------|------|------|
| **Axisflying 2207** | 2207 | 1850 | 22×7 | 5mm | M5 | 32g | 5" | 6S |
| **NEEBRC 2807** | 2807 | 1300 | 28×7 | 5mm | M5 | 52g | 7-10" | 6S |
| **HGLRC Specter 1804** | 1804 | 3500 | 18×4 | 4mm | M3 | 18g | 3-3.5" | 4S |
| **AKK 1407** | 1407 | 3500 | 14×7 | 4mm | M3 | 12g | 3" | 3-4S |
| **HGLRC Specter 1303.5** | 1303.5 | 5500 | 13×3.5 | 1.5mm | M2 | 6g | 2-2.5" | 2-4S |
| **Happymodel EX1103** | 1103 | 11000 | 11×3 | 1.5mm | M2 | 3.5g | 2" | 1-2S |
| **Readytosky 2212** | 2212 | 920 | 22×12 | 5mm | M5 | 48g | 10" | 4S |

---

## VTX SPECIFICATIONS

| VTX | Power | Protocol | Mount | Dim (mm) | Weight | Antenna |
|-----|-------|----------|-------|----------|--------|---------|
| **AKK A1918** | 200-1000mW | SmartAudio | 20×20 / M3 | 36×36 | 8g | SMA |
| **HGLRC Zeus 350mW** | 25-350mW | SmartAudio | 16×16 / M2 | 20×20 | 4g | SMA |
| **Walksnail Avatar Pro** | 400mW | Proprietary | 20×20 | 30×30 | 9g | Dual UFL |
| **Walksnail Avatar HD Mini 1S** | 200mW | Proprietary | 16×16 | 20×20 | 4.5g | Single UFL |
| **DJI O4 Pro** | 400mW | Proprietary | Custom | 30×30 | 8.5g | Dual UFL |

---

## CAMERA SPECIFICATIONS

| Camera | Sensor | Resolution | FOV | Mount | Dim (mm) | Weight | Voltage |
|--------|--------|------------|-----|-------|----------|--------|---------|
| **Foxeer Razer Mini V3** | 1/3" CMOS | 1200TVL | 160° | 14×14 | 14×14 | 2.5g | 5V |
| **Caddx Ant** | 1/3" CMOS | 1200TVL | 160° | 14×14 | 14×14 | 2g | 5V |
| **RunCam Racer Nano 4** | 1/3" CMOS | 1200TVL | 160° | 14×14 | 14×14 | 3g | 5V |
| **Readytosky 1200TVL** | 1/3" CMOS | 1200TVL | 160° | 14×14 | 14×14 | 2.5g | 5V |
| **Walksnail Avatar Pro** | 1/1.8" Starvis 2 | 1080p60 | 160° | Custom | 30×30 | 9g | 5V |
| **Walksnail Avatar HD Mini 1S** | 1/3" CMOS | 1080p60 | 160° | 14×14 | 14×14 | 4.5g | 5V |

---

## RX SPECIFICATIONS

| RX | Protocol | Diversity | Mount | Dim (mm) | Weight | Antenna |
|----|----------|-----------|-------|----------|--------|---------|
| **BETAFPV SuperD V3** | ELRS 2.4GHz | Yes | 20×20 / M3 | 20×20 | 3.5g | Dual UFL |
| **RadioMaster RP3** | ELRS 2.4GHz | No | 16×16 | 16×16 | 1.5g | Single UFL |
| **RadioMaster RP1** | ELRS 2.4GHz | No | 16×16 | 16×16 | 1.5g | Single UFL |
| **HGLRC ELRS Nano** | ELRS 2.4GHz | No | 16×16 | 16×16 | 1.5g | Single UFL |

---

## RADIO SPECIFICATIONS

| Radio | Protocol | Gimbals | Channels | RF Module | Battery |
|-------|----------|---------|----------|-----------|---------|
| **RadioMaster Boxer Crush** | ELRS 2.4GHz | AG01 Hall | 16 | Internal | 18650×2 |
| **RadioMaster Pocket** | ELRS 2.4GHz | Hall | 12 | Internal | 18650×1 |

---

## GOGGLES SPECIFICATIONS

| Goggles | Type | Resolution | FOV | HDMI | DVR | Battery | Weight |
|---------|------|------------|-----|------|-----|---------|--------|
| **EV800D** | Analog | 800×480 | 82° | No | Yes | 2S LiPo | 180g |
| **Walksnail Avatar HD Goggles X** | Digital (Walksnail) | 1920×1080 | 50° | **IN/OUT** | Yes | 2S LiPo | 280g |

---

## GPS/COMPASS SPECIFICATIONS

| Module | GNSS | Compass | Mount | Dim (mm) | Weight | Protocols |
|--------|------|---------|-------|----------|--------|-----------|
| **HGLRC M100-5883** | UBLOX M10 | QMC5883L | 20×20 / M3 | 25×25 | 8g | UBX/NMEA |
| **Matek M10Q-5883** | UBLOX M10 | QMC5883L | 20×20 / M3 | 25×25 | 8g | UBX/NMEA |
| **MicroAir M10G** | UBLOX M10 | QMC5883L | 20×20 | 25×25 | 8g | UBX/NMEA |
| **SEQURE M10-25Q** | UBLOX M10 | QMC5883L | 20×20 | 25×25 | 8g | UBX/NMEA |
| **FPVDrone M8N** | UBLOX M8 | Internal | 20×20 | 25×25 | 8g | UBX/NMEA |

---

## BATTERY SPECIFICATIONS

| Battery | Cells | Capacity | Voltage | C-Rate | Connector | Weight | Use |
|---------|-------|----------|---------|--------|-----------|--------|-----|
| **OVONIC 6S 1300mAh** | 6S | 1300mAh | 22.2V | 130C | XT60 | 210g | 5" 6S |
| **HRB 6S 1800mAh** | 6S | 1800mAh | 22.2V | 50C | XT60 | 250g | 5" 6S |
| **OVONIC 4S 4500mAh** | 4S | 4500mAh | 14.8V | 50C | T-Plug | 420g | 7" / 450mm |
| **HRB 4S 4000mAh** | 4S | 4000mAh | 14.8V | 60C | XT60 | 380g | 450mm |
| **HRB 4S 5000mAh** | 4S | 5000mAh | 14.8V | 50C | XT60 | 450g | 450mm |
| **OVONIC 2S 850mAh** | 2S | 850mAh | 7.4V | 120C | XT30 | 55g | 3" |
| **BETAFPV Lava 2S 550mAh** | 2S | 550mAh | 7.6V | 75C | XT30 | 35g | 2-3" |
| **CNHL 2S 450mAh LiHV** | 2S | 450mAh | 7.6V | 70C | XT30 | 28g | 2-3" |
| **GNB 1S 550mAh** | 1S | 550mAh | 3.7V | 90C | BT2.0 | 14g | Whoop |
| **ZEVORO 1S 450mAh LiHV** | 1S | 450mAh | 3.8V | 95C | BT2.0 | 12g | Whoop |

---

## SBC SPECIFICATIONS (DETAILED)

| SBC | SOC | CPU | NPU | GPU | RAM | Storage | PCIe | HDMI | GPIO | Dim (mm) | Weight | Power |
|-----|-----|-----|-----|-----|-----|---------|------|------|------|----------|--------|-------|
| **Radxa Rock 5C Lite** | RK3588S2 | 4×A76 + 4×A55 | **6 TOPS** | Mali-G610 MP4 | 16GB LPDDR4X | MicroSD | 2.1 x1 (E-key) | 8K@60 | 40-pin | 56×85 | 45g | 5V 5A |
| **Radxa Zero 3W** | RK3566 | 4×A55 | **~1 TOPS** | Mali-G52 2EE | 4GB LPDDR4X | MicroSD | None | 1080p@60 | 40-pin (castellated) | 45×45 | 15g | 5V 1A |
| **Khadas VIM4** | A311D2 | 4×A73 + 4×A53 | **3.2 TOPS** | Mali-G52 MP6 | 8GB LPDDR4X | 32GB eMMC + M.2 2280 | None | **IN 4K@60 / OUT 4K@60** | 40-pin | 82×58 | 45g | 12V 2A |

---

## CONNECTOR PINOUTS (QUICK REF)

### JST-GH 1.25mm (FC↔SBC, GPS, I2C)
| Pin | Signal | Wire |
|-----|--------|------|
| 1 | 5V | 22 AWG red |
| 2 | TX | 26 AWG yellow |
| 3 | RX | 26 AWG white |
| 4 | SDA | 28 AWG blue |
| 5 | SCL | 28 AWG green |
| 6 | GND | 22 AWG black |

### JST-SH 1.0mm (ESC, Camera, LED)
| Pin | Signal | Wire |
|-----|--------|------|
| 1 | GND | 22 AWG black |
| 2 | Signal | 26 AWG |
| 3 | 5V | 22 AWG red |
| 4 | — | — |

### XT60 / XT30
| Connector | Pin | Wire |
|-----------|-----|------|
| XT60 | + | 14 AWG red |
| XT60 | - | 14 AWG black |
| XT30 | + | 18 AWG red |
| XT30 | - | 18 AWG black |

---

## FITMENT CLEARANCE RULES

| Component | Clearance Required | Check Method |
|-----------|-------------------|--------------|
| Prop to frame | ≥ 3mm | Measure at closest point |
| Prop to motor wire | ≥ 2mm | Visual |
| Prop to SBC heatsink | ≥ 5mm | Measure at max RPM |
| Battery strap to FC | ≥ 2mm | Visual |
| Antenna to carbon | ≥ 5mm | Measure |
| Camera lens to prop arc | ≥ 10mm | Visual |
| VTX antenna to RX antenna | ≥ 20mm | Measure |
| ESC to frame (single) | ≥ 3mm | Visual |
| Wire bundle to moving parts | ≥ 2mm | Visual |

---

## THERMAL LIMITS

| Component | Max Safe Temp | Throttle Point | Shutdown |
|-----------|---------------|----------------|----------|
| RK3588S2 (Rock 5C) | 85°C | 80°C | 95°C |
| RK3566 (Zero 3W) | 80°C | 75°C | 90°C |
| A311D2 (VIM4) | 85°C | 80°C | 95°C |
| STM32F4/F7/H7 | 105°C | 100°C | 110°C |
| ESC (BLS) | 100°C | 95°C | 110°C |
| Motors | 80°C | — | 100°C |
| LiPo (discharge) | 60°C | — | 80°C |
| LiPo (charge) | 45°C | — | 50°C |

---

## WIRE CURRENT CAPACITY (Silicone Wire)

| AWG | Max Continuous | Max Burst (10s) | Use |
|-----|----------------|-----------------|-----|
| 14 AWG | 32A | 50A | Main battery (XT60) |
| 16 AWG | 22A | 35A | ESC power (single) |
| 18 AWG | 16A | 25A | XT30 battery |
| 20 AWG | 11A | 18A | 5V BEC output |
| 22 AWG | 7A | 12A | SBC power, servo |
| 24 AWG | 5A | 8A | LED, beeper |
| 26 AWG | 3A | 5A | Signals (UART, I2C) |
| 28 AWG | 2A | 3A | I2C, sensors |
| 30 AWG | 1.5A | 2A | High-density signals |