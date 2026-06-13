# FPV Drone Fleet — Verified Component Dimensions

> Compiled: 2026-06-12  
> Sources: Manufacturer wikis, datasheets, CAD files, retailer listings  
> All measurements in mm (metric). NOT FOUND = unverifiable from public sources.

---

## Table of Contents

1. [RADXA ROCK 5C Lite (RK3588S2)](#1-radxa-rock-5c-lite-rk3588s2)
2. [RADXA Zero 3W (RK3566)](#2-radxa-zero-3w-rk3566)
3. [KHADAS VIM4 (A311D2)](#3-khadas-vim4-a311d2)
4. [Frames](#4-frames)
5. [Flight Controllers](#5-flight-controllers)
6. [ESCs](#6-escs)
7. [Motors](#7-motors)
8. [VTX / Cameras / Receivers](#8-vtx--cameras--receivers)
9. [Radios / Goggles / GPS](#9-radios--goggles--gps)

---

## 1. RADXA ROCK 5C Lite (RK3588S2)

| Property | Value | Source |
|----------|-------|--------|
| PCB Dimensions (L×W) | 86 × 56 mm (bounding box) | [Radxa Wiki](https://docs.radxa.com/en/rock5/rock5c/getting-started/introduction) |
| PCB Thickness | NOT FOUND | |
| Overall Height (H) | NOT FOUND | |
| Weight | NOT FOUND — not in any datasheet | |
| Mounting Hole Dia | NOT FOUND — CAD files available at dl.radxa.com | [DXF](https://dl.radxa.com/rock5/5c/docs/hw/v1100/radxa_rock_5c_2d_dxf_v1100.zip) |
| Mounting Hole Positions | NOT FOUND — extractable from STEP/DXF | [STEP](https://dl.radxa.com/rock5/5c/docs/hw/dimension/5c_pcba.stp.zip) |
| Power Input | 5V DC via USB-C or GPIO pins 2/4 | [Product Brief](https://dl.radxa.com/rock5/5c/docs/hw/v1100/radxa_rock5c_product_brief.pdf) |
| Min PSU | 10W (2A) | Same |
| Full Load PSU | 25W (5A) — with USB 3.0 + PCIe | Same |
| USB Port Current | 2.8A aggregate across 4× USB-A | Same |
| Ambient Operating Temp | 0°C to 50°C | Same |
| SoC Throttle Temp | 80°C (internal) | Same |
| PCIe Connector | 16-pin FPC, 0.5mm pitch, PCIe 2.1 x1, top side near 40-pin header | [Schematic v1.1](https://dl.radxa.com/rock5/5c/docs/hw/v1100/radxa_rock_5c_schematic_v1100.pdf) |
| MIPI CSI | 1× 4-lane (splittable to 2× 2-lane), FPC connector | Same |

### ROCK 5C Lite — GPIO Pinout (40-pin, 2.54mm pitch)

All GPIOs 3.3V logic (max 3.63V). GPIO numbering: `GPIOX_Bn` = (X × 32) + (B × 8) + n (A=0, B=1, C=2, D=3).

Source: [Radxa Hardware Interface](https://docs.radxa.com/en/rock5/rock5c/hardware-design/hardware-interface)

**Left Side (odd pins 1–39):**

| Pin | GPIO# | GPIO Name | Alternate Functions |
|-----|-------|-----------|-------------------|
| 1 | — | +3.3V | Power |
| 3 | 63 | GPIO1_D7 | UART1_CTSN_M1, I2C8_SDA_M2, PWM15_IR_M3 |
| 5 | 62 | GPIO1_D6 | UART1_RTSN_M1, I2C8_SCL_M2, PWM14_M2 |
| 7 | 43 | GPIO1_B3 | UART4_TX_M2 |
| 9 | — | GND | |
| 11 | 139 | GPIO4_B3 | UART8_CTSN_M0, PWM15_IR_M1, I2S1_SDO2_M0 |
| 13 | 138 | GPIO4_B2 | UART8_RTSN_M0, PWM14_M1, I2S1_SDO1_M0, SPI0_CS0_M1 |
| 15 | 140 | GPIO4_B4 | UART9_TX_M1, PWM11_IR_M1, SPDIF0_TX_M1, I2S1_SDO3_M0 |
| 17 | — | +3.3V | Power |
| 19 | 33 | GPIO1_A1 | UART6_TX_M1, I2C2_SCL_M4, SPI4_MOSI_M2 |
| 21 | 32 | GPIO1_A0 | UART6_RX_M1, I2C2_SDA_M4, SPI4_MISO_M2 |
| 23 | 34 | GPIO1_A2 | UART6_RTSN_M1, I2C4_SDA_M3, PWM0_M2, SPI4_CLK_M2 |
| 25 | — | GND | |
| 27 | 23 | GPIO0_C7 | UART1_RTSN_M2, I2C6_SDA_M0, PWM6_M0, I2S1_SDI2_M1, SPI0_MISO_M0 / USB4_DP via R104 |
| 29 | 42 | GPIO1_B2 | UART4_RX_M2, SPI0_MOSI_M2 |
| 31 | 41 | GPIO1_B1 | SPI0_MISO_M2 |
| 33 | 44 | GPIO1_B4 | UART7_RX_M2, SPI0_CS0_M2 |
| 35 | 128 | GPIO4_A0 | UART9_RTSN_M1, I2S1_MCLK_M0, SPI0_MISO_M1 |
| 37 | — | SARADC_VIN2 | 1.8V analog input |
| 39 | — | GND | |

**Right Side (even pins 2–40):**

| Pin | GPIO# | GPIO Name | Alternate Functions |
|-----|-------|-----------|-------------------|
| 2 | — | +5.0V | Power |
| 4 | — | +5.0V | Power |
| 6 | — | GND | |
| 8 | 13 | GPIO0_B5 | UART2_TX_M0, I2C1_SCL_M0, I2S1_MCLK_M1 |
| 10 | 14 | GPIO0_B6 | UART2_RX_M0, I2C1_SDA_M0, I2S1_SCLK_M1 |
| 12 | 129 | GPIO4_A1 | SPI0_MOSI_M1, I2S1_SCLK_M0, UART9_CTSN_M1 |
| 14 | — | GND | |
| 16 | 37 | GPIO1_A5 | SPI2_MOSI_M0 |
| 18 | 40 | GPIO1_B0 | SPI2_CS1_M0 |
| 20 | — | GND | |
| 22 | 45 | GPIO1_B5 | UART7_TX_M2, SPI0_CS1_M2 |
| 24 | 35 | GPIO1_A3 | UART6_CTSN_M1, I2C4_SCL_M3, PWM1_M2, SPI4_CS0_M2 |
| 26 | 36 | GPIO1_A4 | SPI2_MISO_M0 |
| 28 | 24 | GPIO0_D0 | UART1_CTSN_M2, I2C6_SCL_M0, PWM7_IR_M0, I2S1_SDI3_M1, SPI3_MISO_M2 / USB4_DM via R106 |
| 30 | — | GND | |
| 32 | 136 | GPIO4_B0 | UART8_TX_M0, I2C6_SDA_M3, I2S1_SDI3_M0, SPI2_CS1_M1 |
| 34 | — | GND | |
| 36 | 130 | GPIO4_A2 | SPI0_CLK_M1, I2S1_LRCK_M0 |
| 38 | 133 | GPIO4_A5 | UART3_TX_M2, I2C3_SDA_M2, I2S1_SDI0_M0 |
| 40 | 137 | GPIO4_B1 | UART8_RX_M0, I2C6_SCL_M3, SPDIF1_TX_M1, I2S1_SDO0_M0, SPI0_CS1_M1 |

---

## 2. RADXA Zero 3W (RK3566)

| Property | Value | Source |
|----------|-------|--------|
| PCB Dimensions (L×W) | 65 × 30 mm (bounding box) | [DXF CAD](https://dl.radxa.com/zero3/docs/hw/3w/radxa_zero_3w_2d_dxf.zip) |
| PCB Thickness | NOT FOUND | |
| Overall Height (H) | NOT FOUND | |
| Weight | NOT FOUND — not published | |
| Mounting Hole Dia | 2.82 mm (M2.5) | DXF verified |
| Power Input | 5V DC via USB-C or GPIO pins 2/4 | [Product Brief](https://dl.radxa.com/zero3/docs/hw/3w/radxa_zero_3w_product_brief.pdf) |
| Recommended PSU | 5V/2A (10W) | Same |
| Ambient Operating Temp | 0°C to 50°C | Same |
| SoC Throttle Temp | 85°C | Same |
| MIPI CSI | 1× 4-lane, 22-pin FPC connector (0.5mm pitch) | Schematic v1.11 |
| GPIO Header | Standard 40-pin through-hole, 2.54mm pitch (no castellations) | Radxa Wiki |

### Mounting Hole Positions (from DXF, origin at bottom-left)

| Hole | X (mm) | Y (mm) |
|------|--------|--------|
| 1 | 3.60 | 26.45 |
| 2 | 61.40 | 3.60 |
| 3 | 61.40 | 26.50 |
| 4 | 3.55 | 3.60 |

### Zero 3W — GPIO Pinout (40-pin, 2.54mm pitch)

Source: [Zero 3W Hardware Interface](https://docs.radxa.com/en/zero/zero3/hardware-design/hardware-interface)

**Left Side (odd pins 1–39):**

| Pin | GPIO# | GPIO Name | Alt Functions |
|-----|-------|-----------|---------------|
| 1 | — | +3.3V | Power |
| 3 | 32 | GPIO1_A0 | UART3_RX_M0, I2C3_SCL_M0 |
| 5 | 33 | GPIO1_A1 | UART3_TX_M0, I2C3_SDA_M0 |
| 7 | 116 | GPIO3_C4 | PWM14_M0 |
| 9 | — | GND | |
| 11 | 97 | GPIO3_A1 | |
| 13 | 98 | GPIO3_A2 | I2S3_MCLK_M0 |
| 15 | 104 | GPIO3_B0 | |
| 17 | — | +3.3V | Power |
| 19 | 147 | GPIO4_C3 | SPI3_MOSI_M1, I2S3_SCLK_M1, PWM15_IR_M1 |
| 21 | 149 | GPIO4_C5 | SPI3_MISO_M1, I2S3_SDO_M1, PWM12_M1, UART9_TX_M1 |
| 23 | 146 | GPIO4_C2 | SPI3_CLK_M1, I2S3_MCLK_M1, PWM14_M1 |
| 25 | — | GND | |
| 27 | 138 | GPIO4_B2 | I2C4_SDA_M0, I2S2_SDI_M1 (USB2 via resistor mod) |
| 29 | 107 | GPIO3_B3 | I2C5_SCL_M0 |
| 31 | 108 | GPIO3_B4 | I2C5_SDA_M0 |
| 33 | 115 | GPIO3_C3 | I2S1_SCLK_RX_M2, UART5_RX_M1 |
| 35 | 100 | GPIO3_A4 | I2S3_LRCK_M0 |
| 37 | 36 | GPIO1_A4 | I2S1_SCLK_RX_M0 |
| 39 | — | GND | |

**Right Side (even pins 2–40):**

| Pin | GPIO# | GPIO Name | Alt Functions |
|-----|-------|-----------|---------------|
| 2 | — | +5.0V | Power |
| 4 | — | +5.0V | Power |
| 6 | — | GND | |
| 8 | 25 | GPIO0_D1 | UART2_TX_M0 |
| 10 | 24 | GPIO0_D0 | UART2_RX_M0 |
| 12 | 99 | GPIO3_A3 | I2S3_SCLK_M0 |
| 14 | — | GND | |
| 16 | 105 | GPIO3_B1 | UART4_RX_M1, PWM8_M0 |
| 18 | 106 | GPIO3_B2 | UART4_TX_M1, PWM9_M0 |
| 20 | — | GND | |
| 22 | 113 | GPIO3_C1 | I2S1_SDO2_M2 |
| 24 | 150 | GPIO4_C6 | SPI3_CS0_M1, PWM13_M1, UART9_RX_M1, I2S3_SDI_M1 |
| 26 | — | NC | Not connected |
| 28 | 139 | GPIO4_B3 | I2C4_SCL_M0, I2S2_SDO_M1 (USB2 via resistor mod) |
| 30 | — | GND | |
| 32 | 114 | GPIO3_C2 | UART5_TX_M1, I2S1_SDO3_M2 |
| 34 | — | GND | |
| 36 | 103 | GPIO3_A7 | |
| 38 | 102 | GPIO3_A6 | I2S3_SDI_M0 |
| 40 | 101 | GPIO3_A5 | I2S3_SDO_M0 |

---

## 3. KHADAS VIM4 (A311D2)

| Property | Value | Source |
|----------|-------|--------|
| PCB Dimensions (L×W) | 82.0 × 58.0 mm (±0.15) | [Spec Sheet PDF](https://dl.khadas.com/products/vim4/specs/new-vim4-specs.pdf) |
| PCB Thickness | 1.2 mm (±0.05) | [PCBA 2D Drawing](https://dl.khadas.com/products/vim4/blueprints/dxf/vim4-pcba-2d-v13.pdf) |
| Overall Height (H) | 11.5 mm (with tallest components) | Spec Sheet |
| Weight (bare board) | 31 g | Same |
| Weight (with heatsink) | ~48 g | Estimated |
| Mounting Holes | 4× M2 clearance, 2.20 mm dia | PCBA 2D Drawing |
| Mounting Pattern | Proprietary corner-mount (not RPi, not 30.5×30.5) | DXF available |
| Power Input | 9–20V DC via 4-pin Molex (1.25mm pitch) or USB-C PD | Spec Sheet |
| Recommended PSU | 12V/2A (24W) minimum via USB-C PD | Same |
| Idle Power | ~1.2W (0.1A @ 12V) | Same |
| Full Load Power | ~6.0W (0.5A @ 12V) | Same |
| SoC | Amlogic A311D2 — 4× A73 @ 2.2 GHz + 4× A53 @ 2.0 GHz | Same |
| RAM | 8 GB LPDDR4X @ 2016 MHz | Same |
| eMMC | 32 GB 5.1 | Same |
| WiFi | AP6275S, Wi-Fi 6, BT 5.1 | Same |
| HDMI OUT | Type-A, HDMI 2.1, 4K2K HDR | [Docs](http://docs.khadas.com/products/sbc/vim4/hardware/interfaces) |
| HDMI IN | Micro HDMI (Type-D), up to 4K@60fps | [HDMI Input Docs](http://docs.khadas.com/products/sbc/vim4/applications/hdmi-input-5.15) |
| NVMe M.2 | 2280 form factor, PCIe 2.0 ×1 (bottom side) | Spec Sheet |
| MIPI CSI #4 | 20-pin, 0.5mm pitch | Docs |
| MIPI CSI #5 | 30-pin, 0.5mm pitch, 4-lane (up to 16 MP) | Docs |
| MIPI-DSI / eDP | 40-pin, 0.5mm pitch FPC; 4-lane up to 1920×1200 DSI or 2560×1600 eDP | Docs |
| MCU | STM32G031K6 (power mgmt, boot media selection) | Spec Sheet |

### VIM4 Heatsink / Active Cooler

| Property | Value |
|----------|-------|
| Passive Heatsink | 81.0 × 49.1 × 8.9 mm, Al 6063 black anodized, ~17 g |
| Active Cooler | Adds 3705 PWM fan; total height ~13 mm above PCB |
| Fan Header | 4-wire PWM, 0.8mm pitch |

### VIM4 — 40-Pin GPIO Pinout (2.54mm pitch)

GPIO numbers valid for vendor kernel only (mainline differs).

Source: [40-Pin Header Docs](http://docs.khadas.com/products/sbc/vim4/applications/gpio/40pin-header)

| Pin | Name | GPIO# | Notes |
|-----|------|-------|-------|
| 1 | 5V | — | Power out |
| 2 | 5V | — | Power out |
| 3 | HUB_D4N | — | USB D- |
| 4 | HUB_D4P | — | USB D+ |
| 5 | GND | — | |
| 6 | VCCMCU | — | MCU 3.3V out |
| 7 | MCUBOOT0 | — | MCU boot mode |
| 8 | MCUSWDIO | — | MCU SWD data |
| 9 | GND | — | |
| 10 | ADC_CH6 | — | Analog input |
| 11 | VDD1V8 | — | 1.8V reference |
| 12 | ADC_CH3 | — | Analog input |
| 13 | SPDIFOUT | 420 | Digital audio out |
| 14 | GND | — | |
| 15 | UART_E_RX | 491 | UART-E receive (Android) |
| 16 | UART_E_TX | 490 | UART-E transmit (Android) |
| 17 | GND | — | |
| 18 | Linux_RX | — | Linux console RX |
| 19 | Linux_TX | — | Linux console TX |
| 20 | 3V3 | — | Power |
| 21 | GND | — | |
| 22 | I2CM_F_SCL | 501 | I2C-F clock |
| 23 | I2CM_F_SDA | 502 | I2C-F data |
| 24 | GND | — | |
| 25 | I2CM_A_SCL / SPI_A_SCLK | 466 | I2C/SPI clock (DT overlay) |
| 26 | I2CM_A_SDA / SPI_A_SS0 | 467 | I2C/SPI chip select |
| 27 | 3V3 | — | Power |
| 28 | GND | — | |
| 29 | I2S_SCLK1 | 447 | I2S bit clock |
| 30 | I2S_MCLK1 | 446 | I2S master clock |
| 31 | I2S_SDO1 | 449 | I2S data out |
| 32 | I2S_LRCLK1 | 448 | I2S frame sync |
| 33 | I2S_SDI1 | 450 | I2S data in |
| 34 | GND | — | |
| 35 | PWM_F | 492 | PWM output |
| 36 | SPI_A_MOSI | 464 | SPI master out / slave in |
| 37 | SPI_A_MISO | 465 | SPI master in / slave out |
| 38 | PWR_EN1 | — | Power enable |
| 39 | GPIO | 417 | General purpose |
| 40 | GND | — | |

---

## 4. Frames

### 4.1 TBS Source One V5 (5")

| Property | Value | Source |
|----------|-------|--------|
| Wheelbase | 226 mm | [RaceDayQuads](https://www.racedayquads.com/products/tbs-source-one-v5-5-freestyle-long-range-frame) |
| Overall (approx) | ~254 × 114 × 51 mm | Google Shopping |
| Weight | 123.5 g | RaceDayQuads |
| Top/Mid Plate | 2.0 mm CF | [GetFPV](https://www.getfpv.com/tbs-source-one-v5-5-frame-kit.html) |
| Bottom Plate | 2.5 mm CF | Same |
| Arm Thickness | 6.0 mm CF | Same |
| Stack Mount | 30.5×30.5 (M3) **and** 20×20 (M2) + DJI Air Unit | [Lumenier](https://www.lumenier.com/products/tbs-source-one-v5-5-frame-kit) |
| Camera Mount | 19 mm stock gap (20 mm via TPU) | Printables |
| Standoffs | 30 mm and 22 mm | RaceDayQuads |
| Material | 3K carbon fiber | Retailers |
| Configuration | Wide-stance X | TBS |

### 4.2 SpeedyBee Mario 5 O4 (5")

| Property | XH (Stretched-X) | DC (Deadcat) | Source |
|----------|:-----------------:|:-------------:|--------|
| Wheelbase | 226 mm | 227 mm | [SpeedyBee Official](https://www.speedybee.com/speedybee-mario-5-frame/) |
| Weight (no 3D prints) | 126 ±5 g | 129 ±5 g | Same |
| Weight (with 3D prints) | 167 ±5 g | 170 ±5 g | Same |
| Top Plate | 2.5 mm T300 3K CF | 2.5 mm T300 3K CF | Same |
| Middle Plate | 2.0 mm T300 3K CF | 2.0 mm T300 3K CF | Same |
| Bottom Plate | 2.5 mm T300 3K CF | 2.5 mm T300 3K CF | Same |
| Arm Thickness | 6.0 mm T300 3K CF | 6.0 mm T300 3K CF | Same |
| FC Mounting | 30.5×30.5 (M3) | 30.5×30.5 (M3) | Same |
| VTX Mounting | 20×20 (M2) / 25.5×25.5 (M2) | Same | Same |
| Camera Compat | 19 / 20 mm | 19 / 20 mm | Same |
| Motor Mount | 16–19 mm (Φ8 mm holes) | Same | Same |
| Internal Height | 23–31 mm | Same | Same |
| Max Prop | 5.1" | 5.1" | Same |

### 4.3 GEPRC Mark5 HD (5") — user cited "iFlight Mark5 HD"

*Note: "Mark5" is GEPRC product line — no "iFlight Mark5" exists.* iFlight equivalent is Cidora SL5 V2.1 HD.

**GEPRC Mark5:**

| Property | GEP-MK5X O3 (Squashed X) | GEP-MK5D O3 (Deadcat) | Source |
|----------|:------------------------:|:----------------------:|--------|
| Wheelbase | 225 mm | 230 mm | [GEPRC Official](https://geprc.com/product/gep-mk5x-o3-frame/) |
| Dimensions | 214×168×42 mm | 208×193×42 mm | Same |
| Weight | 141.9 g | 168.0 g | Same |
| Arm Thickness | 5.0 mm T300 3K CF | 5.0 mm T300 3K CF | Same |
| Stack Mount | 30.5×30.5 mm | 30.5×30.5 mm | Same |
| Camera | 20 mm | 20 mm | Same |
| Motor Mount | 16×16 / 19×19 mm | 16×16 / 19×19 mm | Same |
| Side Plates | 7075-T6 aluminum | 7075-T6 aluminum | Same |

**iFlight Cidora SL5 V2.1 HD (if needed):** 217 mm wheelbase, 156.1 g, 5.5 mm arms, 30×30 stack.

### 4.4 GX140 140mm (3")

| Property | Value | Source |
|----------|-------|--------|
| Wheelbase | 140 mm | [xt-xinte](https://www.xt-xinte.com/JMT-GX140-Mini-Alien-3-Inch-140mm-Carbon-Fiber-FPV-Frame-Kit-4mm-Arm-with-Print-Accessories-for-FPV-Racing-Drones-Freestyle-DIY-p941667.html) |
| Weight | 53–60 g | xt-xinte / Amazon |
| Arm / Bottom Plate | 4.0 mm 3K CF | xt-xinte |
| Top Plate | 2.0 mm 3K CF | Same |
| Stack Mount | 20×20 mm | Same |
| Motor Mount | 12×12 mm (supports 1306–1608) | Amazon |
| Camera | 3D-printed adjustable, 0–40° tilt | Same |
| Standoffs | M3 × 25 mm aluminum (twin tower) | Same |
| Max Prop | 3" | Same |
| Overall L×W | NOT FOUND — only wheelbase published | |

### 4.5 GEPRC Mark4 7" / FPVDrone 295mm

| Property | Value | Source |
|----------|-------|--------|
| Wheelbase | 295 mm | [Rotorama](https://www.rotorama.com/product/geprc-mark4-7) |
| Overall | ~226 × 266 mm (varies by source) | Same |
| Weight | 121 g | Same |
| Top/Bottom Plate | 2.5 mm (3 mm in some batches) | Same |
| Arm Thickness | 5.0 mm (V2: 6 mm) | Same |
| Stack Mount | 30.5×30.5 (M3) **and** 20×20 (M2) | Same |
| VTX Mount | 30.5×30.5 (M3) **and** 20×20 (M2) | Same |
| Motor Mount | 16×16 / 19×19 mm | Same |
| Camera | 19 mm (micro) | Same |
| Standoff Height | 25 mm (CNC 6061 Al) | Same |
| Battery | 4S 1800–6S 2200 mAh | Same |
| Max Prop | 7" | Same |

### 4.6 F450 Clone (450mm)

| Property | Value | Source |
|----------|-------|--------|
| Wheelbase | 450 mm diagonal (motor-to-motor) | [B&H / DJI](https://www.bhphotovideo.com/c/product/1080059-REG/dji_cp_nz_000012_flame_wheel_f450_with.html/specs) |
| Weight (frame only) | ~280–282 g (no gear) | [Probots](https://probots.co.in/f450-quadcopter-frame-drone-glass-fibre-with-power-distribution.html) |
| Weight (full kit) | ~420 g (with gear) | Amazon |
| Arm Material | PA66+30GF nylon (hollow molded, NOT CF plate) | Various |
| Center Plates | Glass fiber composite | Probots |
| Stack Mount | **50 mm** hole pattern (APM/Pixhawk) — NOT 30.5 mm FPV standard | Same |
| Motor Mount | 16/19 mm, M3 | INVENTO |
| Max Prop | 8–10" | Multiple |

---

## 5. Flight Controllers

### 5.1 Matek H743-WLITE

| Property | Value | Source |
|----------|-------|--------|
| PCB (L×W×H) | 44 × 29 × 14.5 mm (incl. headers) | [MatekSys](http://www.mateksys.com/?portfolio=h743-wlite) |
| Mounting Pattern | **25 × 25 mm** (NOT 30.5×30.5) | Same |
| Hole Diameter | **2 mm** (M2) | Same |
| Weight | 22 g (with extender board) | Same |
| Voltage Input | 6.8–30V (2S–6S) | Same |
| MCU | STM32H743VIH6, 480 MHz, 2 MB Flash, 512 KB RAM | Same |
| IMU | ICM42688-P | Same |
| Baro | DPS310 (I2C2, addr 0x76) | Same |
| OSD | AT7456E | Same |
| Blackbox | MicroSD card (SDIO) | Same |
| UARTs | **7** (all with signal inversion) | Same |
| PWM Outputs | **12** (all 5V tolerant except S2) | Same |
| ADC | VBAT (0–36V), Current (220A), RSSI, AirS, VB2, CU2 | Same |
| I2C | 2 ports (5V tolerant) | Same |
| CAN | 1 port (JST-GH-4P) | Same |
| BEC 1 | 5V/2A cont, 3A peak (FC, RX, OSD, cam, GPS) | Same |
| BEC 2 | 9V/12V/2A cont, 3A peak (VTX/cam; 12V via jumper) | Same |
| BEC 3 (Vx) | Adjustable 5V/6V/7.2V/8A cont, 10A peak (servos) | Same |
| BEC 4 | 3.3V/200 mA (baro/compass) | Same |
| RC Input | PWM/PPM, SBUS (RX6); CRSF/FPort with BRD_ALT_CONFIG=1 | Same |
| Dual Camera | Switchable via PINIO2 | Same |
| FW Targets | MATEKH743 (ArduPilot, INAV) | Same |

### 5.2 SpeedyBee F405 Mini Stack (20×20)

| Property | Value | Source |
|----------|-------|--------|
| PCB (L×W×H) | 32 × 30 × 7.8 mm | [Manual](https://www.manualslib.com/manual/3291258/Speedybee-F405-Mini-Bls.html) |
| Stack Height | 14.2 mm (FC + ESC) | Same |
| Mounting Pattern | **20 × 20 mm** | Same |
| Hole Diameter | **3.5 mm** (M2/M3 compatible) | Same |
| Weight (FC only) | 9.6 g | Same |
| Weight (Stack) | 13.5 g | Same |
| Voltage Input | 3–6S LiPo | Same |
| MCU | STM32F405RGT6, 168 MHz | Same |
| Gyro | ICM-42688P | Same |
| Baro | DPS-310 | Same |
| OSD | AT7456E | Same |
| Blackbox | 8 MB onboard | Same |
| UARTs | **6** (1 dedicated BT, 1 ESC telemetry) | Same |
| BEC | 5V/2A (4 groups), 9V/3A, 3.3V/500mA, 4.5V/1A | Same |
| Bluetooth | Built-in (SpeedyBee App tuning) | Same |
| DJI Compatible | O3, Vista, RunCam Link, Air Unit V1 | Same |
| FW Target | SPEEDYBEEF405MINI | Same |

### 5.3 Radiolink F405

| Property | Value | Source |
|----------|-------|--------|
| PCB Size | 30.5 × 30.5 mm | [Radiolink](https://www.radiolink.com/f405_new_specifications) |
| Mounting Pattern | 30.5 × 30.5 mm | Same |
| Hole Dia | NOT FOUND | |
| Weight | 9.5 g | Same |
| Voltage Input | 2S–6S LiPo (7.4–25.2V) | Same |
| MCU | STM32F405RGT6, 168 MHz | Same |
| Gyro | ICM42688 (6-axis) | Same |
| Baro | SPL06 | Same |
| OSD | AT7456E | Same |
| Blackbox | 128 MB onboard | Same |
| UARTs | **5** | Same |
| BEC | 3.3V/300mA, 5V/3A, 9V/3A (switchable) | Same |
| FW Targets | RADIOLINKF405 (BF), ArduPilot, INAV | Same |

### 5.4 GoolRC GF30F722 (JHEMCU)

| Property | Value | Source |
|----------|-------|--------|
| PCB Size | 36 × 36 mm | [flymod.net](https://flymod.net/en/item/fc_gf30f722_30mm/17157) |
| Mounting Pattern | 30.5 × 30.5 mm | Same |
| Hole Dia | **4 mm** | Same |
| Weight | 8.8 g | Same |
| Voltage Input | 3–8S LiPo (11.4–36V) | Same |
| MCU | STM32F722RET6 | Same |
| Gyro | ICM-42688-P | Same |
| Baro | Yes | Same |
| OSD | AT7456E | Same |
| Blackbox | 16 MB onboard | Same |
| UARTs | **6** | [Betaflight JHEF7DUAL](https://betaflight-com.pages.dev/docs/wiki/boards/archive/JHEF7DUAL) |
| BEC | 5V/2.5A + 10V/2A (dual) | Same |
| FW Target | JHEF7DUAL (BF), INAV | Same |

### 5.5 SoloGood F722 60A Stack

| Property | Value | Source |
|----------|-------|--------|
| PCB Size | 38.5 × 38.5 mm | [lxrcmodel](https://lxrcmodel.com/product/sologood-f722-60a-stack-icm42688p-4in1-esc-flight-controller-blheli_s-2-6s/) |
| Mounting Pattern | 30.5 × 30.5 mm | Same |
| Hole Dia | **4 mm** (M3) | Same |
| Weight (FC) | 8.1 g | Same |
| Stack Weight | ~23 g | Same |
| Voltage Input | 3–6S (11–30V) | Same |
| MCU | STM32F722RET6 | Same |
| Gyro | ICM42688P | Same |
| Baro | DPS310 | Same |
| OSD | AT7456E | Same |
| Blackbox | 16 MB | Same |
| UARTs | **6** (pin mapping in image-only manual) | Same |
| Motor Outputs | M1–M8 (X8 config) | Same |
| BEC | 5V/2A + 10V/2A | Same |
| FW Target | SOLOGOODF722 | Same |

### 5.6 MicoAir H743V2 (Standalone FC)

| Property | Value | Source |
|----------|-------|--------|
| PCB (L×W×H) | 36 × 36 × 8 mm | [MicoAir Docs](https://micoair.cn/docs/MicoAir743V2-fei-kong-yong-hu-shou-ce) |
| Mounting Pattern | 30.5 × 30.5 mm | Same |
| Hole Dia | **4 mm** | Same |
| Weight | 10 g | Same |
| Voltage Input | 2–6S (6–27V) | Same |
| MCU | STM32H743VIH6, 480 MHz, 2 MB Flash | Same |
| Dual IMU | BMI088 + BMI270 | Same |
| Baro | SPL06 | Same |
| Mag | QMC5883L (onboard) | Same |
| OSD | AT7456E | Same |
| Blackbox | MicroSD (4 GB card included) | Same |
| UARTs | **8** | Same |
| PWM Outputs | **10** (1–8 support DShot/bidir) | Same |
| BEC | 5V/3A + 12V/3A | Same |
| Bluetooth | Built-in (UART8, 115200) | Same |
| DJI Compatible | O3/O4/O4 Pro direct plug (SH1.0-6P) | Same |
| FW Targets | MicoAir743v2 (AP), micoair_h743-v2 (PX4), MICOARAIR743V2 (INAV), BF | Same |

---

## 6. ESCs

### 6.1 Radiolink FLYCOLOR 55A 4in1

| Property | Value | Source |
|----------|-------|--------|
| PCB (L×W×H) | 45 × 41 × 5.8 mm | Manuals |
| Weight | 15.8 g | Same |
| Mounting Pattern | 30.5 × 30.5 mm | Same |
| Hole Dia | M3 | Same |
| Voltage | 3S–6S (11.1–25.2V) | Same |
| Continuous Current | 55A per channel | Same |
| Burst Current | 65A | Same |
| Firmware | BLHeli_S (supports Bluejay, A-H-30) | Same |

### 6.2 SoloGood BLS8 60A 4in1

| Property | Value | Source |
|----------|-------|--------|
| PCB Size | 41.5 × 42 mm | Desertcart |
| Weight | ~15 g | Same |
| Mounting Pattern | 30.5 × 30.5 mm | Same |
| Hole Dia | M3 (4 mm aperture) | Same |
| Voltage | 3S–6S (11–26V) | Same |
| Continuous Current | 55A per channel | Same |
| Max Current | 60A | Same |
| Firmware | BLHeli_S (J-H-30-16.7), Bluejay, bidir DShot | Same |

### 6.3 SpeedyBee BLS 35A Mini V2 (20×20)

| Property | Value | Source |
|----------|-------|--------|
| PCB (L×W×H) | 35 × 35 × 5.5 mm | RaceDayQuads |
| Weight | 7.2 g | Same |
| Mounting Pattern | **20 × 20 mm** | Same |
| Hole Dia | **3.5 mm** (M2/M3) | Same |
| Voltage | 3S–6S | Same |
| Continuous Current | 35A per channel | Same |
| Burst Current | 45A (5 sec) | Same |
| Firmware | BLHeli_S (J-H-40) | Same |

### 6.4 HGLRC Specter 60A

*Note: Only produced as 4-in-1, not single ESC.*

**30×30 variant (8-bit):**

| Property | Value |
|----------|-------|
| PCB Size | 37 × 42.7 mm |
| Weight | ~14 g |
| Mounting Pattern | 30.5 × 30.5 mm (M3) |
| Voltage | 2S–6S |
| Current | 60A cont / 70A burst (10s) |
| Firmware | BLHeli_S (J-H-30) |

**20×20 variant (G071 32-bit):**

| Property | Value |
|----------|-------|
| PCB Size | 44 × 36 × 7 mm |
| Weight | 19.5 g |
| Mounting Pattern | 20 × 20 mm (M3) |
| Voltage | 3S–6S |
| Current | 60A cont / 65A burst (10s) |
| MCU | STM32G071 (128K) |
| Firmware | BL32 (SPECTER60_G_128) |

### 6.5 Readytosky 40A (Single)

| Property | Value | Source |
|----------|-------|--------|
| PCB (L×W×H) | ~68–72 × 24–25 × 8–9 mm | Amazon |
| Weight | ~33–34 g (with BEC); ~26 g (OPTO) | Same |
| Mounting | Non-standard (generic ~3 mm holes) | Same |
| Voltage | 2S–4S (OPTO: 2S–6S) | Same |
| Current | 40A cont / 60A burst (10s) | Same |
| BEC | 5V/3A (standard version only) | Same |
| Firmware | Pre-programmed, **not user-flashable** | Same |

---

## 7. Motors

| Motor | Stator | Weight | Dia × H (mm) | Shaft | Mount Pattern | Screws | Voltage | KV |
|-------|--------|--------|--------------|-------|---------------|--------|---------|----|
| Axisflying AE2207 | 22×7 | 31.4 g | 27.2 × 33.3 | 5 mm | 16×16 mm | M3 | 6S | 1850 |
| NEEBRC 2807 V3 | 28×7 | 55 g | 34.5 × 20.4 can | 5 mm* | 16×16 or 19×19* | M3* | 3–6S | 1300 |
| HGLRC Specter 1804 | 18×4 | 13.3 g | 22.68 × 13.2 | 1.5 mm (M2 threaded) | 12×12 mm | M2 | 3–4S | 3500 |
| AKK 1407 | 14×7 | ~17 g | ~20 × 37 | 5 mm | 12×12 mm | M2 | 3–4S | 3500 |
| HGLRC Specter 1303.5 | 13×3.5 | 7.15 g | 17.53 × 11.7 | 1.5 mm (M2 threaded) | 9×9 mm | M2 | 2–4S | 5500 |
| Happymodel EX1103 | 11×3 | 3.8 g | 13.5 × 15.5 | 1.5 mm | 7 mm (T-Mount) | M1.4/1.6 | 1–2S | 11000 |
| Readytosky 2212 | 22×12 | 56 g | 28 × 28 × 46 | 6 mm | 16×19 mm | M3 | 3–4S | 920 |

*\* NEEBRC 2807: mounting pattern not confirmed from manufacturer — verify with seller (Woo-RC Store) before designing mounts.*

### Detailed Motor Specs

**Axisflying AE2207 1850KV:**
- Max power: 797 W (60s), Peak current: 33 A, Max thrust: >1.6 kg
- Prop range: 5", Config: 12N14P N52H arc magnets
- Source: racedayquads.com, amazon.sg

**NEEBRC 2807 1300KV (V3):**
- Max current: 45 A, Max power: 1550 W
- Internal resistance: 55 mOhm, No-load current: ≤1.0A @ 10V
- Prop range: 7–10"
- Source: druav.com, AliExpress SKU 1005009531848814

**HGLRC Specter 1804 3500KV:**
- Max current: 24.5 A, Max power: 392 W
- Prop range: 3–4", Rotor: 7075 Al, Stator: Kawasaki 1200 silicon steel
- Source: speedyfpv.com, druav.com

**AKK 1407 3500KV:**
- Budget rebrand of standard 1407 class. Limited published specs.
- Source: rc-help.com forum, rotorbuilds.com build 23670

**HGLRC Specter 1303.5 5500KV:**
- Max current: 8.9 A, Max power: 130 W
- Prop range: 2–4" (ideal 2–3"), Config: 9N12P
- Source: hobbydrone.cz, robu.in

**Happymodel EX1103 11000KV:**
- Max thrust: 121.9 g @ 7.4V with 2023R prop
- Max current: 9.2 A, Max power: 68.1 W
- For Mobula8, Bassline 2S, 2" toothpick
- Connector: JST 1.25 mm
- Source: tinywhoop.com, happymodel.cn

**Readytosky 2212 920KV:**
- Max thrust: ~500 g per motor
- Recommended ESC: 30 A
- Prop: 1045 (10×4.5"), Connector: 3.5 mm bullet
- Source: uavmarketplace.in, flyrobo.in

---

## 8. VTX / Cameras / Receivers

### VTX Units

| Component | Dimensions (mm) | Weight | Mounting | Voltage | Antenna |
|-----------|----------------|--------|----------|---------|---------|
| AKK A1918 | NOT FOUND | NOT FOUND | NOT FOUND | 7–28V (2–6S) | MMCX |
| HGLRC Zeus Nano 350mW | 18.6 × 13.6 × 6.0 | 2.4 g | 16/20/25.5 mm breakable tabs | 5V DC only | U.FL |
| Walksnail Avatar Pro V2 VTX | 33.0 × 33.0 × 10.5 | 17.6 g | 20/25.5 mm | 6–25.2V (2–6S) | IPEX ×1–2 |
| Walksnail Avatar Mini 1S Lite VTX | 30.0 × 30.0 × 6.5 | 5.1 g | 25.5 mm (M2) | 3.1–13V (1–3S) | IPEX-1 |

**HGLRC Zeus Nano 350mW Details:**
- Power levels: PIT / 25 / 100 / 200 / 350 mW
- 40 ch A/B/E/F/R bands, SmartAudio, push button
- Built-in mic, current: 75–400 mA depending on power level
- Source: [GetFPV](https://www.getfpv.com/hglrc-zeus-nano-350mw-16mm-20mm-25-5mm-vtx.html)

**Walksnail Avatar Pro V2:**
- Pro Cam: 19×19×24 mm, 9.5 g, Sony Starvis II 1/1.8", FOV 160°, F1.6
- Recording: 1080p@60fps, 720p@100/60fps
- Internal storage: 8 GB or 32 GB (no microSD)
- Avg latency: 22 ms
- Source: [Lumenier](https://www.lumenier.com/products/walksnail-avatar-hd-pro-kit-32gb-w-gyro)

**Walksnail Avatar Mini 1S Lite:**
- Cam: 14×14×16 mm, 1.8 g, 1/2.7" sensor, FOV 170°
- Total kit weight: ~7.8 g (VTX + camera + antenna)
- Bitrate: 25/50 Mbps
- Source: [Lumenier](https://www.lumenier.com/products/walksnail-avatar-hd-mini-1s-lite-kit-no-heat-sink)

### Cameras

| Camera | Dimensions (mm) | Weight | Mounting | Voltage | TVL / Sensor |
|--------|----------------|--------|----------|---------|-------------|
| Foxeer Razer Mini V3 | 22×22 (body) | 12 g | 22×22 mm (M2) | 5–25V | 1200 TVL, Sony 1/3" |
| Caddx Ant | 14×14 | 2 g | 14×14 / 19×19 mm | 3.7–18V | 1200 TVL, 1/3" CMOS |
| RunCam Racer Nano 4 | 14×14×20 | 4.5 g | 14×14 / 19×19 mm | 5–36V | 1200 TVL, WDR |

**Foxeer Razer Mini V3:** FOV 98° H, WDR 90 dB, 3DNR, ~4ms latency. 4-pin JST: GND/VCC/Video/OSD. Source: [Unmanned Tech](https://www.unmannedtechshop.co.uk/products/foxeer-razer-mini-v3-fpv-camera)

**Caddx Ant:** FOV 165° (1.8mm lens), 0.001 Lux min, Global WDR. 4-pin JST SH 1.0mm. Source: [Lumenier](https://www.lumenier.com/products/caddx-ant-1200tvl-1-8mm-fpv-nano-camera-14x14-black)

**RunCam Racer Nano 4:** FOV 160° D / 125° H / 97° V, 120mA@5V. Source: [RunCam Official](https://shop.runcam.com/runcam-racer-nano-4/)

### Receivers

| Receiver | Dimensions (mm) | Weight | Voltage | Antenna | Protocol |
|----------|----------------|--------|---------|---------|----------|
| BETAFPV SuperD ELRS (2.4 GHz) | 22 × 14 | 1.1 g | 5V | 2× IPEX | CRSF / ELRS |
| RadioMaster RP3 ELRS | 22 × 13 × 4 | 4.6 g (with antennas) | 5V | 2× IPEX | CRSF / ELRS |

**BETAFPV SuperD:** ESP32 PICO D4, dual SX1280, 20 dBm telemetry. FW: ELRS V3. Source: [Unmanned Tech](https://www.unmannedtechshop.co.uk/products/betafpv-superd-elrs-2-4g-diversity-receiver)

**RadioMaster RP3:** ESP8285, SX1280IMLTRT, Skyworks SE2431L LNA, up to 500Hz/F1000Hz. TCXO on V2. 4 pads: R/T/5V/G. Source: [ExpressLRS Docs](https://www.expresslrs.org/quick-start/receivers/radiomaster-rp-2400/)

---

## 9. Radios / Goggles / GPS

### Radio Transmitters

| Model | Dimensions (mm) | Weight | Screen | RF Module | Gimbals |
|-------|----------------|--------|--------|-----------|---------|
| RadioMaster Boxer Crush | 235 × 178 × 77 | 617 g (no bat), ~801 g (w/ 2×18650) | 128×64 mono LCD | ELRS 2.4 GHz (1W/30dBm) | AG01 CNC Hall |
| RadioMaster Pocket | 156.6 × 65.1 × 125.3 folded | 288 g (no bat), ~378–388 g (w/ 2×18650) | 128×64 mono LCD | ELRS or CC2500 (250mW max) | Hall-effect adj. |

**Boxer Crush:** STM32F407VGT6, EdgeTX, 16ch, JR module bay. Voltage: 6.6–8.4V (2S LiPo or 2×18650).  
**Pocket:** Nano module bay, USB-C QC3 charging, >2 km range @ 20 dBm.

### Goggles

| Model | Dimensions (mm) | Weight | Resolution | FOV | Battery | DVR |
|-------|----------------|--------|-----------|-----|---------|-----|
| Eachine EV800D | 180 × 145 × 82 | 362–375 g | 800×480 LCD | 140°/120° H/V | Built-in 7.4V 1200mAh | Yes, 720×576 |
| Walksnail Goggles X | NOT PUBLISHED | 290 g | 1920×1080 OLED @ 100 Hz per eye | 50° | Ext 2S–6S (7–26V) | Yes, microSD to 256 GB |

**EV800D:** Diversity (dual RX5808 PRO), 40 ch, <20ms delay, 2× RP-SMA.  
**Goggles X:** Dual OLED micro-displays, IPD 57–72 mm, diopter +2 to −6, HDMI in/out, AV in, built-in gyro, modular VRX.

### GPS Modules

| Model | Dims (mm) | Weight | Compass | GNSS Chip | Mounting | Voltage |
|-------|-----------|--------|---------|-----------|----------|---------|
| HGLRC M100-5883 | 21×21×8 | 7.73 g | QMC5883 | U-blox M10 | NOT FOUND | 3.3–5V |
| Matek M10Q-5883 | 20×20×12.4 | 8 g | QMC5883L | U-blox SAM-M10Q | 20×20 mm inferred | 4–9V |
| MicroAir M10G-5883 | 20×20×7.8 | 7 g | QMC5883L | U-blox M10050 | NOT FOUND | 5V |
| SEQURE M10-25Q | 25×25×8 | 12.2 g | QMC5883L | U-blox M10 | NOT FOUND | 5V |
| FPVDrone M8N | ~50 mm dia puck | ~32 g | IST8310 | U-blox NEO-M8N | NOT FOUND | 5V |

**HGLRC M100-5883:** 72ch, GPS+GLONASS+BDS+Galileo+SBAS, 10Hz, −160dBm, ~2m accuracy. Source: [RaceDayQuads](https://www.racedayquads.com/products/hglrc-m100-5883-gps-module-10th-gen)

**Matek M10Q-5883:** 5Hz (UBX), 4-constellation, JST-GH-6P connector (1.27mm pitch), 15×15×4mm patch antenna, ~13 mA. Source: [MatekSys](http://www.mateksys.com/?portfolio=m10q-5883)

**MicroAir M10G-5883:** U-blox M10 (M10050), up to 3 concurrent systems, 5Hz default (10Hz possible), SH1.0-6P connector, −167dBm, 2m CEP. Source: [PyroDrone](https://pyrodrone.com/products/micoair-m10g-5883-gnss-gps-compass-module)

**SEQURE M10-25Q:** U-blox M10, 72ch, 25mm ceramic patch, 1–10Hz, SH1.0-6P + solder pads, −40 to +85°C. Source: [SequreMall](https://sequremall.com/products/sequre-gps-small-size-fast-positioning-drone-fpv-return-qmc5883l-compass)

**FPVDrone M8N:** U-blox NEO-M8N, 72ch, 2.0m CEP, 5V, MAX2659ELT+ LNA, 26cm cable, ≤150mA. Source: [Amazon](https://www.amazon.com/FPVDrone-Compass-Protective-Anti-Interference-Controller/dp/B06XR6JHDW)

---

## Key Fitment Notes

1. **ROCK 5C Lite → Source One V5 or Mario 5:** The 86×56 mm PCB will NOT directly mount on standard 30.5×30.5 stack or 20×20 stack. Requires custom 3D-printed adapter plate or mounting directly to frame baseplate with standoffs.

2. **KHADAS VIM4:** 82×58 mm — also requires custom mounting (no standard FPV stack pattern). The 12V Molex power connector and bottom-side M.2 NVMe slot affect mounting height.

3. **Matek H743-WLITE:** Uses **25×25 mm M2** mounting (NOT 30.5×30.5). Cannot bolt directly to standard 30.5 mm frames without an adapter plate.

4. **SpeedyBee F405 Mini Stack:** The FC uses **20×20 mm** mounting, while its companion ESC (SpeedyBee BLS 35A Mini) also uses 20×20 mm. Pair for compact builds.

5. **F450 Clone:** Uses 50 mm APM/Pixhawk mounting pattern — NOT compatible with standard 30.5×30.5 FPV stacks. Arms are hollow molded nylon, not CF plate.

6. **NEEBRC 2807 motors (7" build):** 55 g each, 1550 W max power. Verify mounting pattern (16×16 vs 19×19) with seller before ordering.

7. **Walksnail Goggles X:** Physical dimensions not published by manufacturer. Weight is 290 g. 7–26V input range.

8. **MicoAir H743V2 AIO-45A** variant uses **25.5×25.5 mm** mounting (not 30.5×30.5 and not 20×20). Standalone FC variant uses standard 30.5×30.5.

---

*End of document. All data sourced from manufacturer wikis, official datasheets, CAD files, or verified retailer listings. NOT FOUND items noted explicitly.*
