# PCB Defect Detection Dataset Card

## Dataset Summary
This dataset contains images of Printed Circuit Board (PCB) designs annotated with specific manufacturing defects. It was created to train computer vision models (specifically YOLOv8) for Automated Optical Inspection (AOI) tasks. The goal is to detect Signal Integrity (SI) and Electromagnetic Interference (EMI) risks early in the design phase.

## Supported Tasks
- **Task:** Object Detection
- **Target Objects:**
  1. `Stub` (Unterminated traces causing signal reflection)
  2. `90_Degree` (Sharp corners causing acid traps and impedance issues)

## Dataset Structure

### Data Split
The dataset consists of **944 total images**, split into the following subsets:

| Subset | Image Count | Percentage | Purpose |
| :--- | :--- | :--- | :--- |
| **Train** | 834 | 88% | Used for model training |
| **Valid** | 76 | 8% | Used for hyperparameter tuning |
| **Test** | 34 | 4% | Used for final performance evaluation |

### Classes
| Class ID | Class Name | Description |
| :--- | :--- | :--- |
| 0 | `Stub` | Excess conductive material or dead-end traces acting as antennas. |
| 1 | `90_Degree` | Traces routed at sharp 90-degree angles instead of 45-degree miters. |

## Data Creation

### Source Data
The dataset was constructed using a **hybrid approach** combining proprietary and open-source materials:

1.  **Author's Proprietary Designs:** Custom PCB layouts previously designed by the author for various embedded systems projects.
2.  **Open Source Repositories:** Validated reference designs sourced from platforms like GitHub and OpenHardware.

### Data Generation Methodology (Fault Injection)
Since real-world manufacturing defects are rare and hard to capture in large volumes, a **"Fault Injection"** methodology was applied:
- **Process:** "Clean" (error-free) PCB designs were selected as a baseline.
- **Manipulation:** Specific defects (Stub errors and 90-degree bends) were **intentionally introduced** into these healthy designs using PCB design software (Altium/KiCad). This ensured the model learned from a diverse range of realistic error scenarios.

### Preprocessing & Augmentation
To improve model generalization and robustness against variations, the following augmentations were applied using Roboflow:
- **Outputs per training example:** 3 (Dataset size tripled)
- **Flip:** Horizontal, Vertical
- **Rotation:** Between -15° and +15°
- **Brightness:** Between -15% and +15°

## Considerations
- **Scope:** The dataset focuses on geometric layout errors relevant to high-speed PCB design.
- **Licensing:** Educational Use / MIT License.
