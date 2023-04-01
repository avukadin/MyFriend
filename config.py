from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get("API_KEY")

GPT_MODEL = "gpt-3.5-turbo"
