#Задание 5**
import random
def buble(a):
    i = 1
    while i < len(a):
        change = False
        for n in range(len(a) - i):
            if a[n] > a[n + 1]:
                a[n], a[n + 1] = a[n + 1], a[n]
                change = True
        if change == False:
            break
        else:
         i += 1
    return a

a = [random.randint(-100, 100) for x in range(20)]
print(a)
print(buble(a))