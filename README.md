🚗 AI-Based Autonomous Navigation System
📌 Overview

This project demonstrates an AI-powered autonomous navigation system that simulates how self-driving systems perceive and navigate environments.

It combines real-time object detection with intelligent path planning.

🎯 Key Features
A* path planning algorithm
YOLOv8 real-time object detection
Obstacle-aware navigation
Simulation-based environment
Animated visualization (GIF)
🧠 Tech Stack
Python
OpenCV
Ultralytics YOLOv8
NumPy
Matplotlib
🔄 System Workflow
Capture environment via webcam
Detect objects using YOLOv8
Identify obstacles
Apply A* algorithm
Generate optimal path
Visualize navigation
🚀 Results
🔴 YOLO Detection

<img width="640" height="480" alt="01_yolo_detection" src="https://github.com/user-attachments/assets/d7a844f9-87ce-4c40-b581-520aa88b1856" />




🟢 Path Planning


<img width="640" height="480" alt="02_output_path" src="https://github.com/user-attachments/assets/4fcecb09-3a2c-4980-ab28-3ed02301ed9e" />



🔵 Animated Navigation


![03_animated_path](https://github.com/user-attachments/assets/3c9dfabf-534b-4715-9c8b-2fffd1859941)



▶️ How to Run
pip install -r requirements.txt
python src/main.py
📚 Learning Outcomes
Built end-to-end AI pipeline (perception → planning → action)
Implemented real-time object detection
Designed simulation-based navigation system
🚀 Future Improvements
CARLA self-driving simulation
Reinforcement learning
Multi-agent systems
Real robot deployment

👤 Author
Challa Kishore
