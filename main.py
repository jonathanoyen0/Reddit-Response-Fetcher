import requests
import pandas as pd
from dotenv import load_dotenv

def get_random_post(subreddit: str):
    url = f"https://www.reddit.com/r/{subreddit}/random.json"
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
    
df = pd.read_csv("subreddits_public.csv",names=["base10_id","base36_reddit_id","creation_epoch","subreddit_name","subscribers_count"])

