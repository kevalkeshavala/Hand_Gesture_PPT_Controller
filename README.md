# Hand Gesture Based PPT Controller
This project allows you to control **PowerPoint (or any presentation software)** using **hand gestures via a webcam**.
It uses **Computer Vision and Hand Tracking** to detect gestures and convert them into keyboard actions like **Next Slide** and **Previous Slide**.

# ✨ Features
* Control presentation **without touching keyboard**
* Uses **webcam hand detection**
* Works with **PowerPoint, Google Slides, Keynote, PDF viewers, etc.**
* Simple **2-gesture control system**

# ✋ Supported Gestures

| Gesture          | Action           |
| ---------------- | ---------------- |
| All 5 fingers up | Next Slide ➡     |
| Only Thumb Up    | Previous Slide ⬅ |

# 📦 Requirements

## Python Version
Python **3.8 – 3.11 recommended**

# 📚 Libraries Used
This project uses the following Python libraries:

###1️⃣ OpenCV

Used for:

* Accessing the webcam
* Image processing
* Displaying camera frames

Install:

pip install opencv-python


### 2️⃣ CVZone

Used for:

* Simplified **hand tracking wrapper**
* Built on top of **MediaPipe**

Install:
pip install cvzone

### 3️⃣ MediaPipe

Used for:

* Core **hand detection and landmark tracking**
* Machine learning based gesture recognition

Install:
pip install mediapipe

### 4️⃣ PyAutoGUI

Used for:

* Simulating **keyboard presses**
* Used here to trigger **left/right arrow keys**

Install:

pip install pyautogui

### 5️⃣ Time (Built-in Library)

Used for:

* Creating **cooldown time**
* Preventing multiple slide triggers instantly

No installation required.


# 📥 Install All Libraries (Quick Method)

You can install everything with one command:

=>  pip install opencv-python cvzone mediapipe pyautogui

# 📂 Project Structure


HandGesturePPTController
│
├── gesture_ppt_controller.py
├── README.md


---

# ▶️ How to Run the Project

### 1️⃣ Clone or Download the Project
git clone https://github.com/yourusername/HandGesturePPTController.git
or download the ZIP.

### 2️⃣ Install Dependencies
pip install opencv-python cvzone mediapipe pyautogui

### 3️⃣ Start Your Presentation
Open **PowerPoint / Google Slides** and start **Slideshow Mode**.

### 4️⃣ Run the Python Script
python gesture_ppt_controller.py

### 5️⃣ Use Hand Gestures

Show your hand in front of the webcam.

| Gesture          | Result         |
| ---------------- | -------------- |
| ✋ All fingers up | Next Slide     |
| 👍 Only thumb up | Previous Slide |

Press **Q** to exit.

# 🧠 How It Works

1. **OpenCV** captures webcam video.
2. **CVZone + MediaPipe** detect hand landmarks.
3. The program identifies **which fingers are up**.
4. Based on gesture:

   * Sends **Right Arrow Key** → Next Slide
   * Sends **Left Arrow Key** → Previous Slide
5. **Cooldown timer** prevents multiple triggers.

# ⚙️ Important Code Settings

### Hand Distance Detection
MIN_HAND_AREA = 9000
This value ensures gestures are detected only when the hand is **within ~50 cm from the camera**.

### Cooldown Timer
cooldown = 1.0

Prevents accidental multiple slide changes.
You can change it to:
```
0.5  → Faster response
1.5  → More stable detection
```

# ⚠️ Notes

* The **presentation window must stay in focus**.
* Use in a **well-lit room**.
* Keep your **hand clearly visible to the camera**.
* Works best when the hand is **within ~50 cm distance**.

# 👤 Developer

**KevalKing**

Instagram
@keval_king_212


