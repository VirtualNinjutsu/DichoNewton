# Newton's method for solving equations / Метод Ньютона для решения уравнений
import numpy as np
import sympy as sp
from dichotomy import search_range
import tkinter as tk
<<<<<<< HEAD
from dichotomy import convert_to_sympy, safe_f_trigonometry
=======
>>>>>>> 20e02dceabe7b5d44b37564cf0aa5ee544262ca0

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

<<<<<<< HEAD
    function = convert_to_sympy(function)
    aproxx_x = aproxx(function)
    if aproxx_x is None:
        print_output('Не удалось найти начальное приближение.')
=======
    aproxx_x = aproxx(function)
    if aproxx_x is None:
>>>>>>> 20e02dceabe7b5d44b37564cf0aa5ee544262ca0
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
<<<<<<< HEAD
        try:
            fx = f(xn)
            fx_diff = f_diff(xn)
            if fx_diff == 0:
                print_output('Производная равна нулю, метод Ньютона не может продолжить.')
                break
            xn_new = xn - fx/fx_diff
            if abs(f(xn_new)) < accuracy:
                flag = True
                xn = xn_new
                break
            xn = xn_new
        except Exception as e:
            print_output(f'Ошибка: {e}')
            break
    if flag:
        message = f'''Решение уравнения: {function} :
                  X = {xn}
                  '''
        print_output(message)
        print_output(f"Проверка: f({xn}) = {f(xn)}")
    else:
        print_output('Не удалось найти корень.')

if __name__ == '__main__':
    function = 'x**2 - 2'
    accuracy = 1e-6
    newton(function, accuracy)
=======
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
>>>>>>> 20e02dceabe7b5d44b37564cf0aa5ee544262ca0
