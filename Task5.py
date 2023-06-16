import pandas as panda

data = panda.read_csv("people_data.csv", delimiter=',')
data = data.replace({'[^a-zA-Z0-9\s.]': ''}, regex=True)
data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
data = data.fillna(data.mode().iloc[0])
data['income'] = panda.to_numeric(data['income'], errors='coerce')
num_ranges = 3
wealth_ranges = panda.qcut(data['income'], q=num_ranges, labels=False)
min_income = data['income'].min()
max_income = data['income'].max()
wealth_ranges = [min_income] + list(data['income'].quantile([i / num_ranges for i in range(1, num_ranges)])) + [
    max_income]
wealth_labels = ["Low", "Mid", "High"]
data['wealth_category'] = panda.cut(data['income'], bins=wealth_ranges, labels=wealth_labels)
panda.set_option('display.max_rows', None)
print(data)
