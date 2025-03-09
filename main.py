# Main file to run the program / Главный файл для запуска программы
import dichotomy, newton, newton_for_syst, gui
import tkinter as tk

# Greeting function / Функция приветствия
def greeting():
    print('''Программа для решения уравнения запущена.
          Выберете метод решения уварнения:
          1)Дихотомия
          2)Метод Ньютона
          3)Метод Ньютона для системы уравнений''')
    choose = int(input())

    if choose == 1:
        function = input('Введите уравнение: ')
        function = function.replace('^', '**')
        accuracy_x = input('Введите погрешность (10^x): ')
        accuracy = 10 ** int(accuracy_x)
        print(accuracy)
        dichotomy.dichotomy(function, accuracy)
    elif choose == 2:
        function = input('Введите уравнение: ')
        function = function.replace('^', '**')
        accuracy_x = input('Введите погрешность (10^x): ')
        accuracy = 10 ** int(accuracy_x)
        print(accuracy)
        newton.newton(function, accuracy)
    elif choose == 3:
        function_1 = input('Введите уравнение 1: ')
        function_1 = function_1.replace('^', '**')
        function_2 = input('Введите уравнение 2: ')
        function_2 = function_2.replace('^', '**')
        accuracy_x = input('Введите погрешность (10^x): ')
        accuracy = 10 ** int(accuracy_x)
        print(accuracy)
        newton_for_syst.plot_graf(function_1, function_2)
        approx_val = []
        approx_val.append(float(input('Введите приближенное значение корня x: ')))
        approx_val.append(float(input('Введите приближенное значение корня y: ')))
        newton_for_syst.newton_for_syst(function_1, function_2, approx_val, accuracy)

# Function for homework / Функция для домашнего задания
def home_work(output_widget=None):
    def print_output(message):
        if output_widget:
            output_widget.insert(tk.END, message + '\n')
            output_widget.see(tk.END)
        else:
            print(message)

    function_1_1 = 'sin(x) + 0.05*x^2 - 0.6'
    accuracies = [10**(-2), 10**(-3), 10**(-4), 10**(-5), 10**(-6)]  
    function_2_1 = 'x^5 - 7*x^2 + 3'
    function_3_1 = 'tan(x*y + 0.2 - x**2)'
    function_3_2 = '(x**2)/(1/0.6) + (y**2)/0.5 - 1'
    approx_val = [0.77, 0.57]
    
    for accuracy in accuracies:
        print_output(f"Решение уравнения методом дихотомии для точности {accuracy}:")
        dichotomy.dichotomy(function_1_1, accuracy, output_widget=output_widget)
    
    for accuracy in accuracies:
        print_output(f"Решение уравнения методом Ньютона для точности {accuracy}:")
        newton.newton(function_2_1, accuracy, output_widget=output_widget)
    
    for accuracy in accuracies:
        print_output(f"Решение системы уравнений методом Ньютона для точности {accuracy}:")
        newton_for_syst.newton_for_syst(function_3_1, function_3_2, approx_val, accuracy, output_widget=output_widget)

# Main block / Главный блок
if __name__ == '__main__':
    gui.app.mainloop()