#!/usr/bin/env python3
"""
GX140 3" Analog FPV Build — KiCad Schematic Generator
Generates a proper .kicad_sch file via S-expression format.
KiCad 7.0 compatible.
Output: /home/mike/projects/Drone Projects/builds/gx140/gx140.kicad_sch
"""

import os

OUTPUT_DIR = "/home/mike/projects/Drone Projects/builds/gx140"
PROJECT_NAME = "gx140"
sch_path = os.path.join(OUTPUT_DIR, f"{PROJECT_NAME}.kicad_sch")
pro_path = os.path.join(OUTPUT_DIR, f"{PROJECT_NAME}.kicad_pro")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─── KiCad 7.0 S-Expression Schematic ───
# Format: https://dev-docs.kicad.org/en/file-formats/sexpr-schematic/

kicad_sch = """(kicad_sch
  (version 20231120)
  (generator "grok_fpv_engineering")
  (generator_version "1.0")

  (page "A4")

  (title_block
    (title "GX140 3\\" Analog FPV — Electrical Schematic")
    (date "2025-12-12")
    (rev "1.0")
    (company "GROK — FPV Drone Engineering")
    (comment 1 "Frame: GX140 140mm, 4mm carbon, twin 20x20 tower")
    (comment 2 "FC: SpeedyBee F405 Mini | ESC: BLS 35A 4in1")
    (comment 3 "Motors: HGLRC Specter 1804 3500KV | Props: GEMFAN 3052")
    (comment 4 "VTX: HGLRC Zeus 350mW | Cam: Caddx Ant | RX: SuperD ELRS")
  )

  (lib_symbols
    (symbol "grok:BATTERY_CONN" (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
      (property "Value" "BAT_CONN" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Connector_XT30" (at 0 0 0) (hide yes))
      (pin "1" line (at -5.08 2.54 0) (length 2.54) (name "VBAT" (effects (font (size 1.27 1.27)))))
      (pin "2" line (at -5.08 -2.54 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))))
    )
    (symbol "grok:FC_F405_MINI" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 12.7 0) (effects (font (size 1.27 1.27))))
      (property "Value" "F405_MINI" (at 0 -12.7 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Module:SpeedyBee_F405_Mini_20x20" (at 0 0 0) (hide yes))
      (pin "1" input (at -25.4 10.16 0) (length 5.08) (name "VBAT" (effects (font (size 1.27 1.27)))))
      (pin "2" input (at -25.4 7.62 0) (length 5.08) (name "GND" (effects (font (size 1.27 1.27)))))
      (pin "3" output (at 25.4 10.16 0) (length 5.08) (name "5V" (effects (font (size 1.27 1.27)))))
      (pin "4" output (at 25.4 7.62 0) (length 5.08) (name "3V3" (effects (font (size 1.27 1.27)))))
      (pin "5" output (at -25.4 5.08 0) (length 5.08) (name "M1" (effects (font (size 1.27 1.27)))))
      (pin "6" output (at -25.4 2.54 0) (length 5.08) (name "M2" (effects (font (size 1.27 1.27)))))
      (pin "7" output (at -25.4 0 0) (length 5.08) (name "M3" (effects (font (size 1.27 1.27)))))
      (pin "8" output (at -25.4 -2.54 0) (length 5.08) (name "M4" (effects (font (size 1.27 1.27)))))
      (pin "9" output (at 25.4 5.08 0) (length 5.08) (name "TX4" (effects (font (size 1.27 1.27)))))
      (pin "10" input (at 25.4 2.54 0) (length 5.08) (name "RX4" (effects (font (size 1.27 1.27)))))
      (pin "11" output (at 25.4 0 0) (length 5.08) (name "TX5" (effects (font (size 1.27 1.27)))))
      (pin "12" input (at 25.4 -2.54 0) (length 5.08) (name "RX5" (effects (font (size 1.27 1.27)))))
      (pin "13" input (at 25.4 -5.08 0) (length 5.08) (name "RX3" (effects (font (size 1.27 1.27)))))
      (pin "14" output (at 25.4 -7.62 0) (length 5.08) (name "TX3" (effects (font (size 1.27 1.27)))))
      (pin "15" bidirectional (at 25.4 -10.16 0) (length 5.08) (name "LED" (effects (font (size 1.27 1.27)))))
      (pin "16" output (at -25.4 -5.08 0) (length 5.08) (name "BZ+" (effects (font (size 1.27 1.27)))))
    )
    (symbol "grok:VTX_ZEUS" (in_bom yes) (on_board yes)
      (property "Reference" "VTX" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
      (property "Value" "ZEUS_350mW" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
      (pin "1" input (at -10.16 5.08 0) (length 2.54) (name "5V" (effects (font (size 1.27 1.27)))))
      (pin "2" input (at -10.16 2.54 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))))
      (pin "3" input (at -10.16 0 0) (length 2.54) (name "VID_IN" (effects (font (size 1.27 1.27)))))
      (pin "4" input (at -10.16 -2.54 0) (length 2.54) (name "SA" (effects (font (size 1.27 1.27)))))
      (pin "5" output (at 10.16 0 0) (length 2.54) (name "ANT" (effects (font (size 1.27 1.27)))))
    )
    (symbol "grok:CAM_ANT" (in_bom yes) (on_board yes)
      (property "Reference" "CAM" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
      (property "Value" "CADDX_ANT" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
      (pin "1" input (at -10.16 2.54 0) (length 2.54) (name "5V" (effects (font (size 1.27 1.27)))))
      (pin "2" input (at -10.16 0 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))))
      (pin "3" output (at 10.16 0 0) (length 2.54) (name "VID" (effects (font (size 1.27 1.27)))))
    )
    (symbol "grok:RX_SUPERD" (in_bom yes) (on_board yes)
      (property "Reference" "RX" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
      (property "Value" "SUPERD_ELRS" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
      (pin "1" input (at -10.16 5.08 0) (length 2.54) (name "5V" (effects (font (size 1.27 1.27)))))
      (pin "2" input (at -10.16 2.54 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))))
      (pin "3" output (at 10.16 5.08 0) (length 2.54) (name "TX" (effects (font (size 1.27 1.27)))))
      (pin "4" input (at 10.16 2.54 0) (length 2.54) (name "RX" (effects (font (size 1.27 1.27)))))
      (pin "5" output (at 10.16 -2.54 0) (length 2.54) (name "ANT1" (effects (font (size 1.27 1.27)))))
      (pin "6" output (at 10.16 -5.08 0) (length 2.54) (name "ANT2" (effects (font (size 1.27 1.27)))))
    )
    (symbol "grok:ESC_35A" (in_bom yes) (on_board yes)
      (property "Reference" "ESC" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
      (property "Value" "BLS_35A_4IN1" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
      (pin "1" input (at -12.7 7.62 0) (length 2.54) (name "VBAT" (effects (font (size 1.27 1.27)))))
      (pin "2" input (at -12.7 5.08 0) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))))
      (pin "3" input (at -12.7 2.54 0) (length 2.54) (name "S1" (effects (font (size 1.27 1.27)))))
      (pin "4" input (at -12.7 0 0) (length 2.54) (name "S2" (effects (font (size 1.27 1.27)))))
      (pin "5" input (at -12.7 -2.54 0) (length 2.54) (name "S3" (effects (font (size 1.27 1.27)))))
      (pin "6" input (at -12.7 -5.08 0) (length 2.54) (name "S4" (effects (font (size 1.27 1.27)))))
      (pin "7" output (at 12.7 7.62 0) (length 2.54) (name "M1" (effects (font (size 1.27 1.27)))))
      (pin "8" output (at 12.7 5.08 0) (length 2.54) (name "M2" (effects (font (size 1.27 1.27)))))
      (pin "9" output (at 12.7 2.54 0) (length 2.54) (name "M3" (effects (font (size 1.27 1.27)))))
      (pin "10" output (at 12.7 0 0) (length 2.54) (name "M4" (effects (font (size 1.27 1.27)))))
    )
  )

  (sheet
    (at 0 0) (size 297 210) (fields_autoplaced)

    (symbol (lib_id "grok:BATTERY_CONN") (at 25.4 177.8 0)
      (property "Reference" "J1" (at 25.4 180.34 0))
      (property "Value" "2S 550mAh LiHV" (at 25.4 175.26 0))
    )
    (symbol (lib_id "grok:FC_F405_MINI") (at 101.6 177.8 0)
      (property "Reference" "U1" (at 101.6 190.5 0))
      (property "Value" "SpeedyBee F405 Mini" (at 101.6 165.1 0))
    )
    (symbol (lib_id "grok:ESC_35A") (at 101.6 101.6 0)
      (property "Reference" "ESC1" (at 101.6 104.14 0))
      (property "Value" "BLS 35A 4in1" (at 101.6 99.06 0))
    )
    (symbol (lib_id "grok:VTX_ZEUS") (at 177.8 177.8 0)
      (property "Reference" "VTX1" (at 177.8 180.34 0))
      (property "Value" "HGLRC Zeus 350mW" (at 177.8 175.26 0))
    )
    (symbol (lib_id "grok:CAM_ANT") (at 177.8 139.7 0)
      (property "Reference" "CAM1" (at 177.8 142.24 0))
      (property "Value" "Caddx Ant 1200TVL" (at 177.8 137.16 0))
    )
    (symbol (lib_id "grok:RX_SUPERD") (at 177.8 76.2 0)
      (property "Reference" "RX1" (at 177.8 78.74 0))
      (property "Value" "SuperD ELRS V3" (at 177.8 73.66 0))
    )

    ;; ─── POWER NETS ───
    (wire (pts (xy 30.48 177.8) (xy 76.2 187.96)))     ;; J1_VBAT → U1_VBAT
    (wire (pts (xy 30.48 175.26) (xy 76.2 185.42)))     ;; J1_GND → U1_GND
    (wire (pts (xy 76.2 187.96) (xy 88.9 109.22)))      ;; U1_VBAT → ESC1_VBAT
    (wire (pts (xy 76.2 185.42) (xy 88.9 106.68)))      ;; U1_GND → ESC1_GND
    (wire (pts (xy 127.0 187.96) (xy 167.64 182.88)))   ;; U1_5V → VTX1_5V
    (wire (pts (xy 127.0 185.42) (xy 167.64 180.34)))   ;; U1_GND → VTX1_GND
    (wire (pts (xy 127.0 185.42) (xy 167.64 142.24)))   ;; U1_GND → CAM1_GND
    (wire (pts (xy 127.0 187.96) (xy 167.64 144.78)))   ;; U1_5V → CAM1_5V
    (wire (pts (xy 127.0 185.42) (xy 167.64 81.28)))    ;; U1_GND → RX1_GND
    (wire (pts (xy 127.0 187.96) (xy 167.64 83.82)))    ;; U1_5V → RX1_5V

    ;; ─── SIGNAL NETS ───
    (wire (pts (xy 127.0 182.88) (xy 167.64 177.8)))    ;; U1_TX4 → VTX1_SA (SmartAudio)
    (wire (pts (xy 187.96 139.7) (xy 167.64 177.8)))    ;; CAM1_VID → VTX1_VID_IN
    (wire (pts (xy 127.0 177.8) (xy 167.64 78.74)))     ;; U1_TX5 → RX1_RX
    (wire (pts (xy 167.64 81.28) (xy 127.0 175.26)))    ;; RX1_TX → U1_RX5

    ;; ─── MOTOR NETS ───
    (wire (pts (xy 76.2 182.88) (xy 88.9 104.14)))      ;; U1_M1 → ESC1_S1
    (wire (pts (xy 76.2 180.34) (xy 88.9 101.6)))       ;; U1_M2 → ESC1_S2
    (wire (pts (xy 76.2 177.8) (xy 88.9 99.06)))        ;; U1_M3 → ESC1_S3
    (wire (pts (xy 76.2 175.26) (xy 88.9 96.52)))       ;; U1_M4 → ESC1_S4

    ;; ─── LABELS ───
    (text "POWER DISTRIBUTION" (at 63.5 200.66 0) (effects (font (size 2.54 2.54))))
    (text "VBAT (7.4V nom) → FC → Internal 5V BEC → VTX/CAM/RX" (at 63.5 195.58 0) (effects (font (size 1.27 1.27))))
    (text "SIGNAL ROUTING" (at 139.7 200.66 0) (effects (font (size 2.54 2.54))))
    (text "UART4: FC_TX4 → VTX SmartAudio" (at 139.7 195.58 0) (effects (font (size 1.27 1.27))))
    (text "UART5: FC_TX5 → RX_RX | RX_TX → FC_RX5 (CRSF)" (at 139.7 193.04 0) (effects (font (size 1.27 1.27))))
    (text "MOTORS: DShot600 | M1(FL-CCW) M2(FR-CW) M3(RL-CCW) M4(RR-CW)" (at 63.5 88.9 0) (effects (font (size 1.27 1.27))))
    (text "CAM: Caddx Ant 1200TVL, 14×14→19×19 adapter" (at 139.7 135.0 0) (effects (font (size 1.27 1.27))))
    (text "ANT: VTX → Foxeer Lollipop RHCP SMA rear" (at 139.7 132.0 0) (effects (font (size 1.27 1.27))))
    (text "ANT1: RX vertical left standoff | ANT2: RX horizontal top plate" (at 139.7 129.0 0) (effects (font (size 1.27 1.27))))
  )
)
"""

# Write schematic
with open(sch_path, 'w') as f:
    f.write(kicad_sch)

# Write project file
kicad_pro = f"""(kicad_project
  (version 7)
  (paper "A4")
  (title "GX140 3\\" Analog FPV")
  (date "2025-12-12")
  (rev "1.0")
  (company "GROK — FPV Drone Engineering")
  (schematic_files
    (0 "{PROJECT_NAME}.kicad_sch")
  )
)
"""
with open(pro_path, 'w') as f:
    f.write(kicad_pro)

# Verify files
for path, label in [(sch_path, "Schematic"), (pro_path, "Project")]:
    size = os.path.getsize(path)
    print(f"✅ {label}: {path} ({size} bytes)")

print(f"\nOpen with: kicad {pro_path}")
print("Or: kiCad → File → Open Project → select gx140.kicad_pro")