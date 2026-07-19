import speech_recognition as sr
import pywhatkit as kit
import webbrowser
import serial
import time
import urllib.parse
import os
import pyautogui
import keyboard

# --- CONFIGURATION ---
ARDUINO_PORT = 'COM3' 

try:
    arduino = serial.Serial(ARDUINO_PORT, 9600, timeout=1)
    time.sleep(2)  
    print(f"[SUCCESS] Connected to Arduino on {ARDUINO_PORT}!")
except Exception as e:
    print(f"[WARNING] Could not connect to Arduino on {ARDUINO_PORT}. Running in desktop-only mode.")
    arduino = None

def trigger_hardware():
    if arduino:
        print("[ACTION] Sending signal to LED and Servo...")
        time.sleep(0.1)     
        arduino.write(b'Y') 
        arduino.flush()     

def listen_and_process():
    recognizer = sr.Recognizer()
    # Using the microphone only when explicitly requested avoids PyAudio hanging backgrounds
    with sr.Microphone() as source:
        print("\n[LISTENING] Speak your command now...")
        try:
            # Short catch window so it never stays stuck
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=5)
            print("[PROCESSING] Converting speech to text...")
            text_command = recognizer.recognize_google(audio).lower().strip()
            print(f"Captured Voice: '{text_command}'")
            
            # --- UNIVERSAL TYPING ENGINE ---
            if "type" in text_command:
                if "on" in text_command:
                    parts = text_command.split("on")
                    message = parts[0].replace("type", "").strip()
                else:
                    message = text_command.replace("type", "").strip()

                print(f"[KEYBOARD] Preparing to type: '{message}'")
                time.sleep(2) 
                pyautogui.write(message, interval=0.08)
                pyautogui.press('enter')
                trigger_hardware()

            # --- UNIVERSAL MEDIA ENGINE ---
            elif "play" in text_command:
                media_query = text_command.replace("play", "").replace("on youtube", "").replace("youtube", "").strip()
                print(f"[MEDIA] Autoplaying match for: '{media_query}'")
                kit.playonyt(media_query)
                trigger_hardware()

            # --- UNIVERSAL OPEN ENGINE ---
            elif "open" in text_command:
                app = text_command.replace("open", "").strip()
                if app in ["calculator", "calc"]:
                    os.system("calc")
                elif app in ["notepad", "notes"]:
                    os.system("notepad")
                else:
                    url = f"https://www.{app}.com" if not app.endswith(('.com', '.org')) else f"https://{app}"
                    webbrowser.open(url)
                trigger_hardware()

            # --- GOOGLE SEARCH FALLBACK ---
            else:
                clean_search = text_command.replace("search for", "").replace("find", "").strip()
                print(f"[SEARCH] Googling: '{clean_search}'")
                webbrowser.open(f"https://www.google.com/search?q={urllib.parse.quote(clean_search)}")
                trigger_hardware()

        except sr.WaitTimeoutError:
            print("[SYSTEM] Timed out waiting for speech.")
        except sr.UnknownValueError:
            print("[SYSTEM] Could not understand the audio.")
        except Exception as e:
            print(f"[ERROR] {e}")

if __name__ == "__main__":
    print("\n=======================================================")
    print("[READY] Voice Assistant Engine Active!")
    print("👉 Press the 'SPACEBAR' key on your keyboard to talk.")
    print("👉 Press 'ctrl+c' in the terminal to exit.")
    print("=======================================================\n")
    
    while True:
        try:
            # Wait until user triggers it manually, dodging the live stream block
            if keyboard.is_pressed('space'):
                listen_and_process()
                time.sleep(1) # Prevent double triggers
            time.sleep(0.05)
        except KeyboardInterrupt:
            print("\n[SYSTEM] Shutting down cleanly.")
            if arduino:
                arduino.close()
            break