import pandas as pd

df = pd.read_csv("people_data.csv", delimiter=',')
df = df.replace({'[^a-zA-Z0-9\s.]': ''}, regex=True)
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df = df.fillna(df.mode().iloc[0])
df['income'] = pd.to_numeric(df['income'], errors='coerce')
total_wealth = df.groupby('Country')['income'].sum()
pd.set_option('display.max_rows', None)
print(total_wealth)
