# Face Recognition-Based Attendance System with Weekly Analysis and Mentor Notification

## 📌 Project Overview
The Face Recognition-Based Attendance System is an automated solution designed to record classroom attendance using facial recognition technology. The system captures images of students, recognizes their faces, and marks attendance automatically.

Additionally, the system performs weekly attendance analysis and notifies mentors if a student’s attendance falls below a predefined threshold.

This system helps reduce manual effort, eliminates proxy attendance, and provides data-driven insights into student attendance patterns.

---

## 🎯 Objectives of the Project

- Automate the process of taking classroom attendance
- Eliminate manual errors and proxy attendance
- Use face recognition to identify students accurately
- Store attendance records digitally
- Provide weekly attendance analysis
- Notify mentors about low attendance students
- Generate visual attendance reports

---

## 🧠 Technologies Used

- Python
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Haar Cascade Classifier
- Machine Learning (LBPH Face Recognizer)

---

## ⚙️ System Modules

### 1️⃣ Face Data Collection
Captures student face images using a camera and stores them in the dataset folder.

### 2️⃣ Face Training Module
Trains the face recognition model using collected images and generates a trained model file.

### 3️⃣ Face Recognition & Attendance Marking
Detects and recognizes student faces in a classroom image and records attendance.

### 4️⃣ Attendance Storage
Attendance is stored in CSV files for record keeping.

### 5️⃣ Weekly Attendance Analysis
Analyzes attendance data and identifies students with low attendance.

### 6️⃣ Mentor Notification
Alerts mentors when student attendance falls below the required percentage.

### 7️⃣ Attendance Visualization
Generates graphs to visually represent student attendance patterns.

---

## 📂 Project Structure
Face_Attendance_System
│
├── dataset/ # Stores student face images
├── trainer/ # Stores trained model
├── attendance/ # Stores attendance records
│
├── capture_faces.py # Captures student images
├── train_model.py # Trains face recognition model
├── attendance_system.py # Detects faces and marks attendance
├── weekly_analysis.py # Analyzes weekly attendance
├── attendance_graph.py # Generates attendance graphs
│
└── haarcascade_frontalface_default.xml

---

## ▶️ How to Run the Project

### Step 1: Capture Student Faces : capture_faces.py

### Step 2: Train the Model : train_model.py

### Step 3: Run Attendance System : attendance_system.py

### Step 4: Generate Weekly Analysis : weekly_analysis.py

### Step 5: Display Attendance Graph : attendance_graph.py

---

## 📊 Expected Output

- Automated attendance marking
- Attendance stored in CSV format
- Weekly attendance report
- Mentor notification for low attendance
- Graphical attendance analysis

---

## 🚀 Future Scope

- Integration with mobile applications
- Cloud-based attendance storage
- Real-time classroom monitoring
- Email or SMS notification to mentors
- Multi-classroom support
- Integration with college ERP systems

---

## 👨‍💻 Author

Final Year Project  
Face Recognition-Based Attendance System
