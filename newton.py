# Newton's method for solving equations / Метод Ньютона для решения уравнений
import numpy as np
import sympy as sp
from dichotomy import search_range
import tkinter as tk

# Function to approximate the root / Функция для приближения корня
def aproxx(function):
    aproxx_x = search_range(function)
    if type(aproxx_x) == list:
        aproxx_x = (aproxx_x[0] + aproxx_x[1])/2
        return aproxx_x
    else:
        print('У уравнения нет решений')
        return None

# Newton's method implementation / Реализация метода Ньютона
def newton(function, accuracy, output_widget=None):
    def print_output(message):
        if output_widget:
            output_widget.insert(tk.END, message + '\n')
            output_widget.see(tk.END)
        else:
            print(message)

    aproxx_x = aproxx(function)
    if aproxx_x is None:
        return
    x = sp.symbols('x')
    f = sp.sympify(function)
    f_diff = sp.diff(f, x)
    f = sp.lambdify(x, f, 'numpy')
    f_diff = sp.lambdify(x, f_diff, 'numpy')
    xn = aproxx_x
    max_itter = 100
    flag = False
    for n in range(max_itter):
        fx = f(xn)
        fx_diff = f_diff(xn)
        xn_new = xn - fx/fx_diff
        if abs(f(xn_new)) < accuracy:
            flag = True
            break
        xn = xn_new
    if flag:
        message = f'''Решение уравнения: {function} :
                  X = {xn_new}
                  '''
        print_output(message)
        print_output(f"Проверка: f({xn_new}) = {f(xn_new)}")
    else:
        print_output('Не удалось найти корень.')