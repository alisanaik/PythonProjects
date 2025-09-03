from gtts import gTTS
from playsound import playsound
import os

print("Welcome to RoboSpeaker 2.0 (Created by Alisa ❤)")

while True:
    x = input("Enter what you want me to speak (or 'q' to quit): ")

    if x.lower() == "q":
        tts = gTTS("Bye bye friends", lang='en')
        tts.save("bye.mp3")
        playsound("bye.mp3")
        os.remove("bye.mp3")
        break

    tts = gTTS(x, lang='en')
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")