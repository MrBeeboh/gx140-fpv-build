// OpenSCAD Parametric Mounts for SBC FPV Integration
// Render with: openscad -o mount.stl mount.scad
// All dimensions in mm

// ============================================================
// GLOBAL PARAMETERS
// ============================================================
$fn = 60;  // Circle resolution

// Carbon fiber thickness
CF_THICK = 3.0;       // Typical 3mm carbon frame
CF_HOLE_DIA = 3.2;    // M3 clearance

// SBC mounting
M2_5_HOLE = 2.8;      // M2.5 clearance
M3_HOLE = 3.2;        // M3 clearance
STANDOFF_H = 10;      // Default standoff height

// ============================================================
// RADXA ROCK 5C LITE MOUNT
// ============================================================
module rock5c_mount(
    standoff_h = 12,
    include_heatsink = true,
    heatsink_w = 30,
    heatsink_l = 30,
    heatsink_h = 10,
    fan_mount = true,
    fan_size = 30,  // 3010 fan
    cable_relief = true,
    orientation = "flat"  // "flat" or "vertical"
) {
    // Rock 5C Lite PCB: 86 x 56 mm (verified from Radxa wiki)
    pcb_w = 86;
    pcb_l = 56;
    pcb_thick = 1.6;
    
    // Mounting holes (4x — from DXF at dl.radxa.com)
    // Exact positions not in public documentation — estimate from DXF
    mh_x = pcb_w - 10;   // ~76mm spacing
    mh_y = pcb_l - 10;   // ~46mm spacing
    
    difference() {
        union() {
            // Base plate with rounded corners
            translate([-pcb_w/2, -pcb_l/2, 0])
            rounded_box(pcb_w + 10, pcb_l + 10, standoff_h, 5);
            
            // Standoffs at mounting holes
            for (x = [-mh_x/2, mh_x/2], y = [-mh_y/2, mh_y/2]) {
                translate([x, y, 0])
                cylinder(d = 6, h = standoff_h);
            }
            
            // Heatsink mount
            if (include_heatsink) {
                translate([0, 0, standoff_h + pcb_thick])
                heatsink_block(heatsink_w, heatsink_l, heatsink_h, fan_mount, fan_size);
            }
            
            // Cable relief slots
            if (cable_relief) {
                translate([0, -pcb_l/2 - 5, standoff_h/2])
                rotate([90, 0, 0])
                cylinder(d = 12, h = 10);
            }
        }
        
        // Mounting holes (M2.5 clearance)
        for (x = [-mh_x/2, mh_x/2], y = [-mh_y/2, mh_y/2]) {
            translate([x, y, -1])
            cylinder(d = M2_5_HOLE, h = standoff_h + 2);
        }
        
        // PCB clearance (board sits on standoffs)
        translate([-pcb_w/2, -pcb_l/2, standoff_h])
        cube([pcb_w, pcb_l, pcb_thick + 0.5]);
        
        // Heatsink clearance
        if (include_heatsink) {
            translate([-heatsink_w/2, -heatsink_l/2, standoff_h + pcb_thick])
            cube([heatsink_w, heatsink_l, heatsink_h + 0.5]);
        }
    }
}

module heatsink_block(w, l, h, fan_mount, fan_size) {
    difference() {
        // Heatsink base
        translate([-w/2, -l/2, 0])
        cube([w, l, h]);
        
        // Fan mount cutout
        if (fan_mount) {
            translate([0, 0, h/2])
            cylinder(d = fan_size + 2, h = h + 1);
            
            // Fan screw holes (3010: 28mm pattern)
            fs = 28;
            for (x = [-fs/2, fs/2], y = [-fs/2, fs/2]) {
                translate([x, y, -1])
                cylinder(d = 3.2, h = h + 2);
            }
        }
        
        // Fin pattern (cosmetic - for airflow simulation)
        // Real fins would be printed separately or use off-the-shelf
    }
}

// ============================================================
// RADXA ZERO 3W MOUNT
// ============================================================
module zero3w_mount(
    standoff_h = 8,
    include_header = true,
    header_h = 8.5,
    orientation = "flat"
) {
    // Zero 3W PCB: 65 x 30 mm (verified from Radxa DXF)
    pcb_w = 65;
    pcb_l = 30;
    pcb_thick = 1.2;
    
    // Mounting holes: from DXF — 4x M2.5 at corners
    // Verified positions: (3.60,26.45), (61.40,3.60), (61.40,26.50), (3.55,3.60)
    // Approximate spacing for parametric model
    mh_spacing_x = 57.80;  // 61.40 - 3.60
    mh_spacing_y = 22.90;  // 26.50 - 3.60
    
    // 40-pin header position (centered)
    header_w = 52;  // 2.54mm × 20 pins
    header_l = 8.5;
    
    difference() {
        union() {
            // Base plate
            translate([-pcb_w/2 - 5, -pcb_l/2 - 5, 0])
            rounded_box(pcb_w + 10, pcb_l + 10, standoff_h, 4);
            
            // Standoffs at 4 corners
            for (x = [-mh_spacing/2, mh_spacing/2], y = [-mh_spacing/2, mh_spacing/2]) {
                translate([x, y, 0])
                cylinder(d = 5, h = standoff_h);
            }
            
            // 40-pin header relief
            if (include_header) {
                translate([-header_w/2, -header_l/2, standoff_h + pcb_thick])
                cube([header_w, header_l, header_h]);
            }
        }
        
        // Mounting holes (M2.5)
        for (x = [-mh_spacing/2, mh_spacing/2], y = [-mh_spacing/2, mh_spacing/2]) {
            translate([x, y, -1])
            cylinder(d = M2_5_HOLE, h = standoff_h + 2);
        }
        
        // PCB clearance
        translate([-pcb_w/2, -pcb_l/2, standoff_h])
        cube([pcb_w, pcb_l, pcb_thick + 0.3]);
        
        // Header clearance
        if (include_header) {
            translate([-header_w/2, -header_l/2, standoff_h + pcb_thick])
            cube([header_w, header_l, header_h + 1]);
        }
    }
}

// ============================================================
// KHADAS VIM4 MOUNT
// ============================================================
module vim4_mount(
    standoff_h = 10,
    include_cooler = true,
    cooler_w = 60,
    cooler_l = 60,
    cooler_h = 25,
    nvme_slot = true,
    orientation = "flat"
) {
    // VIM4 PCB: 82 x 58 mm (verified from Khadas docs)
    pcb_w = 82;
    pcb_l = 58;
    pcb_thick = 1.6;
    
    // Mounting holes: 4x M3 pattern
    // Estimated from PCB dimensions (exact positions not published)
    mh_x = 70;
    mh_y = 46;
    
    difference() {
        union() {
            // Base plate
            translate([-pcb_w/2 - 8, -pcb_l/2 - 8, 0])
            rounded_box(pcb_w + 16, pcb_l + 16, standoff_h, 6);
            
            // Standoffs
            for (x = [-mh_x/2, mh_x/2], y = [-mh_y/2, mh_y/2]) {
                translate([x, y, 0])
                cylinder(d = 7, h = standoff_h);
            }
            
            // Official active cooler mount
            if (include_cooler) {
                translate([0, 0, standoff_h + pcb_thick])
                cooler_block(cooler_w, cooler_l, cooler_h);
            }
            
            // NVMe slot access
            if (nvme_slot) {
                // M.2 2280 at bottom edge
                translate([0, -pcb_l/2 - 2, standoff_h/2])
                cube([25, 10, standoff_h]);
            }
            
            // HDMI IN/OUT port relief
            translate([-pcb_w/2 - 8, 0, standoff_h/2])
            cube([10, 20, standoff_h]);
        }
        
        // Mounting holes (M3)
        for (x = [-mh_x/2, mh_x/2], y = [-mh_y/2, mh_y/2]) {
            translate([x, y, -1])
            cylinder(d = M3_HOLE, h = standoff_h + 2);
        }
        
        // PCB clearance
        translate([-pcb_w/2, -pcb_l/2, standoff_h])
        cube([pcb_w, pcb_l, pcb_thick + 0.5]);
        
        // Cooler clearance
        if (include_cooler) {
            translate([-cooler_w/2, -cooler_l/2, standoff_h + pcb_thick])
            cube([cooler_w, cooler_l, cooler_h + 1]);
        }
    }
}

module cooler_block(w, l, h) {
    difference() {
        translate([-w/2, -l/2, 0])
        cube([w, l, h]);
        
        // Fan cutout (40x40mm typical)
        translate([0, 0, h/2])
        cylinder(d = 42, h = h + 1);
        
        // Fan screw holes
        fs = 32;
        for (x = [-fs/2, fs/2], y = [-fs/2, fs/2]) {
            translate([x, y, -1])
            cylinder(d = 3.2, h = h + 2);
        }
    }
}

// ============================================================
// UNIVERSAL CAMERA MOUNT (MIPI CSI / USB)
// ============================================================
module camera_mount(
    camera_type = "imx219",  // "imx219", "imx477", "ov5647", "usb", "gmsl"
    tilt_deg = 0,
    pan_deg = 0,
    standoff_h = 15
) {
    // Camera board dimensions
    dims = [
        ["imx219", 24, 24, 4, 2],     // Pi Camera v2
        ["imx477", 38, 38, 5, 3],     // Pi HQ Camera
        ["ov5647", 24, 24, 4, 2],     // Pi Camera v1
        ["usb", 30, 30, 10, 2],       // Generic USB
        ["gmsl", 40, 30, 8, 3]        // GMSL serializer + sensor
    ];
    
    cam_w = 24; cam_l = 24; cam_h = 4; mh = 2;
    for (d = dims) {
        if (d[0] == camera_type) { cam_w = d[1]; cam_l = d[2]; cam_h = d[3]; mh = d[4]; }
    }
    
    // Mounting hole pattern: 18mm square for Pi cameras
    mh_spacing = (camera_type == "imx477") ? 30 : 18;
    
    union() {
        // Base
        translate([-cam_w/2 - 10, -cam_l/2 - 10, 0])
        rounded_box(cam_w + 20, cam_l + 20, standoff_h, 5);
        
        // Standoffs at camera mounting holes
        for (x = [-mh_spacing/2, mh_spacing/2], y = [-mh_spacing/2, mh_spacing/2]) {
            translate([x, y, 0])
            cylinder(d = 5, h = standoff_h);
        }
        
        // Camera board mount
        translate([0, 0, standoff_h])
        rotate([tilt_deg, pan_deg, 0])
        translate([-cam_w/2, -cam_l/2, 0])
        cube([cam_w, cam_l, cam_h]);
        
        // Lens opening
        translate([0, 0, standoff_h + cam_h/2])
        rotate([tilt_deg, pan_deg, 0])
        cylinder(d = 12, h = cam_h + 2);
    }
    
    // Mounting holes
    for (x = [-mh_spacing/2, mh_spacing/2], y = [-mh_spacing/2, mh_spacing/2]) {
        translate([x, y, -1])
        cylinder(d = 2.2, h = standoff_h + 2);
    }
}

// ============================================================
// FRAME INTEGRATION MOUNTS
// ============================================================

// 30.5×30.5mm stack mount (standard FC pattern)
module stack30_mount(
    holes = 4,
    standoff_h = 8,
    include_sbc = false
) {
    pattern = 30.5;
    
    difference() {
        translate([-pattern/2 - 5, -pattern/2 - 5, 0])
        rounded_box(pattern + 10, pattern + 10, standoff_h + 3, 4);
        
        for (x = [-pattern/2, pattern/2], y = [-pattern/2, pattern/2]) {
            translate([x, y, -1])
            cylinder(d = M3_HOLE, h = standoff_h + 5);
        }
    }
}

// 20×20mm stack mount
module stack20_mount(
    standoff_h = 8
) {
    pattern = 20;
    
    difference() {
        translate([-pattern/2 - 4, -pattern/2 - 4, 0])
        rounded_box(pattern + 8, pattern + 8, standoff_h + 3, 3);
        
        for (x = [-pattern/2, pattern/2], y = [-pattern/2, pattern/2]) {
            translate([x, y, -1])
            cylinder(d = M2_5_HOLE, h = standoff_h + 5);
        }
    }
}

// 16×16mm whoop mount
module stack16_mount(
    standoff_h = 6
) {
    pattern = 16;
    
    difference() {
        translate([-pattern/2 - 3, -pattern/2 - 3, 0])
        rounded_box(pattern + 6, pattern + 6, standoff_h + 2, 2);
        
        for (x = [-pattern/2, pattern/2], y = [-pattern/2, pattern/2]) {
            translate([x, y, -1])
            cylinder(d = 2.0, h = standoff_h + 4);
        }
    }
}

// ============================================================
// WIRE ROUTING CHANNELS
// ============================================================

module wire_channel(
    length = 100,
    width = 10,
    height = 5,
    cover = true,
    cover_gap = 0.3
) {
    difference() {
        union() {
            translate([-width/2, -length/2, 0])
            cube([width, length, height]);
            
            if (cover) {
                translate([-width/2, -length/2, height + cover_gap])
                cube([width, length, 1.5]);
            }
        }
        
        // Internal cavity
        translate([-width/2 + 1, -length/2 + 1, 0])
        cube([width - 2, length - 2, height - 1]);
    }
}

// ============================================================
// HELPER: Rounded box
// ============================================================
module rounded_box(w, l, h, r) {
    translate([-w/2, -l/2, 0])
    minkowski() {
        cube([w - 2*r, l - 2*r, h]);
        cylinder(r = r, h = 0.01);
    }
}

// ============================================================
// EXAMPLE USAGE - Uncomment to render specific parts
// ============================================================

/*
// Rock 5C mount for 5" frame (30.5 stack)
translate([0, 0, 0])
rock5c_mount(standoff_h = 12, include_heatsink = true);

// Zero 3W mount for 3" frame (20×20 stack)
translate([0, 0, 0])
zero3w_mount(standoff_h = 8);

// VIM4 ground station mount
translate([0, 0, 0])
vim4_mount(standoff_h = 10, include_cooler = true);

// IMX219 camera mount (forward facing, 15° down tilt)
translate([0, 0, 0])
camera_mount("imx219", tilt_deg = -15, standoff_h = 20);

// IMX477 HQ camera (nadir for mapping)
translate([0, 0, 0])
camera_mount("imx477", tilt_deg = -90, standoff_h = 15);

// 30.5 stack with Rock 5C on top
union() {
    stack30_mount(standoff_h = 8);
    translate([0, 0, 8])
    rock5c_mount(standoff_h = 12, orientation = "flat");
}
*/

// ============================================================
// BILL OF MATERIALS FOR 3D PRINTING
// ============================================================

/*
PRINT QUEUE (PLA+ / PETG / ASA):

1. Rock 5C Mount ×2
   - Material: ASA (heat resistance)
   - Infill: 40% gyroid
   - Supports: Yes (heatsink overhang)
   - Time: ~3hr each
   - Hardware: M2.5×12mm standoffs ×8, M2.5×6mm screws ×8, M2.5 nuts ×8

2. Zero 3W Mount ×1
   - Material: PETG
   - Infill: 30%
   - Time: ~1.5hr
   - Hardware: M2.5×8mm standoffs ×4

3. VIM4 Ground Station Mount ×1
   - Material: PLA+ (indoor)
   - Infill: 30%
   - Time: ~2hr
   - Hardware: M3×10mm standoffs ×4

4. Camera Mounts ×3 (IMX219 forward, IMX477 nadir, USB spare)
   - Material: ASA
   - Infill: 40%
   - Time: ~1hr each
   - Hardware: M2×8mm standoffs ×4 each

5. Wire Channels (various lengths)
   - 50mm ×4, 100mm ×2, 150mm ×1
   - Material: TPU (flexible) or PETG
   - Time: ~20min each

6. Stack Spacers
   - 30.5mm: 8mm ×4, 12mm ×2, 20mm ×2
   - 20×20mm: 8mm ×4, 12mm ×2
   - 16×16mm: 6mm ×4
*/

// ============================================================
// FITMENT CHECK TABLES (for manual verification)
// ============================================================

/*
ROCK 5C ON 5" FRAME (Mark5 / Mario 5 / Source One V5)
-----------------------------------------------------
Frame stack height:     30.5mm pattern
FC height:              ~12mm (F4/F7 + OSD)
ESC height:             ~10mm (4in1)
Rock 5C mount:          12mm standoff + 1.6mm PCB + 10mm heatsink = 23.6mm
Total stack:            12 + 10 + 23.6 = 45.6mm
Prop clearance (5"):    Check 2207 motor bell to Rock 5C heatsink
Battery strap path:     Must route around Rock 5C mount

ZERO 3W ON 3" FRAME (GX140)
---------------------------
Frame: 20×20 stack
FC: SpeedyBee F405 Mini (20×20)
Zero 3W mount: 8mm standoff
Total: Fits between FC and top plate
USB-C access: Side cutout needed for OTG

VIM4 GROUND STATION
-------------------
Desktop enclosure
HDMI IN from goggles: 2m cable routing
12V input: Barrel jack panel mount
NVMe: Rear access slot
Fan: 40×40×10mm Noctua NF-A4x10
*/