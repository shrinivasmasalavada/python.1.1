import cv2
import torch
import pygame

# Load sound
pygame.mixer.init()
pygame.mixer.music.load("alert.wav")

# Load YOLO model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    detections = results.xyxy[0]

    id_detected = False

    for *box, conf, cls in detections:
        x1, y1, x2, y2 = map(int, box)

        if conf > 0.5:
            id_detected = True

            # Green box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

            label = f"ID Card {conf:.2f}"
            cv2.putText(frame, label, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    if not id_detected:
        # Red alert
        cv2.putText(frame, "NO ID CARD!", (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

        pygame.mixer.music.play()

    cv2.imshow("ID Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()