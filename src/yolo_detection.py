import cv2
from ultralytics import YOLO
import os

def run_yolo():
    os.makedirs("images", exist_ok=True)
    os.makedirs("videos", exist_ok=True)

    model = YOLO("yolov8n.pt")

    cap = cv2.VideoCapture(0)

    # Video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('videos/demo.mp4', fourcc, 20.0, (640, 480))

    saved = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        annotated_frame = results[0].plot()

        # Save first image only once
        if not saved:
            cv2.imwrite("images/01_yolo_detection.png", annotated_frame)
            saved = True

        out.write(annotated_frame)

        cv2.imshow("YOLO Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()