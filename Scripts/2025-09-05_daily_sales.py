# ライブラリの読み込み
import pandas as pd
import matplotlib.pyplot as plt

# ファイルの読み込み
sales = pd.read_csv('Data/daily_sales.csv')

# データ型の確認
sales.info()

# object型からint64に直す
sales['date'] = pd.to_datetime(sales['date'])
sales['date'] = sales['date'].dt.strftime('%Y-%m')

# 月ごとの売り上げの集計とカラムのリネーム
monthly_sales = sales.groupby('date', as_index=False)['sales'].sum()
monthly_sales = sales.rename(columns={'date': 'month'})

# グラフの可視化
plt.bar(monthly_sales['month'], monthly_sales['sales'])

# グラフを見やすくする
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()