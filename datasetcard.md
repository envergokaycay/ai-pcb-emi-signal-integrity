# PCB Defect Detection Dataset Card

## Dataset Summary
This dataset contains images of Printed Circuit Board (PCB) designs annotated with specific manufacturing defects. It was created to train computer vision models (specifically YOLOv8) for Automated Optical Inspection (AOI) tasks. The goal is to detect Signal Integrity (SI) and Electromagnetic Interference (EMI) risks, such as "Stub Errors" and "90-Degree Bends," early in the design phase.

## Supported Tasks
- **Task:** Object Detection
- **Target Objects:** 1. `Stub` (Unterminated traces causing signal reflection)
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
- **Origin:** The dataset is derived from industrial Gerber files and synthetic PCB design errors generated for simulation purposes.
- **Image Format:** .jpg / .png

### Preprocessing & Augmentation
To improve model generalization and robustness against variations, the following augmentations were applied using Roboflow:

- **Outputs per training example:** 3 (Dataset size tripled)
- **Flip:** Horizontal, Vertical
- **Rotation:** Between -15° and +15°
- **Brightness:** Between -15% and +15%

## Considerations
- **Scope:** The dataset focuses on geometric layout errors relevant to high-speed PCB design.
- **Licensing:** Educational Use / MIT License.
