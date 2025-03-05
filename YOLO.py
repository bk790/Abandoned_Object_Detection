import cv2
import numpy as np
import torch
from ultralytics import YOLO
from tracker import *


device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load YOLOv8 
model = YOLO("yolov8m.pt").to(device) 

# Initialize 
tracker = ObjectTracker()

video_path = r"C:\Users\bk\Desktop\opt\video1.avi"
cap = cv2.VideoCapture(video_path)

frame_count = 0  

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # Increase resolution 
    frame = cv2.resize(frame, (640, 480))

    # confidence threshold
    results = model(frame, conf=0.2) 

    detections = []  # Store detected objects

    # Debugging: Print detected objects
    for result in results:
        for box in result.boxes:
            x, y, w, h = map(int, box.xyxy[0])  # Bounding box coordinates
            label = model.names[int(box.cls[0])]  # Object class name
            confidence = round(float(box.conf[0]), 2)  # Confidence score

            print(f"Frame {frame_count}: Detected {label} with {confidence*100}% confidence")

            # Only track luggage-related objects (Modify if needed)
            if label in ["suitcase", "handbag", "backpack"]:  
                detections.append([x, y, w - x, h - y])
    
    # Update Tracker
    _, abandoned_objects = tracker.update(detections)

    # Draw Bounding Boxes
    for obj in abandoned_objects:
        _, x2, y2, w2, h2, _ = obj
        cv2.putText(frame, "Abandoned Object!", (x2, y2 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 255), 2)

    # Display FPS
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    cv2.putText(frame, f"FPS: {fps}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("Abandoned Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
