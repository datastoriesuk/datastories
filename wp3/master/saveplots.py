import matplotlib.pyplot as plt,matplotlib
matplotlib.rcParams.update({'font.size': 12})

# Column "numerical"

def main(dfname,colname):
    columnlist= [i for i in list(df) if colname in i]

    def plotbar(dfname,col1,col2,col3):
        dfname.groupby([col1, col2])[col3].mean().unstack().plot(kind="bar",title= col2 +" in tweet")
        plt.ylabel("Popularity")
        plt.xlabel("Twitter account")
        plt.xticks([])
        plt.tight_layout()
        plt.savefig("datastories\\wp3\\plots\\temp\\379_acc_315K_tweets_"+col2+".png", dpi=1000)
        plt.close()

    for i in columnlist:
        print(i)
        plotbar(dfname, "id", i, "popperid")


# col1="id"
# col2=["numerical_data","image_data","url_data"]
# col3="popperid"
# for i in ["numerical_data", "image_data", "url_data"]:
#     plotbar(datasl, "id", i, "popperid")
#     plotbar(datasl[datasl["popularity"]>0], "id", i, "popperid")

