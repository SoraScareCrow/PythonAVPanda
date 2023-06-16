import pandas as panda

data = panda.read_csv("people_data.csv", delimiter=',')
data = data.replace({'[^a-zA-Z0-9\s.]': ''}, regex=True)
data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
data = data.dropna()
data['owned_goods'] = data[['owns_car', 'owns_TV', 'owns_house', 'owns_Phone']].apply(
    lambda row: row.str.lower().str.contains('yes').sum(), axis=1)
panda.set_option('display.max_columns', None)
panda.set_option('display.max_rows', None)
print(data)
