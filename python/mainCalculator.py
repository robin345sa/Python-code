import tkinter as tk
class calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("400x500")

        self.window.resizable(False,False)
        self.expression =""
        self.create_buttons()
    def create_display(self):
        self.create_display = tk.Label(self.window,text="",anchor="e",font=("consolas",24),bg="#1e1e13", fg="white",height=2)

        self.display.grid(row=0, column=0, colorama=10,sticky="nsew")

    def create_buttons(self):
        button_colors = {
                'C': "#ff3b3b", '⌫': "#ff9f0a", '√': "#007aff", '/': "#ff9500",
                '*': "#ff9500", '-': "#ff9500", '+': "#ff9500", '=': "#34c759",
                '.': "#a6a6a6", '0': "#333333", '1': "#333333", '2': "#333333",
                '3': "#333333", '4': "#333333", '5': "#333333", '6': "#333333",
                '7': "#333333", '8': "#333333", '9': "#333333"
            }

        buttons=[
             ('c','1',0),('+','1',1),('✓','1',0),('c','1',0),
            ('7', '2', 0),('8','2',1),('9','2',0),('c','2',0),
            ('4', '3', 0),('5','3',1),('6','3',0),('c','3',0),
            ('1', '4', 0),('2','4',1),('3','4',0),('c','4',0),
            ('0', '5', 0),('.','5',1),('=','5',2,2),('c','5',0),
            ]
        for button in buttons:
            text, row, col = button[:3]
            colspan = button[3] if len(button) == 4 else 1

            btn = tk.Button(self.window, text=text, font=("Consolas", 18), bg=button_color, fg="white",
                            activebackground="#d1d1d1", relief="ridge", borderwidth=2)
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)

        for i in range(6):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '⌫':
            self.expression = self.expression[:-1]
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        elif char == '√':
            self.expression = str(eval(f"{self.expression}**0.5"))
        else:
            self.expression += char
        self.display.config(text=self.expression)

    def run(self):
        self.window.mainloop()

calculator().run()