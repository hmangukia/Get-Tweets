from django.shortcuts import render
import tweepy
# Create your views here.

def home(request):
  if request.method == "POST":
    
    username = request.POST['username']
    hashtag = request.POST['hashtag']
    consumer_key = "your consumer key here"
    consumer_secret = "your consumer secret key here"
    access_token = "your access token here"
    access_token_secret = "your access tokey secret key here"
    # Creating the authentication object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Setting your access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # Creating the API object while passing in auth information
    api = tweepy.API(auth)
    tweets = []
    hashtags = []
    if hashtag == "" and username != "":
      for tweet in api.user_timeline(id=username, count=5):
        tweets.append(tweet.text)
    elif username == "" and hashtag != "":
      hashtag = "#" + hashtag
      for tweet in api.search(q=hashtag, lang="en", count=5):
        hashtags.append(tweet.text)
    else:
      hashtag = "#" + hashtag
      for tweet in api.user_timeline(id=username, count=5):
        tweets.append(tweet.text)
      for tweet in api.search(q=hashtag, lang="en", count=5):
        hashtags.append(tweet.text)

    return render(request, 'result.html', {'tweets': tweets, 'hashtags': hashtags})
  
  else:
    return render(request, 'home.html', {})
