import pandas as pd
# new version for github lotto_info

df = pd.read_csv("test.csv")

for column in df:
    series = df[column]
    print(series.values)