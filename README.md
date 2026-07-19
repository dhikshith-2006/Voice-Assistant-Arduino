# 🎙️ Voice Assistant with Arduino Uno

A Python-based desktop voice assistant integrated with an **Arduino Uno** to provide both software automation and physical hardware feedback. The assistant recognizes voice commands, performs desktop tasks, and communicates with Arduino through serial communication to control an LED and a servo motor.

---

## 📖 Overview

This project combines **Speech Recognition**, **Desktop Automation**, and **Arduino Hardware Control** into a single application.

When a voice command is recognized, the assistant can:

- 🔍 Search Google
- ▶️ Play videos on YouTube
- 🌐 Open websites
- 📝 Type text automatically
- 💡 Turn on an LED
- ⚙️ Rotate a servo motor

The Arduino acts as a hardware feedback system while Python handles the voice recognition and automation.

---

## ✨ Features

- 🎤 Speech Recognition using Google Speech API
- ⌨️ Keyboard-triggered voice listening (Spacebar)
- 🌍 Google Search
- ▶️ YouTube Auto Play
- 🖥️ Open desktop applications
- 🌐 Open websites automatically
- ✍️ Automatic text typing
- 🔌 Serial communication with Arduino
- 💡 LED status indication
- ⚙️ Servo motor movement after successful command execution

---

# 🛠 Hardware Used

| Component | Quantity |
|-----------|----------|
| Arduino Uno | 1 |
| SG90 Micro Servo | 1 |
| LED | 1 |
| 220Ω Resistor | 1 |
| Breadboard | 1 |
| Jumper Wires | As Required |
| USB Cable | 1 |

---

# 🔧 Software Used

- Python 3.x
- Arduino IDE
- VS Code (Optional)

### Python Libraries

```bash
pip install speechrecognition
pip install pyserial
pip install pyautogui
pip install pywhatkit
pip install keyboard
```

Or install everything together:

```bash
pip install speechrecognition pyserial pyautogui pywhatkit keyboard
```

---

# 📂 Project Structure

```text
Voice-Assistant-Arduino/
│
├── voice_assistant.py      # Python Application
├── voice_assistant.ino     # Arduino Program
├── README.md               # Documentation
└── images/
      └── setup.jpg         # Circuit Image (Optional)
```

---

# 🔌 Circuit Connections

| Component | Arduino Pin |
|-----------|-------------|
| Servo Signal | D9 |
| Servo VCC | 5V |
| Servo GND | GND |
| LED Anode (+) | D13 (through 220Ω resistor) |
| LED Cathode (-) | GND |

---

# ⚙️ How It Works

1. User presses the **Spacebar**.
2. Python starts listening.
3. Voice is converted into text.
4. The command is analyzed.
5. The requested desktop task is executed.
6. Python sends a signal (`Y`) through Serial.
7. Arduino receives the signal.
8. LED turns ON.
9. Servo rotates to **180°**.
10. After 3 seconds:
    - LED turns OFF
    - Servo returns to **0°**

---

# 🎤 Supported Voice Commands

### Open Applications

```
Open calculator

Open notepad
```

---

### Play YouTube Videos

```
Play Believer

Play Python tutorial
```

---

### Google Search

```
Search for Artificial Intelligence

Find Arduino Projects
```

---

### Automatic Typing

```
Type Hello everyone

Type Welcome to Arduino
```

---

# 🚀 Installation

## Step 1

Clone the repository.

```bash
git clone https://github.com/yourusername/Voice-Assistant-Arduino.git
```

---

## Step 2

Navigate into the project folder.

```bash
cd Voice-Assistant-Arduino
```

---

## Step 3

Install the required Python libraries.

```bash
pip install speechrecognition pyserial pyautogui pywhatkit keyboard
```

---

## Step 4

Open the Arduino sketch in Arduino IDE.

Upload:

```
voice_assistant.ino
```

---

## Step 5

Close the Arduino IDE after uploading.

This releases the Serial Port so Python can communicate with Arduino.

---

## Step 6

Update the COM Port inside:

```python
ARDUINO_PORT = "COM3"
```

Replace **COM3** with your Arduino port.

---

## Step 7

Run the application.

```bash
python voice_assistant.py
```

---

# 📸 Project Demonstration

Add your circuit image here.

```
images/setup.jpg
```

Example:

```markdown
![Project Setup](images/setup.jpg)
```

---

# 🧠 Technologies Used

- Python
- Arduino C++
- Speech Recognition
- Serial Communication
- PyAutoGUI
- PyWhatKit
- Keyboard Module
- Arduino Uno
- SG90 Servo Motor

---

# 🔮 Future Improvements

- Offline Speech Recognition
- Wake Word Detection
- Home Automation Integration
- IoT Dashboard
- ESP32 Wi-Fi Support
- ChatGPT API Integration
- Text-to-Speech Response
- Mobile App Control

---

# 📜 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute this project.

---

# 👨‍💻 Author

**Dhikshith**

B.E. Electronics and Communication Engineering (ECE)

Rajalakshmi Institute of Technology

GitHub: https://github.com/dhikshith-2006

---

## ⭐ If you found this project useful,

Please **Star ⭐ this repository** and consider contributing to improve it.
