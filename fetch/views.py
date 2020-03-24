from django.shortcuts import render
import tweepy
import json

def home(request):
  if request.method == "POST":
    
    username = request.POST['username']
    hashtag = request.POST['hashtag']
<<<<<<< HEAD
    count = request.POST['count']
    consumer_key = "euF2vpAKFSeffdlvY6OLGKjyb"
    consumer_secret = "PDukSba2b7QnQJQPwju8lQhMl0LcJmuK06C0hxs0kY9B7M77ER"
    access_token = "3503980812-Tt3BTqPf2u7FtUeLRtwJvjTzdtqRZ47O6EhdQzU"
    access_token_secret = "8lAmwKFB8Kg5xv6Rd8dQ7uVoHnpA5ZD60GL24hgTcdD0l"
=======
    consumer_key = "your consumer key here"
    consumer_secret = "your consumer secret key here"
    access_token = "your access token here"
    access_token_secret = "your access tokey secret key here"
>>>>>>> 2befe8fff12fccf5deeef072117e75d3bb30a32b
    # Creating the authentication object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Setting your access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # Creating the API object while passing in auth information
    api = tweepy.API(auth)
    tweets = []
    hashtags = []
    if hashtag == "" and username != "":
      for tweet in api.user_timeline(id=username, count=count):
        tweets.append(tweet.text)
        #print(json.dumps(user._json))
    elif username == "" and hashtag != "":
      hashtag = "#" + hashtag
      for tweet in api.search(q=hashtag, lang="en", count=count):
        hashtags.append(tweet.text)
        #print(json.dumps(hashtag._json))
    elif username != "" and hashtag != "":
      hashtag = "#" + hashtag
      for tweet in api.user_timeline(id=username, count=count):
        tweets.append(tweet.text)
        #print(json.dumps(user._json))
      for tweet in api.search(q=hashtag, lang="en", count=count):
        hashtags.append(tweet.text)
        #print(json.dumps(hashtag._json))
    else:
      tweets.append("No Data")
      hashtags.append("No Data")

    return render(request, 'result.html', {'tweets': tweets, 'hashtags': hashtags, 'username': username, 'hashtag': hashtag})
  
  else:
    return render(request, 'home.html', {})
