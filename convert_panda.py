import pandas as pd


df = pd.read_csv("test.csv")

for column in df:
    series = df[column]
    print(series.values)