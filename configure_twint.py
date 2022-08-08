import twint
import numpy as np
import re


# Configure Twint
c = twint.Config()
c.Search = '"#KenyaDecides2022"'
c.Store_json = True
c.output = "kenyadecides_tweets.json"


def clean_tweet(tweet):
    """Function to clean tweet text by removing links, special characters

    Args:
        tweet (str): Tweet text

    Returns:
        str: Cleaned tweet text
    """
    if type(tweet) == np.float:
        return ""
    temp = tweet.lower()
    temp = re.sub("'", "", temp)  # to avoid removing contractions in english
    temp = re.sub("@[A-Za-z0-9_]+", "", temp)
    temp = re.sub("#[A-Za-z0-9_]+", "", temp)
    temp = re.sub(r"http\S+", "", temp)
    temp = re.sub("[()!?]", " ", temp)
    temp = re.sub("\[.*?\]", " ", temp)
    temp = re.sub("[^a-z0-9]", " ", temp)
    temp = temp.split()
    temp = [w for w in temp if not w in stopwords]
    temp = " ".join(word for word in temp)
    return temp


# Run Twint
twint.run.Search(c)
