import pandas as pd

data = pd.read_csv("iris.csv")

#print(data.head())

#print(data.info())

#print(data.isnull().sum())

#data_clean = data.dropna()
#print(data_clean.shape)

#data['SepalLengthCm'] = data['SepalLengthCm'].fillna(data['SepalLengthCm'].mean())
#print(data['SepalLengthCm'].head())

#print(data.duplicated().sum())

#data = data.drop_duplicates()
#print(data.shape)

#print(data.describe())

#data = data[data['SepalLengthCm'] <= 100]
#print(data.shape)

#print(data['Species'].unique())

#data['Species'] = data['Species'].str.lower()
#print(data['Species'].unique())

print(data.info())
print(data.describe())

