import tweepy,csv

# Twitter auth process
auth = tweepy.OAuthHandler('mJ4E1iTrsDdaiiwHRHz6BnPk1', 'ANKgwrxpizaUjzThUj4xsakGu5j6VVDf8QpL0CN7kNYx9yxYSU')
auth.set_access_token("919910347972268032-dkUsnh8aD3dMACBLDyMdPetKSmWbXDi", "fYH5hZgnvtLpqpmbX4rseiBpW4ZZeCONndiV5CXD47kbl")
api = tweepy.API(auth)

# Search for tweets with that term
term="data"




def query():
    # Create a list to tweets/m
    list = []

    while True:
        try:
            for tweet in tweepy.Cursor(api.search,q=term,rpp=100,result_type="recent",include_entities=True,lang="en").items():
                tweets.append(tweet)

        except Exception as e:
            if "e==Twitter error response: status code = 429":
                print("Oops request limit reached")

                # End after first limit
                break

                # Wait for request reset
                time.sleep(901)

csv.writer("tweets.csv")
