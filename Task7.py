import pandas as panda

data = panda.read_csv("people_data.csv", delimiter=',')
data = data.replace({'[^a-zA-Z0-9\s.]': ''}, regex=True)
data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
data = data.fillna(data.mode().iloc[0])
data['income'] = panda.to_numeric(data['income'], errors='coerce')
total_wealth = data.groupby('Country')['income'].sum()
panda.set_option('display.max_rows', None)
print(total_wealth)
