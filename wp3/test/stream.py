import tweepy

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)


# just a list to store statuses as json
# statuses = []
class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # statuses.append(status._json) #If you dont need the list comment this line
        print(status.text)
        return False
        # Define a limit of tweets to stop
        if len(statuses) >= 100:
            return False

    def on_error(self, status_code):
        # Stop if request limit reached
        if status_code == 420:
            return False


stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

# Use any text inside the track, eg. track=['trump','usa'] or track=['#love,britain']
stream.filter(languages=["en"], track=["#sport"])
