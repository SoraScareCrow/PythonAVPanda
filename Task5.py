import pandas as pd

df = pd.read_csv("people_data.csv", delimiter=',')
df = df.replace({'[^a-zA-Z0-9\s.]': ''}, regex=True)
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df = df.fillna(df.mode().iloc[0])
df['income'] = pd.to_numeric(df['income'], errors='coerce')
num_ranges = 3
wealth_ranges = pd.qcut(df['income'], q=num_ranges, labels=False)
min_income = df['income'].min()
max_income = df['income'].max()
wealth_ranges = [min_income] + list(df['income'].quantile([i / num_ranges for i in range(1, num_ranges)])) + [
    max_income]
wealth_labels = ["Low", "Mid", "High"]
df['wealth_category'] = pd.cut(df['income'], bins=wealth_ranges, labels=wealth_labels)
pd.set_option('display.max_rows', None)
print(df)
