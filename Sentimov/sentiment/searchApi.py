import tweepy
import os
import jsonpickle

access_token = "484821005-jH9KAdyZTHiFrn0nQ5by8tloVG62c5RqTqaWK6dq"
access_token_secret = "zjsYzA3VLXrhBftjPgHcOAOWwNUtybLx0inAbHiSMWtuD"
consumer_key = "q420q6xNIZVLYoFAx6CVXkIQB"
consumer_secret = "GfjG0pHoRlfByOylAbS9PIFU5YuNvVVUPFYeQdpHGLf7Iq8lN6"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

def delete_file(movie_name):
	movie_name = movie_name
	m_cut = movie_name.replace(" ", "").replace(":", "").replace("'", "").replace("-","")
	fName = m_cut + '.txt'
	file_path = './Sentimov/sentiment/' + fName
	if(os.path.exists(file_path)):
		os.remove(file_path)

def get_tweets(movie_name, max_id):
	movie_name = movie_name
	m_cut = movie_name.replace(" ", "").replace(":", "").replace("'", "").replace("-","")
	hashtag = '#' + m_cut
	searchQuery = '"' + movie_name + '" OR ' + hashtag
	maxTweets = 10000000
	tweetsPerQry = 100
	fName = m_cut + '.txt'
	file_path = './Sentimov/' + fName
	sinceId = None
	max_id = max_id
	tweetCount = 0
	result = []

	with open(os.path.join('./Sentimov/sentiment/', fName), 'a') as f:
		if (max_id <= 0):
			if (not sinceId):
				new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang="en")
			else:
				new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang="en", since_id=sinceId)
		else:
			if (not sinceId):
				new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang="en", max_id=str(max_id - 1))
			else:
				new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang="en", max_id=str(max_id - 1), since_id=sinceId)

		if not new_tweets:
			print("No more tweets found")
			test = {'no_tweets': "no_tweets"}
			return test

		for tweet in new_tweets:
			f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
			result.append(tweet._json)

		tweetCount += len(new_tweets)
		max_id = new_tweets[-1].id
		test = {'test': result, 'maxid':max_id, 'count':tweetCount}

	return test
