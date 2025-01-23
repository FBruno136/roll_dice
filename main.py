import tkinter as tk
from tkinter import ttk
from helpers.roll_dice import roll_dice

def on_roll():
    dice_type = dice_selector.get()  # Obtém o tipo de dado selecionado
    result = roll_dice(dice_type)    # Rola o dado
    result_label.config(text=f"Resultado: {result}")  # Atualiza o resultado
    history_listbox.insert(0, f"{dice_type}: {result}")  # Adiciona ao histórico

# Inicializando a interface gráfica
root = tk.Tk()
root.title("Rolagem de Dados RPG")

# Menu para selecionar o dado
dice_selector = ttk.Combobox(root, values=["d4", "d6", "d8", "d10", "d20", "d100"])
dice_selector.set("Escolha um dado")
dice_selector.pack(pady=10)

# Botão para rolar o dado
roll_button = tk.Button(root, text="Rolar Dado", command=on_roll)
roll_button.pack(pady=10)

# Exibir o resultado
result_label = tk.Label(root, text="Resultado: -", font=("Helvetica", 14))
result_label.pack(pady=10)

# Histórico das rolagens
history_label = tk.Label(root, text="Histórico de Rolagens:", font=("Helvetica", 12))
history_label.pack()
history_listbox = tk.Listbox(root, height=10, width=30)
history_listbox.pack(pady=10)

# Iniciar a interface
root.mainloop()
