import tkinter as tk
from tkinter import messagebox, ttk

def bemvindo():
    # .get() serve para pegar o valor digitado no campo de entrada
    nome_usuario = usuario_nome.get()
    idade_usuario = usuario_idade.get()

    if nome_usuario == "":
        messagebox.showwarning("Atenção", "Por favor, digite seu nome!")
    elif idade_usuario == "":
        messagebox.showwarning("Atenção", "Por favor, digite sua idade!")
    else:
        messagebox.showinfo("Bem-vindo", f"Olá, {nome_usuario}! Você tem {idade_usuario} anos e é do(a) {combo_nivel.get()}.")

# Janela
janela_bemvindo = tk.Tk()
janela_bemvindo.title("Saudações ao usuário")
janela_bemvindo.geometry("250x500")
janela_bemvindo.configure(bg="#464646")

def abrir_segunda_janela():
    segunda_janela = tk.Toplevel(janela_bemvindo)
    segunda_janela.title("Segunda Janela")
    segunda_janela.geometry("500x500")
    segunda_janela.configure(bg="#A0B2F3")

    lbl_segunda_janela = tk.Label(segunda_janela, text="Bem vindo à segunda janela!", font=("Arial", 16), bg="#A0B2F3")
    lbl_segunda_janela.grid(row=0, column=0, padx=10, pady=10)

# Widgets
lbl_mensagem_usuario = tk.Label(janela_bemvindo, text="Digite seu nome:", font=("Arial", 14), bg="#C0C0C0")  # O "bg" é para mudar a cor de fundo do rótulo
lbl_mensagem_usuario.grid(row=0, column=0, padx=10, pady=10)

# Entrys
usuario_nome = tk.Entry(janela_bemvindo, font=("Arial", 14))
usuario_nome.grid(row=1, column=0, padx=10, pady=10)

# Componentes de ComboBox
lbl_mensagem_país = tk.Label(janela_bemvindo, text="Selecione seu país:", font=("Arial", 14), bg="#C0C0C0")
lbl_mensagem_país.grid(row=2, column=0, padx=10, pady=10)
combo_nivel = tk.ttk.Combobox(janela_bemvindo, values=["Brasil", "Marrocos", "Egito", "Escócia", "Agartha"], width=30)
combo_nivel.grid(row=3, column=0, pady=10, padx=10)


# Idade
lbl_mensagem_idade = tk.Label(janela_bemvindo, text="Digite sua idade:", font=("Arial", 14), bg="#C0C0C0")
lbl_mensagem_idade.grid(row=4, column=0, padx=10, pady=10)

# Entrys
usuario_idade = tk.Entry(janela_bemvindo, font=("Arial", 14))
usuario_idade.grid(row=5, column=0, padx=10, pady=10)

# Botão
btn_enviar_mensagem = tk.Button(janela_bemvindo, text="Enviar Mensagem", font=("Arial", 14), bg="#A0B2F3", fg="white", command=bemvindo)
# o "fg" é para mudar a cor da fonte do texto do botão
btn_enviar_mensagem.grid(row=6, column=0, padx=10, pady=10)

btn_segunda_janela = tk.Button(janela_bemvindo, text="Abrir Segunda Janela", command=abrir_segunda_janela)
btn_segunda_janela.grid(row=7, column=0, pady=10, padx=10)

# Fechar aplicativo
btn_fechar_aplicativo = tk.Button(janela_bemvindo, text="Fechar Aplicativo", font=("Arial", 14), bg="#CF23B3", fg="white", command=janela_bemvindo.destroy)
btn_fechar_aplicativo.grid(row=8, column=0, padx=10, pady=10)

# Rodar interface
janela_bemvindo.mainloop()
