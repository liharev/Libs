#Визуализация данных в Matplotlib
#Задание 1
import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5, 6, 7]
y = [3.5, 3.8, 4.2, 4.5, 5, 5.5, 7]
plt.plot(x,y)
plt.show()
plt.scatter(x,y)
plt.show()
#Задание 2
t = np.linspace(0,10,51, endpoint=True)
f = np.cos(t)
plt.plot(t,f, color="green")
plt.title('График f(t)')
plt.xlabel('Значения t')
plt.ylabel('Значения f')
plt.axis([0.5, 9.5, -2.5, 2.5])
plt.show()
#*Задание 3
x = np.linspace(-3,3,51, endpoint=True)
y1 = x**2
y2 = 2 * x + 0.5
y3 = -3 * x - 1.5
y4 = np.sin(x)
fig, ax = plt.subplots(nrows=2, ncols=2)
ax1, ax2, ax3, ax4 = ax.flatten()
fig.set_size_inches(8, 6)
fig.subplots_adjust(wspace=0.3, hspace=0.3)
ax1.plot(x, y1)
ax1.set_title("График y1")
ax1.set_xlim([-5, 5])
ax2.plot(x, y2)
ax2.set_title("График y2")
ax3.plot(x, y3)
ax3.set_title("График y3")
ax4.plot(x, y4)
ax4.set_title("График y4")
plt.show()
#*Задание 4
import pandas as pd
import matplotlib.style as style
style.use('fivethirtyeight')
direct_link = 'creditcard.csv'
cards = pd.read_csv(direct_link)
plt.bar([0, 1], cards["Class"].value_counts())
plt.show()
plt.bar([0, 1], cards["Class"].value_counts())
plt.yscale("log")
plt.show()
#-----------
plt.hist(cards.loc[cards['Class'] == 1]["V1"], bins=20, density=True, color="red", alpha = 0.5)
plt.hist(cards.loc[cards['Class'] == 0]["V1"], bins=20, density=True, color="grey", alpha = 0.5)
plt.xlabel('V1')
plt.show()