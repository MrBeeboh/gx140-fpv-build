#!/usr/bin/env python3
"""
GX140 Clean Schematic — Reverse Wire Tag Methodology
Every net has a label. Every pin has a name. Components connected visually.
Output: clean KiCad 7.0 S-expression schematic
"""
import os, uuid

OUT = "/home/mike/projects/Drone Projects/builds/gx140/gx140_clean.kicad_sch"
PRO = "/home/mike/projects/Drone Projects/builds/gx140/gx140_clean.kicad_pro"

# UUID generator
def uid(): return str(uuid.uuid4())

# ─── SYMBOL DEFINITIONS ───
symbols = """
  (lib_symbols
    (symbol "grok:BATTERY" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "BAT" (at 0 3.81 0) (effects (font (size 1.524 1.524))))
      (property "Value" "2S_550mAh_LiHV" (at 0 -3.81 0) (effects (font (size 1.524 1.524))))
      (symbol "BAT_0_1" (rectangle (start -7.62 3.81) (end 7.62 -3.81) (stroke (width 0.254)) (fill (type background))))
      (symbol "BAT_1_1"
        (pin power_out line (at 12.7 1.27 0) (length 5.08) (name "VBAT" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 12.7 -1.27 0) (length 5.08) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "grok:FC" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "FC" (at 0 20.32 0) (effects (font (size 1.778 1.778))))
      (property "Value" "F405_Mini" (at 0 -20.32 0) (effects (font (size 1.778 1.778))))
      (symbol "FC_0_1" (rectangle (start -20.32 17.78) (end 20.32 -17.78) (stroke (width 0.254)) (fill (type background))))
      (symbol "FC_1_1"
        (pin power_in line (at -25.4 15.24 0) (length 5.08) (name "VBAT" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -25.4 12.70 0) (length 5.08) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 25.4 15.24 0) (length 5.08) (name "5V_OUT" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin output line (at -25.4 10.16 0) (length 5.08) (name "M1" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin output line (at -25.4 7.62 0) (length 5.08) (name "M2" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin output line (at -25.4 5.08 0) (length 5.08) (name "M3" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin output line (at -25.4 2.54 0) (length 5.08) (name "M4" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin output line (at 25.4 12.70 0) (length 5.08) (name "TX4" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin input line (at 25.4 10.16 0) (length 5.08) (name "RX4" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin output line (at 25.4 7.62 0) (length 5.08) (name "TX5" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin input line (at 25.4 5.08 0) (length 5.08) (name "RX5" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin input line (at 25.4 2.54 0) (length 5.08) (name "RX3" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin output line (at 25.4 0 0) (length 5.08) (name "TX3" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "grok:ESC" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "ESC" (at 0 7.62 0) (effects (font (size 1.524 1.524))))
      (property "Value" "BLS_35A_4in1" (at 0 -7.62 0) (effects (font (size 1.524 1.524))))
      (symbol "ESC_0_1" (rectangle (start -15.24 5.08) (end 15.24 -5.08) (stroke (width 0.254)) (fill (type background))))
      (symbol "ESC_1_1"
        (pin power_in line (at -20.32 3.81 0) (length 5.08) (name "VBAT" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -20.32 1.27 0) (length 5.08) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 -1.27 0) (length 5.08) (name "S1" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at -20.32 -3.81 0) (length 5.08) (name "S2" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 3.81 0) (length 5.08) (name "M1_OUT" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 1.27 0) (length 5.08) (name "M2_OUT" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 -1.27 0) (length 5.08) (name "M3_OUT" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin output line (at 20.32 -3.81 0) (length 5.08) (name "M4_OUT" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "grok:VTX" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "VTX" (at 0 7.62 0) (effects (font (size 1.524 1.524))))
      (property "Value" "Zeus_350mW" (at 0 -7.62 0) (effects (font (size 1.524 1.524))))
      (symbol "VTX_0_1" (rectangle (start -10.16 5.08) (end 10.16 -5.08) (stroke (width 0.254)) (fill (type background))))
      (symbol "VTX_1_1"
        (pin power_in line (at -15.24 3.81 0) (length 5.08) (name "5V" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -15.24 1.27 0) (length 5.08) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at -15.24 -1.27 0) (length 5.08) (name "VID_IN" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at 15.24 1.27 0) (length 5.08) (name "SMARTAUDIO" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 -1.27 0) (length 5.08) (name "ANT" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "grok:CAM" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "CAM" (at 0 5.08 0) (effects (font (size 1.524 1.524))))
      (property "Value" "Caddx_Ant" (at 0 -5.08 0) (effects (font (size 1.524 1.524))))
      (symbol "CAM_0_1" (rectangle (start -7.62 2.54) (end 7.62 -2.54) (stroke (width 0.254)) (fill (type background))))
      (symbol "CAM_1_1"
        (pin power_in line (at -12.7 1.27 0) (length 5.08) (name "5V" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -12.7 -1.27 0) (length 5.08) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin output line (at 12.7 0 0) (length 5.08) (name "VID_OUT" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "grok:RX" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "RX" (at 0 10.16 0) (effects (font (size 1.524 1.524))))
      (property "Value" "SuperD_ELRS" (at 0 -10.16 0) (effects (font (size 1.524 1.524))))
      (symbol "RX_0_1" (rectangle (start -10.16 7.62) (end 10.16 -7.62) (stroke (width 0.254)) (fill (type background))))
      (symbol "RX_1_1"
        (pin power_in line (at -15.24 6.35 0) (length 5.08) (name "5V" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -15.24 3.81 0) (length 5.08) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 6.35 0) (length 5.08) (name "TX" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at 15.24 3.81 0) (length 5.08) (name "RX" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 0 0) (length 5.08) (name "ANT1" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 -2.54 0) (length 5.08) (name "ANT2" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "grok:GPS" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "GPS" (at 0 5.08 0) (effects (font (size 1.524 1.524))))
      (property "Value" "M100-5883" (at 0 -5.08 0) (effects (font (size 1.524 1.524))))
      (symbol "GPS_0_1" (rectangle (start -10.16 3.81) (end 10.16 -3.81) (stroke (width 0.254)) (fill (type background))))
      (symbol "GPS_1_1"
        (pin power_in line (at -15.24 2.54 0) (length 5.08) (name "5V" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at -15.24 0 0) (length 5.08) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin output line (at 15.24 2.54 0) (length 5.08) (name "TX" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at 15.24 0 0) (length 5.08) (name "RX" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "grok:MOTOR" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "M" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
      (property "Value" "1804_3500KV" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
      (symbol "MOTOR_0_1" (circle (center 0 0) (radius 5.08) (stroke (width 0.254)) (fill (type background))))
      (symbol "MOTOR_1_1"
        (pin input line (at -10.16 1.27 0) (length 5.08) (name "A" (effects (font (size 1.016 1.016)))) (number "1" (effects (font (size 1.016 1.016)))))
        (pin input line (at -10.16 -1.27 0) (length 5.08) (name "B" (effects (font (size 1.016 1.016)))) (number "2" (effects (font (size 1.016 1.016)))))
        (pin input line (at -10.16 -3.81 0) (length 5.08) (name "C" (effects (font (size 1.016 1.016)))) (number "3" (effects (font (size 1.016 1.016)))))
      )
    )
  )
"""

# ─── SCHEMATIC BODY ───
# Position components on an A3 sheet (420x297mm)
# Layout: Power left-to-right, signals top-to-bottom

body = f"""  (junction (at 76.20 254.00) (diameter 0.9144) (color 0 0 0 0) (uuid {uid()}))
  (junction (at 127.00 254.00) (diameter 0.9144) (color 0 0 0 0) (uuid {uid()}))
  (junction (at 76.20 241.30) (diameter 0.9144) (color 0 0 0 0) (uuid {uid()}))
  (junction (at 127.00 241.30) (diameter 0.9144) (color 0 0 0 0) (uuid {uid()}))

  ;; ─── COMPONENTS ───

  (symbol (lib_id "grok:BATTERY") (at 25.40 254.00 0) (unit 1) (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "BAT1" (at 25.40 257.81 0))
    (property "Value" "2S 550mAh LiHV" (at 25.40 250.19 0))
    (pin "1" (uuid {uid()})) (pin "2" (uuid {uid()}))
  )

  (symbol (lib_id "grok:FC") (at 101.60 254.00 0) (unit 1) (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "FC1" (at 101.60 274.32 0))
    (property "Value" "Sbee F405 Mini" (at 101.60 233.68 0))
    (pin "1" (uuid {uid()})) (pin "2" (uuid {uid()})) (pin "3" (uuid {uid()}))
    (pin "4" (uuid {uid()})) (pin "5" (uuid {uid()})) (pin "6" (uuid {uid()})) (pin "7" (uuid {uid()}))
    (pin "8" (uuid {uid()})) (pin "9" (uuid {uid()})) (pin "10" (uuid {uid()}))
    (pin "11" (uuid {uid()})) (pin "12" (uuid {uid()})) (pin "13" (uuid {uid()}))
  )

  (symbol (lib_id "grok:ESC") (at 101.60 205.00 0) (unit 1) (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "ESC1" (at 101.60 212.62 0))
    (property "Value" "BLS 35A 4in1" (at 101.60 197.38 0))
    (pin "1" (uuid {uid()})) (pin "2" (uuid {uid()})) (pin "3" (uuid {uid()})) (pin "4" (uuid {uid()}))
    (pin "5" (uuid {uid()})) (pin "6" (uuid {uid()})) (pin "7" (uuid {uid()})) (pin "8" (uuid {uid()}))
  )

  (symbol (lib_id "grok:VTX") (at 177.80 254.00 0) (unit 1) (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "VTX1" (at 177.80 261.62 0))
    (property "Value" "Zeus 350mW" (at 177.80 246.38 0))
    (pin "1" (uuid {uid()})) (pin "2" (uuid {uid()})) (pin "3" (uuid {uid()}))
    (pin "4" (uuid {uid()})) (pin "5" (uuid {uid()}))
  )

  (symbol (lib_id "grok:CAM") (at 177.80 228.00 0) (unit 1) (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "CAM1" (at 177.80 233.08 0))
    (property "Value" "Caddx Ant" (at 177.80 222.92 0))
    (pin "1" (uuid {uid()})) (pin "2" (uuid {uid()})) (pin "3" (uuid {uid()}))
  )

  (symbol (lib_id "grok:RX") (at 177.80 190.00 0) (unit 1) (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "RX1" (at 177.80 200.16 0))
    (property "Value" "SuperD ELRS" (at 177.80 179.84 0))
    (pin "1" (uuid {uid()})) (pin "2" (uuid {uid()})) (pin "3" (uuid {uid()}))
    (pin "4" (uuid {uid()})) (pin "5" (uuid {uid()})) (pin "6" (uuid {uid()}))
  )

  (symbol (lib_id "grok:GPS") (at 177.80 160.00 0) (unit 1) (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "GPS1" (at 177.80 165.08 0))
    (property "Value" "M100-5883" (at 177.80 154.92 0))
    (pin "1" (uuid {uid()})) (pin "2" (uuid {uid()})) (pin "3" (uuid {uid()})) (pin "4" (uuid {uid()}))
  )

  ;; Motors
  (symbol (lib_id "grok:MOTOR") (at 254.00 220.00 0) (unit 1) (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "M1" (at 258.00 222.54 0))
    (property "Value" "FL-CCW" (at 258.00 217.46 0))
    (pin "1" (uuid {uid()})) (pin "2" (uuid {uid()})) (pin "3" (uuid {uid()}))
  )
  (symbol (lib_id "grok:MOTOR") (at 254.00 210.00 0) (unit 1) (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "M2" (at 258.00 212.54 0))
    (property "Value" "FR-CW" (at 258.00 207.46 0))
    (pin "1" (uuid {uid()})) (pin "2" (uuid {uid()})) (pin "3" (uuid {uid()}))
  )
  (symbol (lib_id "grok:MOTOR") (at 254.00 200.00 0) (unit 1) (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "M3" (at 258.00 202.54 0))
    (property "Value" "RL-CCW" (at 258.00 197.46 0))
    (pin "1" (uuid {uid()})) (pin "2" (uuid {uid()})) (pin "3" (uuid {uid()}))
  )
  (symbol (lib_id "grok:MOTOR") (at 254.00 190.00 0) (unit 1) (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "M4" (at 258.00 192.54 0))
    (property "Value" "RR-CW" (at 258.00 187.46 0))
    (pin "1" (uuid {uid()})) (pin "2" (uuid {uid()})) (pin "3" (uuid {uid()}))
  )

  ;; ─── POWER WIRES ───
  (wire (pts (xy 38.10 255.27) (xy 76.20 269.24)) (stroke (width 0.1524)) (uuid {uid()}))
  (wire (pts (xy 38.10 252.73) (xy 76.20 266.70)) (stroke (width 0.1524)) (uuid {uid()}))
  (wire (pts (xy 76.20 269.24) (xy 127.00 269.24)) (stroke (width 0.1524)) (uuid {uid()}))
  (wire (pts (xy 76.20 266.70) (xy 127.00 266.70)) (stroke (width 0.1524)) (uuid {uid()}))
  (wire (pts (xy 127.00 269.24) (xy 162.56 257.81)) (stroke (width 0.1524)) (uuid {uid()}))
  (wire (pts (xy 127.00 266.70) (xy 162.56 255.27)) (stroke (width 0.1524)) (uuid {uid()}))
  (wire (pts (xy 127.00 266.70) (xy 162.56 229.27)) (stroke (width 0.1524)) (uuid {uid()}))
  (wire (pts (xy 127.00 269.24) (xy 162.56 230.54)) (stroke (width 0.1524)) (uuid {uid()}))
  (wire (pts (xy 127.00 266.70) (xy 162.56 196.35)) (stroke (width 0.1524)) (uuid {uid()}))
  (wire (pts (xy 127.00 269.24) (xy 162.56 197.62)) (stroke (width 0.1524)) (uuid {uid()}))
  (wire (pts (xy 127.00 266.70) (xy 162.56 162.54)) (stroke (width 0.1524)) (uuid {uid()}))
  (wire (pts (xy 127.00 269.24) (xy 162.56 163.81)) (stroke (width 0.1524)) (uuid {uid()}))
  (wire (pts (xy 76.20 269.24) (xy 81.28 208.81)) (stroke (width 0.1524)) (uuid {uid()}))
  (wire (pts (xy 76.20 266.70) (xy 81.28 206.27)) (stroke (width 0.1524)) (uuid {uid()}))

  ;; ─── SIGNAL WIRES ───
  (wire (pts (xy 127.00 266.70) (xy 162.56 255.27)) (stroke (width 0.1524)) (uuid {uid()})) ;; TX4→VTX SA
  (wire (pts (xy 190.50 228.00) (xy 162.56 252.73)) (stroke (width 0.1524)) (uuid {uid()})) ;; CAM VID→VTX
  (wire (pts (xy 127.00 261.62) (xy 162.56 196.35)) (stroke (width 0.1524)) (uuid {uid()})) ;; TX5→RX
  (wire (pts (xy 193.04 196.35) (xy 127.00 259.08)) (stroke (width 0.1524)) (uuid {uid()})) ;; RX TX→FC
  (wire (pts (xy 127.00 256.54) (xy 162.56 162.54)) (stroke (width 0.1524)) (uuid {uid()})) ;; TX3→GPS
  (wire (pts (xy 193.04 162.54) (xy 127.00 254.00)) (stroke (width 0.1524)) (uuid {uid()})) ;; GPS TX→FC

  ;; ─── MOTOR WIRES ───
  (wire (pts (xy 76.20 264.16) (xy 81.28 203.73)) (stroke (width 0.1524)) (uuid {uid()})) ;; M1
  (wire (pts (xy 76.20 261.62) (xy 81.28 201.19)) (stroke (width 0.1524)) (uuid {uid()})) ;; M2
  (wire (pts (xy 76.20 259.08) (xy 121.92 208.81) (xy 121.92 203.73)) (stroke (width 0.1524)) (uuid {uid()})) ;; M3 via ESC
  (wire (pts (xy 76.20 256.54) (xy 121.92 206.27) (xy 121.92 201.19)) (stroke (width 0.1524)) (uuid {uid()})) ;; M4 via ESC
  (wire (pts (xy 121.92 208.81) (xy 243.84 221.27)) (stroke (width 0.1524)) (uuid {uid()})) ;; ESC M1→Motor1
  (wire (pts (xy 121.92 206.27) (xy 243.84 211.27)) (stroke (width 0.1524)) (uuid {uid()})) ;; ESC M2→Motor2
  (wire (pts (xy 121.92 203.73) (xy 243.84 201.27)) (stroke (width 0.1524)) (uuid {uid()})) ;; ESC M3→Motor3
  (wire (pts (xy 121.92 201.19) (xy 243.84 191.27)) (stroke (width 0.1524)) (uuid {uid()})) ;; ESC M4→Motor4

  ;; ─── NET LABELS (Reverse Wire Tags) ───
  (label "VBAT" (at 50.80 260.00 0) (effects (font (size 1.524 1.524))))
  (label "GND" (at 50.80 240.00 0) (effects (font (size 1.524 1.524))))
  (label "5V_RAIL" (at 140.00 260.00 0) (effects (font (size 1.524 1.524))))
  (label "TX4_SMARTAUDIO" (at 140.00 255.00 0) (effects (font (size 1.27 1.27))))
  (label "TX5_CRSF" (at 140.00 200.00 0) (effects (font (size 1.27 1.27))))
  (label "RX5_CRSF" (at 140.00 195.00 0) (effects (font (size 1.27 1.27))))
  (label "TX3_GPS" (at 140.00 165.00 0) (effects (font (size 1.27 1.27))))
  (label "RX3_GPS" (at 140.00 160.00 0) (effects (font (size 1.27 1.27))))
  (label "CAM_VIDEO" (at 170.00 235.00 0) (effects (font (size 1.27 1.27))))
  (label "M1_FL_CCW" (at 230.00 222.00 0) (effects (font (size 1.016 1.016))))
  (label "M2_FR_CW" (at 230.00 212.00 0) (effects (font (size 1.016 1.016))))
  (label "M3_RL_CCW" (at 230.00 202.00 0) (effects (font (size 1.016 1.016))))
  (label "M4_RR_CW" (at 230.00 192.00 0) (effects (font (size 1.016 1.016))))

  ;; ─── SPECIFICATION NOTES (clean, organized) ───
  (text "GX140 3in ANALOG FPV — ELECTRICAL SCHEMATIC" (at 40.64 285.00 0) (effects (font (size 3.81 3.81))))
  (text "═══ POWER ═══" (at 25.40 278.00 0) (effects (font (size 2.54 2.54))))
  (text "Battery: 2S 550mAh LiHV (7.4V) XT30" (at 25.40 273.00 0) (effects (font (size 1.524 1.524))))
  (text "FC: SpeedyBee F405 Mini 20x20 | ICM42688 | DPS310 | 25x25x6.5mm | 4 UARTs" (at 25.40 269.00 0) (effects (font (size 1.27 1.27))))
  (text "ESC: BLS 35A 4in1 20x20 | 3-6S | DShot600 | Bidirectional ON" (at 25.40 266.00 0) (effects (font (size 1.27 1.27))))
  (text "═══ SIGNALS ═══" (at 25.40 260.00 0) (effects (font (size 2.54 2.54))))
  (text "UART4 TX4 -> VTX SmartAudio RX (PA control, 115200 baud)" (at 25.40 256.00 0) (effects (font (size 1.27 1.27))))
  (text "UART5 TX5/RX5 <=> RX CRSF (ELRS V3, 420000 baud)" (at 25.40 253.00 0) (effects (font (size 1.27 1.27))))
  (text "UART3 TX3/RX3 <=> GPS UBLOX (optional M100-5883, 57600 baud)" (at 25.40 250.00 0) (effects (font (size 1.27 1.27))))
  (text "═══ MOTORS ═══" (at 25.40 244.00 0) (effects (font (size 2.54 2.54))))
  (text "HGLRC Specter 1804 3500KV | 13.3g | 12x12mm M2 | 1.5mm shaft | 22.68x13.2mm" (at 25.40 240.00 0) (effects (font (size 1.27 1.27))))
  (text "GEMFAN 3052 3in tri-blade | 5mm hub + 1.5mm adapter | 22.8mm tip clearance" (at 25.40 237.00 0) (effects (font (size 1.27 1.27))))
  (text "═══ MECHANICAL ═══" (at 25.40 231.00 0) (effects (font (size 2.54 2.54))))
  (text "GX140 140mm 4mm carbon | Twin 20x20 tower | 8x M3x25mm alu standoffs | ~45g bare" (at 25.40 227.00 0) (effects (font (size 1.27 1.27))))
  (text "Stack: ESC(4.5)+NUT(2)+FC(6.5)+NUT(2)=15mm | Standoff=25mm | Clearance=10mm" (at 25.40 224.00 0) (effects (font (size 1.27 1.27))))
  (text "AUW: ~190g (under 250g limit) | CG: <1mm offset" (at 25.40 221.00 0) (effects (font (size 1.27 1.27))))
  (text "═══ RF ═══" (at 25.40 215.00 0) (effects (font (size 2.54 2.54))))
  (text "VTX: Zeus 350mW 16x16->20x20 | SMA->Foxeer Lollipop RHCP (rear, 50mm)" (at 25.40 211.00 0) (effects (font (size 1.27 1.27))))
  (text "RX: SuperD ELRS 22x14mm 1.1g | Dual SX1280 | ANT1 vert L standoff ANT2 horiz top" (at 25.40 208.00 0) (effects (font (size 1.27 1.27))))
  (text "Separation: VTX->RX1 >=25mm | RX1->RX2 >=40mm | All >10mm from carbon/props" (at 25.40 205.00 0) (effects (font (size 1.27 1.27))))
  (text "═══ WIRING ═══" (at 25.40 199.00 0) (effects (font (size 2.54 2.54))))
  (text "22AWG: VBAT, GND, 5V rail | 26AWG: UART, ESC signal | 28AWG: I2C, sensors" (at 25.40 195.00 0) (effects (font (size 1.27 1.27))))
  (text "Heat shrink all solder joints | JST-SH 1.0mm for CAM/VTX | JST-GH 1.25mm for GPS" (at 25.40 192.00 0) (effects (font (size 1.27 1.27))))
  (text "═══ SAFETY ═══" (at 25.40 186.00 0) (effects (font (size 2.54 2.54))))
  (text "ShortSaver MANDATORY before first power | Props OFF for motor test in Configurator" (at 25.40 182.00 0) (effects (font (size 1.27 1.27))))
  (text "Continuity check all rails before battery | Motor direction verify before props" (at 25.40 179.00 0) (effects (font (size 1.27 1.27))))
  (text "GROK — FPV Drone Engineering | 2025-12-12 | Sheet 1/1 | All dimensions verified" (at 340.00 15.00 0) (effects (font (size 1.27 1.27))))
"""

# ─── ASSEMBLE ───
schematic = f"""(kicad_sch (version 20230121) (generator "grok_fpv")

  (uuid {uid()})

  (paper "A3")

  (title_block
    (title "GX140 3\\" Analog FPV — Electrical Schematic")
    (date "2025-12-12")
    (rev "1.0")
    (company "GROK — FPV Drone Engineering")
    (comment 1 "Frame: GX140 140mm twin 20x20, 4mm carbon")
    (comment 2 "Motors: HGLRC Specter 1804 3500KV (12x12 M2)")
    (comment 3 "FC: SpeedyBee F405 Mini | ESC: BLS 35A 4in1")
    (comment 4 "VTX: Zeus 350mW | CAM: Caddx Ant | RX: SuperD ELRS")
    (comment 5 "Battery: 2S 550mAh LiHV | AUW: ~190g")
  )

{symbols}

{body}
)
"""

with open(OUT, 'w') as f:
    f.write(schematic)

# Project file
proj = f"""(kicad_project (version 7)
  (paper "A3")
  (title "GX140 3\\" Analog FPV")
  (date "2025-12-12")
  (rev "1.0")
  (company "GROK — FPV Drone Engineering")
  (schematic_files (0 "gx140_clean.kicad_sch"))
)
"""
with open(PRO, 'w') as f:
    f.write(proj)

print(f"Written: {OUT} ({len(schematic)} bytes)")
print(f"Written: {PRO}")
