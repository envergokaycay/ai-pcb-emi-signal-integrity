# Model Card for PCB Fault Detector (YOLOv8)

## Model Details
- **Model Name:** PCB-Fault-Detector-v1.0
- **Model Architecture:** YOLOv8 (You Only Look Once - Version 8)
- **Task:** Object Detection
- **Framework:** PyTorch / Ultralytics
- **Developer:** Enver Gökay ÇAY
- **Dataset:** Trained on 944 PCB images (See `datasetcard.md`)
- **Training Environment:** Google Colab (T4 GPU)

## Intended Use
- **Primary Use Case:** Automated Optical Inspection (AOI) of PCB designs.
- **Function:** Detects "Stub" and "90-Degree" errors in Gerber files or PCB photos.
- **Target Audience:** PCB Designers, Hardware Engineers, Manufacturing Quality Control.

## Training Data
The model was trained on a dataset of **944 images** with extensive augmentation (Rotation +/- 15°, Brightness +/- 15%, Flips).
- **Classes:** `hata_stub` (Stub Error), `hata_90` (90-Degree Error)

## Performance Metrics
The model achieved high accuracy after training for **50 Epochs**.

| Metric | Score | Description |
| :--- | :--- | :--- |
| **mAP@50** | **0.914** | High detection accuracy (91.4%). |
| **Precision** | **0.904** | 90.4% of detected errors were actual errors. |
| **Recall** | **0.917** | 91.7% of all real errors in the images were successfully found. |
| **mAP@50-95**| **0.462** | Average precision across different thresholds. |

### Confusion Matrix Analysis
As seen in the confusion matrix results:
- **90-Degree Errors:** The model correctly identified **91** instances, missing only 5 (classified as background).
- **Stub Errors:** The model correctly identified **90** instances, with extremely low confusion (only 1 misclassified as 90-degree).

![Confusion Matrix](https://github.com/envergokaycay/ai-pcb-emi-signal-integrity/blob/main/confusion_matrix.png) 

## How to Use (Python)

```python
from ultralytics import YOLO

# Load the model
model = YOLO('best.pt')

# Run inference
results = model.predict('pcb_sample.jpg', conf=0.45)

# Show results
results[0].show()
