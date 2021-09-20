from tkinter import *
import matplotlib.pyplot as plt
import random
import math

def clicked():
        # Построение папоротника Барнсли
        global n, x, y
        for i in range(1, n):
                rand = random.randint(1,100)
                if (rand == 1):
                        x[i] = 0
                        y[i] = 0.16 * y[i - 1]
                if ((rand >= 2) and (rand <= 85)):
                        x[i] = 0.85 * x[i - 1] + 0.04 * y[i - 1]
                        y[i] = -0.04 * x[i - 1] + 0.85 * y[i - 1] + 1.6
                if ((86 <= rand) and (rand <= 93)):
                        x[i] = 0.2 * x[i - 1] - 0.26 * y[i - 1]
                        y[i] = 0.23 * x[i - 1] + 0.22 * y[i - 1] + 1.6
                if ((94 <= rand) and (rand <= 100)):
                        x[i] = -0.15 * x[i - 1] + 0.28 * y[i - 1]
                        y[i] = 0.26 * x[i - 1] + 0.24 * y[i - 1] + 0.44

        plt.scatter(x, y, s=0.2, edgecolor='green')
        plt.title("Паппоротник Барнсли")
        plt.show()


def clicked2():
    global n,x,y
    # Дальше идет реализация алгоритма нахождения фрактальной размерности Минковского
    t = 0.001
    l = int(10 / t)
    x1 = [0] * l
    y1 = [0] * l
    p = 0
    i = 0
    a = 0.001
    for p in range(1, l):
        x1[p] = round(a, 1)
        a = a + t
    a = 0.001
    for i in range(1, l):
        y1[i] = round(a, 1)
        a = a + t

    i = 0
    p = 0
    j = 0
    count = 0
    for j in range(1, n):
        for i in range(1, l):
            if (x[j - 1] >= x1[i - 1]) and (x[j - 1] < x1[i]):
                for p in range(1, l):
                    if (y[j - 1] >= y1[p - 1]) and (y[j - 1] < y1[p]):
                        count = count + 1

                        break

    print(count)
    D = (math.log(count)) / (-math.log(t))
    print("Фрактальная размерность: ")
    print(D)

# Графический интерфейс
window = Tk()
window.title("Паппоротник Бэрнсли")
window.geometry('480x100')
lbl = Label(window, text="Количество итераций", font=("Arial", 11))
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="Диаметр множеств для нахождения", font=("Arial", 11))
lbl2.grid(column=4, row=0)
lbl3 = Label(window, text="фрактальной размерности", font=("Arial", 11))
lbl3.grid(column=4, row=1)
lbl5 = Label(window, text="                ", font=("Arial", 11))
lbl5.grid(column=3, row=2)
lbl4 = Label(window, text="0.001", font=("Arial", 11))
lbl4.grid(column=4, row=2)
txt = Entry(window,width=10)
txt.grid(column=0, row=2)
txt.focus()
###################### --- начальные значения
n = int(txt.get())
x = [0] * n
y = [0] * n
x[0] = 0
y[0] = 0
######################
btn = Button(window, text="Построить", command=clicked)
btn.grid(column=0, row=3)
btn2 = Button(window, text="Найти", command=clicked2)
btn2.grid(column=4, row=3)
window.mainloop()

