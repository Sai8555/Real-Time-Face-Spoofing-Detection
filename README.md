# Design and Implementation of a Real-Time Face Spoofing Detection System

An AI-powered biometric security solution developed to distinguish between genuine and spoofed faces in real-time, preventing unauthorized access through print, replay, or 3D mask attacks.

---

## 👥 Project Developers & Credentials

This project is a collaborative team effort, developed under the curriculum of the Bachelor of Technology (B.Tech) program.

### 🎓 Submitted By:
* **JANAPAREDDY GIRI SAI DURGA** (Regd No: **21U41A4218**) — *B.Tech Computer Science and Engineering (Artificial Intelligence & Machine Learning)*

### 🤝 Project Associates (The Team):
* **J. Giri Sai Durga** (Regd No: **21U41A4218**)
* **K. Abhishek** (Regd No: **21U41A4222**)
* **P. Sai Durga Rao** (Regd No: **21U41A4231**)
* **Y. Vamsi Ganga Arjun** (Regd No: **22U45A4223**)

### 🏫 Academic Credentials:
* **Academic Period:** 2021 – 2025
* **Project Guide:** **Mrs. K. LAVANYA**, Assistant Professor, Department of CSM & CSD
* **Institution:** **DADI INSTITUTE OF ENGINEERING & TECHNOLOGY** (An Autonomous Institute, Approved by A.I.C.T.E. & Permanently Affiliated to JNTUGV, Accredited by NAAC with 'A' Grade), Anakapalle - 530002, Visakhapatnam, Andhra Pradesh, India.

---

## 📖 Project Abstract & Overview

Facial recognition technology has gained widespread adoption in security and authentication systems. However, these systems are highly vulnerable to presentation attacks (spoofing), where an attacker presents printed photos, digital screens, or 3D masks to deceive the scanner.

To mitigate these threats, this project implements a **Real-Time Face Spoofing Detection System** utilizing a deep learning Convolutional Neural Network (CNN) based on the **MobileNetV2** architecture. MobileNetV2 is selected for its lightweight design, employing depthwise separable convolutions to reduce computational overhead, making it ideal for real-time inference on edge devices.

The model is trained and validated on the publicly available **LCC-FASD** (Large Crowdcollected Face Anti-Spoofing Dataset), which contains a diverse set of real and spoofed face images.

### 🛠️ Key Pipeline Stages:
1. **Data Preprocessing & Augmentation**: Normalization, resizing to $224 \times 224 \times 3$, and augmentation (rotation, zooming, shearing, horizontal flipping) to prevent overfitting and improve generalization.
2. **Feature Extraction**: Leverages a pre-trained **MobileNetV2** backbone (with ImageNet weights) to capture micro-texture, depth, and reflectance properties.
3. **Classification**: Employs custom dense layers, dropout normalization, and a sigmoid activation function to output a binary classification (Real vs. Spoofed).
4. **Real-Time Interface**: Integrated into an interactive web interface powered by **Flask** and a standalone cv2 webcam monitor.

---

## 📈 Model Performance & Results

The system achieves exceptional accuracy and low-latency performance:

* **Classification Accuracy**: **98.02%** on test data
* **Precision**: **99.25%**
* **Recall**: **98.68%**
* **F1 Score**: **98.96%**
* **ROC-AUC**: **0.995**
* **Real-time Latency**: **< 100 milliseconds** per frame

---

## 📁 Repository Structure

```directory
Final Year Project/
├── README.md                     # Main project documentation (This file)
├── requirements.txt              # Project dependencies
├── Website/                      # Main Flask Web Application
│   ├── app.py                    # Flask web app script
│   ├── face_antispoofing_model.h5 # Trained MobileNetV2 model binary
│   ├── templates/                # Frontend HTML templates (index.html, etc.)
│   └── static/                   # CSS styles and JavaScript assets
├── Face_liveness/                # Standalone Python Test Scripts
│   ├── run.py                    # Independent webcam liveness script
│   └── face-liveliness.ipynb     # Jupyter Notebook detailing model evaluation
└── server/                       # Proxy configurations (Node-based)
    └── node-proxy/               # Node-proxy server
```

---

## 🚀 Setup & Execution Guide

### 1️⃣ Installation
Ensure you have Python 3.7+ installed. Clone this repository, navigate to the root directory, and install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Standalone Webcam Liveness Tester
For a direct OpenCV webcam interface that tests face liveness:
```bash
python Face_liveness/run.py
```
*Press `q` to exit the live camera feed.*

### 3️⃣ Run the Interactive Flask Web Application
```bash
cd Website
python app.py
```
Then, open your browser and go to: `http://127.0.0.1:5000`

---

## 🌐 Deploying Live to the Web

Since this is a Python Flask backend application that loads a TensorFlow machine learning model, it cannot be hosted directly using static hosting services like **GitHub Pages** (which only support static HTML/CSS/JS with no backend execution).

However, you can easily host this project live for free by linking your GitHub repository to a cloud platform like **Render** or **Railway**:

### How to Deploy on Render (Free Tier):
1. Create a free account on **[Render.com](https://render.com/)**.
2. Click **New +** and select **Web Service**.
3. Connect your GitHub account and select your **`Real-Time-Face-Spoofing-Detection`** repository.
4. Set the following configuration details:
   - **Name**: `face-spoofing-detection`
   - **Environment**: `Python 3`
   - **Region**: Choose the closest region (e.g., Oregon or Singapore)
   - **Branch**: `main`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn Website.app:app` (or `python Website/app.py` for direct dev execution)
5. Click **Deploy Web Service**. Render will automatically pull the code, install dependencies, load the TensorFlow model, and give you a public URL (e.g. `https://face-spoofing-detection.onrender.com`)!

---

## 📜 License
This project is licensed under the MIT License.
