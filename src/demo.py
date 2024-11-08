import pandas as pd

# Password: 1234

# バージョンを表示する
print(pd.__version__)

# CSV ファイルを読み込む
df = pd.read_csv('data.csv')

# データを表示する
print(df)
