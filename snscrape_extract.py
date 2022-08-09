import os
import pandas
import fire


def extract_tweets_from_hashtag(hashtag, maximum_tweet_count, file_name="tweets.json"):
    """Function to scrape tweets from a given hashtag using snscrape

    Args:
        hashtag (str): String value of Hashtag to scrape
        maximum_tweet_count (int): Maximum number of tweets to scrape
        file_name (str, optional): Name of the output json file. Defaults to "tweets.json".
    """
    # Call snscrape cli to extract
    os.system(
        f"snscrape --jsonl --progress --max-results {maximum_tweet_count} twitter-hashtag {hashtag} > {file_name}"
    )


if __name__ == "__main__":
    fire.Fire(extract_tweets_from_hashtag)
