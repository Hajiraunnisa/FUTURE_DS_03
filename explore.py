import pandas as pd

df = pd.read_csv(
    r'c:\Users\Hajira\OneDrive\Documents\Data Science\Task 3\2019-Oct.csv',
    nrows=5
)
print('Columns:', df.columns.tolist())
print()
print(df.to_string())
