from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get("API_KEY") # put your api key in a .env file, like API_KEY=123

GPT_MODEL = "gpt-3.5-turbo"
MY_LOCATION = 'toronto ontario'
MY_NAME = 'Alex'
