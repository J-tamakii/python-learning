# ライブラリの読み込みと共通設定
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bins = range(0, 16)

# ファイルの読み込み込み
customer_visits = pd.read_csv('Data/customer_visits.csv')



# 男性の来店回数の可視化
plt.subplot(1, 2, 1)
df_male = customer_visits.query('Gender == "Male"')
plt.hist(df_male['Visits'])
plt.title('Male')


# 女性の来店回数の可視化
plt.subplot(1, 2, 2)
df_female = customer_visits.query('Gender == "Female"')
plt.hist(df_female['Visits'])
plt.title('Female')


plt.figure(figsize = (15, 5))
plt.tight_layout()
plt.show()



# 属性に'年代'を追加
customer_visits['AgeGroup'] = np.floor(customer_visits['Age'] / 10) * 10

# 10代の来店回数の可視化
plt.subplot(2, 3, 1)
under_20years = customer_visits.query('AgeGroup == 10')
plt.hist(under_20years['Visits'], bins = bins)
plt.title('10s')
plt.xlabel('Number of Visits')
plt.ylabel('Number of Customers')


# 20代の来店回数の可視化
plt.subplot(2, 3, 2)
over_20years = customer_visits.query('AgeGroup == 20')
plt.hist(over_20years['Visits'], bins = bins)
plt.title('20s')
plt.xlabel('Number of Visits')
plt.ylabel('Number of Customers')


# 30代の来店回数の可視化
plt.subplot(2, 3, 3)
over_30years = customer_visits.query('AgeGroup == 30')
plt.hist(over_30years['Visits'], bins = bins)
plt.title('30s')
plt.xlabel('Number of Visits')
plt.ylabel('Number of Customers')


# 40代の来店回数の可視化
plt.subplot(2, 3, 4)
over_40years = customer_visits.query('AgeGroup == 40')
plt.hist(over_40years['Visits'], bins = bins)
plt.title('40s')
plt.xlabel('Number of Visits')
plt.ylabel('Number of Customers')


# 50代の来店回数の可視化
plt.subplot(2, 3, 5)
over_50years = customer_visits.query('AgeGroup == 50')
plt.hist(over_50years['Visits'], bins = bins)
plt.title('50s')
plt.xlabel('Number of Visits')
plt.ylabel('Number of Customers')


# 60代の来店回数の可視化
plt.subplot(2, 3, 6)
over_60years = customer_visits.query('AgeGroup == 60')
plt.hist(over_60years['Visits'], bins = bins)
plt.title('60s')
plt.xlabel('Number of Visits')
plt.ylabel('Number of Customers')


plt.figure(figsize = (15, 5))
plt.tight_layout()
plt.show()