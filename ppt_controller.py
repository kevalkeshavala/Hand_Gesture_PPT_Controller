import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import time

# Webcam setup
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Cooldown timer
last_action_time = 0
cooldown = 1.0  # seconds (adjust if needed)

while True:
    success, img = cap.read()
    if not success:
        break

    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        current_time = time.time()
        if current_time - last_action_time > cooldown:
            # If all 5 fingers up → Next slide
            if fingers == [1, 1, 1, 1, 1]:
                pyautogui.press("right")
                print("➡ Next Slide")
                last_action_time = current_time

            # If only thumb up → Previous slide
            elif fingers == [1, 0, 0, 0, 0]:
                pyautogui.press("left")
                print("⬅ Previous Slide")
                last_action_time = current_time

    cv2.imshow("Hand Gesture PPT Controller", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
