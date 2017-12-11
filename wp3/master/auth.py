import tweepy,os

def main():
    #sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("keys.txt"))))
    keys = [line.rstrip('\n') for line in open(os.path.abspath("..\\keys.txt"))]
    auth = tweepy.OAuthHandler(keys[0], keys[1])
    auth.set_access_token(keys[2], keys[3])
    api = tweepy.API(auth)
    return api
