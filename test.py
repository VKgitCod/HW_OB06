import matplotlib.pyplot as plt
import numpy as np

# Параметры опциона
strike_price = 100  # Цена исполнения (страйк)
premium_received = 10  # Полученная премия за проданный опцион

# Цены базового актива
stock_prices = np.linspace(50, 150, 100)

# Вычисление прибыли по проданному пут-опциону
profit = np.where(stock_prices < strike_price,
                  (stock_prices - strike_price) + premium_received,
                  premium_received)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(stock_prices, profit, label='Проданный Put-опцион', color='b')
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(strike_price, color='gray', linestyle='--')
plt.title('Прибыль по проданному Put-опциону')
plt.xlabel('Цена базового актива')
plt.ylabel('Прибыль')
plt.legend()
plt.grid(True)
plt.show()