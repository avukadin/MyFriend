import speech_recognition as sr

class Brain():
    audio_recognizer = sr.Recognizer()

    def process_audio(self, audio):
        text = self.audio_recognizer.recognize_google(audio)
        text = text.lower()
        return text

    def _formulate_response(self, text):
        pass
