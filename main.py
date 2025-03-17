import requests

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")

def get_post():
    url = ""
    #This will attempt to get the random post from reddit
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("We did it")
            response = response.json()
            return response
        else:
            print("Error: ", response.status_code)
            return None
    #This just cathches any network related errors
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None