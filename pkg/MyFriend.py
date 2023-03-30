
import speech_recognition as sr
import pyttsx3


class MyFriend():
    ears = None
    mouth = None

    def __init__(self, brain):
        self.brain = brain

    def set_ears(self, ears):
        pass

    def set_eyes(self, eyes):
        pass

    def set_mouth(self, mouth):
        pass

    def say(self, text):
        if not self.mouth:
            print("I cannot speak, I have no mouth.")
            return
        self.mouth.speak(text)

    def listen(self):
        if not self.ears:
            print("I have no ears, I can't hear anything.")
            return
        audio = self.ears.listen()
        text = self.brain.process_audio(audio)
        return text
