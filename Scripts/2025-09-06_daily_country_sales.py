# ライブラリの読み込み
import pandas as pd
import matplotlib.pyplot as plt

# ファイルの読み込み
sales = pd.read_csv('Data/daily_country_sales.csv')

# データの確認
sales.info()
print(sales.head())
print(sales['country'].unique())
sales.isnull()



# dateカラムをobject型からdatetime型に変える
sales['date'] = pd.to_datetime(sales['date'])

# sales の文字NAを欠損に置換 → 数値化
sales['sales'] = sales['sales'].replace({'N/A': None, '-': None})
sales['sales'] = pd.to_numeric(sales['sales'], errors='coerce')

# 欠損値を含む行を削除する
sales = sales.dropna(subset=['sales', 'country'])

# year_month を「月初日の datetime」にしておく
sales['year_month'] = sales['date'].dt.to_period('M').dt.to_timestamp()

# 表記を統一する
sales['country'] = sales['country'].replace(['United States of America', 'USA'], 'America')

# 国と月ごとに売り上げを集計する
grouped_country = sales.groupby(['country', 'year_month'], as_index=False)['sales'].sum()

# それぞれの国のデータを格納する
China_data   = grouped_country[grouped_country['country'] == 'China'  ].sort_values('year_month')
Japan_data   = grouped_country[grouped_country['country'] == 'Japan'  ].sort_values('year_month')
Korea_data   = grouped_country[grouped_country['country'] == 'Korea'  ].sort_values('year_month')
America_data = grouped_country[grouped_country['country'] == 'America'].sort_values('year_month')



# それぞれの国のグラフを1つに描く
plt.plot(China_data['year_month'], China_data['sales'], label='China')
plt.plot(Japan_data['year_month'], Japan_data['sales'], label='Japan')
plt.plot(Korea_data['year_month'], Korea_data['sales'], label='Korea')
plt.plot(America_data['year_month'], America_data['sales'], label='America')

# データを見やすくする
plt.title('Monthly Sales by Country')
plt.xlabel('Year_Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.legend()
plt.show()