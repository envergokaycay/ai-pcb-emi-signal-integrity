# 🖥️ PCB Defect Detection: AI-Powered AOI System
### Early Detection of EMI & Signal Integrity Risks using YOLOv8

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Framework](https://img.shields.io/badge/Framework-YOLOv8-green)
![UI](https://img.shields.io/badge/UI-Streamlit-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📖 Overview
**PCB Defect Detection** is a Deep Learning-based Automated Optical Inspection (AOI) tool designed to identify critical geometric errors in Printed Circuit Board designs **before manufacturing**. 

By leveraging **Computer Vision (YOLOv8)**, this system detects high-risk patterns—specifically **Stub Errors** and **90-Degree Bends**—that cause Signal Integrity (SI) issues and Electromagnetic Interference (EMI). Unlike traditional tools, it not only detects faults but also provides **actionable technical solutions** to fix them.

---

## 🎯 Key Features
* **High Accuracy Detection:** Detects microscopic errors with **91.4% mAP@50**.
* **Specific Fault Classification:**
    * 🔴 **Stub Errors:** Dead-end traces acting as antennas (EMI Risk).
    * 🟠 **90° Bends:** Sharp corners causing acid traps and impedance mismatch.
* **Smart Action Plan:** The system flags errors and guides the engineer with specific solutions (e.g., *"Remove segment," "Apply 45° miter"*).
* **User-Friendly Interface:** Web-based analysis via **Streamlit**.

---

## 🌍 Alignment with UN SDGs
This project supports the United Nations Sustainable Development Goals:

* **Goal 9: Industry, Innovation and Infrastructure:** Digitalizing manufacturing to reduce defect rates.
* **Goal 12: Responsible Consumption:** Preventing E-Waste (electronic scrap) by ensuring "First-Time-Right" production.
* **Goal 4: Quality Education:** Acting as a virtual mentor to teach junior engineers about EMI risks.

---

## 📊 Model Performance
The model was trained on a hybrid dataset of **944 images** (Real Industrial Designs + Synthetic Fault Injection) using **YOLOv8**.

| Metric | Score | Description |
| :--- | :--- | :--- |
| **mAP@50** | **91.4%** | Excellent general detection capability. |
| **Precision** | **90.4%** | Low false alarm rate. |
| **Recall** | **91.7%** | Misses very few actual errors. |
| **mAP@50-95**| **46.2%** | High geometric localization accuracy. |

*(See `modelcard.md` for detailed training graphs and confusion matrix.)*

---

## 🚀 Installation & Usage

## 1. Clone the Repository
git clone [https://github.com/envergokaycay/ai-pcb-emi-signal-integrity
.git]([https://github.com/YOUR_USERNAME/REPO_NAME.git](https://github.com/envergokaycay/ai-pcb-emi-signal-integrity
.git))
cd REPO_NAME

## 2. Install Dependencies
pip install -r requirements.txt

## 3. Run the Application
streamlit run app.py

## 4. Test
Upload a PCB image (Gerber export or photo) to the interface and view the results instantly.

📂 Project Structure
Plaintext

├── app.py              # Streamlit Web Application
├── best.pt             # Trained YOLOv8 Model Weights
├── datasetcard.md      # Dataset documentation & sources
├── modelcard.md        # Technical model details & metrics
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

🛠️ Tech Stack
Core Engine: Python, PyTorch

Model Architecture: YOLOv8 (Ultralytics)

Interface: Streamlit

Image Processing: PIL (Pillow), OpenCV

Dataset Management: Roboflow

👨‍💻 Developer
Enver Gökay ÇAY Project developed for Samsung Innovation Campus / Capstone Project.

📜 License
This project is licensed under the MIT License.
