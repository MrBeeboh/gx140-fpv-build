# FPV Fleet Wiring Diagrams & Pinout Tables
**Generated:** 2025-12-12
**Format:** Text tables for KiCad netlist import / manual wiring

---

## 1. ROCK 5C → FC UART (MSP/MAVLink) — Primary Telemetry

### Rock 5C GPIO (40-pin Header) — J2

All GPIOs 3.3V logic (max 3.63V). Source: [Radxa Rock 5C Hardware Interface](https://docs.radxa.com/en/rock5/rock5c/hardware-design/hardware-interface)

| Pin | Name | GPIO# | Alt Function | FC Connection | Wire | Notes |
|-----|------|-------|-------------|---------------|------|-------|
| 1 | 3.3V | — | Power | — | — | Do not connect to FC |
| 2 | 5V | — | Power in | **BEC 5V out** | 22 AWG red | **Main power input** |
| 3 | GPIO1_D7 | 63 | UART1_CTSN_M1, I2C8_SDA_M2 | — | — | Free |
| 4 | 5V | — | Power in | **BEC 5V out** | 22 AWG red | Parallel |
| 5 | GPIO1_D6 | 62 | UART1_RTSN_M1, I2C8_SCL_M2 | — | — | Free |
| 6 | GND | — | Ground | **BEC GND** / FC GND | 22 AWG black | **Main ground** |
| 7 | GPIO1_B3 | 43 | UART4_TX_M2 | — | — | Free |
| 8 | **GPIO0_B5** | **13** | **UART2_TX_M0**, I2C1_SCL_M0 | **FC UART_RX (TELEM2)** | 26 AWG | **MSP TX → FC RX** |
| 9 | GND | — | Ground | FC GND | 26 AWG black | Signal ground |
| 10 | **GPIO0_B6** | **14** | **UART2_RX_M0**, I2C1_SDA_M0 | **FC UART_TX (TELEM2)** | 26 AWG | **MSP RX ← FC TX** |
| 11 | GPIO4_B3 | 139 | UART8_CTSN_M0 | — | — | Free |
| 12 | GPIO4_B2 | 138 | UART8_RTSN_M0, SPI0_CS0_M1 | — | — | Free |
| 13 | GPIO4_B4 | 140 | UART9_TX_M1, PWM11_IR_M1 | — | — | Free |
| 14 | GND | — | Ground | — | — | — |
| 15 | GPIO1_A1 | 33 | UART6_TX_M1, I2C2_SCL_M4 | — | — | Free |
| 16 | GPIO1_A0 | 32 | UART6_RX_M1, I2C2_SDA_M4 | — | — | Free |
| 17 | 3.3V | — | Power | — | — | Do not connect |
| 18 | GPIO1_A2 | 34 | UART6_RTSN_M1, I2C4_SDA_M3 | — | — | Free |
| 19 | GND | — | Ground | — | — | — |
| 20 | GPIO0_C7 | 23 | UART1_RTSN_M2, I2C6_SDA_M0 | — | — | Free (USB4 via R104) |
| 21 | GPIO1_B2 | 42 | UART4_RX_M2, SPI0_MOSI_M2 | — | — | Free |
| 22 | GPIO1_B1 | 41 | SPI0_MISO_M2 | — | — | Free |
| 23 | GPIO1_B4 | 44 | UART7_RX_M2, SPI0_CS0_M2 | — | — | Free |
| 24 | GPIO4_A0 | 128 | UART9_RTSN_M1, I2S1_MCLK_M0 | — | — | Free |
| 25 | GND | — | Ground | — | — | — |
| 26 | GPIO1_A5 | 37 | SPI2_MOSI_M0 | — | — | Free |
| 27 | GPIO1_B0 | 40 | SPI2_CS1_M0 | — | — | Free |
| 28 | GND | — | Ground | — | — | — |
| 29 | GPIO1_B5 | 45 | UART7_TX_M2 | — | — | Free |
| 30 | GPIO1_A3 | 35 | PWM1_M2 | — | — | Free |
| 31 | GPIO1_A4 | 36 | SPI2_MISO_M0 | — | — | Free |
| 32 | GPIO0_D0 | 24 | UART1_CTSN_M2, SPI3_MISO_M2 | — | — | Free (USB4 via R106) |
| 33 | GND | — | Ground | — | — | — |
| 34 | GPIO4_B0 | 136 | UART8_TX_M0, I2C6_SDA_M3 | — | — | Free |
| 35 | GND | — | Ground | — | — | — |
| 36 | GPIO4_A2 | 130 | SPI0_CLK_M1, I2S1_LRCK_M0 | — | — | Free |
| 37 | GPIO4_A5 | 133 | UART3_TX_M2, I2C3_SDA_M2 | — | — | Free |
| 38 | GPIO4_A1 | 129 | SPI0_MOSI_M1, I2S1_SCLK_M0 | — | — | Free |
| 39 | GND | — | Ground | — | — | — |
| 40 | GPIO4_B1 | 137 | UART8_RX_M0, I2C6_SCL_M3, SPI0_CS1_M1 | — | — | Free |

### Critical Connections (Minimum Viable)
| Rock 5C | GPIO# | Wire | FC (TELEM2) | Protocol |
|---------|-------|------|-------------|----------|
| Pin 2 (5V) | — | 22 AWG red | BEC 5V | Power |
| Pin 6 (GND) | — | 22 AWG black | BEC GND | Power |
| Pin 8 (UART2_TX) | **GPIO 13** | 26 AWG | FC UART_RX | MSP/MAVLink |
| Pin 10 (UART2_RX) | **GPIO 14** | 26 AWG | FC UART_TX | MSP/MAVLink |
| Pin 9 (GND) | — | 26 AWG black | FC GND | Signal ref |

### Baude Rate Config
- **MSP:** 115200 / 921600 (Betaflight Configurator → Ports → TELEM2 → MSP)
- **MAVLink:** 57600 / 115200 (ArduPilot / INAV)

---

## 2. RADXA ZERO 3W → FC (Lightweight Bridge)

### Zero 3W GPIO (40-pin Header) — J2

All GPIOs 3.3V logic. Source: [Radxa Zero 3W Hardware Interface](https://docs.radxa.com/en/zero/zero3/hardware-design/hardware-interface)

| Pin | Name | GPIO# | Alt Function | FC Connection | Wire | Notes |
|-----|------|-------|-------------|---------------|------|-------|
| 1 | 3.3V | — | Power | — | — | Max 500mA |
| 2 | 5V | — | **Power in** | **FC 5V BEC** | 22 AWG red | **Main power** |
| 3 | GPIO1_A0 | 32 | UART3_RX_M0, I2C3_SCL_M0 | — | — | Free (alt UART) |
| 4 | 5V | — | **Power in** | **FC 5V BEC** | 22 AWG red | Parallel |
| 5 | GPIO1_A1 | 33 | UART3_TX_M0, I2C3_SDA_M0 | — | — | Free (alt UART) |
| 6 | GND | — | **Ground** | **FC GND** | 22 AWG black | **Main ground** |
| 7 | PWM14_M0 | 116 | PWM | — | — | Free |
| 8 | **GPIO0_D1** | **25** | **UART2_TX_M0** | **FC UART_RX (TELEM1)** | 26 AWG | **MSP TX → FC RX** |
| 9 | GND | — | Ground | FC GND | 26 AWG black | Signal ref |
| 10 | **GPIO0_D0** | **24** | **UART2_RX_M0** | **FC UART_TX (TELEM1)** | 26 AWG | **MSP RX ← FC TX** |
| 11 | GPIO3_A1 | 97 | Free | — | — | Free |
| 12 | GPIO3_A2 | 98 | I2S3_MCLK_M0 | — | — | Free |
| 13 | GPIO3_B0 | 104 | Free | — | — | Free |
| 14 | GND | — | Ground | — | — | — |
| 15 | GPIO4_C3 | 147 | SPI3_MOSI_M1 | — | — | Free |
| 16 | GPIO3_B1 | 105 | UART4_RX_M1 | FC LED | 26 AWG | Status LED |
| 17 | 3.3V | — | Power | — | — | Max 500mA |
| 18 | GPIO3_B2 | 106 | UART4_TX_M1 | FC BUZZER | 26 AWG | Beeper trigger |
| 19 | GPIO4_C5 | 149 | SPI3_MISO_M1 | — | — | Free |
| 20 | GND | — | Ground | — | — | — |
| 21 | GPIO4_C2 | 146 | SPI3_CLK_M1 | — | — | Free |
| 22 | GPIO3_C1 | 113 | I2S1_SDO2_M2 | — | — | Free |
| 23 | GPIO4_C6 | 150 | SPI3_CS0_M1 | — | — | Free |
| 24 | NC | — | Not connected | — | — | — |
| 25 | GND | — | Ground | — | — | — |
| 26 | GPIO4_B2 | 138 | I2C4_SDA_M0 | — | — | Free (USB2 alt) |
| 27 | GPIO3_B3 | **107** | **I2C5_SCL_M0** | **FC I2C1 SCL** | 28 AWG | **Optical flow clock** |
| 28 | GPIO4_B3 | 139 | I2C4_SCL_M0 | — | — | Free (USB2 alt) |
| 29 | GND | — | Ground | — | — | — |
| 30 | GPIO3_C2 | 114 | UART5_TX_M1 | — | — | Free |
| 31 | GPIO3_B4 | **108** | **I2C5_SDA_M0** | **FC I2C1 SDA** | 28 AWG | **Optical flow data** |
| 32 | GND | — | Ground | — | — | — |
| 33 | GPIO3_A7 | 103 | Free | — | — | Free |
| 34 | GPIO3_A6 | 102 | I2S3_SDI_M0 | — | — | Free |
| 35 | GPIO3_A5 | 101 | I2S3_SDO_M0 | — | — | Free |
| 36 | GPIO3_C3 | 115 | UART5_RX_M1 | — | — | Free |
| 37 | GPIO1_A4 | 36 | I2S1_SCLK_RX_M0 | — | — | Free |
| 38 | GND | — | Ground | — | — | — |
| 39 | 3.3V | — | Power | — | — | Max 500mA |
| 40 | NC | — | Not connected | — | — | — |

### Critical Connections (Zero 3W)
| Zero 3W | GPIO# | Wire | FC | Purpose |
|---------|-------|------|-----|---------|
| Pin 2 (5V) | — | 22 AWG red | 5V BEC | Power |
| Pin 6 (GND) | — | 22 AWG black | GND | Power |
| Pin 8 (UART2_TX) | **GPIO 25** | 26 AWG | UART_RX (TELEM1) | MSP TX → FC RX |
| Pin 10 (UART2_RX) | **GPIO 24** | 26 AWG | UART_TX (TELEM1) | MSP RX ← FC TX |
| Pin 29 (I2C5_SCL) | **GPIO 107** | 28 AWG | I2C1 SCL | Optical flow clock |
| Pin 31 (I2C5_SDA) | **GPIO 108** | 28 AWG | I2C1 SDA | Optical flow data |
| Pin 9 (GND) | — | 26 AWG black | GND | Signal ref |

---

## 3. KHADAS VIM4 — Ground Station HDMI Capture

### VIM4 Ports (No GPIO wiring needed for primary function)
| Port | Connection | Cable | Notes |
|------|------------|-------|-------|
| HDMI IN | **Walksnail Goggles X HDMI OUT** | HDMI 2.0 cable 2m | 4K@60 capture |
| HDMI OUT | Monitor / HDMI splitter | HDMI cable | Passthrough |
| USB3 | NVMe enclosure / Coral M.2 | USB3 cable | Storage / +4 TOPS |
| GbE | LAN / GCS tether | Cat6 | 1Gbps |
| 12V Barrel | 12V 2A supply | Barrel jack | Center positive |
| WiFi 6 | Router / Phone hotspot | — | Wireless stream |
| BT 5.1 | Gamepad / Phone | — | Control |

### Optional GPIO (40-pin) — Expansion
| Pin | Function | Use Case |
|-----|----------|----------|
| 3/5 | I2C | External sensors |
| 8/10 | UART | Secondary telemetry |
| 12 | PWM | Fan control |
| 16 | GPIO | Record trigger button |

---

## 4. FC STANDARD PORT MAPPINGS (Betaflight)

### Typical 30.5×30.5 FC (Radiolink F405, SpeedyBee F405, Matek H743)
| Port | Pins | Default Function | Our Use |
|------|------|------------------|---------|
| **USB** | USB-C | Configurator / MSP | Ground config |
| **UART1** | TX1/RX1 | MSP (USB fallback) | — |
| **UART2** | TX2/RX2 | **TELEM2** | **Rock 5C MSP** |
| **UART3** | TX3/RX3 | GPS | GPS module |
| **UART4** | TX4/RX4 | VTX (SmartAudio) | VTX control |
| **UART5** | TX5/RX5 | RX (CRSF/ELRS) | ELRS receiver |
| **UART6** | TX6/RX6 | — | Zero 3W MSP (if available) |
| **I2C1** | SDA/SCL | Baro/Compass | Zero 3W optical flow |
| **I2C2** | SDA/SCL | — | Free |
| **SPI1** | SCK/MISO/MOSI/CS | Gyro/OSD | Internal |
| **SPI2** | SCK/MISO/MOSI/CS | SD Card | Blackbox |
| **CAN** | CANH/CANL | — | Future (DroneCAN) |
| **ADC** | Vbat/Ibat | Battery monitor | Internal |
| **PWM** | M1-M8 | Motors/ESC | DShot600 |
| **LED** | LED_STRIP | WS2812 | Status |
| **BUZZER** | BZ+/BZ- | Beeper | Beeper |
| **CAM** | CAM_CTRL | Camera control | Optional |

### 20×20 FC (SpeedyBee F405 Mini, GoolRC F722)
| Port | Pins | Use |
|------|------|-----|
| UART1 | TX1/RX1 | USB/MSP |
| UART2 | TX2/RX2 | **Rock 5C / Zero 3W** |
| UART3 | TX3/RX3 | GPS |
| UART4 | TX4/RX4 | VTX / ELRS RX |
| I2C | SDA/SCL | Sensors / Optical flow |

---

## 5. BATTERY & POWER DISTRIBUTION

### 5" / 7" Build (6S LiPo)
```
LiPo 6S (22.2V)
    │
    ├─► XT60 → FC BAT pads (Vbat/Ibat sensing)
    │
    ├─► 5V 5A BEC (Pololu D24V50F5 / Matek 5V 5A)
    │       │
    │       ├─► 22 AWG → Rock 5C Pin 2/4 (5V)
    │       ├─► 22 AWG → Rock 5C Pin 6/9/14/20/25/30/34/39 (GND)
    │       ├─► 22 AWG → Zero 3W Pin 2/4 (5V)
    │       ├─► 22 AWG → Zero 3W Pin 6 (GND)
    │       ├─► Servo rail (if used)
    │       └─► LED strip (5V)
    │
    └─► ESC → Motors (DShot600)
```

### 3" Build (3-4S LiPo)
```
LiPo 4S (14.8V)
    │
    ├─► FC Vbat/Ibat
    │
    ├─► 5V 3A BEC (integrated in SpeedyBee F405 Mini)
    │       │
    │       ├─► 22 AWG → Zero 3W Pin 2/4 (5V)
    │       ├─► 22 AWG → Zero 3W Pin 6 (GND)
    │       └─► FC 5V rail
    │
    └─► ESC → Motors
```

### Goggle Battery (2S LiPo)
```
2S 7.4V → XT30 → Goggles / VTX / Camera
```

---

## 6. GROUND STATION WIRING (VIM4)

```
Walksnail Goggles X
    │
    HDMI OUT ──────────► HDMI IN (VIM4) ──► HDMI OUT ──► Monitor
    │
    USB-C ────────────► Power (2S LiPo via XT30)
    │
    UART ─────────────► ELRS Module (CRSF)

VIM4
    │
    HDMI IN ───────────► Capture pipeline
    HDMI OUT ──────────► HDMI splitter ──► Monitor + Recorder
    USB3 ──────────────► NVMe 512GB (recordings)
    USB3 ──────────────► Coral M.2 (optional +4 TOPS)
    GbE ───────────────► Router ──► Phone/PC (stream)
    12V ────────────────► 12V 2A Supply
```

---

## 7. WIRE GAUGE & LENGTH RECOMMENDATIONS

| Function | Gauge | Max Length | Color | Connector |
|----------|-------|------------|-------|-----------|
| Main 5V (BEC→SBC) | 22 AWG | 150mm | Red | JST-GH / bare |
| Main GND | 22 AWG | 150mm | Black | JST-GH / bare |
| Signal (UART/I2C) | 26-28 AWG | 200mm | Yellow/White | JST-GH / bare |
| ESC Signal | 26 AWG | 100mm | White | JST-SH / bare |
| Battery (XT60) | 14 AWG | 50mm | Red/Black | XT60 |
| Battery (XT30) | 18 AWG | 50mm | Red/Black | XT30 |
| LED Strip | 24 AWG | 300mm | Green | JST-SM |
| Beeper | 26 AWG | 100mm | Orange | JST-SH |

### Crimp Connectors Used
| Connector | Pitch | Use | Crimper |
|-----------|-------|-----|---------|
| JST-GH | 1.25mm | FC↔SBC, GPS, I2C | Engineer PA-09 |
| JST-SH | 1.0mm | ESC, Camera, LED | Engineer PA-09 |
| JST-SM | 2.5mm | Battery, High current | Engineer PA-20 |
| XT60 | — | 6S/4S Main | — |
| XT30 | — | 2S/3S, Goggles | — |
| BT2.0 | — | 1S Whoop | — |

---

## 8. KICAD NETLIST (S-Expression) — Import to Eeschema

```
(kicad_netlist
  (version 4)
  (tool "fpv_fleet_generator")
  (date "2025-12-12")
  (components
    (comp (ref "ROCK5C_1") (value "Radxa_Rock5C_Lite") (footprint "Package_DIP:DIP-40_W7.62mm") (libsource "fpv:SBC"))
    (comp (ref "ROCK5C_2") (value "Radxa_Rock5C_Lite") (footprint "Package_DIP:DIP-40_W7.62mm") (libsource "fpv:SBC"))
    (comp (ref "ZERO3W") (value "Radxa_Zero3W") (footprint "Package_DIP:DIP-40_W7.62mm") (libsource "fpv:SBC"))
    (comp (ref "VIM4") (value "Khadas_VIM4") (footprint "Package_DIP:DIP-40_W7.62mm") (libsource "fpv:SBC"))
    (comp (ref "FC_5INCH") (value "FC_F405_F722_H743") (footprint "Package_DIP:DIP-30_W7.62mm") (libsource "fpv:FC"))
    (comp (ref "FC_3INCH") (value "FC_F405_Mini") (footprint "Package_DIP:DIP-20_W7.62mm") (libsource "fpv:FC"))
    (comp (ref "BEC_5V5A") (value "Pololu_D24V50F5") (footprint "Package_TO_SOT:TO-220-3_Vertical") (libsource "fpv:Power"))
    (comp (ref "ESC_4IN1") (value "ESC_4in1_30A_60A") (footprint "fpv:ESC_4in1_30x30") (libsource "fpv:ESC"))
    (comp (ref "ESC_SINGLE") (value "ESC_Single_60A") (footprint "fpv:ESC_Single") (libsource "fpv:ESC"))
    (comp (ref "VOLTAGE") (value "LiPo_6S_22.2V") (footprint "Connector_XT60") (libsource "fpv:Battery"))
    (comp (ref "CAM_IMX219") (value "IMX219_Camera") (footprint "fpv:Camera_MIPI") (libsource "fpv:Camera"))
    (comp (ref "FLOW_PAA5100") (value "PAA5100_OpticalFlow") (footprint "fpv:Sensor_SPI") (libsource "fpv:Sensor"))
    (comp (ref "GPS_MATEK") (value "Matek_M10Q_5883") (footprint "fpv:GPS_M10") (libsource "fpv:GPS"))
  )
  (nets
    (net (code "1") (name "5V_SBC") (nodes (ref "BEC_5V5A" pin "VOUT") (ref "ROCK5C_1" pin "2") (ref "ROCK5C_1" pin "4") (ref "ROCK5C_2" pin "2") (ref "ROCK5C_2" pin "4") (ref "ZERO3W" pin "2") (ref "ZERO3W" pin "4")))
    (net (code "2") (name "GND") (nodes (ref "BEC_5V5A" pin "GND") (ref "ROCK5C_1" pin "6") (ref "ROCK5C_1" pin "9") (ref "ROCK5C_1" pin "14") (ref "ROCK5C_2" pin "6") (ref "ROCK5C_2" pin "9") (ref "ZERO3W" pin "6") (ref "FC_5INCH" pin "GND") (ref "FC_3INCH" pin "GND") (ref "ESC_4IN1" pin "GND") (ref "VOLTAGE" pin "GND")))
    (net (code "3") (name "UART_ROCK5C_MSP") (nodes (ref "ROCK5C_1" pin "8") (ref "FC_5INCH" pin "UART2_RX")))  // ROCK5C TX → FC RX
    (net (code "4") (name "UART_ROCK5C_MSP_RET") (nodes (ref "ROCK5C_1" pin "10") (ref "FC_5INCH" pin "UART2_TX")))  // FC TX → ROCK5C RX
    (net (code "5") (name "UART_ZERO3W_MSP") (nodes (ref "ZERO3W" pin "8") (ref "FC_3INCH" pin "UART2_RX")))  // ZERO3W TX → FC RX
    (net (code "6") (name "UART_ZERO3W_MSP_RET") (nodes (ref "ZERO3W" pin "10") (ref "FC_3INCH" pin "UART2_TX")))  // FC TX → ZERO3W RX
    (net (code "7") (name "I2C_FLOW") (nodes (ref "ZERO3W" pin "29") (ref "FLOW_PAA5100" pin "SDA") (ref "ZERO3W" pin "31") (ref "FLOW_PAA5100" pin "SCL")))  // I2C5_SCL_M0 (GPIO107), I2C5_SDA_M0 (GPIO108)
    (net (code "8") (name "UART_GPS") (nodes (ref "FC_5INCH" pin "UART3_TX") (ref "GPS_MATEK" pin "RX") (ref "FC_5INCH" pin "UART3_RX") (ref "GPS_MATEK" pin "TX")))
    (net (code "9") (name "UART_VTX") (nodes (ref "FC_5INCH" pin "UART4_TX") (ref "VTX" pin "RX") (ref "FC_5INCH" pin "UART4_RX") (ref "VTX" pin "TX")))
    (net (code "10") (name "UART_ELRS") (nodes (ref "FC_5INCH" pin "UART5_TX") (ref "ELRS_RX" pin "RX") (ref "FC_5INCH" pin "UART5_RX") (ref "ELRS_RX" pin "TX")))
    (net (code "11") (name "PWM_MOTORS") (nodes (ref "FC_5INCH" pin "M1") (ref "ESC_4IN1" pin "S1") ... (ref "FC_5INCH" pin "M8") (ref "ESC_4IN1" pin "S8")))
    (net (code "12") (name "VBAT") (nodes (ref "VOLTAGE" pin "VCC") (ref "FC_5INCH" pin "VBAT") (ref "ESC_4IN1" pin "VBAT")))
    (net (code "13") (name "IBAT") (nodes (ref "VOLTAGE" pin "GND") (ref "FC_5INCH" pin "IBAT") (ref "ESC_4IN1" pin "GND")))
    (net (code "14") (name "HDMI_VIM4_IN") (nodes (ref "GOGGLES_X" pin "HDMI_OUT") (ref "VIM4" pin "HDMI_IN")))
    (net (code "15") (name "HDMI_VIM4_OUT") (nodes (ref "VIM4" pin "HDMI_OUT") (ref "MONITOR" pin "HDMI_IN") (ref "RECORDER" pin "HDMI_IN")))
  )
)
```

---

## 9. ASSEMBLY WIRING CHECKLIST PER BUILD

### 5" Analog (Rock 5C #1)
- [ ] BEC 5V 5A → Rock 5C Pins 2,4,6,9,14,20,25,30,34,39
- [ ] Rock 5C Pin 8 (UART2_TX) → FC UART2_RX (TELEM2)
- [ ] Rock 5C Pin 10 (UART2_RX) → FC UART2_TX (TELEM2)
- [ ] Rock 5C Pin 9 (GND) → FC GND (signal ref)
- [ ] GPS → FC UART3
- [ ] VTX SmartAudio → FC UART4
- [ ] ELRS RX → FC UART5 (CRSF)
- [ ] ESC DShot → FC M1-M4
- [ ] LED Strip → FC LED_STRIP
- [ ] Beeper → FC BUZZER
- [ ] Battery XT60 → FC VBAT/IBAT + ESC
- [ ] Rock 5C NVMe installed
- [ ] Rock 5C heatsink + fan mounted
- [ ] All wires routed in channels, secured
- [ ] Smoke stopper test before first plug

### 3" Analog (Zero 3W)
- [ ] FC 5V BEC → Zero 3W Pins 2,4,6
- [ ] Zero 3W Pin 8 (UART2_TX) → FC UART2_RX (TELEM1)
- [ ] Zero 3W Pin 10 (UART2_RX) → FC UART2_TX (TELEM1)
- [ ] Zero 3W Pin 3,5 (I2C) → Optical Flow PAA5100
- [ ] GPS → FC UART3
- [ ] ELRS RX → FC UART4/5
- [ ] ESC DShot → FC M1-M4
- [ ] Battery → FC + ESC
- [ ] Zero 3W header soldered

### 7" Long Range (Rock 5C #2 or MicoAir H743 AIO)
- [ ] Decision: Rock 5C + Matek H743-WLITE OR MicoAir H743 AIO
- [ ] If Rock 5C: Same as 5" but GPS Rescue tuned
- [ ] If MicoAir: Built-in 45A 4in1, no separate ESC
- [ ] Crossfire/ELRS Diversity RX
- [ ] Dual GPS (Matek M10Q-5883 ×2)
- [ ] 8× NEEBRC 2807 motors
- [ ] 6S batteries

---

## 10. CONTINUITY TEST MATRIX (Post-Assembly)

| Test | Expected | Method |
|------|----------|--------|
| BEC 5V → Rock 5C Pin 2 | < 0.1Ω | Multimeter continuity |
| BEC GND → Rock 5C Pin 6 | < 0.1Ω | Multimeter continuity |
| Rock 5C Pin 8 → FC UART2_RX | < 0.5Ω | Multimeter continuity |
| Rock 5C Pin 10 → FC UART2_TX | < 0.5Ω | Multimeter continuity |
| FC UART2_TX → Rock 5C Pin 10 | Signal check | Oscilloscope / logic analyzer |
| GPS TX → FC UART3_RX | Signal check | Betaflight Configurator GPS tab |
| VTX SmartAudio → FC UART4 | Signal check | VTX tables in Configurator |
| ELRS RX → FC UART5 | Signal check | RSSI/LQ in OSD |
| ESC DShot → FC M1-M4 | Motor spin test | Configurator Motors tab |
| Battery voltage → FC VBAT | 22.2V ±0.1V | Multimeter |
| Current sensor → FC IBAT | 0A at rest | Configurator |
| Smoke stopper | No light | Visual |