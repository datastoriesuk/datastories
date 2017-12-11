import pandas as pd
import auth,query,textscrape,saveplots

#Get twitter auth
api = auth.main()

# Function variables: type, terms, max number elements
# Available Query Types: bio, user, tweet
# Example query.main('bio','data journalist',1000000)
# Saves data as csv in wp3/data folder
# Returns filename
filename=query.main("bio","data",10000)
print ("Data stored in:" + filename)

# Read an older file
# filename = "379_bio_data_journalist_315K_tweets.csv"
# Function variables: query type, terms, users, max number of elements
# Query type and terms are read from data filename
# Example query.gettweets('bio','data',["guardian","times","bbc"],1000000)
# Saves data as csv in wp3/data folder
# Returns filename
filename2=query.usertweets(filename.replace(".csv","").split("/")[-1].split("_")[0],
                 filename.replace(".csv","").split("/")[-1].split("_")[1],
                 pd.DataFrame.from_csv("datastories/wp3/data/"+filename).screen_name.unique(),
                 1000000)

# Identify data types inside tweets (Currently only numericals)
# Calculate user popularity over account and per tweet
# Function variables: filename
# Returns the df
df=textscrape.main(filename2)

# Plot tweet popularity data for columnname of a dataframe if term is in columnname
# Function variables: dataframe, term
saveplots.main(df,"numerical")


