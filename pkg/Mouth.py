import pyttsx3

class Mouth():
    speaker = None

    def __init__(self):
        self.speaker = pyttsx3.init()

    def speak(self, text:str):
        self.speaker.say(text)
        self.speaker.runAndWait()
