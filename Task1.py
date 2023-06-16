import pandas as pd

df = pd.read_csv("people_data.csv", delimiter=',')
df = df.replace({'[^a-zA-Z0-9\s]': ''}, regex=True)
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df = df.dropna()
country_multiplicity = df['Country'].value_counts()
for country, count in country_multiplicity.items():
    print(f"Country: {country}, Count: {count}")
