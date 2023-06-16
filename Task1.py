import pandas as panda

data = panda.read_csv("people_data.csv", delimiter=',')
data = data.replace({'[^a-zA-Z0-9\s]': ''}, regex=True)
data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
data = data.dropna()
country_multiplicity = data['Country'].value_counts()
for country, count in country_multiplicity.items():
    print(f"Country: {country}, Count: {count}")
