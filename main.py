import pandas as pd



# Загрузка данных из файла .csv
df = pd.read_csv('data.csv')

# Объединение таблиц EMP и SALES
result_df1 = df.groupby(['F_NAME', 'L_NAME'])['AMOUNT'].sum().reset_index()
result_df1 = result_df1.sort_values(by='AMOUNT', ascending=False)

print(result_df1)

# Объединяем таблицы по столбцу "CLIENTS_ID"
merged_df = pd.merge(df, df, left_on='CLIENTS_ID', right_on='ROW_ID', how='left')

# Группируем по "CLIENTS_ID" и считаем количество заказов
order_counts = merged_df.groupby('CLIENTS_ID')['ROW_ID'].count()

# Находим клиента с наименьшим количеством заказов
min_order_count_client = order_counts.idxmin()
result2 = df.loc[df['CLIENTS_ID'] == min_order_count_client, 'NAME'].values[0]

print(f"Клиент с наименьшим количеством заказов: {result2}")

# Преобразование даты в месяц
df['month'] = pd.to_datetime(df['DATE']).dt.to_period('M')

# Группировка по месяцу и статусу
result3 = df.groupby(['month', 'STATUS']).size().reset_index(name='order_count')

# Сортировка результатов
result3.sort_values(by=['month', 'STATUS'], inplace=True)

print(result3)

# Группировка по месяцу и статусу
result4 = df[df['STATUS'] == 'Оплачено'].groupby('month')['AMOUNT'].sum().cumsum().reset_index()
result4.rename(columns={'AMOUNT': 'cumulative_units'}, inplace=True)

print(result4)