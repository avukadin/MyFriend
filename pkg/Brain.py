import speech_recognition as sr
import os
import openai
from config import API_KEY
from enum import Enum

class Actions(Enum):
    do_nothing = 0
    turn_off = 1
    say = 2

class Brain():
    bot_name:str
    audio_recognizer = sr.Recognizer()
    gpt_model:str
    memory:list[dict[str,str]]

    def __init__(self, bot_name:str, gpt_model:str):
        openai.api_key = API_KEY
        self.bot_name = bot_name.lower()
        self.gpt_model = gpt_model

    def process_audio(self, audio):
        text = self.audio_recognizer.recognize_google(audio)
        text = text.lower()
        return text

    def determine_action(self, text:str) -> int:
        text = text.lower()

        if not text.startswith(self.bot_name):
            return Actions.do_nothing

        text = text[len(self.bot_name):]

        if 'turn off' in text:
            return Actions.turn_off
        else:
            return Actions.say

    def formulate_response(self, text):
        if len(self.memory) == 0:
            system_text = "You are a friendly AI named {self.bot_name}. Try to answer my questions in less than 50 words."
            self.memory.append({"role":"system", "content":system_text})

        try:
            self.memory.append({"role":"user", "content":text})
            returned = openai.ChatCompletion.create(
                  model=self.gpt_model,
                  max_tokens = 200,
                  messages=self.memory
            )
            response = returned.choices[0].message.content
            self.memory.append({"role":"assistant", "content":response})
        except:
            self.memory = self.memory[0:len(self.memory)-1]
            response = "Sorry, I ran into an issue, plese try me again."

        return response
