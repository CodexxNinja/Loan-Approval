import pandas as pd

data = pd.read_csv("dataset/train.csv")
print(data.head())

print(data.shape)

print(data.columns)

print(data.info())
