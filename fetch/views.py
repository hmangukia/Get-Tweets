from django.shortcuts import render
import tweepy
# Create your views here.

def home(request):
  if request.method == "POST":
    
    username = request.POST['username']
    hashtag = request.POST['hashtag']
    
    consumer_key = "euF2vpAKFSeffdlvY6OLGKjyb"
    consumer_secret = "PDukSba2b7QnQJQPwju8lQhMl0LcJmuK06C0hxs0kY9B7M77ER"
    access_token = "3503980812-Tt3BTqPf2u7FtUeLRtwJvjTzdtqRZ47O6EhdQzU"
    access_token_secret = "8lAmwKFB8Kg5xv6Rd8dQ7uVoHnpA5ZD60GL24hgTcdD0l"
    # Creating the authentication object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Setting your access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # Creating the API object while passing in auth information
    api = tweepy.API(auth)
    tweets = ""
    hashtag = ""
    for tweet in api.user_timeline(id=username, count=5):
      tweets += tweet.text
    for ht in api.search(q=hashtag, lang="en"):
      t = ht.user.screen_name + "Tweeted:" + ht.text
      hashtag += t
      t = ""

    return render(request, 'result.html', {'tweets': tweets, 'username': username})
  
  else:
    return render(request, 'home.html', {})