import speech_recognition as sr

def listen_and_write():
    recognizer = sr.Recognizer()  # Create recognizer object

    with sr.Microphone() as source:  # Use microphone as input source
        print("Listening... Speak something:")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)  # Capture audio

    try:
        # Recognize the speech using Google's recognition engine
        text = recognizer.recognize_google(audio)
        print("You said:", text)  # Print the recognized text

        # Save the text to a file
        with open("output.txt", "a") as file:
            file.write(text + "\n")
        print("Text saved to output.txt")

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError:
        print("Sorry, could not request results; check your internet connection.")

if __name__ == "__main__":
    listen_and_write()