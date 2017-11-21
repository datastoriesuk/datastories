import os,pandas as pd,requests,re,time
from bs4 import BeautifulSoup
from datetime import datetime

data=pd.read_csv(os.path.abspath("datastories\wp3\data\@guardian.csv"),encoding="ISO-8859-1")

data=data[data.text.str.contains(r'http')]
data["url"]=""
data["url_creation"], data["tweet_creation"], data["time_diff_minutes"] = [0,0,0]

for i in data.index:
    try:
        link = re.search("(?P<url>https?://[^\s]+)", data.text[i]).group("url")
        session = requests.Session()
        resp = session.head(link, allow_redirects=True).url
        page = requests.get(resp)
        soup = BeautifulSoup(page.content, 'html.parser')
        timeofcr = soup.find_all('time', class_="content__dateline-wpd js-wpd")[0].get("datetime")
        data["url"][i] = resp
        data["url_creation"][i] = datetime.strptime(timeofcr,"%Y-%m-%dT%H:%M:%S+0000")
        data["tweet_creation"][i] = datetime.strptime(data["created_at"][i], '%a %b %d %H:%M:%S +0000 %Y')
        data["time_diff_minutes"][i] = (data["tweet_creation"][i] - data["url_creation"][i]).total_seconds() / 60.0
    except Exception as e:
        print(e)
        time.sleep(1)
