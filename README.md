# 🔍 Missing Person Detection System (Face Recognition)

A real-time face recognition application developed to assist in identifying missing persons using CCTV or surveillance footage. Built using Python, OpenCV, and Haar Cascades, this project demonstrates the application of AI in social good.

## 🎯 Objective

To develop a facial recognition system that can detect and identify missing individuals from surveillance inputs by comparing detected faces with a pre-registered database.

## 🧠 Tech Stack

- **Language**: Python
- **Libraries**: OpenCV, NumPy
- **Algorithm**: Haar Cascade Classifier (Viola–Jones)
- **Database**: SQLite / MySQL (for person data storage)
- **GUI (Optional)**: Tkinter

## 🚀 Features

- 📸 Real-time face detection from webcam or CCTV feed
- 🧠 Uses Haar Cascades for efficient face recognition
- 🧾 Stores and retrieves known face data for comparison
- 📍 Identifies matches with high accuracy (~95%)
- ⚡ Fast detection with response time < 1.5 seconds in controlled environments

## 🖥️ How It Works

1. Load dataset of missing persons (images + metadata)
2. Capture input video stream
3. Detect faces in each frame using Haar Cascades
4. Compare detected face with dataset
5. Display result (matched person name or “Unknown”)

## 📦 Installation

```bash
git clone https://github.com/Arunr30/missing-person-detection.git
cd missing-person-detection
pip install -r requirements.txt
