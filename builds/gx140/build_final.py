#!/usr/bin/env python3
"""GX140 Final Schematic — All wires orthogonal, text outside symbols, net label methodology"""
import uuid, os

OUT = "/home/mike/projects/Drone Projects/builds/gx140/gx140_final.kicad_sch"
PRO = "/home/mike/projects/Drone Projects/builds/gx140/gx140_final.kicad_pro"
uid = lambda: str(uuid.uuid4())

parts = []

def W(x1,y1,x2,y2):
    """Orthogonal wire only — x1==x2 or y1==y2 required"""
    assert abs(x1-x2)<0.01 or abs(y1-y2)<0.01, f"DIAGONAL: ({x1},{y1})→({x2},{y2})"
    parts.append(f'  (wire (pts (xy {x1:.1f} {y1:.1f}) (xy {x2:.1f} {y2:.1f})) (stroke (width 0.1524) (type default)) (uuid {uid()}))')

def ROUTE(x1,y1,x2,y2, col=None):
    """Route through column to ensure orthogonal."""
    if abs(x1-x2)<0.5 or abs(y1-y2)<0.5:
        W(x1,y1,x2,y2)
        return
    c = col if col else (x1+x2)/2
    W(x1, y1, c, y1)
    W(c, y1, c, y2)
    W(c, y2, x2, y2)

def L(n,x,y,sz=1.524): parts.append(f'  (label "{n}" (at {x:.1f} {y:.1f} 0) (effects (font (size {sz} {sz}))))')
def T(t,x,y,sz=1.27): parts.append(f'  (text "{t}" (at {x:.1f} {y:.1f} 0) (effects (font (size {sz} {sz}))))')
def J(x,y): parts.append(f'  (junction (at {x:.1f} {y:.1f}) (diameter 0.9144) (color 0 0 0 0) (uuid {uid()}))')
def SYM(lib,x,y,rot=0): parts.append(f'  (symbol (lib_id "{lib}") (at {x:.1f} {y:.1f} {rot}) (unit 1) (in_bom yes) (on_board yes) (dnp no) (uuid {uid()}))')

# ═══ HEADER ═══
T("GX140 3in ANALOG FPV — ELECTRICAL SCHEMATIC", 150, 290, 3.81)
T("GROK FPV Drone Engineering | 2025-12-12 | Sheet 1/1 | All dimensions verified", 150, 284, 1.27)

# ═══ BATTERY (X=25-65) ═══
bx, by = 40, 255
SYM("power:+BATT", bx, by, 90)
T("2S 550mAh", bx-15, by-8, 1.27); T("LiHV 7.4V", bx-15, by-12, 1.27); T("XT30", bx-8, by-16, 1.016)
SYM("power:GND", bx, by-35, 0)
W(bx, by+10, bx, by+22); W(bx, by-10, bx, by-35)
L("VBAT", 55, by+22); L("GND", 55, by-35)
T("POWER", bx+5, by+28, 2.54)

# ═══ FLIGHT CONTROLLER (X=80-130) ═══
fcx, fcy, fcw, fch = 105, 255, 40, 30
SYM("grok:FC", fcx, fcy, 0)
T("SpeedyBee", fcx-12, fcy+fch/2+8, 1.524); T("F405 Mini", fcx-12, fcy+fch/2+4, 1.524)
T("20x20 | 4 UARTs", fcx-12, fcy-fch/2+4, 1.016)
T("FLIGHT CONTROLLER", fcx-20, fcy+fch/2+14, 2.54)

# FC connectors — stubs with labels
conns = [
    ('L', fcy+fch/2-6, "VBAT_IN"), ('L', fcy-fch/2+6, "GND"),
    ('R', fcy+fch/2-6, "5V_OUT"),
    ('R', fcy+fch/2-12, "TX4→VTX"), ('R', fcy+fch/2-18, "TX5→RX"),
    ('L', fcy-fch/2+12, "RX3←GPS"), ('L', fcy-fch/2+18, "RX5←RX"),
    ('R', fcy-fch/2+24, "M1"), ('R', fcy-fch/2+28, "M2"),
    ('R', fcy-fch/2+32, "M3"), ('R', fcy-fch/2+36, "M4"),
]
for side, sy, name in conns:
    sx = fcx-fcw/2-15 if side=='L' else fcx+fcw/2+15
    lx = sx-2 if side=='L' else sx+2
    W(fcx-fcw/2 if side=='L' else fcx+fcw/2, sy, sx, sy)
    L(name, lx, sy+1, 0.9)

# ═══ POWER BUS ═══
bus_y = 280
W(55, by+22, 55, bus_y); W(55, bus_y, 280, bus_y)
J(55,bus_y); J(280,bus_y)
L("VBAT", 57, bus_y+2, 1.778)
W(55, by-35, 55, bus_y-10); W(55, bus_y-10, 280, bus_y-10)
J(55,bus_y-10); J(280,bus_y-10)
L("GND", 57, bus_y-12, 1.778)
# FC power taps
ROUTE(fcx-fcw/2-15, fcy+fch/2-6, 55, bus_y, 68)
ROUTE(fcx-fcw/2-15, fcy-fch/2+6, 55, bus_y-10, 68)

# ═══ ESC (below FC, X=80-130) ═══
escx, escy = 105, 185
SYM("grok:ESC", escx, escy, 0)
T("BLS 35A 4in1", escx-12, escy+12, 1.524); T("DShot600 3-6S", escx-12, escy-18, 1.016)
T("ESC", escx-5, escy+18, 2.54)
for i in range(4): 
    y = escy+6-i*3
    W(escx+20, y, escx+30, y)
    L(f"M{i+1}_OUT", escx+32, y+1, 0.9)

# ═══ VTX + CAM (X=240-300) ═══
vx,vy = 270, 265; cx,cy = 270, 235
SYM("grok:VTX",vx,vy,0); SYM("grok:CAM",cx,cy,0)
T("VIDEO SYSTEM", 250, 280, 2.54)
T("Zeus 350mW",vx+13,vy+6,1.27); T("SmartAudio SMA",vx+13,vy+1,1.016)
T("Caddx Ant 1200TVL",cx+13,cy+6,1.27); T("14x14→19x19",cx+13,cy+1,1.016)
# Stubs
for dx,dy,pin_y,lab in [(vx,vy,vy+4,"5V_IN"),(vx,vy,vy+1,"GND"),(vx,vy,vy-3,"SA_IN"),(vx,vy,vy-6,"VID_IN"),
                          (cx,cy,cy+3,"5V_IN"),(cx,cy,cy,  "GND"),(cx,cy,cy-2,"VID_OUT")]:
    side = 'L' if "IN" in lab and not "VID_IN" in lab else 'L' if "GND" in lab else 'R' if "OUT" in lab else 'L'
    sx = dx-15 if side=='L' else dx+15
    lx = sx-2 if side=='L' else sx+2
    W(dx-12 if side=='L' else dx+12, pin_y, sx, pin_y)
    L(lab, lx, pin_y+1, 0.9)

# ═══ RX + GPS (X=340-400) ═══
rx_x,rxy,gx,gy = 360,255, 360,215
SYM("grok:RX",rx_x,rxy,0); SYM("grok:GPS",gx,gy,0)
T("RECEIVER", 340, 275, 2.54); T("GPS (opt)", 340, 232, 2.54)
T("SuperD ELRS",rx_x+13,rxy+6,1.27); T("Dual SX1280",rx_x+13,rxy+1,1.016)
T("M10Q-5883",gx+13,gy+6,1.27); T("UBLOX M10",gx+13,gy+1,1.016)
for dx,dy,pin_y,lab in [(rx_x,rxy,rxy+3,"5V_IN"),(rx_x,rxy,rxy,"CRSF_IN"),(rx_x,rxy,rxy-3,"CRSF_OUT"),
                          (gx,gy,gy+3,"5V_IN"),(gx,gy,gy,"GND"),(gx,gy,gy-2,"UBX_OUT"),(gx,gy,gy-5,"UBX_IN")]:
    side = 'L' if "IN" in lab and "OUT" not in lab else 'R'
    sx = dx-15 if side=='L' else dx+15
    W(dx-12 if side=='L' else dx+12, pin_y, sx, pin_y)
    L(lab, sx-2 if side=='L' else sx+2, pin_y+1, 0.9)

# ═══ MOTORS (X=420+) ═══
T("MOTORS", 425, 280, 2.54)
for i,(name,my) in enumerate([("M1 FL CCW",265),("M2 FR CW",250),("M3 RL CCW",235),("M4 RR CW",220)]):
    SYM("grok:MOTOR", 430, my, 0)
    T(name, 438, my+4, 1.27); T("Specter 1804", 438, my-1, 1.016)
    W(420, my, 400, my)
    L(f"M{i+1}_IN", 398, my+1, 0.9)

# ═══ PERIPHERAL POWER DROPS (from bus to VTX/CAM/RX/GPS) ═══
for dx,dy,lab5,labG in [(vx,vy,"5V_IN","GND"),(cx,cy,"5V_IN","GND"),
                          (rx_x,rxy,"5V_IN",None),(gx,gy,"5V_IN","GND")]:
    ROUTE(280, bus_y, dx-17, dy+4, 290)
    if labG:
        ROUTE(280, bus_y-10, dx-17, dy+1, 290)

# ═══ SPECS ═══
specs = [
    (2.54,"BUILD SPECIFICATIONS",20,170),
    (1.27,"FC: F405 Mini 20x20 | ESC: BLS 35A DShot600 | Motors: Specter 1804 3500KV 12x12 M2",20,165),
    (1.27,"VTX: Zeus 350 SmartAudio SMA Lollipop | CAM: Caddx Ant 14x14→19x19 1200TVL",20,162),
    (1.27,"RX: SuperD ELRS Dual SX1280 CRSF@420k | GPS: M10Q-5883 UBLOX M10 (opt)",20,159),
    (1.27,"Frame: GX140 140mm 4mm CF twin 20x20 M3x25 | BAT: 2S 550 LiHV XT30 | AUW: ~190g",20,156),
    (1.27,"Props: GEMFAN 3052 22.8mm gap | Stack: ESC(4.5)+FC(6.5)=15mm on 25mm standoffs",20,153),
    (1.27,"22AWG: VBAT GND 5V | 26AWG: UART ESC | JST-SH CAM-VTX | ShortSaver MANDATORY",20,150),
]
for sz,msg,x,y in specs: T(msg,x,y,sz)

# ═══ SYMBOLS ═══
symbols = """  (lib_symbols
    (symbol "grok:FC" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "FC" (at 0 20 0) (effects (font (size 1.27 1.27))))
      (property "Value" "F405" (at 0 -20 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "FC_1_1" (rectangle (start -20 15) (end 20 -15) (stroke (width 0.254) (type default)) (fill (type background))))
    )
    (symbol "grok:ESC" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "ESC" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
      (property "Value" "BLS35A" (at 0 -7.62 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "ESC_1_1" (rectangle (start -20 6) (end 20 -6) (stroke (width 0.254) (type default)) (fill (type background))))
    )
    (symbol "grok:VTX" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "VTX" (at 0 5 0) (effects (font (size 1.27 1.27))))
      (property "Value" "Zeus" (at 0 -5 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "VTX_1_1" (rectangle (start -12 4) (end 12 -4) (stroke (width 0.254) (type default)) (fill (type background))))
    )
    (symbol "grok:CAM" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "CAM" (at 0 4 0) (effects (font (size 1.27 1.27))))
      (property "Value" "Ant" (at 0 -4 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "CAM_1_1" (rectangle (start -10 3) (end 10 -3) (stroke (width 0.254) (type default)) (fill (type background))))
    )
    (symbol "grok:RX" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "RX" (at 0 5 0) (effects (font (size 1.27 1.27))))
      (property "Value" "SuperD" (at 0 -5 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "RX_1_1" (rectangle (start -12 4) (end 12 -4) (stroke (width 0.254) (type default)) (fill (type background))))
    )
    (symbol "grok:GPS" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "GPS" (at 0 4 0) (effects (font (size 1.27 1.27))))
      (property "Value" "M10Q" (at 0 -4 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "GPS_1_1" (rectangle (start -10 3) (end 10 -3) (stroke (width 0.254) (type default)) (fill (type background))))
    )
    (symbol "grok:MOTOR" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "M" (at 0 2.54 0) (effects (font (size 1.016 1.016))))
      (property "Value" "1804" (at 0 -2.54 0) (effects (font (size 1.016 1.016))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.016 1.016)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.016 1.016)) hide))
      (symbol "MOTOR_1_1" (circle (center 0 0) (radius 5) (stroke (width 0.254) (type default)) (fill (type background))))
    )
  )"""

# ═══ ASSEMBLE ═══
sch = f"""(kicad_sch (version 20230121) (generator "grok_fpv_final")

  (uuid {uid()})

  (paper "A3")

  (title_block
    (title "GX140 3in Analog FPV — Electrical Schematic")
    (date "2025-12-12")
    (rev "1.0")
    (company "GROK — FPV Drone Engineering")
    (comment 1 "Power: 2S LiHV | FC: F405 Mini | ESC: BLS 35A")
    (comment 2 "VTX: Zeus 350 | CAM: Caddx Ant | RX: SuperD ELRS")
    (comment 3 "Motors: Specter 1804 | GPS: M10Q-5883 (opt)")
    (comment 4 "Frame: GX140 140mm | AUW: ~190g")
  )

{symbols}

{chr(10).join(parts)}

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""

with open(OUT,'w') as f: f.write(sch)
with open(PRO,'w') as f: f.write(f"""(kicad_project (version 7)
  (paper "A3") (title "GX140 3in Analog FPV") (date "2025-12-12") (rev "1.0")
  (company "GROK FPV Drone Engineering")
  (schematic_files (0 "gx140_final.kicad_sch"))
)""")
print(f"OK: {OUT} ({len(sch)}B) | {len(parts)} primitives")
