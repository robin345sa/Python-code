import pyttsx3

engine = pyttsx3.init()

def spack (text):
    engine.say(text)
    engine.runAndWait()

print("text to voice convater")
while True:
    text = input("Enter your text :")
    spack(text)