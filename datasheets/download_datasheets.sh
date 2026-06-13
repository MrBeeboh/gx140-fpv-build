#!/bin/bash
# Download datasheets and manuals for all drone components
# Save to: /home/mike/projects/Drone Projects/datasheets/

DEST="/home/mike/projects/Drone Projects/datasheets"
mkdir -p "$DEST"

echo "=== Downloading datasheets and manuals ===" > "$DEST/download_log.txt"

# Radxa Rock 5C Lite
curl -sL -o "$DEST/radxa_rock5c_schematic.pdf" "https://dl.radxa.com/rock5/5c/radxa_rock_5c_lite_schematic.pdf" -w "\nradxa_rock5c: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &
curl -sL -o "$DEST/radxa_rock5c_datasheet.pdf" "https://dl.radxa.com/rock5/5c/radxa_rock_5c_lite_product_brief.pdf" -w "\nradxa_rock5c_brief: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &

# Radxa Zero 3W
curl -sL -o "$DEST/radxa_zero3w_schematic.pdf" "https://dl.radxa.com/zero3w/radxa_zero_3w_schematic.pdf" -w "\nradxa_zero3w_schematic: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &
curl -sL -o "$DEST/radxa_zero3w_datasheet.pdf" "https://dl.radxa.com/zero3w/radxa_zero_3w_product_brief.pdf" -w "\nradxa_zero3w_brief: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &

# Khadas VIM4
curl -sL -o "$DEST/khadas_vim4_specs.pdf" "https://dl.khadas.com/products/vim4/specs/vim4_specifications.pdf" -w "\nkhadas_vim4_specs: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &
curl -sL -o "$DEST/khadas_vim4_datasheet.pdf" "https://dl.khadas.com/products/vim4/specs/vim4_datasheet.pdf" -w "\nkhadas_vim4_datasheet: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &

# Matek H743-WLITE
curl -sL -o "$DEST/matek_h743_wlite_manual.pdf" "https://www.mateksys.com/downloads/FC/H743-WLITE/H743-WLITE_Manual.pdf" -w "\nmatek_h743_wlite: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &

# Matek M10Q-5883 GPS
curl -sL -o "$DEST/matek_m10q_5883_manual.pdf" "https://www.mateksys.com/downloads/GPS/M10Q-5883/M10Q-5883_Manual.pdf" -w "\nmatek_m10q_5883: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &

# Matek Optical Flow 3901-L0X
curl -sL -o "$DEST/matek_3901_l0x_manual.pdf" "https://www.mateksys.com/downloads/Sensors/3901-L0X/3901-L0X_Manual.pdf" -w "\nmatek_3901l0x: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &

# Matek PDB-HEX
curl -sL -o "$DEST/matek_pdb_hex_manual.pdf" "https://www.mateksys.com/downloads/PDB/PDB-HEX/PDB-HEX_Manual.pdf" -w "\nmatek_pdb_hex: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &

# Betaflight 2025.12 CLI Reference
curl -sL -o "$DEST/betaflight_2025_12_cli_reference.md" "https://raw.githubusercontent.com/betaflight/betaflight.com/master/docs/wiki/guides/current/Betaflight-2025.12-CLI-commands.md" -w "\nbetaflight_cli: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &

# Betaflight MSP Protocol Reference
curl -sL -o "$DEST/betaflight_msp_protocol.md" "https://raw.githubusercontent.com/betaflight/betaflight.com/master/docs/development/MSP-Protocol-Reference-Dev.md" -w "\nbetaflight_msp: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &

# RK3588 Technical Reference Manual (Rockchip)
curl -sL -o "$DEST/rk3588_trm_part1.pdf" "https://opensource.rock-chips.com/images/4/4e/Rockchip_RK3588_TRM_V1.0-Part1-20220309.pdf" -w "\nrk3588_trm1: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &

# RK3566 Datasheet (Rockchip)
curl -sL -o "$DEST/rk3566_datasheet.pdf" "https://opensource.rock-chips.com/images/c/c5/Rockchip_RK3566_Datasheet_V1.0-20201201.pdf" -w "\nrk3566_ds: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &

# SpeedyBee F405 Mini
curl -sL -o "$DEST/speedybee_f405_mini_manual.pdf" "https://www.speedybee.com/download/F405Mini/F405Mini_Manual.pdf" -w "\nspeedybee_f405: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &

# SpeedyBee Adapter (BT Nano)
curl -sL -o "$DEST/speedybee_bt_nano_manual.pdf" "https://www.speedybee.com/download/BTNano/BTNano_Manual.pdf" -w "\nspeedybee_btnano: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &

# Walksnail Avatar Goggles X
curl -sL -o "$DEST/walksnail_goggles_x_manual.pdf" "https://caddxfpv.com/pages/download" -w "\nwalksnail_goggles_x: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &

# Walksnail Avatar Pro Kit
curl -sL -o "$DEST/walksnail_avatar_pro_manual.pdf" "https://caddxfpv.com/pages/download" -w "\nwalksnail_avatar_pro: %{http_code} %{size_download}B\n" >> "$DEST/download_log.txt" 2>&1 &

echo "All downloads launched in background. Check $DEST/download_log.txt for status."