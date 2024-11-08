import pandas as pd

# CSV ファイルを読み込む
df = pd.read_csv('data.csv')

# データの最初の5行を表示する
print("データの最初の5行:")
print(df.head())

# データの基本統計情報を表示する
print("\n基本統計情報:")
print(df.describe())

# 特定の列の平均値を表示する（例: 'column_name' 列）
column_name = 'column_name'
if column_name in df.columns:
    print(f"\n'{column_name}' 列の平均値:")
    print(df[column_name].mean())
else:
    print(f"\n'{column_name}' 列は存在しません。")