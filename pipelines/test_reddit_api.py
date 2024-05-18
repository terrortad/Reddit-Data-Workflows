import praw

# Hardcoded credentials
client_id = "v3pkZk4oyXR13AyJz6mp5Q"
client_secret = "nq9bFJu5pSKSnKrl4j9DwhlHir-1Hw"
user_agent = "web:Pipeline:v1.0 (by u/CowUnfair4318)"
redirect_uri = "http://localhost:8080"  # Update as needed

def connect_reddit(client_id, client_secret, user_agent, redirect_uri):
    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
            redirect_uri=redirect_uri
        )
        print("Connected to Reddit!")
        return reddit
    except Exception as e:
        print(f"Failed to connect to Reddit: {e}")

def fetch_subreddit_info(reddit, subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    print(f"Subreddit: {subreddit.display_name}")
    print(f"Title: {subreddit.title}")
    print(f"Description: {subreddit.public_description}")

if __name__ == "__main__":
    reddit = connect_reddit(client_id, client_secret, user_agent, redirect_uri)
    if reddit:
        fetch_subreddit_info(reddit, "dataengineering")
