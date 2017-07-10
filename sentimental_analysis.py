from get_recent_media import get_recent_media
from get_user_id import get_user_id, get_user_username
from const import BASE_URL, APP_ACCESS_TOKEN
import requests
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import matplotlib.pyplot as plt


def perform_sentiment_analysis():
    username = get_user_username()
    id = get_user_id(username)
    if id != 0:
        pass
    else:
        exit()

    post_id = get_recent_media(id)
    print "Fetching data..."
    req_url = BASE_URL + "media/" + post_id + "/comments/?access_token=" + APP_ACCESS_TOKEN

    comments = requests.get(req_url).json()
    data = ""
    if not comments['data']:
        print "No comments found."
    else:
        for temp in comments['data']:
            temp['text'] += " " + temp['text']
            data = temp['text']

    #
    #   SENTIMENT ANALYSIS. DO NOT MESS WITH THE CODE UNDER THIS.
    #

        blob = TextBlob(data, analyzer=NaiveBayesAnalyzer())
        if blob.sentiment.classification == "neg":
            print "Overall negative content found. More details in the pie chart."
        else:
            print "Overall Positive content found. More details in the pie chart."
        print blob.sentiment.classification
        pos = blob.sentiment.p_pos
        neg = blob.sentiment.p_neg
        labels = 'Positive Comments %age', 'Negative Comments %age'
        sizes = [pos, neg]
        explode = (0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()
perform_sentiment_analysis()