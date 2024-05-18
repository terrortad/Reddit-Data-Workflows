import sys
import os
import pandas as pd
import praw
import configparser

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv

# Read configuration
config = configparser.ConfigParser()
config_file_path = os.path.join(os.path.dirname(__file__), '../config/config.conf')
config.read(config_file_path)

if not config.sections():
    print(f"Failed to read config file from: {os.path.abspath(config_file_path)}")
    sys.exit(1)

CLIENT_ID = config['api_keys']['reddit_client_id']
SECRET = config['api_keys']['reddit_secret_key']
USER_AGENT = "web:Pipeline:v1.0 (by u/CowUnfair4318)"
OUTPUT_PATH = config['file_paths']['output_path']

def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    # connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, USER_AGENT)
    # extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    # transformation
    post_df = transform_data(post_df)
    # loading to csv
    file_path = os.path.join(OUTPUT_PATH, f'{file_name}.csv')
    print(f"Saving to file path: {file_path}")
    load_data_to_csv(post_df, file_path)
    print("saved to output")

    return file_path

if __name__ == "__main__":
    # Example usage
    file_name = 'example_file'
    subreddit = 'dataengineering'
    reddit_pipeline(file_name, subreddit)
