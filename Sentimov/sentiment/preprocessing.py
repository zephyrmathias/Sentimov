import cleanText
import HTMLParser

html_parser = HTMLParser.HTMLParser()

def pre_process(tweet, movie_name):
    tweet = tweet.lower()
    tweet = tweet.replace("\n", "")
    tweet = html_parser.unescape(tweet).encode('utf-8')
    tweet = cleanText.replace_via(tweet)
    tweet = cleanText.replace_hashtag(tweet, movie_name)
    hashtag_movie = movie_name + 'Movie'
    tweet = cleanText.replace_hashtag(tweet, hashtag_movie)
    tweet = cleanText.replaceEmoji(tweet)
    tweet = cleanText.removeURL(tweet)
    tweet = cleanText.removeRT(tweet)
    tweet = cleanText.removeAcc(tweet)
    tweet = tweet.strip().decode('unicode_escape').encode('ascii', 'ignore')
    return tweet
