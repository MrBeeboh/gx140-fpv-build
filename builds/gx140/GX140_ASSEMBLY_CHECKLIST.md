# GX140 3" Analog — Assembly Flow & Checklist
**Builder:** GROK  
**Frame:** GX140 140mm, 4mm carbon, 20×20 twin-tower  
**Target AUW:** <250g

---

## ASSEMBLY FLOW (Mermaid — renders in GitHub/VS Code/Notion)

```mermaid
flowchart TD
    START([Unbox GX140 Frame]) --> FRAME[Install 8x M3x25mm Standoffs<br/>4 front tower + 4 rear tower]
    FRAME --> MOUNT[Mount Specter 1804 Motors<br/>M2 screws, 12x12mm — DIRECT FIT]
    MOUNT --> WIRES[Route Motor Wires<br/>Along Arm Undersides]
    WIRES --> ESC[Mount ESC BLS 35A<br/>Bottom of Front Tower]
    ESC --> FC[Mount F405 Mini FC<br/>Nylon Nut Between ESC and FC]
    FC --> SOLDER[Solder Motor Wires → ESC<br/>Solder XT30 → FC VBAT]
    SOLDER --> VTX[Mount Zeus 350mW<br/>Rear Tower 20x20 Adapter]
    VTX --> VTX_WIRE[VTX SmartAudio → FC UART4 TX<br/>VTX 5V/GND → FC Rail]
    VTX_WIRE --> CAM[Camera Mount<br/>Caddx Ant + included 19x19 adapter]
    CAM --> CAM_WIRE[CAM → VTX CAM_IN]
    CAM_WIRE --> RX[Mount SuperD RX<br/>Top Plate, 3M Tape]
    RX --> RX_WIRE[RX → FC UART5 CRSF]
    RX_WIRE --> ANT[Antenna Placement<br/>ANT1 Vertical Left<br/>ANT2 Horizontal Rear]
    ANT --> SMOKE{SMOKE TEST<br/>ShortSaver}
    SMOKE -->|LIGHT ON| FIX[Find Short — DISCONNECT]
    SMOKE -->|NO LIGHT| BF[Betaflight Config<br/>Ports, Rates, OSD, Modes]
    BF --> MOTOR_TEST[Motor Direction Test<br/>Props OFF]
    MOTOR_TEST --> PROPS[Install Props<br/>M1+M4 CW, M2+M3 CCW]
    PROPS --> MAIDEN[MAIDEN FLIGHT]
    MAIDEN --> PASS{Hover 30s<br/>Punch 75%<br/>Roll/Pitch/Yaw}
    PASS -->|Pass| DONE([BUILD COMPLETE])
    PASS -->|Fail| TUNE[PID Tune<br/>Check Filters]
    TUNE --> MAIDEN
    FIX --> SMOKE
```

---

## PRE-FLIGHT PATTERN (Mermaid Gantt)

```mermaid
gantt
    title GX140 Build Timeline
    dateFormat mm
    axisFormat %M min
    
    section Frame
    Unbox & Inspect        :f1, 0, 3m
    Install Standoffs      :f2, after f1, 5m
    
    section Power
    Mount Motors           :m1, after f2, 5m
    Mount ESC              :m2, after m1, 3m
    Mount FC               :m3, after m2, 3m
    Solder Connections     :m4, after m3, 15m
    
    section Electronics
    Mount VTX              :v1, after m4, 5m
    Mount Camera           :v2, after v1, 5m
    Mount RX               :v3, after v2, 5m
    
    section Testing
    Smoke Test             :t1, after v3, 2m
    Betaflight Config      :t2, after t1, 15m
    Motor Direction        :t3, after t2, 3m
    
    section Flight
    Props On               :p1, after t3, 2m
    Maiden Flight          :p2, after p1, 10m
    PID Tuning             :p3, after p2, 30m
```

---

## FITMENT MATRIX (Quick Reference)

| # | Component | Mount Pattern | Frame Match | Verdict | Fix if Needed |
|---|-----------|---------------|-------------|---------|---------------|
| 1 | GX140 Frame | 20×20 twin tower | — | ✅ | — |
| 2 | F405 Mini FC | 20×20mm | 20×20mm | ✅ | — |
| 3 | BLS 35A ESC | 20×20mm | 20×20mm | ✅ | — |
| 4 | Specter 1804 | 12×12mm M2 | 12×12mm M2 | ✅ | Direct fit |
| 5 | Zeus 350mW | 16×16→20×20 adapter | 20×20mm rear | ✅ | Use 20×20 adapter |
| 6 | Caddx Ant | 14×14 / 19×19 adapter | 19mm HD bay | ✅ | Adapter included |
| 7 | SuperD RX | 20×20mm / tape | Top plate | ✅ | VHB tape |
| 8 | XT30 pigtail | Solder to FC | FC VBAT pads | ✅ | — |
| 9 | 2S 550mAh | Strap mount | Bottom plate | ✅ | Anti-slip pad |

---

## POST-BUILD VALIDATION

### Electrical
- [ ] Resistance: Battery + to FC VBAT < 0.1Ω
- [ ] Resistance: Battery - to FC GND < 0.1Ω
- [ ] Continuity: FC TX4 → VTX SmartAudio pad < 0.5Ω
- [ ] Continuity: FC TX5 → RX RX pad < 0.5Ω
- [ ] No continuity between adjacent signal pins
- [ ] No continuity between any pin and carbon frame

### Mechanical
- [ ] All 8 standoffs tight (hand + 1/8 turn)
- [ ] All 16 motor screws tight
- [ ] No loose wires in prop arc
- [ ] VTX antenna SMA tight
- [ ] Battery strap holds pack without shifting
- [ ] Camera angle set and locked

### Software
- [ ] Betaflight 2025.12 firmware
- [ ] DShot600 protocol
- [ ] Bidirectional DShot ON
- [ ] RPM filter ON (3 harmonics)
- [ ] Dynamic notch ON (100-600Hz)
- [ ] UART4: VTX (SmartAudio) at 115200
- [ ] UART5: Serial RX (CRSF) at 420000
- [ ] OSD elements positioned and visible
- [ ] Failsafe: Stage 1 = 1.5s hold, Stage 2 = Drop
- [ ] ARM angle limit = 180° (any angle)

### Flight
- [ ] Hover rock solid, no drift
- [ ] Punch-out clean, no oscillations
- [ ] Roll/Pitch stops clean, no bounce
- [ ] Yaw responsive, no wag
- [ ] Video clear, no lines in throttle
- [ ] RSSI/LQ stable (≥90 LQ at close range)
- [ ] Flight time ≥4 min on 2S 550mAh
- [ ] Motor temp post-flight < 50°C
- [ ] ESC temp post-flight < 60°C
- [ ] Battery voltage post-flight > 3.5V/cell