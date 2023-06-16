import pandas as pd

df = pd.read_csv("people_data.csv", delimiter=',')
df = df.replace({'[^a-zA-Z0-9\s.]': ''}, regex=True)
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df = df.dropna()
df['owned_goods'] = df[['owns_car', 'owns_TV', 'owns_house', 'owns_Phone']].apply(
    lambda row: row.str.lower().str.contains('yes').sum(), axis=1)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df)
