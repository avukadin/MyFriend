import speech_recognition as sr

class Ears():

    _listener = None

    def __init__(self):
        self._listener = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            self._listener.adjust_for_ambient_noise(source, duration=0.2)
            audio = self._listener.listen(source)
        return audio
