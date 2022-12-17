import pandas as pd

df1 = pd.read_csv("daily_sales_data_0.csv")
df2 = pd.read_csv("daily_sales_data_1.csv")
df3 = pd.read_csv("daily_sales_data_2.csv")
merge = pd.concat([df1, df2])
final = pd.concat([merge, df3])
final = final[final['product'] == 'pink morsel']
final = final.reset_index()
for i in range(0,5880):
  final['sales'] = float((str(final['price'][i]).split('$')[1])) * float(final['quantity'][i])
final = final.drop('index', axis = 1)
final = final.drop('price', axis = 1)
final = final.drop('quantity', axis = 1)
final = final.drop('product', axis = 1)
final.to_csv('data_merged.csv')
