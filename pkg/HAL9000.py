import webbrowser
import config
from pkg.Brain import Brain
from pkg.Ears import Ears
from pkg.Hands import Hands
from pkg.Mouth import Mouth

class HAL9000():
    brain:Brain
    ears:Ears
    hands:Hands
    mouth:Mouth
    
    def __init__(self):
        self.brain = Brain()
        self.ears = Ears()
        self.hands = Hands()
        self.mouth = Mouth()

    def start(self):
        self.mouth.say("Hello, I am online")

        while True:
            audio = self.ears.listen()
            text = self.brain.process_audio(audio)

            action = self.brain.determine_action(text)

            if action == Actions.chatGPT:
                response = self.brain.formulate_response(text)
                self.mouth.say(response)
            elif action == Actions.explain_code:
                c = self.hands.copy_highlighted() 
                response = self.brain.formulate_response(f"Explain this code to me:\n{c}")
                self.mouth.say(response)
            elif action == Actions.rewrite_code:
                c = self.hands.copy_highlighted() 
                response = self.brain.formulate_response(f"Rewrite this code for me in a cleaner way. Only show the code.\n{c}")
                self.hands.paste(response)
            elif action == Actions.weather:
                self.mouth.say(f"This is the weather in {config.MY_LOCATION}")
                url = 'https://www.google.com/search?q=weather+' + config.MY_LOCATION.replace(' ', '+')
                webbrowser.open(url)
