# ライブラリの読み込み
import pandas as pd
import matplotlib.pyplot as plt

# ファイルの読み込み
data = pd.read_csv('Data/call_center_analysis.csv')

# データの基本統計量の確認
describe_data = data.describe()
print(describe_data)

# オペレーター別の待ち時間ごとの満足度を求める
data['WaitTimeMin'] = round(data['WaitTimeMin'])
grouped_operator = data.groupby(['WaitTimeMin', 'Operator'])['Satisfaction'].mean()
unstacked_operator = grouped_operator.unstack(fill_value=0)

# 折れ線グラフに可視化
unstacked_operator.plot(kind='line')

plt.xlabel('WaitTimeMin')
plt.ylabel('Satisfaction')
plt.tight_layout()
plt.show()

# 問題タイプごとの解決率をクロス集計表にする
crosstab = pd.crosstab(data['IssueType'], data['Resolved'], normalize='index') * 100
print(crosstab)

# 通話時間と満足度の関係性を求める
data['CallDurationMin'] = round(data['CallDurationMin'])
grouped_callduration = data.groupby('CallDurationMin', as_index=False)['Satisfaction'].mean()

# 可視化
grouped_callduration.plot(kind='bar', x='CallDurationMin', y='Satisfaction')

plt.xlabel('CallDurationMin')
plt.ylabel('Satisfaction')
plt.tight_layout()
plt.show()