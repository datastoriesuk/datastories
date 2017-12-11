import tweepy,sys,os,pandas as pd,numpy as np,time,csv,ast,re,matplotlib.pyplot as plt,matplotlib
from pandas.io.json import json_normalize

def main(qtype,terms,maxtweets):
    twlist = []
    while len(twlist)<maxtweets:
            try:
                if type=="user":
                    for item in tweepy.Cursor(api.user_timeline,screen_name=terms.replace("@",""),lang="en").items():
                        twlist.append(item._json)
                elif type=="tweet":
                    for item in tweepy.Cursor(api.search,q=terms,rpp=100,result_type="recent",include_entities=True,lang="en").items():
                        twlist.append(item._json)
                elif type=='bio':
                    for item in tweepy.Cursor(api.search_users,q=terms,rpp=100,result_type="recent",include_entities=True,lang="en").items():
                        twlist.append(item._json)
            except Exception as e:
                if e=="Twitter error response: status code = 429":
                    print("Request limit reached")
                    # End after first limit
                    break
                    # Wait for request limit reset
                    time.sleep(61)
    # Flatten Json
    normtl = json_normalize(twlist)
    pd.DataFrame(normtl).to_csv("datastories/wp3/data/" + qtype + "_" + terms.replace(" ","_") + ".csv",encoding="utf-8")
    return "datastories/wp3/data/" + qtype + "_" + terms.replace(" ","_") + ".csv"



def usertweets(qtype,terms,users, maxtweets):
    tweetlist = []
    peraccount = int(maxtweets / len(users))
    for user in users:
        j = 0
        if len(tweetlist) < maxtweets and j < peraccount:
            try:
                for item in tweepy.Cursor(api.user_timeline, screen_name=user, lang="en").items():
                    tweetlist.append(item._json)
                    j += 1
                    if j >= peraccount:
                        break
            except Exception as e:
                print(e)
                print(len(tweetlist))
                time.sleep(61)
        else:
            break

    normtl = json_normalize(tweetlist)
    pd.DataFrame(normtl).to_csv("datastories/wp3/data/" + str(len(normtl['user.id'].unique())) + "_" + qtype + "_" +
                                terms.replace(" ", "_") + "_" + str(int(len(normtl) / 1000)) + "K_tweets.csv",
                                encoding="utf-8")
    return "datastories/wp3/data/" + str(len(normtl['user.id'].unique())) + "_" + qtype + "_" +terms.replace(" ", "_") + "_" + str(int(len(normtl) / 1000)) + "K_tweets.csv"