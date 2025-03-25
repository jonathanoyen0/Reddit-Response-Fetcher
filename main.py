import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def get_oauth_token():
    CLIENT_ID = os.environ.get("CLIENT_ID")  # Stored in environment variables
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    USER_AGENT = os.environ.get("USER_AGENT")
    PASSWORD = os.environ.get("PASSWORD")
    USERNAME = os.environ.get("USERNAME")

    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

    data = {'grant_type': 'password',
            'password': PASSWORD,
            'username' : USERNAME}
    
    headers = {'User-Agent': USER_AGENT}

    response = requests.post("https://www.reddit.com/api/v1/access_token",
                             auth=auth, data=data, headers=headers)
    try:
        if response.status_code == 200:
            token = response.json().get('access_token')
            print("OAuth Token:", token)  # Debugging, remove in production
            return token
        else:
            print("Error obtaining token:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None


def get_random_post(subreddit: str):
    url = f"https://www.reddit.com/r/{subreddit}/new.json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("We did it")
            response = response.json()
            response
        else:
            print("Error: ", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None


# df = pd.read_csv("subreddits_public.csv",names=["base10_id","base36_reddit_id","creation_epoch","subreddit_name","subscribers_count"])




# print(get_oauth_token())