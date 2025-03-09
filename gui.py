# GUI for solving equations / GUI для решения уравнений
import tkinter as tk
import dichotomy, newton, newton_for_syst, main

# Function to solve equation using dichotomy method / Функция для решения уравнения методом дихотомии
def solve_dichotomy():
    function = entry_function.get()
    function = function.replace('^', '**')
    accuracy_x = entry_accuracy.get()
    accuracy = 10 ** int(accuracy_x)
    dichotomy.dichotomy(function, accuracy, output_widget=output_text)

# Function to solve equation using Newton's method / Функция для решения уравнения методом Ньютона
def solve_newton():
    function = entry_function.get()
    function = function.replace('^', '**')
    accuracy_x = entry_accuracy.get()
    accuracy = 10 ** int(accuracy_x)
    newton.newton(function, accuracy, output_widget=output_text)

# Function to solve system of equations using Newton's method / Функция для решения системы уравнений методом Ньютона
def solve_newton_for_syst():
    function_1 = entry_function1.get()
    function_1 = function_1.replace('^', '**')
    function_2 = entry_function2.get()
    function_2 = function_2.replace('^', '**')
    accuracy_x = entry_accuracy.get()
    accuracy = 10 ** int(accuracy_x)
    approx_x = float(entry_approx_x.get())
    approx_y = float(entry_approx_y.get())
    approx_val = [approx_x, approx_y]
    newton_for_syst.newton_for_syst(function_1, function_2, approx_val, accuracy, output_widget=output_text)

# Function to plot the graph of equations / Функция для построения графика уравнений
def plot_graph():
    function_1 = entry_function1.get()
    function_1 = function_1.replace('^', '**')
    function_2 = entry_function2.get()
    function_2 = function_2.replace('^', '**')
    newton_for_syst.plot_graf(function_1, function_2)

# Function to check homework / Функция для проверки домашнего задания
def check_homework():
    main.home_work(output_widget=output_text)

# Function to show dichotomy fields / Функция для отображения полей метода дихотомии
def show_dichotomy_fields():
    hide_all_fields()
    lbl_function.pack()
    entry_function.pack()
    lbl_accuracy.pack()
    entry_accuracy.pack()
    btn_solve_dichotomy.pack()

# Function to show Newton's method fields / Функция для отображения полей метода Ньютона
def show_newton_fields():
    hide_all_fields()
    lbl_function.pack()
    entry_function.pack()
    lbl_accuracy.pack()
    entry_accuracy.pack()
    btn_solve_newton.pack()

# Function to show Newton's method for system of equations fields / Функция для отображения полей метода Ньютона для системы уравнений
def show_newton_for_syst_fields():
    hide_all_fields()
    lbl_function1.pack()
    entry_function1.pack()
    lbl_function2.pack()
    entry_function2.pack()
    btn_plot_graph.pack()
    lbl_accuracy.pack()
    entry_accuracy.pack()
    lbl_approx_x.pack()
    entry_approx_x.pack()
    lbl_approx_y.pack()
    entry_approx_y.pack()
    btn_solve_newton_for_syst.pack()

# Function to hide all fields / Функция для скрытия всех полей
def hide_all_fields():
    lbl_function.pack_forget()
    entry_function.pack_forget()
    lbl_function1.pack_forget()
    entry_function1.pack_forget()
    lbl_function2.pack_forget()
    entry_function2.pack_forget()
    lbl_accuracy.pack_forget()
    entry_accuracy.pack_forget()
    lbl_approx_x.pack_forget()
    entry_approx_x.pack_forget()
    lbl_approx_y.pack_forget()
    entry_approx_y.pack_forget()
    btn_solve_dichotomy.pack_forget()
    btn_solve_newton.pack_forget()
    btn_solve_newton_for_syst.pack_forget()
    btn_plot_graph.pack_forget()

# Main application window / Главное окно приложения
app = tk.Tk()
app.title("Решение уравнений")

tk.Label(app, text="Выберите метод решения:").pack()

frame = tk.Frame(app)
frame.pack()

btn_dichotomy = tk.Button(frame, text="Дихотомия", command=show_dichotomy_fields)
btn_dichotomy.pack(side=tk.LEFT)

btn_newton = tk.Button(frame, text="Метод Ньютона", command=show_newton_fields)
btn_newton.pack(side=tk.LEFT)

btn_newton_for_syst = tk.Button(frame, text="Метод Ньютона для системы уравнений", command=show_newton_for_syst_fields)
btn_newton_for_syst.pack(side=tk.LEFT)

btn_homework = tk.Button(frame, text="Решение домашнего задания", command=check_homework)
btn_homework.pack(side=tk.LEFT)

lbl_function = tk.Label(app, text="Введите уравнение:")
entry_function = tk.Entry(app)

lbl_function1 = tk.Label(app, text="Введите уравнение 1:")
entry_function1 = tk.Entry(app)

lbl_function2 = tk.Label(app, text="Введите уравнение 2:")
entry_function2 = tk.Entry(app)

lbl_accuracy = tk.Label(app, text="Введите погрешность (10^x):")
entry_accuracy = tk.Entry(app)

lbl_approx_x = tk.Label(app, text="Введите приближенное значение корня x:")
entry_approx_x = tk.Entry(app)

lbl_approx_y = tk.Label(app, text="Введите приближенное значение корня y:")
entry_approx_y = tk.Entry(app)

btn_solve_dichotomy = tk.Button(app, text="Решить", command=solve_dichotomy)
btn_solve_newton = tk.Button(app, text="Решить", command=solve_newton)
btn_solve_newton_for_syst = tk.Button(app, text="Решить", command=solve_newton_for_syst)
btn_plot_graph = tk.Button(app, text="Построить график", command=plot_graph)  

output_text = tk.Text(app, height=10, width=50)
output_text.pack()

app.mainloop()