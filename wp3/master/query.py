import tweepy,sys,os,pandas as pd,numpy as np,time,csv,ast,re,matplotlib.pyplot as plt,matplotlib
from pandas.io.json import json_normalize
matplotlib.rcParams.update({'font.size': 12})


keys = [line.rstrip('\n') for line in open(os.path.abspath("..\\keys.txt"))]
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("keys.txt"))))
auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth)

#qr=sys.argv[1]
tupleqr=('bio','data journalist')
mintweets=20000


def query(qr):
    twlist = []
    while len(twlist)<mintweets:
            try:
                if qr[0]=="user":
                    for item in tweepy.Cursor(api.user_timeline,screen_name=qr[1].replace("@",""),lang="en").items():
                        twlist.append(item._json)
                elif qr[0]=="tweet":
                    for item in tweepy.Cursor(api.search,q=qr[1],rpp=100,result_type="recent",include_entities=True,lang="en").items():
                        twlist.append(item._json)
                elif qr[0]=='bio':
                    for item in tweepy.Cursor(api.search_users,q=qr[1],rpp=100,result_type="recent",include_entities=True,lang="en").items():
                        twlist.append(item._json)
            except Exception as e:
                if e=="Twitter error response: status code = 429":
                    print("Request limit reached")
                    # End after first limit
                    break
                    # # Wait for request limit reset
                    # time.sleep(910)
    # Need to flatten Json
    pd.DataFrame(twlist).to_csv("datastories/wp3/data/" + qr[0] + "_" + qr[1].replace(" ","_") + ".csv",encoding="utf-8")

# dj=pd.DataFrame.from_csv("datastories/wp3/data/data_journalist.csv")
# djs=dj.screen_name.unique()
# gettweets(tupleqr,djs,100000)

def gettweets(qr,users,totaltweets):
    tweetlist=[]
    peraccount=int(totaltweets/len(users))
    for user in users:
        j=0
        if len(tweetlist) < totaltweets and j<peraccount:
            try:
                for item in tweepy.Cursor(api.user_timeline, screen_name=user, lang="en").items():
                    tweetlist.append(item._json)
                    j+=1
                    if j>=peraccount:
                        break
            except Exception as e:
                print(e)
                print(len(tweetlist))
                time.sleep(61)
                gettweets.tl = tweetlist
        else:
            break
    normtl=json_normalize(tweetlist)
    pd.DataFrame(normtl).to_csv("datastories/wp3/data/" + str(len(normtl['user.id'].unique())) + "_" + qr[0] + "_" +
                                qr[1].replace(" ", "_") + "_" + str(int(len(normtl) / 1000)) + "K_tweets.csv",
                                encoding="utf-8")

# data = pd.DataFrame.from_csv("datastories/wp3/data/29_bio_data_journalist_67K_tweets.csv")
# datasl = data[["user.id","text","retweet_count","favorite_count","user.followers_count","user.favourites_count"]]
# datasl = datasl[np.isfinite(datasl['user.id'])]
# datasl["text"]=[str(i).lower() for i in datasl["text"]]
# datasl["retweet_weight"] = datasl["retweet_count"] * 1.0
# datasl["favorite_weight"] = datasl["favorite_count"] * 2
# datasl['popularity'] = datasl[["favorite_weight","retweet_weight"]].sum(axis=1)
# datasl["id"]=pd.factorize(datasl["user.id"])[0]
# datasl["normpop"]=datasl.groupby(["id"])['popularity'].transform(lambda x: (x - x.min()) / x.max() - x.min())
# datasl['numerical_data'] = [1 if bool(re.compile('\d').search(str(i))) else 0 for i in datasl["text"]]
# datasl['image_data'] = [1 if bool(re.compile('.jpg|.png|.gif|.img|.tiff|.pct|.jpeg|.jpe|.bmp').search(str(i))) else 0 for i in datasl["text"]]
# datasl['url_data'] = [1 if bool(re.compile('http').search(str(i))) else 0 for i in datasl["text"]]

# col1="id"
# col2=["numerical_data","image_data","url_data"]
# col3="normpop"
# for i in ["numerical_data", "image_data", "url_data"]:
#     plotbar(datasl, "id", i, "normpop")
#     plotbar(datasl[datasl["popularity"]>0], "id", i, "normpop")

def plotbar(df,col1,col2,col3):
    df.groupby([col1, col2])[col3].mean().unstack().plot(kind="bar",title= col2 +" in tweet with pop > 0")
    plt.ylabel("Popularity")
    plt.xlabel("Twitter account")
    plt.tight_layout()
    plt.savefig("datastories\\wp3\\plot\\temp\\29_acc_67K_tweets_"+col2+"_shared.png", dpi=1000)
    plt.close()

def main():
    # query()
    # gettweets()

if __name__ == '__main__':
    sys.exit(main())
