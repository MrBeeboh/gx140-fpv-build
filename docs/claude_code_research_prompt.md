# Drone Project Dimensional Research — Claude Code Prompt
# Run with: claude --chrome -p "$(cat this_file.txt)"
# Or interactively: claude --chrome then paste the prompt below

---

## MISSION
Extract exact dimensions, mounting patterns, pinouts, and specifications for every component in my FPV drone fleet. Output as structured markdown tables with mm measurements, verified from manufacturer datasheets and documentation.

## COMPONENTS TO RESEARCH

### 1. RADXA ROCK 5C LITE (RK3588S2) — 2 units
- URL: https://wiki.radxa.com/Rock5/5c
- Need: PCB dimensions (L×W×H mm), mounting hole positions (x,y from origin), hole diameter, GPIO pinout (all 40 pins with function names), weight, power specs (voltage/current range), thermal limits, MIPI CSI pinout, PCIe connector type and location
- Verify against: https://dl.radxa.com/rock5/5c/

### 2. RADXA ZERO 3W (RK3566) — 1 unit  
- URL: https://wiki.radxa.com/Zero3w
- Need: Same as above — PCB dims, mounting holes, GPIO pinout, weight, power, MIPI CSI
- Castellations: pin pitch and arrangement for soldering 40-pin header

### 3. KHADAS VIM4 (A311D2) — 1 unit
- URL: https://docs.khadas.com/products/sbc/vim4/start
- Need: PCB dims, mounting holes, GPIO pinout, HDMI IN specifications, power (12V barrel), active cooler dimensions, NVMe M.2 slot length
- Verify: https://dl.khadas.com/products/vim4/specs/

### 4. FRAMES (all 7)
| Frame | URL to search |
|-------|--------------|
| Source One V5 5" | Search: "TBS Source One V5 frame dimensions 3D print" |
| iFlight Mark5 HD 5" | Search: "iFlight Mark5 HD frame specs dimensions mounting" |
| GX140 140mm 3" | Search: "GX140 frame dimensions 140mm 3 inch FPV" |
| Mario 5 O4 5" | Search: "Mario 5 O4 frame 226mm DJI O4 specs" |
| FPVDrone 295mm 7" | Search: "FPVDrone 295mm 7 inch frame dimensions" |
| F450 clone 450mm | Standard — 450mm wheelbase, 30.5×30.5 stack |

### 5. FLIGHT CONTROLLERS
| FC | Search terms |
|----|-------------|
| Radiolink F405 | "Radiolink F405 flight controller pinout dimensions" |
| SpeedyBee F405 Mini Stack | "SpeedyBee F405 Mini 20x20 dimensions pinout" |
| GoolRC GF30F722 | "GoolRC F722 flight controller 30x30 pinout" |
| SoloGood F722 60A Stack | "SoloGood F722 60A stack dimensions pinout" |
| Matek H743-WLITE | https://www.mateksys.com/?portfolio=h743-wlite |
| MicoAir H743V2 AIO | "MicoAir743V2 AIO flight controller specs" |

### 6. ESCs  
| ESC | Search terms |
|-----|-------------|
| Radiolink FLYCOLOR 55A 4in1 | "Flycolor 55A 4in1 ESC 30x30 dimensions" |
| SoloGood BLS8 60A 4in1 | "SoloGood 60A BLS8 4in1 ESC specs" |
| SpeedyBee BLS 35A (20×20) | Standard 20×20 4in1 dimensions |
| HGLRC Specter 60A single | "HGLRC Specter 60A ESC dimensions weight" |
| Readytosky 40A singles | "Readytosky 40A brushless ESC dimensions" |

### 7. MOTORS — mounting pattern + weight + can dimensions
| Motor | Search |
|-------|--------|
| Axisflying 2207 1850KV | "Axisflying 2207 dimensions weight mounting pattern" |
| NEEBRC 2807 1300KV | "NEEBRC 2807 1300KV motor specs weight" |
| HGLRC Specter 1804 3500KV | "HGLRC Specter 1804 dimensions weight" |
| AKK 1407 3500KV | "AKK 1407 motor dimensions weight" |
| HGLRC Specter 1303.5 5500KV | "HGLRC 1303.5 motor dimensions weight" |
| Happymodel EX1103 11000KV | "EX1103 11000KV motor specs" |
| Readytosky 2212 920KV | Standard 2212 dimensions |

### 8. VTX / CAMERAS / RX
| Component | Search |
|-----------|--------|
| AKK A1918 VTX | "AKK A1918 5.8G VTX dimensions pinout" |
| HGLRC Zeus 350mW | "HGLRC Zeus VTX specs dimensions" |
| Walksnail Avatar Pro | "Walksnail Avatar Pro dimensions weight mounting" |
| Walksnail Avatar HD Mini 1S | "Walksnail Avatar Mini 1S lite kit specs" |
| Foxeer Razer Mini V3 | "Foxeer Razer Mini V3 camera dimensions" |
| Caddx Ant camera | "Caddx Ant FPV camera dimensions weight" |
| RunCam Racer Nano 4 | "RunCam Racer Nano 4 dimensions" |
| BETAFPV SuperD ELRS Diversity RX | "BETAFPV SuperD ELRS diversity receiver dimensions" |
| RadioMaster RP3 ELRS RX | "RP3 ELRS receiver dimensions weight" |

### 9. RADIOS / GOGGLES / GPS
| Component | Search |
|-----------|--------|
| RadioMaster Boxer Crush | "RadioMaster Boxer dimensions screen resolution weight" |
| RadioMaster Pocket | "RadioMaster Pocket dimensions weight" |
| EV800D Goggles | "EV800D FPV goggles dimensions weight" |
| Walksnail Goggles X | "Walksnail Avatar Goggles X specs dimensions weight" |
| HGLRC M100-5883 GPS | "HGLRC M100 GPS module dimensions weight" |
| Matek M10Q-5883 | "Matek M10Q-5883 GPS dimensions" |
| MicroAir M10G | "MicroAir M10G GPS module specs" |
| SEQURE M10-25Q | "SEQURE M10Q GPS module dimensions" |
| FPVDrone M8N GPS | "FPVDrone M8N GPS module specs" |

## OUTPUT FORMAT

For each component, provide this exact table structure:

```markdown
### [COMPONENT NAME]
| Property | Value | Source |
|----------|-------|--------|
| Dimensions (L×W×H mm) | | |
| Weight (g) | | |
| Mounting Pattern (mm) | | |
| Mounting Hole Dia (mm) | | |
| Power (V/A) | | |
| Pinout / Ports | | |

**Pinout Table (if applicable):**
| Pin | Function | Notes |
|-----|----------|-------|
```

## RULES
1. Extract EXACT numbers from manufacturer pages — do not estimate
2. If a dimension cannot be found, mark as "NOT FOUND — [what was searched]"
3. For FPV standard sizes (30.5×30.5, 20×20, 16×16), verify against manufacturer
4. Include direct URLs to source pages for every number
5. Prefer manufacturer wiki/docs over 3rd party reviews
6. For GPIO pinouts, include the linux GPIO number (e.g., GPIO14, GPIO15)
7. Metric units only (mm, g, V, A)
8. When you find a full specification PDF, download and parse it

## PRIORITY ORDER
Research in this order — these are the most critical for fitment:
1. Rock 5C Lite (will ride on 5" and 7" builds — must fit)
2. Source One V5 frame + Mario 5 O4 (primary frames)
3. Matek H743-WLITE + SpeedyBee F405 Mini (primary FCs)
4. NEEBRC 2807 + Axisflying 2207 + EX1103 motors
5. Walksnail Goggles X + VIM4 ground station
6. Remaining components as time allows

## SAVE OUTPUT
Save complete results to: `/home/mike/projects/Drone Projects/hardware/verified_dimensions.md`