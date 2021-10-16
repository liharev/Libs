#Вычисления с помощью Numpy
#Задание 1
import numpy as np
a = np.array([[1, 6],
             [2, 8],
             [3, 11],
             [3, 10],
             [1, 7]])
mean_a = np.array([np.mean(a, axis=0)], dtype=float)
print(mean_a)
#Задание 2
a_centered = a - mean_a
print(a_centered)
#Задание 3
a_centered = a_centered.T
a_centered_sp = (a_centered[0] @ a_centered[1])/(len(a_centered[0])-1)
#Задание 4*
cov = np.cov(a.T)[0, 1]
print(a_centered_sp, cov)

