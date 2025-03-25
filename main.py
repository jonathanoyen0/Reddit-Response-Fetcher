import requests
import pandas as pd


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

