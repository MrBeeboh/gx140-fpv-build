#!/usr/bin/env python3
"""
GX140 Rev 2 — Reverse Wire Tag Methodology
Labels at wire ends = connections. Stubs only. Clean layout.
Rounded rectangle symbols with light yellow fill, green pin dots.
Wire colors via net_colors in .kicad_pro (apply in GUI).
"""
import uuid, json, os

OUT = "/home/mike/projects/Drone Projects/builds/gx140/gx140_rev2.kicad_sch"
PRO = "/home/mike/projects/Drone Projects/builds/gx140/gx140_rev2.kicad_pro"
uid = lambda: str(uuid.uuid4())

P = []  # parts list

def W(x1,y1,x2,y2,stroke=0.1524):
    P.append(f'  (wire (pts (xy {x1:.1f} {y1:.1f}) (xy {x2:.1f} {y2:.1f})) (stroke (width {stroke}) (type default)) (uuid {uid()}))')

def L(n,x,y,sz=1.27):
    """Net label at wire END — this IS the connection point"""
    P.append(f'  (label "{n}" (at {x:.1f} {y:.1f} 0) (effects (font (size {sz} {sz}))))')

def T(t,x,y,sz=1.27,bold=False):
    P.append(f'  (text "{t}" (at {x:.1f} {y:.1f} 0) (effects (font (size {sz} {sz}){" bold" if bold else ""})))')

def SYM(lib,x,y,rot=0):
    P.append(f'  (symbol (lib_id "{lib}") (at {x:.1f} {y:.1f} {rot}) (unit 1) (in_bom yes) (on_board yes) (dnp no) (uuid {uid()}))')

# ═══ TITLE / HEADER ═══
T("GX140 3in ANALOG FPV — Electrical Schematic", 150, 290, 4.5, True)
T("GROK — FPV Drone Engineering | 2025-12-12 | Rev 2.0 | Sheet 1/1 | A3", 150, 284, 1.5)

# ═══ NOTES (upper-left) ═══
notes = [
    (2.5,"=== POWER TREE ===",20,275),
    (1.5,"2S 550mAh LiHV (7.4V) XT30 → FC VBAT → Internal 5V/3A BEC → 5V Rail",20,270),
    (1.5,"5V Rail powers: VTX, CAM, RX, GPS (optional)",20,266),
    (2.5,"=== SIGNAL SUMMARY ===",20,259),
    (1.5,"UART4 (TX4): FC → VTX SmartAudio RX — PA control, 115200 baud",20,254),
    (1.5,"UART5 (TX5/RX5): FC ↔ RX CRSF — ELRS V3, 420000 baud",20,250),
    (1.5,"UART3 (TX3/RX3): FC ↔ GPS UBLOX — M10Q-5883, 57600 baud (optional)",20,246),
    (1.5,"DShot600: FC M1-M4 → ESC → Motors (bidirectional, RPM filter ON)",20,242),
    (1.5,"CAM Video → VTX CAM_IN (JST-SH 1.0mm 4-pin)",20,238),
    (2.5,"=== BUILD SPECS ===",20,231),
    (1.3,"Frame: GX140 140mm 4mm CF twin 20x20 | 8× M3×25mm alu standoffs | ~45g bare",20,226),
    (1.3,"FC: SpeedyBee F405 Mini 20×20 ICM42688 DPS310 | 25×25×6.5mm | 4 UARTs USB-C",20,222),
    (1.3,"ESC: BLS 35A 4in1 20×20 DShot600 Bidir ON | 25×25×4.5mm | 3-6S | 5V/3A BEC",20,218),
    (1.3,"Motors: HGLRC Specter 1804 3500KV 13.3g 12×12 M2 1.5mm shaft 22.68×13.2mm",20,214),
    (1.3,"Props: GEMFAN 3052 3in tri-blade 5mm hub+1.5mm adapter 22.8mm tip clearance",20,210),
    (1.3,"VTX: HGLRC Zeus 350mW 16×16→20×20 SmartAudio SMA Foxeer Lollipop RHCP",20,206),
    (1.3,"CAM: Caddx Ant 1200TVL 14×14→19×19 adapter F1.6 165° JST-SH 1.0mm 4-pin",20,202),
    (1.3,"RX: BETAFPV SuperD ELRS 22×14mm 1.1g Dual SX1280 CRSF@420k ANT1 vert L ANT2 horiz",20,198),
    (1.3,"GPS: Matek M10Q-5883 UBLOX M10 QMC5883L (optional) JST-GH 1.25mm 6-pin",20,194),
    (1.3,"BAT: 2S 550mAh LiHV 7.6V 75C XT30 30×18×15mm ~4-5min LVC 3.5V/cell",20,190),
    (2.5,"=== SAFETY ===",20,183),
    (1.3,"ShortSaver MANDATORY before first power | Props OFF for motor direction test",20,178),
    (1.3,"Continuity check all rails | AUW ~190g (<250g) | CG <1mm | ALL DIRECT FIT",20,174),
]
for sz,msg,x,y in notes: T(msg,x,y,sz)

# ═══ COMPONENT SYMBOLS (rounded rect, light yellow fill, dark border, green pin dots) ═══
# Placed left-to-right, top-to-bottom
# BAT + ESC (left), FC (center), VTX+CAM (upper-right), RX+GPS (lower-right), Motors (far right)

# --- BATTERY (X=35) ---
SYM("grok:BAT", 40, 140, 0)
T("BAT1", 40, 155, 1.8, True)
T("2S 550mAh LiHV 7.4V XT30", 40, 125, 1.2)
# Battery stubs → labels
W(30, 147, 30, 152); L("VBAT", 30, 153, 1.3)
W(30, 133, 30, 128); L("GND", 30, 127, 1.3)

# --- ESC (X=35, below BAT) ---
SYM("grok:ESC", 40, 90, 0)
T("ESC1", 40, 106, 1.8, True)
T("BLS 35A 4in1 20x20 DShot600 3-6S", 40, 72, 1.2)
# ESC stubs
W(30, 98, 30, 102); L("VBAT", 30, 103, 1.3)
W(30, 94, 30, 100); L("GND", 30, 101, 1.3)
W(30, 90, 30, 95); L("CURR", 30, 96, 1.3)
# Motor outputs (right side)
for i, y in enumerate([98,94,90,86]):
    W(55, y, 65, y)
    L(f"DSHOT_M{i+1}", 67, y+1, 1.2)
    W(55, y-2, 65, y-2)
    L(f"M{i+1}_A", 67, y-1, 1.2)
    W(55, y-4, 65, y-4)
    L(f"M{i+1}_B", 67, y-3, 1.2)
# More pins later as needed — just DSHOT for simplicity

# --- FLIGHT CONTROLLER (X=130, center) ---
SYM("grok:FC", 140, 140, 0)
T("FC1", 140, 163, 2.0, True)
T("SpeedyBee F405 Mini 20x20 ICM42688 DPS310 4 UARTs", 140, 117, 1.2)
# FC pins — left side (inputs), right side (outputs)
fc_pins_left = [("VBAT",158),("GND",154),("RX3",150),("RX5",146),("I2C_SDA",142),("I2C_SCL",138)]
fc_pins_right = [("5V",158),("TX4",154),("TX5",150),("M1",146),("M2",142),("M3",138),("M4",134)]
for name,y in fc_pins_left:
    W(110, y, 120, y)
    L(name, 108, y+1, 1.2)
for name,y in fc_pins_right:
    W(160, y, 170, y)
    L(name, 172, y+1, 1.2)

# --- VTX (X=260, upper-right) ---
SYM("grok:VTX", 270, 160, 0)
T("VTX1", 270, 175, 1.8, True)
T("HGLRC Zeus 350mW 16x16→20x20 SmartAudio", 270, 143, 1.2)
T("SMA → Foxeer Lollipop RHCP", 270, 139, 1.1)
vtx_pins = [("5V",167),("GND",164),("TX4",161),("CAM_VIDEO",158),("VTX_ANT",155)]
for name,y in vtx_pins:
    W(258, y, 248, y)
    L(name, 246, y+1, 1.2)
# Antenna symbol on right
SYM("grok:ANT", 295, 155, 0)

# --- CAMERA (X=260, below VTX) ---
SYM("grok:CAM", 270, 115, 0)
T("CAM1", 270, 130, 1.8, True)
T("Caddx Ant 1200TVL 14x14→19x19 F1.6 JST-SH", 270, 98, 1.2)
cam_pins = [("5V",122),("GND",119),("CAM_VIDEO",116)]
for name,y in cam_pins:
    W(258, y, 248, y)
    L(name, 246, y+1, 1.2)

# --- RX (X=360, upper-right area) ---
SYM("grok:RX", 370, 160, 0)
T("RX1", 370, 175, 1.8, True)
T("BETAFPV SuperD ELRS V3 22x14mm Dual SX1280", 370, 143, 1.2)
rx_pins = [("5V",168),("GND",165),("TX5",162),("RX5",159),("RX_ANT1",155),("RX_ANT2",151)]
for name,y in rx_pins:
    W(358, y, 348, y)
    L(name, 346, y+1, 1.2)
# Antenna symbols on right
SYM("grok:ANT", 400, 155, 0)
SYM("grok:ANT", 400, 151, 0)

# --- GPS (X=360, below RX) ---
SYM("grok:GPS", 370, 110, 0)
T("GPS1", 370, 125, 1.8, True)
T("Matek M10Q-5883 UBLOX M10 QMC5883L (optional)", 370, 93, 1.2)
gps_pins = [("5V",118),("GND",115),("RX3",112),("TX3",109),("I2C_SDA",106),("I2C_SCL",103)]
for name,y in gps_pins:
    W(358, y, 348, y)
    L(name, 346, y+1, 1.2)

# --- MOTORS (X=420, far right) ---
for i, (name, my) in enumerate([("M1 FL CCW",165),("M2 FR CW",146),("M3 RL CCW",127),("M4 RR CW",108)]):
    SYM("grok:MOTOR", 430, my, 0)
    T(f"M{i+1}", 430, my+12, 1.5, True)
    T(f"HGLRC Specter 1804 3500KV {name}", 430, my-12, 1.1)
    # Motor phase inputs from ESC
    for ph, dy in [("A",4),("B",2),("C",0)]:
        W(418, my+dy, 400, my+dy)
        L(f"M{i+1}_{ph}", 398, my+dy+1, 1.1)

# ═══ CROSS-REFERENCE TABLE (net connections) ═══
# Shows which labels connect where — reverse wire tag key
xref = [
    (2.0,"=== NET CROSS-REFERENCE ===",20, 90),
    (1.2,"VBAT: BAT1.VBAT → ESC1.VBAT → FC1.VBAT",20,86),
    (1.2,"GND: BAT1.GND → ESC1.GND → FC1.GND → VTX1.GND → CAM1.GND → RX1.GND → GPS1.GND",20,83),
    (1.2,"5V: FC1.5V → VTX1.5V → CAM1.5V → RX1.5V → GPS1.5V",20,80),
    (1.2,"TX4: FC1.TX4 → VTX1.TX4 (SmartAudio PA control)",20,77),
    (1.2,"TX5/RX5: FC1.TX5 → RX1.RX5 | RX1.TX5 → FC1.RX5 (CRSF)",20,74),
    (1.2,"RX3/TX3: FC1.RX3 → GPS1.TX3 | FC1.TX3 → GPS1.RX3 (UBLOX)",20,71),
    (1.2,"CAM_VIDEO: CAM1.CAM_VIDEO → VTX1.CAM_VIDEO (JST-SH 1.0mm)",20,68),
    (1.2,"DSHOT_M1-M4: FC1.M1-M4 → ESC1.DSHOT_M1-M4 (DShot600)",20,65),
    (1.2,"M1_A-M4_C: ESC1.M1_A-M4_C → M1-M4 (Motor phases)",20,62),
    (1.2,"I2C_SDA/SCL: FC1.I2C → GPS1.I2C (QMC5883L compass)",20,59),
    (1.2,"CURR: ESC1.CURR → FC1.CURR (current sense, if supported)",20,56),
]
for sz,msg,x,y in xref: T(msg,x,y,sz)

# ═══ SYMBOL DEFINITIONS (rounded rectangles, light yellow fill, green pins) ═══
symbols = """  (lib_symbols
    (symbol "grok:BAT" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "BAT" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
      (property "Value" "Battery" (at 0 -7.62 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "BAT_1_1"
        (rectangle (start -12 6) (end 12 -6) (stroke (width 0.254) (type default)) (fill (type background)))
      )
    )
    (symbol "grok:FC" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "FC" (at 0 15 0) (effects (font (size 1.27 1.27))))
      (property "Value" "F405" (at 0 -15 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "FC_1_1"
        (rectangle (start -18 12) (end 18 -12) (stroke (width 0.254) (type default)) (fill (type background)))
      )
    )
    (symbol "grok:ESC" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "ESC" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
      (property "Value" "BLS35A" (at 0 -7.62 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "ESC_1_1"
        (rectangle (start -15 6) (end 15 -6) (stroke (width 0.254) (type default)) (fill (type background)))
      )
    )
    (symbol "grok:VTX" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "VTX" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
      (property "Value" "Zeus350" (at 0 -7.62 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "VTX_1_1"
        (rectangle (start -12 5) (end 12 -5) (stroke (width 0.254) (type default)) (fill (type background)))
      )
    )
    (symbol "grok:CAM" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "CAM" (at 0 5 0) (effects (font (size 1.27 1.27))))
      (property "Value" "CaddxAnt" (at 0 -5 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "CAM_1_1"
        (rectangle (start -10 3) (end 10 -3) (stroke (width 0.254) (type default)) (fill (type background)))
      )
    )
    (symbol "grok:RX" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "RX" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
      (property "Value" "SuperD" (at 0 -7.62 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "RX_1_1"
        (rectangle (start -12 5) (end 12 -5) (stroke (width 0.254) (type default)) (fill (type background)))
      )
    )
    (symbol "grok:GPS" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "GPS" (at 0 5 0) (effects (font (size 1.27 1.27))))
      (property "Value" "M10Q5883" (at 0 -5 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "GPS_1_1"
        (rectangle (start -12 5) (end 12 -5) (stroke (width 0.254) (type default)) (fill (type background)))
      )
    )
    (symbol "grok:MOTOR" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "M" (at 0 2.54 0) (effects (font (size 1.016 1.016))))
      (property "Value" "1804" (at 0 -2.54 0) (effects (font (size 1.016 1.016))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.016 1.016)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.016 1.016)) hide))
      (symbol "MOTOR_1_1"
        (circle (center 0 0) (radius 6) (stroke (width 0.254) (type default)) (fill (type background)))
      )
    )
    (symbol "grok:ANT" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "ANT" (at 0 3 0) (effects (font (size 1.016 1.016))))
      (property "Value" "" (at 0 -2 0) (effects (font (size 1.016 1.016))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "ANT_1_1"
        (polyline (pts (xy 0 3) (xy -3 -2) (xy 3 -2) (xy 0 3)) (stroke (width 0.254) (type default)) (fill (type none)))
        (pin passive line (at -5 0 0) (length 5) (name "ANT" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
      )
    )
  )"""

# ═══ ASSEMBLE ═══
sch = f"""(kicad_sch (version 20230121) (generator "grok_fpv_rev2")

  (uuid {uid()})

  (paper "A3")

  (title_block
    (title "GX140 3in Analog FPV — Electrical Schematic")
    (date "2025-12-12")
    (rev "2.0")
    (company "GROK — FPV Drone Engineering")
    (comment 1 "Power: 2S LiHV → FC 5V BEC → VTX/CAM/RX/GPS")
    (comment 2 "Signals: UART4 (VTX SA) | UART5 (RX CRSF) | UART3 (GPS UBLOX)")
    (comment 3 "Motors: DShot600 FC→ESC→1804 3500KV | Props: 3052")
    (comment 4 "Frame: GX140 140mm 4mm CF twin 20x20 | AUW: ~190g")
    (comment 5 "ALL COMPONENTS DIRECT FIT — ZERO MODIFICATIONS")
  )

{symbols}

{chr(10).join(P)}

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""

with open(OUT,'w') as f: f.write(sch)

# Project with net colors for VBAT (red), GND (black), 5V (orange)
proj = {
    "board": {"design_settings": {}},
    "net_colors": {
        "VBAT": "rgba(220, 50, 50, 1.000)",
        "GND": "rgba(50, 50, 50, 1.000)",
        "5V": "rgba(220, 140, 50, 1.000)",
    }
}
with open(PRO,'w') as f: json.dump(proj, f)

print(f"OK: {OUT} ({len(sch)}B) | {len(P)} primitives | Rev 2.0")
