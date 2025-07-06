import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import time

# ===== Speech Engine Setup =====
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# ===== Automatically Detect a Working Microphone =====
def get_working_mic():
    r = sr.Recognizer()
    for index in range(40):  # Check first 40 microphone indices
        try:
            with sr.Microphone(device_index=index) as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print(f"Using microphone index {index}")
                return index
        except Exception:
            continue
    raise RuntimeError("No working microphone found.")

# ===== Listen to Voice Command =====
def listen_command(mic_index):
    r = sr.Recognizer()
    with sr.Microphone(device_index=mic_index) as source:
        speak("Listening...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=7)
            command = r.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.WaitTimeoutError:
            speak("I didn't hear anything.")
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand.")
        except sr.RequestError as e:
            speak(f"Service error: {e}")
    return ""

# ===== Process Commands =====
def handle_command(command):
    if any(keyword in command for keyword in ["open browser", "open google", "search"]):
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif "youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif "music" in command or "play song" in command:
        speak("Playing music.")
        music_path = "C:\\Users\\Public\\Music\\Sample Music"  # Change this path if needed
        os.startfile(music_path)
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today is {today}")
    elif "shutdown" in command:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 5")
    elif "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I did not understand that command.")

# ===== Main Assistant Loop =====
def main():
    speak("Hello! I am your voice assistant.")
    time.sleep(1)
    try:
        mic_index = get_working_mic()
    except RuntimeError as e:
        speak(str(e))
        return

    while True:
        command = listen_command(mic_index)
        if command:
            handle_command(command)

if __name__ == "__main__":
    main()
