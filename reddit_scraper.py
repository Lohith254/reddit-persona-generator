import praw
import os
from dotenv import load_dotenv

load_dotenv()

def get_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

def fetch_user_comments(username: str, limit=50):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)
    comments = []

    try:
        for comment in user.comments.new(limit=limit):
            comments.append({
                "body": comment.body,
                "url": f"https://www.reddit.com{comment.permalink}",
                "subreddit": comment.subreddit.display_name
            })
    except Exception as e:
        print(f"Error fetching comments: {e}")
    return comments