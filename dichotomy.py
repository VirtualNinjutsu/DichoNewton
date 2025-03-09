# Dichotomy method for solving equations / Метод дихотомии для решения уравнений
import numpy as np
import sympy as sp
import re
import tkinter as tk

# List of equations / Список уравнений
list_equations = ['arccos(x) + 1','x**2 - 2','x**3 - 4','e^(-x^(2)) - 2', 'x * ln(x) - 1']

# Safe trigonometry function / Безопасная тригонометрическая функция
def safe_f_trigonometry(f, x):
    function_name = getattr(f, "__name__", "")
    if function_name in ["acos", "asin"] and not (-1 <= x <= 1):
        print(f'Недопустимое значение функции {function_name} в точке X = {x}')
        return float('nan')
    elif function_name in ["asec", "acsc"] and not (abs(x) >= 1):
        print(f'Недопустимое значение функции {function_name} в точке X = {x}')
        return float('nan')
    else:
        return f(x)  

# Function to search the range / Функция для поиска диапазона
def search_range(function):
    x_pr = 0
    search_error = 'search error'
    premature_response = 'premature response'
    range = []
    iteration = 0
    max_iteration = 100
    error = 0
    x = sp.symbols('x')
    equation = sp.sympify(function)
    f = sp.lambdify(x, equation, "numpy")
    x = 0.1
    while safe_f_trigonometry(f,x) > 0:
        if f(x) == 0:
            error = premature_response
            x_pr = x
            break
        else:
            x = x - 1
            iteration = iteration + 1
        if iteration >= max_iteration:
            print(f'Функция {function} может принимать только положительное значение!')
            error = error + 1
            break
    a = x
    x = 0.1
    iteration = 0
    max_iteration = 100
    test = f(x)
    while safe_f_trigonometry(f,x) < 0:
        if error == premature_response:
            break
        elif f(x) == 0:
            error = premature_response
            x_pr = x
            break
        x = x + 1
        iteration = iteration + 1
        if iteration >= max_iteration:
            print(f'Функция {function} может принимать только отрицательное значение!')
            error = error + 1
            break
    b = x
    if error == 0:
        range.append(a)
        range.append(b)
        return range
    elif error == premature_response:
        print(f'X = {x_pr}')
        return premature_response
    else:
        print('Существование нужного интервала - невозможно')
        return search_error

# Function to find the solution / Функция для поиска решения
def solution(function, range, accuracy, print_output):
    x = sp.symbols('x')
    equation = sp.sympify(function)
    f = sp.lambdify(x, equation, "numpy")
    x = (range[0] + range[1]) / 2
    while True:
        y = safe_f_trigonometry(f, x)
        
        if np.isnan(y):  
            print_output(f'Недопустимое значение функции {function} в точке X = {x}')
            break
        if f(x) == 0 or 0 < f(x) < accuracy:
            print_output(f'f(x) = 0, для функции: {function} при: ')
            print_output(f'X = {x}')
            break
        else:
            x = (range[0] + range[1]) / 2
        if f(x) < 0:
            range[0] = x
        else:
            range[1] = x

# Function to convert to sympy / Функция для преобразования в sympy
def convert_to_sympy(function):
    replacements = {
        r'e\^': r'exp',  
        r'ln\(': r'log(',        
        r'arccos\(': r'acos(',   
        r'arcsin\(': r'asin(',   
        r'arctan\(': r'atan(',    
        r'tg\(': r'tan('         
    }
    for old, new in replacements.items():
        function = re.sub(old, new, function)  # Заменяем в строке
    
    return function

# Dichotomy method implementation / Реализация метода дихотомии
def dichotomy(function, accuracy, output_widget=None):
    def print_output(message):
        if output_widget:
            output_widget.insert(tk.END, message + '\n')
            output_widget.see(tk.END)
        else:
            print(message)

    accuracy = float(sp.sympify(accuracy))
    function = convert_to_sympy(function)
    range = search_range(function)
    if range == 'search error':
        print_output(f'Уравнение {function} не может быть решено методом деления отрезка пополам!')
    elif range == 'premature response':
        print_output(f'X = {range}')
    else:
        solution(function, range, accuracy, print_output)

# Main block / Главный блок
if __name__ == '__main__':
    dichotomy()