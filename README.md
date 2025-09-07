Hand Gesture Based PPT Controller

This project allows you to control PowerPoint (or any presentation software) using hand gestures via webcam.
It uses computer vision to detect hand gestures and maps them to keyboard actions (next/previous slide).

✨ Supported Gestures:
All 5 fingers up → Next Slide ➡
Only thumb up → Previous Slide ⬅

📦 Requirements
Python Version
Python 3.8 or later (Recommended: 3.8 – 3.11 for library compatibility)

Libraries Used
Install the following dependencies before running:
opencv-python
 → For webcam and image processing
cvzone
 → Hand tracking wrapper (built on MediaPipe)
mediapipe
 → Core hand tracking framework
pyautogui
 → To simulate keyboard events
time
 → Built-in Python library (no installation needed

▶️ How to Run
Connect a webcam to your system (or use your laptop’s built-in camera).
Start your PowerPoint presentation in Slideshow Mode.
Run the script:
python gesture_ppt_controller.py

Show your hand in front of the camera and use gestures:
All fingers up → Next slide
Only thumb up → Previous slide
Press Q on the keyboard to exit.

⚠️ Notes
Make sure the presentation window is in focus, otherwise keystrokes won’t work.
Lighting conditions affect detection accuracy. Use in a well-lit room.
You can adjust the cooldown value in the code to avoid accidental multiple triggers.

👤 Developer KevalKing Instagram: @keval_king_212
