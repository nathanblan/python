#this is some datasci stuff hehe

import pandas as pd

csv_path = 'https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv'
df = pd.read_csv(csv_path)

x = df[['Name']]
print(x)
