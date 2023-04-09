# Import the required module
import pyttsx3
 
# Create a string
string = "Thanks for watching do not forget to like, subscribe, and hit the notification bell for more!" 
# Initialize the Pyttsx3 engine
engine = pyttsx3.init()
 
# We can use file extension as mp3 and wav, both will work
engine.save_to_file(string, 'hal thanks for wathcing.mp3')
 
# Wait until above command is not finished.
engine.runAndWait()
