import pandas as panda

data = panda.read_csv("people_data.csv", delimiter=',')
data = data.replace({'[^a-zA-Z0-9\s.]': ''}, regex=True)
data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
data = data.dropna()
data['income'] = data['income'].astype(float)
avg_wealth = data.groupby('gender')['income'].mean()
print(avg_wealth)
