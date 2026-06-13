# FPV Drone Fleet — Project Scope & Build Plan
**Version:** 1.0  
**Date:** 2025-12-12  
**Owner:** Mike  
**Status:** Planning Complete — Procurement Blocked  

---

## 1. EXECUTIVE SUMMARY

Six-aircraft FPV fleet with onboard AI companion computers (Rock 5C, Zero 3W) and a ground-based video processing station (Khadas VIM4). Analog + Walksnail HD dual ecosystem. ELRS control. Betaflight configuration with GPS rescue on all builds ≥3".

**Total builds:** 6  
**SBC companions:** 3  
**Ground station:** 1  
**Current state:** 80% parts in hand, 20% procurement needed  

---

## 2. WHAT WE'RE BUILDING

| # | Build | Class | Role | FC | VTX | SBC | Status |
|---|-------|-------|------|-----|-----|-----|--------|
| 1 | **5" Analog Freestyle** | 5" 6S | Daily flyer, CV testbed | Radiolink F405 + 55A 4in1 | AKK A1918 (analog) | Rock 5C #1 | Parts ready, need carbon frame |
| 2 | **5" Walksnail HD Cinematic** | 5" 6S | Cinematic, HD recording | SoloGood F722 + 60A BLS8 | Walksnail Avatar Pro (have) | None | Parts ready — use Walksnail, NOT DJI |
| 3 | **3" Analog Freestyle** | 3" 3-4S | Proximity, indoor CV | SpeedyBee F405 Mini + 35A 4in1 | HGLRC Zeus 350mW (analog) | Zero 3W | Parts ready, need header solder |
| 4 | **2-2.5" Whoop** (×2) | 85mm 1-2S | Indoor, proximity | X12 AIO (built-in) | Built-in | None | RTF — bind only |
| 5 | **7" Long Range** | 7" 4-6S | LR, GPS rescue, CV | Matek H743-WLITE + 40A singles | AKK A1918 (analog) | Rock 5C #2 | FC decision pending |
| 6 | **450mm Platform** | 450mm 4S | Payload, mapping | GoolRC F722 / Matek H743 | AKK A1918 (analog) | None | Parts ready |
| — | **Ground Station** | Desktop | HDMI capture + record | — | Walksnail Goggles X input | Khadas VIM4 | Need cooler + NVMe |

---

## 3. SCOPE BOUNDARIES

### IN SCOPE
- [x] FPV aircraft assembly (frame, stack, motors, VTX, cam, RX)
- [x] SBC companion computer integration (Rock 5C, Zero 3W)
- [x] FC↔SBC UART telemetry bridge (MSP/MAVLink)
- [x] Betaflight 2025.12 configuration (rates, filters, GPS rescue, OSD)
- [x] ELRS binding, failsafe, GPS rescue testing
- [x] Ground station HDMI capture pipeline (VIM4)
- [x] 3D printed mounts for SBC integration
- [x] Wire harness fabrication with verified pinouts
- [x] Pre-flight safety checks (smoke stopper mandatory)
- [x] Maiden flights + tuning

### OUT OF SCOPE (v1)
- [ ] Autonomous flight / waypoint missions (v2)
- [ ] Real-time object detection during flight (v2 — needs model quantization)
- [ ] Live video streaming from Rock 5C (v2 — needs MIPI camera)
- [ ] Drone-to-drone communication (v3)
- [ ] Swarm / formation flight (v3)
- [ ] DJI O3/O4 ecosystem (user chose Walksnail — incompatible)
- [ ] Custom PCB design for SBC↔FC interface (using JST-GH wires for v1)
- [ ] Long-range 900MHz (ELRS 2.4GHz only for v1)

---

## 4. DEPENDENCIES & BLOCKERS

### Critical Path — MUST ORDER
| # | Item | Qty | Est $ | Blocks Build(s) | Priority |
|---|------|-----|-------|-----------------|----------|
| 1 | **Source One V5 5" carbon frame** | 1 | $80 | #1 (5" Analog) | P0 |
| 2 | **VIFLY ShortSaver smoke stopper** | 1 | $15 | ALL (safety) | P0 |
| 3 | **40-pin header 2.54mm + solder** | 1 | $5 | #3 (Zero 3W GPIO) | P0 |
| 4 | **DJI O4 Pro Air Unit** | 1 | $150 | #2 (5" DJI) | P1 |
| 4 | **Rock 5C PCIe M.2 adapter + NVMe 256GB** | 2 | $70 | SBC deploy | P1 |
| 5 | **Rock 5C active heatsink + 3010 fan** | 2 | $50 | SBC deploy | P1 |
| 6 | **5V 5A BEC (Matek/Pololu)** | 2 | $30 | SBC power | P1 |
| 7 | **Matek H743 25×25→30.5 adapter plate** | 1 | $10 | #5 (7" LR) | P2 |
| 8 | **OVONIC 6S 1300mAh 100C+** | 4-6 | $150 | All 6S builds | P2 |

**Total procurement:** ~$350 (P0-P1: ~$250, P2: ~$160)

### Non-Purchase Blockers
| Blocker | Resolution | Effort |
|---------|------------|--------|
| Zero 3W no GPIO header | Solder 40-pin header | 15 min |
| Matek H743 incompatible with 30.5mm frames | Print adapter plate or use MicoAir AIO instead | 1 hr |
| Rock 5C doesn't fit standard stack patterns | 3D print custom mount (OpenSCAD ready) | 2 hr |
| Mark5 frame is 3D printed copy | Replace with Source One V5 carbon | Purchase |
| HGLRC Specter 60A = 4in1 (corrected) | Use as 4in1, not single | 0 min |

---

## 5. BUILD SCHEDULE

### Phase 1: Tools & Parts (Week 1)
```
Day 1-2: Order items #1-7 above
Day 3-4: Install OpenSCAD, Blender, ezdxf (for mount generation)
Day 5: Zero 3W — solder 40-pin header
Day 6-7: Flash Radxa Debian 12 on Rock 5C ×2 + Zero 3W
```

### Phase 2: First Builds (Week 2)
```
Day 1: Build #3 (3" GX140 + Zero 3W) — simplest, validates SBC↔FC link
Day 2: Build #4 (Mobula8 ×2) — bind to Boxer/Pocket, set rates
Day 3: Bench test Rock 5C #1 — YOLOv11n RKNN quantization, verify 120 FPS
Day 4: Build #1 (5" Source One V5 + Rock 5C #1) — primary freestyle
Day 5: Maiden flights #1 + #3 — hover test, punch-out, PID tuning
```

### Phase 3: Advanced Builds (Week 3)
```
Day 1-2: Build #6 (450mm Platform) — payload testing, GPS rescue
Day 3: Build #5 (7" LR) — FC decision, adapter plate, GPS ×2
Day 4: Maiden flight #5 — GPS rescue validation
Day 5: Ground station — VIM4 cooler + NVMe + HDMI capture test
```

### Phase 4: Walksnail Cinematic (Week 3-4)
```
Day 1: Build #2 (Mario 5 O4 frame + Walksnail Avatar Pro) — use existing Walksnail, no DJI
Day 2: Bind Walksnail to Goggles X, camera setup
Day 3: Maiden cinematic flights, gyroflow stabilization
```

---

## 6. SUCCESS CRITERIA

### Per Build
| Build | Hover | Punch-out | GPS Lock | GPS Rescue | SBC MSP | YOLO Inference |
|-------|-------|-----------|----------|------------|---------|----------------|
| #1 5" Analog | ✅ | ✅ | ✅ <60s | ✅ <15m radius | ✅ 921600 baud | ✅ >100 FPS |
| #2 5" Walksnail | ✅ | ✅ | ✅ <60s | ✅ <15m radius | N/A | N/A |
| #3 3" Analog | ✅ | ✅ | ✅ <60s | ✅ <10m radius | ✅ 921600 baud | ✅ >15 FPS |
| #4 Whoop ×2 | ✅ | ✅ | N/A | N/A | N/A | N/A |
| #5 7" LR | ✅ | ✅ | ✅ <30s | ✅ <5m radius | ✅ 921600 baud | ✅ >100 FPS |
| #6 450mm | ✅ | ✅ | ✅ <60s | ✅ <10m radius | N/A | N/A |
| Ground Station | N/A | N/A | N/A | N/A | N/A | N/A |

### Ground Station
- [ ] HDMI IN from Walksnail Goggles X → captured at 4K@60
- [ ] H.265 hardware encode → NVMe recording
- [ ] Real-time detection overlay on stream
- [ ] RTSP/WebRTC stream to phone/PC
- [ ] Post-flight model inference on recorded footage

### System-Wide
- [ ] All builds bound to Boxer Crush + Pocket (ELRS)
- [ ] All builds smoke-stopper tested before first plug
- [ ] All SBCs reachable via SSH
- [ ] All builds documented with diff + dump backups
- [ ] GPS rescue validated on all GPS-equipped builds
- [ ] Motor temps < 50°C, SBC temps < 65°C under load

---

## 7. ARCHITECTURE DIAGRAM (Text)

```
                    ┌─────────────────────────────────┐
                    │     RadioMaster Boxer Crush      │
                    │     (ELRS 2.4GHz, EdgeTX)        │
                    └────────────┬────────────────────┘
                                 │ CRSF 2.4GHz
                    ┌────────────▼────────────────────┐
                    │     BETAFPV SuperD Diversity     │
                    │     (ELRS V3, dual antenna)      │
                    └────────────┬────────────────────┘
                                 │ UART (CRSF)
                    ┌────────────▼────────────────────┐
                    │          Flight Controller        │
                    │   F405/F722/H743 + 4in1 ESC      │
                    │   Betaflight 2025.12              │
                    └──┬──────┬──────┬──────┬──────┬───┘
                       │      │      │      │      │
              ┌────────▼─┐ ┌──▼──┐ ┌─▼──┐ ┌─▼──┐ ┌─▼──────┐
              │Rock 5C #1│ │ GPS │ │VTX │ │Cam │ │ Motors │
              │(UART MSP)│ │M10Q │ │AKK │ │Fox │ │ Axisfly│
              │CV + ROS2 │ │     │ │    │ │Razr│ │ 2207   │
              └──────────┘ └─────┘ └────┘ └────┘ └────────┘

                    ┌─────────────────────────────────┐
                    │     Walksnail Goggles X V2       │
                    │     HDMI OUT ───────────────┐    │
                    └─────────────────────────────│────┘
                                                  │
                    ┌─────────────────────────────▼────┐
                    │       Khadas VIM4 (Ground)        │
                    │   HDMI IN → H.265 encode → NVMe   │
                    │   Real-time detect → stream phone │
                    └──────────────────────────────────┘
```

---

## 8. FILE INDEX (All Docs)

| File | Content | Status |
|------|---------|--------|
| `README.md` | Master index + next actions | ✅ |
| `inventory/fleet_inventory.md` | 119 items, 6 builds, gaps | ✅ Verified |
| `sbc/sbc_deployment_checklist.md` | SBC HW/SW/perf/power/cooling | ✅ Updated dims |
| `hardware/hardware_reference.md` | Dims, pinouts, clearance, thermal | ✅ Updated (Matek, Rock 5C) |
| `hardware/verified_dimensions.md` | Claude Code research — 759 lines | ✅ Verified |
| `cad/mounts.scad` | OpenSCAD parametric mounts | ✅ Updated PCB dims |
| `wiring/wiring_diagrams.md` | Pin-to-pin, KiCad netlist, test matrix | ✅ GPIOs verified |
| `assembly/assembly_sheets.md` | Step-by-step 6 builds, torque, pre-flight | ✅ Updated (Matek note) |
| `docs/claude_code_research_prompt.md` | Reusable research prompt | ✅ |
| `datasheets/betaflight_2025_12_cli_reference.md` | CLI reference (38 KB) | ✅ |
| `datasheets/betaflight_msp_protocol.md` | MSP protocol (223 KB) | ✅ |
| **`docs/SCOPE.md`** | **This document** | ✅ |

---

## 9. NEXT ACTION (Right Now)

The single most impactful thing you can do in the next 10 minutes:

```
Open Amazon → order these 3 items:

1. "Source One V5 5 inch frame kit carbon" → $60-80
2. "VIFLY ShortSaver 2-6S XT60 smoke stopper" → $15
3. "2.54mm 40-pin male header strip" → $5
```

That unblocks Build #1 (primary freestyle with Rock 5C), protects all future builds (safety), and gives the Zero 3W I/O it needs for Build #3.

**You do NOT need to buy DJI O4 — you own a complete Walksnail system.**