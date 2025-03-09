# Newton's method for system of equations / Метод Ньютона для системы уравнений
import numpy as np
import sympy as sp
from newton import aproxx
from dichotomy import convert_to_sympy
import matplotlib.pyplot as plt
import tkinter as tk

# Equations / Уравнения
function_1 = 'tan(x*y + 0.2 - x**2)'
function_2 = '(x**2)/(1/0.6) + (y**2)/0.5 - 1'

# Approximate values / Приближенные значения
approx_val = [1.89, 0.55]
accuracy = 1e-3  # Accuracy / Точность

# Newton's method implementation for system of equations / Реализация метода Ньютона для системы уравнений
def newton_for_syst(function_1, function_2, approx_val, accuracy, output_widget=None):
    def print_output(message):
        if output_widget:
            output_widget.insert(tk.END, message + '\n')
            output_widget.see(tk.END)
        else:
            print(message)

    function_1 = convert_to_sympy(function_1)
    function_2 = convert_to_sympy(function_2)
    x, y = sp.symbols('x y')

    f_1 = sp.sympify(function_1)
    f_2 = sp.sympify(function_2)

    df1_dx = sp.diff(f_1, x) 
    df1_dy = sp.diff(f_1, y)  
    df2_dx = sp.diff(f_2, x)  
    df2_dy = sp.diff(f_2, y)  

    Fx_symp = sp.Matrix([
        [function_1],
        [function_2]
    ])

    F = sp.Matrix([
        [df1_dx, df1_dy],
        [df2_dx, df2_dy]
    ])
    
    max_iter = 100
    x_val, y_val = approx_val

    for i in range(max_iter):
        F_inv_numeric = F.subs({x: x_val, y: y_val}).inv()
        F_inv_numeric = np.array(F_inv_numeric, dtype=float)

        Fx_num = Fx_symp.subs({x: x_val, y: y_val})
        Fx_num = np.array(Fx_num, dtype=float)

        roots_matrix = np.array([
            [x_val],
            [y_val]
        ])
        new_roots_matrix = roots_matrix - np.dot(F_inv_numeric, Fx_num)
        x_val = new_roots_matrix[0,0]
        y_val = new_roots_matrix[1,0]
        
        Fx_num = Fx_symp.subs({x: x_val, y: y_val})
        Fx_num = np.array(Fx_num, dtype=float)

        if np.linalg.norm(Fx_num) < accuracy:
            print_output(f"Корни уравнения: x = {x_val}, y = {y_val}")
            return x_val, y_val

    print_output('Превышено число итераций')
    return None

# Function to plot the graph / Функция для построения графика
def plot_graf(function_1, function_2):
    x_sym, y_sym = sp.symbols('x y')
    x = np.linspace(-5, 5, 400)
    y = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x, y)

    f1 = sp.lambdify((x_sym,y_sym),function_1, "numpy")  
    f2 = sp.lambdify((x_sym,y_sym),function_2, "numpy") 
    F1 = f1(X, Y)
    F2 = f2(X, Y)

    plt.figure(figsize=(8, 8))
    plt.contour(X, Y, F1, levels=[0], colors='blue', label='Уравнение 1')
    plt.contour(X, Y, F2, levels=[0], colors='red', label='Уравнение 2')
    plt.grid(True)
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.title('График двух уравнений')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['Уравнение 1', 'Уравнение 2'])
    plt.show()
    
# Main block / Главный блок
if __name__ == '__main__':
    newton_for_syst(function_1, function_2, approx_val, accuracy)