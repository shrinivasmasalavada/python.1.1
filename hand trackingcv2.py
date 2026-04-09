import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

points = []

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            h, w, c = img.shape

            # Index finger tip
            cx = int(handLms.landmark[8].x * w)
            cy = int(handLms.landmark[8].y * h)

            points.append((cx, cy))

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    # Draw colorful lines
    for i in range(1, len(points)):
        cv2.line(img, points[i-1], points[i],
                 (i % 255, (i*2) % 255, (i*3) % 255), 5)

    cv2.imshow("Hand Drawing", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break