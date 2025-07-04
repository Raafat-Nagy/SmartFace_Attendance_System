# **SmartFace Attendance System**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-orange.svg)](https://opencv.org/)
[![face\_recognition](https://img.shields.io/badge/face__recognition-1.3.0-green.svg)](https://github.com/ageitgey/face_recognition)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

**SmartFace\_Attendance\_System** is a real-time face recognition system for automated student attendance tracking using computer vision. It detects and recognizes faces from a webcam, logs attendance to CSV files with timestamps, and optionally sends data to a university backend via API.

---

## Key Features

* Real-time face detection and recognition using webcam
* Encodes known face images and saves as `.pkl`
* Automatic CSV attendance logging (date + time)
* API integration with university systems (optional)
* Session-based duplicate prevention
* Modular, maintainable Python architecture

---

## Sample Use Cases

* Classroom attendance automation
* University smart attendance systems
* Student presence analytics
* Integration with college management platforms

---

## Tech Stack

| Component         | Description                |
| ----------------- | -------------------------- |
| Python            | Main programming language  |
| OpenCV            | Real-time video processing |
| face\_recognition | Face detection & encoding  |
| NumPy             | Numerical operations       |
| CSV               | Local attendance logging   |
| Requests          | API communication          |

---

## Project Structure

```
SmartFace_Attendance_System/
│
├── attendance_records/
│   └── 04-07-2025_22-32-13_attendance.csv
│
├── known_faces_data/
│   └── Raafat_Nagy.jpg
│
├── models/
│   └── encodings.pkl
│
├── src/
│   ├── api/
│   │   └── send_attendance_api.py
│   ├── encoder/
│   │   └── face_encoder.py
│   ├── recognizer/
│   │   └── face_recognition_system.py
│   ├── logger/
│   │   └── csv_logger.py
│   └── utils/
│       └── draw_box_label.py
│
├── encode_faces.ipynb
├── face_recognition_system_main.ipynb
├── requirements.txt
└── run_recognition.py
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Raafat-Nagy/SmartFace_Attendance_System.git
cd SmartFace_Attendance_System
```

### Create virtual environment

```bash
python -m venv venv
source venv/bin/activate      # For Linux/macOS
venv\Scripts\activate         # For Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Face Encoding

Place labeled student images in `known_faces_data/`, where each filename corresponds to the student name or ID.

Then run:

```bash
python encode_faces.py
```

This creates `models/encodings.pkl`.

---

## Run the System

Launch the recognition system:

```bash
python run_recognition.py
```

The webcam window will show face boxes and names. Attendance will be saved automatically.

---

## API Integration

If `send_api=True`, attendance is sent to:

```
GET https://nextgenedu-database.azurewebsites.net/api/attendance/{hall_id}/{student_tag}
```

You can enable or disable this in `run_recognition.py`.

---

## Output Example

* Real-time webcam feed with name overlays
* Logs saved in `attendance_records/DATE_TIME_attendance.csv`
* Columns: `Name`, `Time`

---

## Acknowledgments

* [face\_recognition](https://github.com/ageitgey/face_recognition)
* [OpenCV](https://opencv.org/)
* [NumPy](https://numpy.org/)

---
