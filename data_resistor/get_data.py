import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

file_path = 'ozhigova.csv'
data = pd.read_csv(file_path, sep='\t', header=None, names=['sensor', 'value', 'timestamp'])

data['timestamp'] = pd.to_datetime(data['timestamp'])
data['timestamp'] = data['timestamp'] + timedelta(hours=8)

p_data = data[data['sensor'] == 'p']
t_data = data[data['sensor'] == 't']
m_data = data[data['sensor'] == 'm']

print(f'Всего данных с фоторезистора: {len(p_data)}')

plt.figure(figsize=(10, 6))
plt.plot_date(p_data['timestamp'], p_data['value'].apply(lambda x: int(''.join(filter(str.isdigit, str(x))))), label='p')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.title('Данные фоторезистора')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(t_data['timestamp'], t_data['value'], 'go', label='t')
plt.xlabel('Время')
plt.title('Данные кнопки')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(m_data['timestamp'], m_data['value'], 'ro', label='m')
plt.xlabel('Время')
plt.title('Данные магнита')
plt.legend()
plt.grid(True)
plt.show()