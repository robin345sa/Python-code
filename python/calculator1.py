import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        self.total_expression = ""
        self.current_expression = ""
        self.digits = {7: (1, 1), 8: (1, 2), 9: (1, 3), 4: (2, 1), 5: (2, 2), 6: (2, 3), 1: (3, 1), 2: (3, 2), 3: (3, 3), 0: (4, 2), '.': (4, 1)}
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        
        self.display_frame = tk.Frame(self.window, height=100, bg="#E3E3E3")
        self.display_frame.pack(expand=True, fill="both")
        self.total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="#E3E3E3", fg="#2C3E50", font=("Consolas", 18))
        self.total_label.pack(expand=True, fill='both')
        self.label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="#E3E3E3", fg="#2C3E50", font=("Consolas", 38, "bold"))
        self.label.pack(expand=True, fill='both')
        
        self.buttons_frame = tk.Frame(self.window)
        self.buttons_frame.pack(expand=True, fill="both")
        for x in range(5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        
        self.create_buttons()
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits: self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations: self.window.bind(key, lambda event, operator=key: self.append_operator(operator))
        
    def create_buttons(self):
        for digit, grid_value in self.digits.items():
            tk.Button(self.buttons_frame, text=str(digit), bg="#000", fg="#fff", font=("Consolas", 26, "bold"), borderwidth=0, command=lambda x=digit: self.add_to_expression(x)).grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
        i = 0
        for operator, symbol in self.operations.items():
            tk.Button(self.buttons_frame, text=symbol, bg="#F1F1F1", fg="#2C3E50", font=("Consolas", 22), borderwidth=0, command=lambda x=operator: self.append_operator(x)).grid(row=i, column=4, sticky=tk.NSEW)
            i += 1
        tk.Button(self.buttons_frame, text="C", bg="#F1F1F1", fg="#2C3E50", font=("Consolas", 22), borderwidth=0, command=self.clear).grid(row=0, column=1, sticky=tk.NSEW)
        tk.Button(self.buttons_frame, text="x²", bg="#F1F1F1", fg="#2C3E50", font=("Consolas", 22), borderwidth=0, command=self.square).grid(row=0, column=2, sticky=tk.NSEW)
        tk.Button(self.buttons_frame, text="√x", bg="#F1F1F1", fg="#2C3E50", font=("Consolas", 22), borderwidth=0, command=self.sqrt).grid(row=0, column=3, sticky=tk.NSEW)
        tk.Button(self.buttons_frame, text="=", bg="#A7C7E7", fg="#2C3E50", font=("Consolas", 22), borderwidth=0, command=self.evaluate).grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)
    
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()
    
    def append_operator(self, operator):
        self.total_expression += self.current_expression + operator
        self.current_expression = ""
        self.update_total_label()
    
    def clear(self):
        self.current_expression, self.total_expression = "", ""
        self.update_label(), self.update_total_label()
    
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()
    
    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()
    
    def evaluate(self):
        try:
            self.total_expression += self.current_expression
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except:
            self.current_expression = "Error"
        finally:
            self.update_label()
    
    def update_total_label(self):
        self.total_label.config(text=self.total_expression)
    
    def update_label(self):
        self.label.config(text=self.current_expression[:11])
    
    def run(self):
        self.window.mainloop()
        
if __name__ == "__main__":
    Calculator().run()