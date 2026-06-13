# SBC FPV Companion Deployment Checklists
**Generated:** 2025-12-12

---

## RADXA ROCK 5C LITE ×2 — Primary Airborne Companion

### Specifications
| Parameter | Value |
|-----------|-------|
| **SOC** | Rockchip RK3588S2 |
| **CPU** | 4× Cortex-A76 @ 2.4GHz + 4× Cortex-A55 @ 1.8GHz |
| **NPU** | **6 TOPS INT8** (RKNPU2) |
| **GPU** | Mali-G610 MP4 |
| **RAM** | 16GB LPDDR4X |
| **Storage** | MicroSD + PCIe 2.1 x1 (M.2 E-key) |
| **Video** | HDMI 8K@60, MIPI CSI ×2, MIPI DSI ×1 |
| **Network** | GbE, WiFi 6/BT 5.1 (module) |
| **GPIO** | 40-pin header (UART ×4, I2C ×3, SPI ×2, PWM ×4) |
| **Dimensions** | 86mm × 56mm (from Radxa wiki) |
| **Weight** | ~45g (board only) |
| **Mounting** | **Custom pattern** — does NOT fit standard 30.5×30.5 or 20×20 stacks. Needs adapter plate. Mounting holes in DXF at dl.radxa.com |

### Model Performance (RK3588S2 @ 6 TOPS INT8)
| Model | Resolution | FPS | Precision |
|-------|------------|-----|-----------|
| YOLOv11n | 640×640 | **~120 FPS** | INT8 |
| YOLOv11s | 640×640 | **~65 FPS** | INT8 |
| YOLOv8n-seg | 640×640 | **~55 FPS** | INT8 |
| DepthAnything-ViT-S | 640×640 | **~18 FPS** | INT8 |
| MobileSAM | 640×640 | **~30 FPS** | INT8 |
| LLaMA-3.2-3B-GGUF-q4 | - | **~25 tok/s** | INT4/INT8 |
| Phi-3.5-mini-GGUF-q4 | - | **~35 tok/s** | INT4/INT8 |

### Power Requirements
| State | Power | Current @ 5V |
|-------|-------|--------------|
| Idle | 2.5-3W | 0.5-0.6A |
| Full NPU | 5-7W | 1.0-1.4A |
| Peak | 8-10W | 1.6-2.0A |
| **Recommended** | **5V 5A** | **2S-6S → 5V 5A BEC** |

### Cooling
**Active mandatory.** Passive hits 85°C+ in 3 min at full NPU.
- Solution: 30×30×10mm heatsink + 5V 3010 fan = 55°C sustained
- Mount: M2.5 standoffs on 4 mounting holes (3.5mm Ø)

### FPV Integration Role
**Heavy edge inference / ROS2 navigation / Computer vision on 5-7" quads**
- ROS2 Nav2 + YOLOv11 obstacle avoidance + depth estimation
- UART/MAVLink to FC for closed-loop control
- NVMe for model storage + blackbox logs + video recording

### Hardware Needed (per unit)
- [ ] Rock 5C Lite 16GB (have 2)
- [ ] PCIe M.2 E-key → M-key adapter + NVMe 256GB+ (need)
- [ ] Active heatsink + 5V 3010 fan kit (need)
- [ ] 5V 5A BEC: Matek 5V 5A or Pololu D24V50F5 (need 2)
- [ ] MicroSD UHS-I A2 128GB+ (need 2)
- [ ] 40-pin GPIO header + right-angle for low profile (need)
- [ ] Mini HDMI → HDMI cable (for dev)
- [ ] USB-C PD trigger board or 20V→5V buck (optional)

### Software Stack
| Layer | Technology |
|-------|------------|
| OS | Radxa Official Debian 12 (Bookworm) + RKNPU2 toolkit |
| NPU Runtime | RKNPU2 / rknn-toolkit2 (Python/C++) |
| CV | OpenCV 4.x + GStreamer (RKMPP hardware decode) |
| Inference | rknn-toolkit2 → ONNX → RKNN quantization |
| LLM | llama.cpp (RKNPU backend) or MLC-LLM |
| ROS2 | Humble/Iron on Ubuntu 22.04/24.04 |
| Serial | pyserial / MAVLink / MSP over UART (GPIO UART2/4) |

### FC Link
- **Primary:** UART (TELEM2) → MSP/MAVLink for telemetry + control
- **Secondary:** CAN (if FC supports) for higher bandwidth
- **Baud:** 921600 (MSP) / 57600 (MAVLink)

### Camera Options
| Interface | Options | Notes |
|-----------|---------|-------|
| MIPI CSI | IMX219, IMX477, OV5647, AR0234 | Need camera module + ribbon |
| USB3 | Logitech Brio, ELP USB3, FLIR Boson | UVC/V4L2, easier integration |
| GMSL | Maxim GMSL2 serializer + IMX390 | Long cable runs, automotive grade |

### Storage
- **NVMe (PCIe):** Models + blackbox logs + video recording
- **MicroSD:** OS boot only (A2 class minimum)

---

## RADXA ZERO 3W — Lightweight Telemetry/Bridge

### Specifications
| Parameter | Value |
|-----------|-------|
| **SOC** | Rockchip RK3566 |
| **CPU** | 4× Cortex-A55 @ 1.8GHz |
| **NPU** | **~1 TOPS INT8** |
| **GPU** | Mali-G52 2EE |
| **RAM** | 4GB LPDDR4X |
| **Storage** | MicroSD (no eMMC) |
| **Video** | HDMI 1080p@60, MIPI CSI ×1, MIPI DSI ×1 |
| **Network** | WiFi 5 + BT 5.0 (onboard) |
| **GPIO** | 40-pin castellated edges (need header solder) |
| **Dimensions** | 45mm × 45mm |
| **Weight** | ~15g (board only) |

### Power
| State | Power | Current @ 5V |
|-------|-------|--------------|
| Idle | 1.2W | 0.24A |
| Full | 2.5-3W | 0.5-0.6A |
| **Source** | **5V from FC BEC** | |

### Cooling
Passive sufficient for typical loads. Small 20×20×5mm heatsink recommended.

### FPV Integration Role
**Sensor fusion / Optical flow / Telemetry bridge / KWS on 3-5" builds**
- Optical flow (PAA5100/PMW3901) via SPI/I2C
- Precision hover, indoor nav, obstacle proximity
- WiFi/BT telemetry backup (ELRS primary)
- Keyword spotting (Porcupine/Picovoice on NPU)

### Hardware Needed
- [ ] Zero 3W 4GB (have 1, no GPIO header)
- [ ] **Solder 40-pin header** (2.54mm pitch) or use castellated edges
- [ ] MicroSD UHS-I 64GB+
- [ ] Tiny heatsink 20×20×5mm
- [ ] Optional: MIPI CSI camera (OV5647/IMX219)

### Software Stack
| Layer | Technology |
|-------|------------|
| OS | Radxa Debian/Ubuntu for Zero 3W |
| NPU | RKNPU2 (RK3566 support in rknn-toolkit2) |
| CV | OpenCV + libcamera (MIPI) or v4l2 (USB) |
| Inference | YOLOv8n/YOLOv11n INT8, MobileNet-SSD |
| Audio | Keyword spotting (Porcupine/Picovoice on NPU) |

---

## KHADAS VIM4 — Ground Station / Video Processor

### Specifications
| Parameter | Value |
|-----------|-------|
| **SOC** | Amlogic A311D2 |
| **CPU** | 4× Cortex-A73 @ 2.2GHz + 4× Cortex-A53 @ 2.0GHz |
| **NPU** | **3.2 TOPS INT8** (NPU) |
| **GPU** | Mali-G52 MP6 (8EE) |
| **RAM** | 8GB LPDDR4X |
| **Storage** | 32GB eMMC + MicroSD + M.2 2280 NVMe |
| **Video** | **HDMI IN 4K@60** (unique), HDMI OUT 4K@60, MIPI CSI ×2, MIPI DSI ×1 |
| **Network** | WiFi 6 + BT 5.1, GbE |
| **GPIO** | 40-pin header |
| **Dimensions** | 82mm × 58mm |
| **Weight** | ~45g (board only) |

### Unique Feature
**HDMI IN 4K@60 → Hardware H.265 encode** — Capture goggles output directly.

### Power
| State | Power | Voltage |
|-------|-------|---------|
| Idle | 3W | 12V/2A barrel or USB-C PD |
| HDMI Capture + Encode | 5-7W | 12V |
| Full NPU | 6-8W | 12V |

### Cooling
**Official active cooler required** for sustained HDMI capture + NPU.

### FPV Integration Role
**HDMI capture → encode → stream/record / Moderate inference on recorded footage**
- Input: HDMI IN from Walksnail/DJI/HDZero goggles
- Process: Real-time detect → overlay → re-stream to phone/PC
- Record: Full 4K60 H.265 recording of FPV feed + telemetry overlay
- Post-flight: Run heavier models (YOLOv11x, SAM2, DepthAnything) on recorded footage

### Hardware Needed
- [ ] VIM4 8+32GB (have)
- [ ] VIM4 case (have)
- [ ] **VIM4 official active cooler** (need)
- [ ] **12V 2A power supply** (barrel jack)
- [ ] **M.2 NVMe 512GB+** (need for recording)
- [ ] HDMI cable (goggles → VIM4 IN)

### Software Stack
| Layer | Technology |
|-------|------------|
| OS | Khadas Official Ubuntu 22.04 (Focal) / 24.04 (Noble) |
| HDMI Capture | V4L2 / GStreamer (Amlogic VPU hardware) |
| Encode | H.264/H.265 hardware encode (VPU) |
| NPU | NN SDK (3.2 TOPS, INT8/INT16/FP16) |
| Inference | YOLOv8, MobileNet, custom TFLite/ONNX → NN SDK |
| Streaming | GStreamer → RTSP/SRT/WHIP/WebRTC |
| Recording | MP4/TS via GStreamer + NVMe |

---

## IMMEDIATE NEXT STEPS (Priority Order)

| # | Task | Why |
|---|------|-----|
| 1 | Order Rock 5C PCIe M.2 adapter + NVMe 256GB | Enables model storage |
| 2 | Order 2× Rock 5C active heatsink + fan kits | Required for sustained NPU |
| 3 | Order 2× 5V 5A BEC (Matek/Pololu) for 2S-6S → 5V | Clean power from flight battery |
| 4 | Order 40-pin header for Zero 3W + solder | Enable UART/I2C/SPI for FC |
| 5 | Order VIM4 active cooler + 12V supply + M.2 NVMe 512GB | Enable HDMI capture |
| 6 | Flash Radxa Debian 12 on Rock 5C ×2 + Zero 3W | Baseline OS with RKNPU2 |
| 7 | Flash Khadas Ubuntu 22.04 on VIM4 | Baseline OS with NN SDK |
| 8 | Build MSP/MAVLink telemetry bridge (Python) on Rock 5C | FC ↔ Companion communication |
| 9 | Quantize YOLOv11n + MobileSAM to RKNN for Rock 5C | Primary CV models |
| 10 | Test HDMI IN capture on VIM4 with Walksnail goggles | Validate ground station |