import os,pandas as pd,requests,re,time,numpy as np,matplotlib.pyplot as plt, seaborn as sns,matplotlib,sys
from bs4 import BeautifulSoup
from datetime import datetime
from collections import Counter
matplotlib.rcParams.update({'font.size': 24})

data=pd.read_csv("datastories\wp3\data\@guardian_url.csv",encoding="ISO-8859-1")

def readqueryresults():
    data=pd.read_csv("datastories\wp3\data\@guardian.csv",encoding="ISO-8859-1")
    data=data[data.text.str.contains(r'http')]
    data["url"]=""
    data["url_creation"], data["tweet_creation"], data["time_diff_minutes"] = [0,0,0]

def plots():
    plt.plot(data["time_diff_minutes"])
    plt.title("Minutes passed before posting to twitter")
    plt.xlabel("Tweet")
    plt.ylabel("Minutes")
    plt.savefig("datastories\\wp3\\data\\@guardian_news2tweet.png")
    plt.close()

    plt.boxplot(data["url"].value_counts())
    plt.title("URL frequency boxplot")
    plt.savefig("datastories\\wp3\\data\\@guardian_urlfreq.png")
    plt.close()

def main():
    for i in data.index:
        try:
            print(i)
            link = re.search("(?P<url>https?://[^\s]+)", data.text[i]).group("url")
            resp = requests.Session().head(link, allow_redirects=True).url
            soup = BeautifulSoup(requests.get(resp).content, 'html.parser')
            data["url"][i] = resp
            data["url_creation"][i] = datetime.strptime(soup.find_all('time', class_="content__dateline-wpd js-wpd")[0].get("datetime"),"%Y-%m-%dT%H:%M:%S%z")
            data["tweet_creation"][i] = datetime.strptime(data["created_at"][i], '%a %b %d %H:%M:%S %z %Y')
            data["time_diff_minutes"][i] = (data["tweet_creation"][i] - data["url_creation"][i]).total_seconds() / 60.0
        except Exception as e:
            print(e)
            time.sleep(1)
    plots()

if __name__ == '__main__':
    sys.exit(main())
