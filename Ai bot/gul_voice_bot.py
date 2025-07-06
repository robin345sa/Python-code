from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os
import platform
import tkinter as tk
from tkinter import filedialog
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def choose_output_directory():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory(title="Select Output Directory")

def speak_and_save(text, filename="output.mp3", lang="en", slow=False, output_dir="."):
    try:
        tts = gTTS(text=text, lang=lang, slow=slow)
        filepath = os.path.join(output_dir, filename)
        tts.save(filepath)
        logging.info(f"Saved to {filepath}")

        # Optional: Use pydub to play with cross-platform compatibility
        sound = AudioSegment.from_file(filepath)
        play(sound)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

def list_languages():
    from gtts.lang import tts_langs
    langs = tts_langs()
    for code, name in sorted(langs.items()):
        print(f"{code}: {name}")

if __name__ == "__main__":
    print("=== Advanced Text-to-Speech Bot ===")
    output_dir = choose_output_directory()
    if not output_dir:
        print("[!] No directory selected. Exiting.")
        exit()

    print("\nAvailable languages:")
    list_languages()
    lang = input("\nChoose language code (default 'en'): ").strip().lower() or "en"

    slow = input("Speak slowly? (y/n): ").strip().lower() == 'y'

    count = 1
    while True:
        user_input = input("\nEnter text (or type 'exit' to quit): ").strip()
        if user_input.lower() == "exit":
            speak_and_save("Goodbye!", f"goodbye.mp3", lang, slow, output_dir)
            break

        filename = f"voice_output_{count}.mp3"
        speak_and_save(user_input, filename, lang, slow, output_dir)
        count += 1
