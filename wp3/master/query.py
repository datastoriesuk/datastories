import tweepy,sys,os,pandas as pd

keys = [line.rstrip('\n') for line in open(os.path.abspath("..\\keys.txt"))]
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("keys.txt"))))
auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth)

#qr=sys.argv[1]
qr="@guardian"
twlist = []

def query(qr):
    while True:
            try:
                if qr.startswith("@"):
                    for item in tweepy.Cursor(api.user_timeline,screen_name=qr.replace("@",""),lang="en").items():
                        twlist.append(item._json)
                else:
                    for item in tweepy.Cursor(api.search,q=qr,rpp=100,result_type="recent",include_entities=True,lang="en").items():
                        twlist.append(item)
            except Exception as e:
                if "e==Twitter error response: status code = 429":
                    print("Request limit reached")
                    # End after first limit
                    break
                    # # Wait for request limit reset
                    # time.sleep(910)

def main():
    query(qr)
    pd.DataFrame(twlist).to_csv("datastories/wp3/data/" + qr + ".csv")

if __name__ == '__main__':
    sys.exit(main())
