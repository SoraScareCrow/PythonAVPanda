import pandas as panda

data = panda.read_csv("people_data.csv", delimiter=',')
data = data.replace({'[^a-zA-Z0-9\s.]': ''}, regex=True)
data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
data = data.dropna()
summary_df = data.groupby('Country').agg(
    {'owns_car': 'count', 'Age': 'min', 'owns_TV': 'count', 'owns_house': 'count', 'owns_Phone': 'count'})
summary_df['average_owned_goods'] = summary_df[['owns_car', 'owns_TV', 'owns_house', 'owns_Phone']].mean(axis=1).round(
    2)
summary_df = summary_df[['average_owned_goods', 'Age']]
summary_df.columns = ['Average Owned Goods', 'Minimum Age']
panda.set_option('display.max_rows', None)
print(summary_df)
