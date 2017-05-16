import json
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import fwords
import preprocessing
import os
from sklearn.externals import joblib
import cleanText
import HTMLParser

html_parser = HTMLParser.HTMLParser()
#TweetTokenizer = TweetTokenizer()

def sentiment(movie_name):
    #print(datetime.now())
    model = joblib.load('./Sentimov/sentiment/model.sav')

    feature_words = fwords.create_feature_words('./Sentimov/sentiment/feature_words.txt')
    emo_list = fwords.create_feature_words('./Sentimov/sentiment/emo_list.txt')
    word_features = feature_words + emo_list

    name = movie_name.replace(" ", "").replace(":", "").replace("'","").replace("-","")
    hashtag = str("#" + name)

    inputf = open("./Sentimov/sentiment/" + name + ".txt")
    lines=inputf.readlines()
    inputf.close()
    output = open("./Sentimov/sentiment/" + name + '.tsv', 'w')
    tweetlist=[]
    pos_list=[]
    neg_list=[]
    neu_list=[]
    #count = 0;
    for line in lines:
        #count = count + 1
        if line!="\n":
            try:
                d = json.loads(line)
                text = d[u'text']
                tweet = preprocessing.pre_process(text, hashtag)
                text = text.replace("\n", "")
                text = html_parser.unescape(text).encode('utf-8')
                tweetlist.append(tweet)
                #remove stopword and specailcharacter
                stop_words = set(stopwords.words('english'))
                #word_tokens = TweetTokenizer.tokenize(tweet)
                word_tokens = word_tokenize(tweet)
                #word_tokens = cleanText.remove_repeated_characters(word_tokens)
                label = model.classify(fwords.find_features(word_tokens,word_features))
                arr = []

                if ('retweeted_status' in d):
                    arr.append(d[u'retweeted_status'][u'text'])
                    arr.append(d[u'created_at'])
                    arr.append(d[u'retweeted_status'][u'user'][u'screen_name'])
                    arr.append(d[u'retweeted_status'][u'id_str'])
                    arr.append(d[u'retweeted_status'][u'user'][u'profile_image_url_https'])
                    arr.append("retweeted")
                    arr.append(d[u'user'][u'screen_name'])
                else:
                    arr.append(text)
                    arr.append(d[u'created_at'])
                    arr.append(d[u'user'][u'screen_name'])
                    arr.append(d[u'id_str'])
                    arr.append(d[u'user'][u'profile_image_url_https'])
                    arr.append("not_retweeted")

                if (label == "positive"):
                    pos_list.append(arr)
                    output.write(str(text)+"\tpositive\n")
                elif (label == "negative"):
                    neg_list.append(arr)
                    output.write(str(text)+"\tnegative\n")
                else:
                    neu_list.append(arr)
                    output.write(str(text)+"\tneutral\n")
            except:
                pass

    output.close()
    result = {'pos':pos_list, 'neg':neg_list, 'neu':neu_list}
    #print(result)

    return result
