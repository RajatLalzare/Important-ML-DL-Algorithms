import pandas as pd
data =pd.read_csv("C:\\Users\\panka\\Downloads\\DataSets\\Tweets.csv")
print(data.head())
print(data.shape)

x =pd.DataFrame(data)
print(x.head())
print(x.columns)
print(data['text'].head())

#for splliting the words we will creatw a new col which will count the no of words
data['count']=data['text'].apply(lambda x:len(str(x).split()))

print(data['text'],data['count'])
print(x.columns)