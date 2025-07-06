from gtts import gTTS
import os
import platform
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk


# Function to convert text and play it
def speak_and_save(text, filename="output.mp3", lang='en', speed=1.0):
    try:
        if not text.strip():
            messagebox.showwarning("Empty Input", "Please enter some text.")
            return

        # Convert text to speech
        tts = gTTS(text=text, lang=lang, slow=speed < 1)
        tts.save(filename)
        print(f"[✔] Saved to {filename}")

        # Play the audio file based on OS
        system_platform = platform.system()

        if system_platform == "Windows":
            os.system(f"start {filename}")
        elif system_platform == "Darwin":  # macOS
            os.system(f"afplay {filename}")
        elif system_platform == "Linux":
            os.system(f"xdg-open {filename}")
        else:
            messagebox.showinfo("Playback", f"Audio saved as {filename}, but auto-play is not supported on this OS.")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")


# GUI setup
def create_gui():
    root = tk.Tk()
    root.title("Advanced Gul TTS Bot")
    root.geometry("500x350")
    root.resizable(False, False)

    tk.Label(root, text="Enter text to convert to speech:", font=("Arial", 12)).pack(pady=10)

    text_input = tk.Text(root, height=5, width=40, wrap=tk.WORD, font=("Arial", 11))
    text_input.pack(pady=5)

    # Language selection
    lang_label = tk.Label(root, text="Choose Language:", font=("Arial", 10))
    lang_label.pack(pady=5)

    lang_options = ['en', 'es', 'fr', 'de', 'it', 'pt', 'ja']
    lang_var = tk.StringVar(value='en')
    lang_menu = ttk.Combobox(root, textvariable=lang_var, values=lang_options, state="readonly")
    lang_menu.pack(pady=5)

    # Speed control
    speed_label = tk.Label(root, text="Select Speech Speed:", font=("Arial", 10))
    speed_label.pack(pady=5)

    speed_var = tk.DoubleVar(value=1.0)
    speed_scale = tk.Scale(root, variable=speed_var, from_=0.5, to_=2.0, orient="horizontal", resolution=0.1)
    speed_scale.pack(pady=5)

    count = {"val": 1}

    def on_speak():
        text = text_input.get("1.0", tk.END).strip()
        language = lang_var.get()
        speed = speed_var.get()
        filename = f"voice_output_{count['val']}.mp3"
        speak_and_save(text, filename, lang=language, speed=speed)
        count['val'] += 1

    def on_play():
        filename = f"voice_output_{count['val'] - 1}.mp3"
        if os.path.exists(filename):
            speak_and_save("", filename)  # Just play the file
        else:
            messagebox.showwarning("File Not Found", "No audio file to play yet.")

    def on_exit():
        speak_and_save("Goodbye!", "goodbye.mp3")
        root.destroy()

    # Add buttons
    tk.Button(root, text="Speak", command=on_speak, font=("Arial", 11)).pack(pady=10)
    tk.Button(root, text="Play Last Audio", command=on_play, font=("Arial", 11)).pack(pady=5)
    tk.Button(root, text="Exit", command=on_exit, font=("Arial", 10)).pack()

    # Progress bar for speech conversion
    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
    progress.pack(pady=10)

    # Show progress while speaking
    def update_progress():
        progress.start()
        on_speak()
        progress.stop()

    root.mainloop()


# Run GUI
if __name__ == "__main__":
    create_gui()
