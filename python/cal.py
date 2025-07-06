import tkinter as tk
from tkinter import ttk


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("400x500")
        self.window.resizable(False, False)
        self.expression = ""

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Consolas", 18), relief="flat")
        self.style.map("TButton", background=[("active", "#ffcc00")])

        self.create_display()
        self.create_buttons()

    def create_display(self):
        self.display = tk.Label(self.window, text="", anchor="e", font=("Consolas", 24), bg="#222", fg="white",
                                height=2, padx=10)
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")