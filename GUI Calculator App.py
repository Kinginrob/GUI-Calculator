import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the calculator display
        self.display = tk.Entry(master, width=40, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create the calculator buttons
        self.button_1 = tk.Button(master, text="1", padx=40, pady=20, command=lambda: self.button_click(1))
        self.button_2 = tk.Button(master, text="2", padx=40, pady=20, command=lambda: self.button_click(2))
        self.button_3 = tk.Button(master, text="3", padx=40, pady=20, command=lambda: self.button_click(3))
        self.button_4 = tk.Button(master, text="4", padx=40, pady=20, command=lambda: self.button_click(4))
        self.button_5 = tk.Button(master, text="5", padx=40, pady=20, command=lambda: self.button_click(5))
        self.button_6 = tk.Button(master, text="6", padx=40, pady=20, command=lambda: self.button_click(6))
        self.button_7 = tk.Button(master, text="7", padx=40, pady=20, command=lambda: self.button_click(7))
        self.button_8 = tk.Button(master, text="8", padx=40, pady=20, command=lambda: self.button_click(8))
        self.button_9 = tk.Button(master, text="9", padx=40, pady=20, command=lambda: self.button_click(9))
        self.button_0 = tk.Button(master, text="0", padx=40, pady=20, command=lambda: self.button_click(0))

        self.button_add = tk.Button(master, text="+", padx=39, pady=20, command=self.button_add)
        self.button_subtract = tk.Button(master, text="-", padx=41, pady=20, command=self.button_subtract)
        self.button_multiply = tk.Button(master, text="*", padx=40, pady=20, command=self.button_multiply)
        self.button_divide = tk.Button(master, text="/", padx=41, pady=20, command=self.button_divide)

        self.button_clear = tk.Button(master, text="Clear", padx=79, pady=20, command=self.button_clear)
        self.button_equals = tk.Button(master, text="=", padx=91, pady=20, command=self.button_equals)

        # Put the buttons on the screen
        self.button_1.grid(row=3, column=0)
        self.button_2.grid(row=3, column=1)
        self.button_3.grid(row=3, column=2)

        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)

        self.button_7.grid(row=1, column=0)
        self.button_8.grid(row=1, column=1)
        self.button_9.grid(row=1, column=2)

        self.button_0.grid(row=4, column=0)

        self.button_add.grid(row=5, column=0)
        self.button_subtract.grid(row=6, column=0)
        self.button_multiply.grid(row=6, column=1)
        self.button_divide.grid(row=5, column=2)

        self.button_clear.grid(row=4, column=1, columnspan=2)
        self.button_equals.grid(row=4, column=3, columnspan=2)

    def button_click(self, number):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, str(current) + str(number))

    def button_clear(self):
        self.display.delete(0, tk.END)

    def button_add(self):
        first_number = self.display.get()
        global f_num
        global math_operation
        math_operation = "addition"
        f_num = int(first_number)
        self.display.delete(0, tk.END)

    def button_subtract(self):
        first_number = self.display.get()
        global f_num
        global math_operation
        math_operation = "subtraction"
        f_num = int(first_number)
        self.display.delete(0, tk.END)

    def button_multiply(self):
        first_number = self.display.get()
        global f_num
        global math_operation
        math_operation = "multiplication"
        f_num = int(first_number)
        self.display.delete(0, tk.END)

    def button_divide(self):
        first_number = self.display.get()
        global f_num
        global math_operation
        math_operation = "division"
        f_num = int(first_number)
        self.display.delete(0, tk.END)

    def button_equals(self):
        second_number = self.display.get()
        self.display.delete(0, tk.END)

        if math_operation == "addition":
            self.display.insert(0, f_num + int(second_number))
        elif math_operation == "subtraction":
            self.display.insert(0, f_num - int(second_number))
        elif math_operation == "multiplication":
            self.display.insert(0, f_num * int(second_number))
        elif math_operation == "division":
            self.display.insert(0, f_num / int(second_number))


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
