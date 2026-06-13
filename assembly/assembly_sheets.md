# FPV Fleet Assembly Sheets
**Generated:** 2025-12-12

---

## BUILD 1: 5" ANALOG FREESTYLE — Mark5 HD Frame
**FC:** Radiolink F405 / SpeedyBee F405 Mini Stack
**ESC:** Radiolink FLYCOLOR 55A 4in1
**Motors:** Axisflying 2207 1850KV ×4
**Props:** HQProp Ethix S5 5x4x3
**VTX:** AKK A1918 200-1000mW
**Cam:** Foxeer Razer Mini V3
**RX:** BETAFPV SuperD Diversity / RadioMaster RP3
**SBC:** Rock 5C Lite #1
**Battery:** OVONIC 6S 1300mAh / HRB 6S 1800mAh

### PARTS CHECKLIST
- [ ] Mark5 HD frame (carbon — **need to order Source One V5**)
- [ ] Radiolink F405 FC
- [ ] Radiolink FLYCOLOR 55A 4in1 ESC
- [ ] Axisflying 2207 1850KV motors ×4
- [ ] HQProp Ethix S5 5x4x3 props (8 CW, 8 CCW)
- [ ] AKK A1918 VTX + SMA antenna (RHCP)
- [ ] Foxeer Razer Mini V3 camera
- [ ] BETAFPV SuperD ELRS Diversity RX
- [ ] Rock 5C Lite #1 + mount + heatsink + fan + NVMe
- [ ] 5V 5A BEC (Pololu D24V50F5)
- [ ] M3×8mm standoffs ×4 (FC stack)
- [ ] M3×12mm standoffs ×4 (Rock 5C mount)
- [ ] M3×6mm screws ×16
- [ ] M3 nylon nuts ×8
- [ ] M5×6mm motor screws ×16 + M5 locknuts ×16
- [ ] XT60 pigtail (male)
- [ ] 22 AWG silicone wire (red/black) 200mm
- [ ] 26 AWG silicone wire (assorted) 300mm
- [ ] JST-GH 1.25mm connectors + pins
- [ ] Heat shrink 2mm/4mm/6mm
- [ ] 3M double-sided tape (for RX/VTX)
- [ ] Battery strap ×2
- [ ] Prop tool

### ASSEMBLY SEQUENCE

#### Step 1: Frame Prep (10 min)
1. Unpack frame, verify all carbon parts present
2. Clean edges with IPA if needed
3. Install M3×8mm standoffs at 30.5mm pattern (bottom plate)
4. Install M3×12mm standoffs at Rock 5C mount positions (top plate)

#### Step 2: Motor Mount (15 min)
1. Mount motors to arms: M5×6mm screws + locknuts
2. Torque: 1.5 Nm (hand tight + 1/4 turn)
3. Verify motor rotation: CW/CCW alternating
4. Route motor wires through arm channels

#### Step 3: ESC Install (10 min)
1. Place 4in1 ESC on FC standoffs (bottom of stack)
2. Connect motor wires to ESC pads (M1-M4)
3. Solder or plug: verify pinout matches motor order
4. Add capacitor (included) to ESC VBAT/GND

#### Step 4: FC Install (10 min)
1. Mount FC on standoffs above ESC (M3×8mm)
3. Connect ESC signal wires to FC M1-M4
4. Solder XT60 pigtail to FC VBAT/GND pads
5. Solder 5V BEC to FC 5V/GND (or use FC 5V out if 3A+)

#### Step 5: Rock 5C Mount (15 min)
1. Assemble Rock 5C mount: standoffs + heatsink + fan
2. Install NVMe SSD in PCIe slot
3. Mount Rock 5C on top plate standoffs
4. Connect 5V BEC → Rock 5C pins 2,4,6,9,14,20,25,30,34,39
5. Connect UART: Rock 5C Pin 8 → FC UART2_RX, Pin 10 → FC UART2_TX, Pin 9 → FC GND

#### Step 6: VTX & Camera (10 min)
1. Mount camera on front plate (adjustable angle)
2. Mount VTX on rear/top plate (3M tape + zip tie)
3. Connect camera → VTX CAM_IN
4. Connect VTX SmartAudio → FC UART4 (TX4/RX4)
5. Connect VTX power → FC 5V/GND (or BEC direct)

#### Step 7: RX Install (5 min)
1. Mount SuperD Diversity on top plate (3M tape)
2. Route antennas: one vertical, one horizontal
3. Connect RX → FC UART5 (CRSF): TX5→RX, RX5→TX, 5V, GND

#### Step 8: GPS & Extras (10 min)
1. Mount GPS (Matek M10Q-5883) on GPS mast
2. Connect GPS → FC UART3
3. Mount LED strip on rear arm
4. Connect LED → FC LED_STRIP
5. Mount beeper → FC BUZZER

#### Step 9: Wiring & Dress (15 min)
1. Route all wires in channels
2. Secure with zip ties every 50mm
3. Verify no wire touches props/carbon edges
4. Add heat shrink to all solder joints

#### Step 10: Pre-Flight Checks (10 min)
1. [ ] Continuity: BEC 5V → Rock 5C, BEC GND → Rock 5C
2. [ ] Continuity: Rock 5C UART ↔ FC UART2
3. [ ] Continuity: GPS → FC UART3
4. [ ] Continuity: VTX SmartAudio → FC UART4
5. [ ] Continuity: RX → FC UART5
6. [ ] Continuity: ESC signals → FC M1-M4
7. [ ] Battery voltage at FC VBAT pad
8. [ ] Smoke stopper test
9. [ ] Betaflight Configurator: verify all sensors, ports, motors
10. [ ] Motor direction test (props OFF)
11. [ ] SBC boot test (SSH to Rock 5C)
12. [ ] MSP telemetry flowing (Configurator CLI: `status`)

### TORQUE SPECS
| Fastener | Torque | Notes |
|----------|--------|-------|
| M3 standoffs | 0.5 Nm | Hand tight + 1/8 turn |
| M5 motor screws | 1.5 Nm | Hand tight + 1/4 turn |
| M3 stack screws | 0.5 Nm | Nylon nuts — don't overtorque |
| Camera screws | 0.3 Nm | Tiny — just snug |

---

## BUILD 2: 3" ANALOG FREESTYLE — GX140 Frame
**FC:** SpeedyBee F405 Mini Stack (35A 4in1)
**ESC:** Integrated 35A 4in1 BLS
**Motors:** HGLRC Specter 1804 3500KV ×4
**Props:** GEMFAN 3052 3in
**VTX:** HGLRC Zeus 350mW
**Cam:** Caddx Ant 1200TVL
**RX:** SuperD Diversity / RP3 ELRS
**SBC:** Radxa Zero 3W
**Battery:** BETAFPV 2S 550mAh LiHV / OVONIC 2S 850mAh

### PARTS CHECKLIST
- [ ] GX140 140mm frame
- [ ] SpeedyBee F405 Mini Stack
- [ ] HGLRC Specter 1804 3500KV ×4
- [ ] GEMFAN 3052 props
- [ ] HGLRC Zeus 350mW VTX
- [ ] Caddx Ant camera
- [ ] SuperD Diversity / RP3 ELRS
- [ ] Radxa Zero 3W + 40-pin header soldered + mount
- [ ] M2.5×8mm standoffs ×4 (FC)
- [ ] M2.5×8mm standoffs ×4 (Zero 3W)
- [ ] M2.5×6mm screws ×16
- [ ] M2.5 nylon nuts ×8
- [ ] M3×5mm motor screws ×16 (1804 uses M3)
- [ ] XT30 pigtail
- [ ] 22/26 AWG wire
- [ ] JST-GH connectors
- [ ] Optical flow PAA5100 (optional)

### ASSEMBLY SEQUENCE
1. **Frame prep:** Install 20×20 standoffs
2. **Motors:** M3×5mm to arms, verify CW/CCW
3. **Stack:** Place 4in1 ESC bottom, FC top (20×20 pattern)
4. **Zero 3W:** Solder 40-pin header first, mount above FC
5. **VTX/Cam:** Front camera, rear VTX
6. **RX:** Top plate, antennas vertical/horizontal
7. **GPS:** On mast (optional for 3")
8. **Wiring:** FC 5V BEC → Zero 3W pins 2,4,6; UART2 cross-connect; I2C to optical flow
9. **Smoke test → Configurator → Motor test → SBC test**

### SPECIAL NOTES
- Zero 3W **no GPIO header** — must solder 40-pin header first
- SpeedyBee Mini 5V BEC only 3A — Zero 3W draws ~0.6A, OK
- 20×20 stack height tight — keep wires flat
- 3" props close to frame — verify Zero 3W mount clears

---

## BUILD 3: 2-2.5" WHOOP — Mobula8 (×2 Complete)
**Status:** RTF — Bind and fly
**FC:** Built-in X12 AIO (40A 4in1)
**Motors:** EX1103 11000KV
**VTX/Cam:** Built-in
**RX:** Built-in ELRS V3
**Battery:** BETAFPV 2S 550mAh LiHV

### PRE-FLIGHT
- [ ] Bind to RadioMaster Pocket / Boxer Crush
- [ ] Verify motor directions in Configurator
- [ ] Set failsafe (GPS Rescue not applicable)
- [ ] Check prop direction (all CCW on whoop? — verify)

---

## BUILD 4: 7" LONG RANGE — FPVDrone 295mm
**Status:** PENDING FC DECISION
**Options:**
- A) Matek H743-WLITE + Readytosky 40A singles ×4 + Rock 5C #2
- B) MicoAir H743V2 AIO (45A 4in1 built-in) + Rock 5C #2
- C) MicoAir H743 AIO alone (no SBC)

### PARTS NEEDED
- [ ] Frame (have)
- [ ] FC + ESC per decision above
- [ ] NEEBRC 2807 1300KV ×8 (have)
- [ ] HQProp 7x3.5x3 ×8 (have)
- [ ] GPS ×2 (Matek M10Q-5883 + FPVDrone M8N) (have)
- [ ] VTX: AKK A1918 / HGLRC Zeus (have)
- [ ] Cam: RunCam Racer Nano 4 (have)
- [ ] RX: SuperD Diversity + RP1 backup (have)
- [ ] Rock 5C #2 + mount + heatsink + NVMe (need mount parts)
- [ ] 5V 5A BEC ×2 (need)
- [ ] 4S/6S batteries (have HRB 4S + OVONIC 4S)

### DECISION MATRIX
| Factor | Matek H743 + Singles | MicoAir AIO | MicoAir Only |
|--------|---------------------|-------------|--------------|
| Mounting | **25×25 M2** (needs adapter) | 30.5×30.5 / **25.5×25.5 AIO-45A** | 25.5×25.5 |
| Redundancy | ESC separate | All-in-one | All-in-one |
| SBC support | Rock 5C UART | Rock 5C UART | None |
| Weight | Higher | Lower | Lowest |
| Current capability | 40A×4 = 160A | 45A×4 = 180A | 45A×4 |
| Complexity | Medium | Low | Lowest |
| **Recommendation** | **Option A** — best for SBC + redundancy |

---

## BUILD 5: 450MM PLATFORM — YoungRC / HAWK'S WORK
**FC:** Matek H743-WLITE + PDB-HEX OR GoolRC F722
**ESC:** Readytosky 40A singles ×4
**Motors:** Readytosky 2212 920KV ×4
**Props:** 10x4.5 ×12
**VTX:** AKK A1918
**Cam:** Readytosky 1200TVL
**RX:** ELRS (RP3)
**Battery:** HRB 4S 4000/5000mAh

### STATUS
- Frame: Have both
- FC: Have both (choose one)
- ESC: Have singles
- Motors: Have
- Props: Have
- VTX/Cam: Have
- RX: Have
- **Ready to assemble** — pick FC, wire per 5" but 4S

---

## BUILD 6: MARIO 5 O4 — DJI O4 CINEMATIC
**Frame:** Mario 5 O4 XH 226mm
**VTX/Cam:** **NEED DJI O4 PRO AIR UNIT**
**FC:** GoolRC F722 / SoloGood F722 Stack
**ESC:** SoloGood 60A BLS8
**Motors:** Axisflying 2207 1850KV
**RX:** SuperD Diversity
**Battery:** OVONIC 6S 1300mAh

### BLOCKER
**DJI O4 Pro Air Unit — $150 — MUST ORDER**

---

## UNIVERSAL PRE-FLIGHT CHECKLIST (ALL BUILDS)

### Electrical
- [ ] Smoke stopper test (no light = pass)
- [ ] Continuity: all power rails (5V, 3.3V, GND)
- [ ] Continuity: all signal wires (UART, I2C, SPI, PWM)
- [ ] No shorts between adjacent pins
- [ ] Battery leads: correct polarity at FC/ESC

### Mechanical
- [ ] All screws torqued to spec
- [ ] No loose wires near props
- [ ] Antennas secured, not touching carbon
- [ ] Camera angle set (verify in Configurator)
- [ ] Battery strap holds pack firmly
- [ ] Props correct orientation (CW/CCW)

### Software (Betaflight Configurator)
- [ ] Firmware current (2025.12)
- [ ] Ports: MSP, GPS, VTX, RX, SBC UART all assigned
- [ ] Sensor: Gyro/Accel calibrated
- [ ] Motor direction: all correct
- [ ] Motor protocol: DShot600
- [ ] RPM filter: ON (if bidirectional DShot)
- [ ] Dynamic notch: ON
- [ ] ESC telemetry: ON
- [ ] OSD: elements positioned
- [ ] Failsafe: stage 1/2 configured
- [ ] GPS Rescue: tuned (if GPS)
- [ ] SBC MSP: telemetry flowing (`status` in CLI)

### SBC Specific
- [ ] OS booted (SSH accessible)
- [ ] RKNPU2 / NN SDK loaded
- [ ] Model inference test passes
- [ ] MSP bridge running (Rock 5C) / Telemetry bridge (Zero 3W)
- [ ] NVMe mounted (Rock 5C)
- [ ] Temps under load < 70°C

### Field Test
- [ ] Hover test 30s — no vibrations
- [ ] Punch-out — no oscillations
- [ ] Roll/Flip — clean stops, no bounce
- [ ] GPS lock < 60s (if equipped)
- [ ] RTH test (if GPS Rescue)
- [ ] SBC telemetry logging
- [ ] Post-flight: motor temps < 50°C, SBC temps < 65°C