import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("600x600")
        self.expression = ""

        # Farben
        self.bg_color = "#2E2E2E"  # Hintergrund
        self.btn_color = "#4C4C4C"  # Standardfarbe der Tasten
        self.btn_hover_color = "#6E6E6E"  # Hover-Farbe der Tasten
        self.display_color = "#1C1C1C"  # Farbe des Displays
        self.text_color = "#FFFFFF"  # Textfarbe

        # Hintergrundfarbe setzen
        self.root.configure(bg=self.bg_color)

        # Gewichtung für flexible Anpassung
        for i in range(7):  # Für Zeilen
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(5):  # Für Spalten
            self.root.grid_columnconfigure(i, weight=1)

        # Display
        self.display = tk.Entry(root, font=("Arial", 24), bd=10, relief="flat", bg=self.display_color, fg=self.text_color, justify="right")
        self.display.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

        # Button Layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('⌫', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('(', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), (')', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3), ('√', 5, 4),
            ('π', 6, 0), ('e', 6, 1), ('^', 6, 2), ('%', 6, 3), ('exit', 6, 4),
        ]

        # Add buttons to the grid
        for (text, row, col) in buttons:
            self.add_button(text, row, col)

    def add_button(self, text, row, col):
        # Tasten erstellen
        button = tk.Button(
            self.root, text=text, font=("Arial", 16), bg=self.btn_color, fg=self.text_color,
            relief="flat", command=lambda t=text: self.on_button_click(t)
        )
        button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Hover-Effekte hinzufügen
        button.bind("<Enter>", lambda e, b=button: b.config(bg=self.btn_hover_color))
        button.bind("<Leave>", lambda e, b=button: b.config(bg=self.btn_color))

    def on_button_click(self, button_text):
        if button_text == "C":
            self.expression = ""
        elif button_text == "⌫":
            self.expression = self.expression[:-1]
        elif button_text == "=":
            try:
                # Safely evaluate the expression
                self.expression = str(eval(self.expression))
            except Exception as e:
                messagebox.showerror("Error", "Invalid input")
                self.expression = ""
        elif button_text == "exit":
            self.root.quit()
        elif button_text in ["sin", "cos", "tan", "log", "√", "π", "e"]:
            self.add_advanced_function(button_text)
        else:
            self.expression += button_text

        self.update_display()

    def add_advanced_function(self, func):
        try:
            if func == "sin":
                self.expression = str(math.sin(math.radians(float(self.expression))))
            elif func == "cos":
                self.expression = str(math.cos(math.radians(float(self.expression))))
            elif func == "tan":
                self.expression = str(math.tan(math.radians(float(self.expression))))
            elif func == "log":
                self.expression = str(math.log10(float(self.expression)))
            elif func == "√":
                self.expression = str(math.sqrt(float(self.expression)))
            elif func == "π":
                self.expression += str(math.pi)
            elif func == "e":
                self.expression += str(math.e)
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
