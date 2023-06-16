import pandas as pd

df = pd.read_csv("people_data.csv", delimiter=',')
df = df.replace({'[^a-zA-Z0-9\s.]': ''}, regex=True)
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df = df.fillna(df.mode().iloc[0])
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
age_ranges = [0, 17, 29, 49, float('inf')]
age_labels = ['0-17', '18-29', '30-49', '50+']
df['age_group'] = pd.cut(df['Age'], bins=age_ranges, labels=age_labels)
age_group_count = df.groupby(['Country', 'age_group']).size().unstack(fill_value=0)
pd.set_option('display.max_rows', None)
print(age_group_count)
