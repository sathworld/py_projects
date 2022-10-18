# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:54:07 2021

@author: super
"""

#from da.py import function (graph)

import matplotlib.pyplot as plt
# Указываем токен
# Импортируем типы из модуля, чтобы создавать кнопки


# Заготовки для трёх предложений
first = []
second = []
second_add = []
third = []


def graph(y, k, x):
    fig = plt.figure()

    plt.axis([-10, 10, -10, 10])
    plt.grid(True)
    plt.plot((x, -x), (y, -y))
    plt.plot([x, -x], [y, -y], 'ro')
    plt.plot((0, 0), (10, -10), color='#ff7f0e')
    plt.plot((-10, 10), (0, 0), color='#ff7f0e')
    plt.ylabel('Линейная функция')
    plt.show()

    fig.savefig('мой график')

    return fig



graph(10,5,2)