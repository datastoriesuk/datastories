import tweepy,sys,os,pandas as pd

data=pd.read_csv(os.path.abspath("datastories\wp3\data\@guardian.csv"),encoding="ISO-8859-1")

data=data[data.text.cont]