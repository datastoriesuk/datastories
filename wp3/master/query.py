import tweepy,csv,sys,pandas as pd

# Twitter auth process
auth = tweepy.OAuthHandler('mJ4E1iTrsDdaiiwHRHz6BnPk1', 'ANKgwrxpizaUjzThUj4xsakGu5j6VVDf8QpL0CN7kNYx9yxYSU')
auth.set_access_token("919910347972268032-dkUsnh8aD3dMACBLDyMdPetKSmWbXDi", "fYH5hZgnvtLpqpmbX4rseiBpW4ZZeCONndiV5CXD47kbl")
api = tweepy.API(auth)

qr=sys.argv[1]

def query(qr):
    # Create a list to store items
    list = []
    while True:
            try:
                if qr.startswith("@"):
                    for item in tweepy.Cursor(api.user_timeline,screen_name=qr.replace("@",""),lang="en").items():
                        list.append(item._json)
                else:
                    for item in tweepy.Cursor(api.search,q=qr,rpp=100,result_type="recent",include_entities=True,lang="en").items():
                        list.append(item)
            except Exception as e:
                if "e==Twitter error response: status code = 429":
                    print("Request limit reached")
                    # End after first limit
                    break
                    # Wait for request reset
                    time.sleep(901)

pd.DataFrame(list).to_csv("datastories/wp3/data/"+qr+".csv")