
import speech_recognition as sr
import pyttsx3
from pkg.Brain import Brain, Actions


class MyFriend():
    ears = None
    mouth = None
    brain:Brain
    
    def __init__(self, brain:Brain):
        self.brain = brain

    def start(self):
        while 1:
            text = self.listen()
            print(text)
            action = self.brain.determine_action(text)

            if action == Actions.say:
                response = self.brain.formulate_response(text)
                self.mouth.say(response)

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
        print("Listening")
        audio = self.ears.listen()
        text = self.brain.process_audio(audio)
        return text

    def make_response(self, text):
        pass
