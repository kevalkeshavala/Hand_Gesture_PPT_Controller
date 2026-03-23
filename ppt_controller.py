import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

last_action_time = 0
cooldown = 1.0

# Set this after calibration
MIN_HAND_AREA = 9000   # This is for approx 50 cm distance

while True:
    success, img = cap.read()
    if not success:
        break

    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        hand_area = w * h

        if hand_area > MIN_HAND_AREA:   # Only detect within 50 cm
            fingers = detector.fingersUp(hand)
            current_time = time.time()

            if current_time - last_action_time > cooldown:
                if fingers == [1, 1, 1, 1, 1]:
                    pyautogui.press("right")
                    print("➡ Next Slide")
                    last_action_time = current_time

                elif fingers == [1, 0, 0, 0, 0]:
                    pyautogui.press("left")
                    print("⬅ Previous Slide")
                    last_action_time = current_time
        else:
            print("Hand too far (more than 50 cm)")

    cv2.imshow("Hand Gesture PPT Controller", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
