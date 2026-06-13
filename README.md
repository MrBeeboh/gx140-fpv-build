# FPV Drone Fleet Project — Master Index
**Location:** `/home/mike/projects/Drone Projects/`
**Generated:** 2025-12-12
**Last Updated:** 2025-12-12
**Verification:** Claude Code `--chrome` researcher validated SBC/motor/GPS/radio dimensions against manufacturer wikis, DXF files, and datasheets. Mounting patterns corrected (Matek 25×25 M2, Rock 5C 86×56mm).

---

## DIRECTORY STRUCTURE

```
/home/mike/projects/Drone Projects/
├── inventory/
│   └── fleet_inventory.md          # Complete parts inventory (119 line items)
├── sbc/
│   └── sbc_deployment_checklist.md # SBC companion computer deployment
├── hardware/
│   └── hardware_reference.md       # Dimensions, pinouts, fitment data
├── cad/
│   └── mounts.scad                 # OpenSCAD parametric mounts
├── wiring/
│   └── wiring_diagrams.md          # Pin-to-pin tables, KiCad netlist
├── assembly/
│   └── assembly_sheets.md          # Step-by-step build sheets
└── docs/
    └── (future: flight logs, tuning notes, etc.)
```

---

## QUICK NAVIGATION

### Inventory & Status
| Document | Purpose | Key Data |
|----------|---------|----------|
| `inventory/fleet_inventory.md` | Complete BOM | 6 builds, 119 items, gaps, priority orders |
| `inventory/fleet_inventory.md` | Walksnail ecosystem | Complete (Avatar Pro, Mini 1S, Goggles X, Patch V2) |

### SBC Companion Computers
| Document | Purpose | Key Data |
|----------|---------|----------|
| `sbc/sbc_deployment_checklist.md` | Deploy Rock 5C ×2, Zero 3W, VIM4 | Hardware, software, power, cooling, model perf |

### Mechanical & CAD
| Document | Purpose | Key Data |
|----------|---------|----------|
| `cad/mounts.scad` | 3D printable mounts | Rock 5C, Zero 3W, VIM4, cameras, wire channels |
| `hardware/hardware_reference.md` | Fitment bible | All dims, pinouts, clearance rules, thermal limits |

### Electrical & Wiring
| Document | Purpose | Key Data |
|----------|---------|----------|
| `wiring/wiring_diagrams.md` | Wire-by-wire | SBC↔FC UART, power distro, KiCad netlist, test matrix |

### Build Instructions
| Document | Purpose | Key Data |
|----------|---------|----------|
| `assembly/assembly_sheets.md` | Step-by-step | 6 builds, torque specs, pre-flight checklist |

---

## BUILD STATUS SUMMARY

| # | Build | Frame | Status | Blocker |
|---|-------|-------|--------|---------|
| 1 | **5" Analog Freestyle** | Mark5 HD (3D printed) | **READY** | Need Source One V5 carbon frame |
| 2 | **5" DJI O4 Cinematic** | Mario 5 O4 XH | **BLOCKED** | **DJI O4 Pro Air Unit ($150)** |
| 3 | **3" Analog Freestyle** | GX140 140mm | **READY** | Zero 3W header solder |
| 4 | **2-2.5" Whoop** | Mobula8 ×2 | **RTF** | Bind only |
| 5 | **7" Long Range** | FPVDrone 295mm | **PENDING** | FC decision: Matek H743 + singles vs MicoAir AIO |
| 6 | **450mm Platform** | YoungRC / HAWK'S WORK | **READY** | Pick FC |

### SBC Deployment Status
| SBC | Qty | Status | Next Step |
|-----|-----|--------|-----------|
| Radxa Rock 5C Lite 16GB | 2 | Have | Mounts, heatsinks, NVMe, BEC |
| Radxa Zero 3W 4GB | 1 | Have | **Solder 40-pin header**, mount |
| Khadas VIM4 8+32GB | 1 | Have | Active cooler, NVMe, 12V supply |

### Priority Shopping List
| # | Item | Qty | Est $ | For |
|---|------|-----|-------|-----|
| 1 | Source One V5 5" Frame | 1 | $80 | Build 1 (replace 3D printed) |
| 2 | DJI O4 Pro Air Unit | 1 | $150 | Build 2 (unblock) |
| 3 | SpeedyBee 50A/60A 4in1 3-6S | 3 | $45 | Build 1, spare |
| 4 | VIFLY ShortSaver | 1 | $15 | **Safety — all builds** |
| 5 | Rock 5C PCIe M.2 adapter + NVMe 256GB | 2 | $35 | SBC model storage |
| 6 | Rock 5C Heatsink + Fan | 2 | $25 | Sustained NPU |
| 7 | 5V 5A BEC (Matek/Pololu) | 2 | $30 | Rock 5C power |
| 8 | 40-pin Header + Solder (Zero 3W) | 1 | $5 | GPIO access |
| 9 | VIM4 Cooler + 12V Supply + NVMe 512GB | 1 | $60 | HDMI capture |
| 10 | OVONIC 6S 1300mAh 100C+ | 6 | $25 | 6S depth |

---

## KEY TECHNICAL SPECS (QUICK REF)

### SBC Compute
| SBC | NPU | Best Model | FPS (YOLOv11n) | Power |
|-----|-----|------------|----------------|-------|
| Rock 5C (RK3588S2) | **6 TOPS** | 8B LLM, Seg, Depth | **120 FPS** | 5V 5A |
| Zero 3W (RK3566) | **~1 TOPS** | YOLOv11n, Flow, KWS | **20 FPS** | 5V 1A |
| VIM4 (A311D2) | **3.2 TOPS** | YOLOv11s, Post-flight heavy | **65 FPS** | 12V 2A |

### Critical Wiring (Rock 5C → FC)
| Rock 5C Pin | Signal | FC Port | Wire |
|-------------|--------|---------|------|
| 2,4 (5V) | Power | BEC 5V | 22 AWG red |
| 6,9,14... (GND) | Ground | BEC GND | 22 AWG black |
| 8 (UART2_TX) | MSP TX | UART2_RX | 26 AWG |
| 10 (UART2_RX) | MSP RX | UART2_TX | 26 AWG |

### Critical Wiring (Zero 3W → FC)
| Zero 3W Pin | Signal | FC Port | Wire |
|-------------|--------|---------|------|
| 2,4 (5V) | Power | FC 5V BEC | 22 AWG red |
| 6 (GND) | Ground | FC GND | 22 AWG black |
| 8 (UART2_TX) | MSP TX | UART2_RX | 26 AWG |
| 10 (UART2_RX) | MSP RX | UART2_TX | 26 AWG |
| 3/5 (I2C) | Optical Flow | I2C1 | 28 AWG |

---

## NEXT ACTIONS (This Week)

### Monday-Tuesday: Hardware Procurement
- [ ] Order Source One V5 frame
- [ ] Order DJI O4 Pro Air Unit
- [ ] Order SpeedyBee 60A 4in1 ×3
- [ ] Order VIFLY ShortSaver
- [ ] Order Rock 5C PCIe adapters + NVMe
- [ ] Order Rock 5C heatsinks ×2
- [ ] Order 5V 5A BECs ×2
- [ ] Order Zero 3W header + solder

### Wednesday-Thursday: SBC Prep
- [ ] Flash Radxa Debian 12 on Rock 5C ×2
- [ ] Flash Radxa Debian on Zero 3W (after header solder)
- [ ] Flash Khadas Ubuntu 22.04 on VIM4
- [ ] Install RKNPU2 toolkit on Rock 5Cs
- [ ] Install NN SDK on VIM4
- [ ] Bench test YOLOv11n on Rock 5C (verify 120 FPS)

### Friday: Assembly Starts
- [ ] Build 3" GX140 (Zero 3W) — simplest, validates SBC→FC link
- [ ] Build 5" Mark5 (Rock 5C #1) — main freestyle
- [ ] Test MSP telemetry both builds
- [ ] Smoke stopper every build

### Weekend: Ground Station
- [ ] VIM4: Cooler + NVMe + 12V supply
- [ ] Test HDMI IN from Walksnail Goggles X
- [ ] GStreamer capture pipeline
- [ ] Stream to phone/PC

---

## FILE REFERENCES FOR CODE GENERATION

When you need to generate code later:
- **MSP Bridge (Python):** `wiring/wiring_diagrams.md` → UART tables
- **YOLO RKNN Quantize:** `sbc/sbc_deployment_checklist.md` → model perf table
- **GStreamer Pipeline:** `sbc/sbc_deployment_checklist.md` → VIM4 HDMI section
- **OpenSCAD Mounts:** `cad/mounts.scad` → render STLs
- **KiCad Schematic:** `wiring/wiring_diagrams.md` → netlist section
- **Assembly:** `assembly/assembly_sheets.md` → step-by-step

---

## CONTACT / NOTES
- **User:** Mike (Harold persona)
- **Platform:** HAL2026 (dual Arc B70, 64GB RAM)
- **FPV Style:** Freestyle + Long Range + Cinematic
- **Radio:** RadioMaster Boxer Crush + Pocket (ELRS)
- **Goggles:** Walksnail Goggles X (primary), EV800D (analog backup)
- **Safety:** Smoke stopper mandatory, props off for motor test

---

*End of Index — all project docs in `/home/mike/projects/Drone Projects/`*