# ライブラリの読み込み
import pandas as pd
import matplotlib.pyplot as plt

# ファイルの読み込み込み
performance = pd.read_csv('Data/team_performance.csv')
sales = pd.read_csv('Data/team_merch_sales.csv')

# チームごとのすべての売り上げを合計する
annual_sales = sales.groupby('TeamID', as_index=False)['MerchRevenueJPY'].sum()

# 2つのファイルを合わせる
merged = pd.merge(performance, annual_sales, on='TeamID')

# データの可視化
plt.scatter(merged['WinRate'], merged['MerchRevenueJPY'])

plt.xlabel('WinRate')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()