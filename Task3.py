import pandas as pd

df = pd.read_csv("people_data.csv", delimiter=',')
df = df.replace({'[^a-zA-Z0-9\s.]': ''}, regex=True)
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df = df.dropna()
df['income'] = df['income'].astype(float)
avg_wealth = df.groupby('gender')['income'].mean()
print(avg_wealth)
