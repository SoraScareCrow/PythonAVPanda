import pandas as panda

data = panda.read_csv("people_data.csv", delimiter=',')
data = data.replace({'[^a-zA-Z0-9\s.]': ''}, regex=True)
data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
data = data.fillna(data.mode().iloc[0])
data['Age'] = panda.to_numeric(data['Age'], errors='coerce')
age_ranges = [0, 17, 29, 49, float('inf')]
age_labels = ['0-17', '18-29', '30-49', '50+']
data['age_group'] = panda.cut(data['Age'], bins=age_ranges, labels=age_labels)
age_group_count = data.groupby(['Country', 'age_group']).size().unstack(fill_value=0)
panda.set_option('display.max_rows', None)
print(age_group_count)
