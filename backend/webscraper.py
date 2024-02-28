import os
import praw
import pandas as pd
import re
import json


reddit_authorized = praw.Reddit(os.getenv("r_client_id"),
                                    os.getenv("r_client_secret"),
                                    os.getenv("r_user_agent"),
                                    os.getenv("r_username"),
                                    os.getenv("r_password"))

name_subreddit = "wallstreetbets"
subreddit = reddit_authorized.subreddit(name_subreddit)

def posts_day():
    
    posts = subreddit.top("day")

    posts_dict = {}
    
    ticker_pattern = r'\$([A-Z]+)'  # Regular expression pattern to match tickers

    for post in posts:
        # Combine title, description, and the first 10 comments as text
        top_comments = [comment.body for comment in post.comments.list() if isinstance(comment, praw.models.Comment)][:15]
        text = f"{post.title} {' '.join(top_comments)}"

        # Extract tickers from the text
        title_tickers = re.findall(ticker_pattern, text)

        # Append data to the dictionary
        for ticker in title_tickers:
            if ticker in posts_dict:
                posts_dict[ticker].append(text)
            else:
                posts_dict[ticker] = [text]

    return json.dumps(posts_dict, indent=2)

def ticker_freq():
    posts = subreddit.top("day")

    posts_dict = {}
    
    ticker_pattern = r'\$([A-Z]+)'  # Regular expression pattern to match tickers

    for post in posts:
        # Combine title, description, and the first 10 comments as text
        top_comments = [comment.body for comment in post.comments.list() if isinstance(comment, praw.models.Comment)][:15]
        text = f"{post.title} {' '.join(top_comments)}"

        # Extract tickers from the text
        title_tickers = re.findall(ticker_pattern, text)

        # Append data to the dictionary
        for ticker in title_tickers:
            if ticker in posts_dict:
                posts_dict[ticker] += 1
            else:
                posts_dict[ticker] = 1

     # Create lists of tickers and frequencies
    tickers = list(posts_dict.keys())
    frequencies = list(posts_dict.values())

    # Create a dictionary with the lists
    result = {"tickers": tickers, "frequencies": frequencies}
    return json.dumps(result, indent=2)