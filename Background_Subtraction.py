import cv2
import numpy as np
from tracker import *

# Initialize Tracker
tracker = ObjectTracker()

# Use Adaptive Background Subtraction (Instead of a Fixed First Frame)
bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)

# Load video
video_path = r"C:\Users\bk\Desktop\opt\video1.avi"  
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Replace First Frame Subtraction with Background Subtraction
    fg_mask = bg_subtractor.apply(frame_gray)

    #Apply Morphological Transformations
    kernel = np.ones((10, 10), np.uint8)
    thresh = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    #Find Contours
    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    detections = []
    for c in cnts:
        contour_area = cv2.contourArea(c)
        if 50 < contour_area < 10000:
            x, y, w, h = cv2.boundingRect(c)
            detections.append([x, y, w, h])

    #Update Tracker
    _, abandoned_objects = tracker.update(detections)

    #Draw bounding boxes on abandoned objects
    for obj in abandoned_objects:
        _, x2, y2, w2, h2, _ = obj
        cv2.putText(frame, "Abandoned Object!", (x2, y2 - 10), cv2.FONT_HERSHEY_PLAIN, 1.2, (0, 0, 255), 2)
        cv2.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 255), 2)

    cv2.imshow('Abandoned Object Detection', frame)

    if cv2.waitKey(15) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
