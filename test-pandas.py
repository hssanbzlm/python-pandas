import pandas as pd
from pandas.plotting import scatter_matrix
df=pd.read_csv("sbux.csv")

print(type(df))
print(df.tail(20))
print(df.head(20))
print(df.info())
"select a column"
print(df["open"])
print(df[["open","close"]])
"select columns"
print(df.iloc[0])
print(df.loc[0])

df2=pd.read_csv("sbux.csv",index_col="date")
print(df2.loc["2013-02-08"])

print(df[df["open"]>64])

print(df.values)

print(df[["open","close"]].values)

smalldf=df[["open","close"]]
smalldf.to_csv("output.csv")

"apply is the for loop for pandas"

def date_to_year(row):
    return int(row["date"].split("-")[0])
"apply the function to all rows (axis=1)"
print(df.apply(date_to_year,axis=1))
df["year"]=df.apply(date_to_year,axis=1)
print(df.head())


