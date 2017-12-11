import re, pandas as pd, numpy as np

def main(file):
    data = pd.DataFrame.from_csv("datastories/wp3/data/"+file)
    datasl = data[["user.id","text","retweet_count","favorite_count","user.followers_count","user.favourites_count"]]
    datasl = datasl[np.isfinite(datasl['user.id'])]
    datasl["text"]=[str(i).lower() for i in datasl["text"]]
    datasl["retweet_weight"] = datasl["retweet_count"].astype(int).multiply(1)
    datasl["favorite_weight"] = datasl["favorite_count"].astype(int).multiply(2)
    datasl['popularity'] = datasl[["favorite_weight","retweet_weight"]].sum(axis=1)
    datasl["id"]=pd.factorize(datasl["user.id"])[0]
    datasl["popperid"]=datasl.groupby(["id"])['popularity'].transform(lambda x: (x - x.min()) / x.max() - x.min())
    datasl['numerical_data'] = [1 if bool(re.compile('\d').search(str(i))) else 0 for i in datasl["text"]]
    datasl['image_data'] = [1 if bool(re.compile('.jpg|.png|.gif|.img|.tiff|.pct|.jpeg|.jpe|.bmp').search(str(i)))
                            else 0 for i in datasl["text"]]
    datasl['url_data'] = [1 if bool(re.compile('http').search(str(i))) else 0 for i in datasl["text"]]
    datasl['numerical_percent'] = [1 if bool(re.compile('\d+%|%\d+').search(str(i)))
                                        else 0 for i in datasl["text"]]
    datasl['numerical_currency'] = [1 if bool(re.compile('\d+[$€£₤]|[$€£₤]\d+|\d+.+[$€£₤]').search(str(i)))
                                        else 0 for i in datasl["text"]]
    datasl['numerical_cardinal'] = [1 if bool(re.compile('one|two|three|four|five|six|seven|eight|nine|ten')
                                            .search(str(i))) else 0 for i in datasl["text"]]
    datasl['numerical_ordinal'] = [1 if bool(re.compile('first|second|third|fourth|fifth|sixth|seventh|eighth|'
                                                       'ninth|tenth|\d+th|\d+st|\d+nd|\d+rd|\d+th')
                                            .search(str(i))) else 0 for i in datasl["text"]]
    datasl['numerical_fraction'] = [1 if bool(re.compile('\d+/\d+').search(str(i)))
                                        else 0 for i in datasl["text"]]
    datasl['numerical_temperature'] = [1 if bool(re.compile('\d+C|\d+F|\d+K|K\d+|C\d+|F\d+').search(str(i)))
                                        else 0 for i in datasl["text"]]
    datasl['numerical_velocity'] = [1 if bool(re.compile('mph|kph').search(str(i)))
                                        else 0 for i in datasl["text"]]
    datasl['numerical_score'] = [1 if bool(re.compile('\d+-\d+|\d+ - \d+').search(str(i)))
                                        else 0 for i in datasl["text"]]
    datasl['numerical_year'] =  [1 if bool(re.compile('1\d{3}|20\d{2}').search(str(i)))
                                        else 0 for i in datasl["text"]]
    datasl['numerical_month'] = [1 if bool(re.compile('january|february|march|april|may|'
                                                      'june|july|august|september|october|'
                                                      'november|december').search(str(i)))
                                        else 0 for i in datasl["text"]]
    datasl['numerical_date'] = [1 if bool(re.compile('\d+/\d+/\d+').search(str(i)))
                                        else 0 for i in datasl["text"]]

    datasl["medianuser"]=datasl.groupby(["id"])["popperid"].transform("median")

    return datasl