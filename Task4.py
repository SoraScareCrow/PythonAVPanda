import pandas as pd

df = pd.read_csv("people_data.csv", delimiter=',')
df = df.replace({'[^a-zA-Z0-9\s.]': ''}, regex=True)
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df = df.dropna()
summary_df = df.groupby('Country').agg(
    {'owns_car': 'count', 'Age': 'min', 'owns_TV': 'count', 'owns_house': 'count', 'owns_Phone': 'count'})
summary_df['average_owned_goods'] = summary_df[['owns_car', 'owns_TV', 'owns_house', 'owns_Phone']].mean(axis=1).round(
    2)
summary_df = summary_df[['average_owned_goods', 'Age']]
summary_df.columns = ['Average Owned Goods', 'Minimum Age']
pd.set_option('display.max_rows', None)
print(summary_df)
