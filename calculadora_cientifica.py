import tkinter as tk
import math
import re

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.configure(bg="#2d2d2d")  # Fundo escuro para um tema mais moderno
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Criação da tela de exibição
        display = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 24, "bold"), 
                           bd=15, relief="flat", justify="right", bg="#1e1e1e", fg="white")
        display.grid(row=0, column=0, columnspan=6, sticky="nsew", padx=10, pady=10)

        # Ajuste das linhas e colunas para redimensionamento
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(6):
            self.root.grid_columnconfigure(i, weight=1)

        # Definição dos botões
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('√', 1, 4), ('^', 1, 5),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4), (')', 2, 5),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('log', 3, 4), ('ln', 3, 5),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('exp', 4, 3), ('π', 4, 4), ('e', 4, 5),
            ('C', 5, 0), ('=', 5, 1), ('tan', 5, 2), ('cos', 5, 3), ('sin', 5, 4), ('%', 5, 5)
        ]

        # Cores personalizadas para os botões
        button_bg_color = "#3e3e3e"
        button_fg_color = "white"
        special_button_color = "#ff5722"

        # Criação dos botões
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 16, "bold"), 
                               bg=button_bg_color if text not in ['=', 'C'] else special_button_color, 
                               fg=button_fg_color, relief="flat", 
                               activebackground="#5e5e5e", activeforeground="white", 
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    def on_button_click(self, text):
        if text == 'C':
            self.result_var.set('')
        elif text == '=':
            try:
                expression = self.result_var.get()
                expression = self.replace_functions(expression)
                result = eval(expression)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set('Erro')
        else:
            current_text = self.result_var.get()
            new_text = current_text + text
            self.result_var.set(new_text)

    def replace_functions(self, expression):
        # Substituindo as funções por operações matemáticas seguras
        expression = expression.replace('√', 'math.sqrt')
        expression = expression.replace('^', '**')
        expression = expression.replace('log', 'math.log10')
        expression = expression.replace('ln', 'math.log')
        expression = expression.replace('exp', 'math.exp')
        expression = expression.replace('tan', 'math.tan')
        expression = expression.replace('cos', 'math.cos')
        expression = expression.replace('sin', 'math.sin')
        expression = expression.replace('π', 'math.pi')
        expression = expression.replace('e', 'math.e')
        return expression

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x500")  # Ajuste de tamanho da janela
    calc = ScientificCalculator(root)
    root.mainloop()
