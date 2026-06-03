# Projeto de Revisão: Sistema de Empréstimo "Biblioteca Digital"
# Contexto: Você foi contratado para desenvolver o módulo de validação de
# empréstimos de livros de uma biblioteca comunitária. O sistema precisa coletar os dados
# do usuário, do livro e decidir se o empréstimo será aprovado, negado ou se haverá
# cobrança de taxa de segurança.
# Regras de Negócio (O que o sistema deve fazer):
# 1. Classificação do Usuário: A biblioteca atende [1] Alunos e [2] Comunidade
# Geral.
# 2. Limite de Dias: * Alunos podem ficar com o livro por até 14 dias de graça.
# ○ A Comunidade Geral pode ficar por até 7 dias de graça.
# 3. Taxa de Renovação: Se o usuário quiser ficar mais tempo do que o limite do seu
# perfil, será cobrada uma taxa fixa de R$ 5,00 por dia adicional.
# 4. Restrição de Categoria: Livros da categoria "Raros" não podem ser emprestados
# para a Comunidade Geral, apenas para Alunos.

import tkinter as tk
from tkinter import messagebox, ttk

def bemvindo():
    # .get() serve para pegar o valor digitado no campo de entrada
    nome_usuario = usuario_nome.get()
    quantidade_dias = usuario_dias.get()

    if combo_tipo_usuario.get() == "Aluno":
        if int(quantidade_dias) <= 14:
            messagebox.showinfo("Empréstimo", f"Empréstimo Aprovado! Você ficará com o livro por {quantidade_dias} dias. Será cobrada uma taxa de R$ 5 por dia adicional. Aproveite a leitura, {nome_usuario}!")
        else:
            messagebox.showinfo("Empréstimo", f"Empréstimo Recusado! Você excedeu o limite de dias para o seu tipo de usuário.")

    if combo_tipo_usuario.get() == "Comunidade Geral":
        if int(quantidade_dias) <= 7:
            messagebox.showinfo("Empréstimo", f"Empréstimo Aprovado! Você ficará com o livro por {quantidade_dias} dias. Será cobrada uma taxa de R$ 5 por dia adicional. Aproveite a leitura, {nome_usuario}!")
        else:
            messagebox.showinfo("Empréstimo", f"Empréstimo Recusado! Você excedeu o limite de dias para o seu tipo de usuário.")

    if nome_usuario == "":
        messagebox.showwarning("Atenção", "Por favor, digite seu nome!")
    elif quantidade_dias == "":
        messagebox.showwarning("Atenção", "Por favor, digite a quantidade de dias!")
    elif combo_tipo_usuario.get() == "":
        messagebox.showwarning("Atenção", "Por favor, selecione seu tipo de usuário!")
janela_biblioteca = tk.Tk()
janela_biblioteca.title("Biblioteca Digital")
messagebox.showinfo("Bem-vindo", "Bem-vindo à Biblioteca Digital! \nPor favor, preencha os campos para solicitar um empréstimo (Selecione Aluno caso for um aluno ou Comunidade Geral caso for um membro da comunidade geral).")
janela_biblioteca.geometry("500x500")
janela_biblioteca.configure(bg="#464646")

lbl_janela_biblioteca = tk.Label(janela_biblioteca, text="Bem-vindo à Biblioteca Digital!", font=("Arial", 14, "bold"), bg="#464646", fg="white")
lbl_janela_biblioteca.grid(row=0, column=0, padx=10, pady=10)

lbl_mensagem_usuario = tk.Label(janela_biblioteca, text="Digite seu nome completo:", font=("Arial", 14), bg="#C0C0C0")  
lbl_mensagem_usuario.grid(row=1, column=0, padx=10, pady=10)
lbl_mensagem_dias = tk.Label(janela_biblioteca, text="Digite a quantidade de dias para empréstimo:", font=("Arial", 14), bg="#C0C0C0")
lbl_mensagem_dias.grid(row=7, column=0, padx=10, pady=10)

usuario_nome = tk.Entry(janela_biblioteca, font=("Arial", 14))
usuario_nome.grid(row=2, column=0, padx=10, pady=10)
usuario_dias = tk.Entry(janela_biblioteca, font=("Arial", 14))
usuario_dias.grid(row=8, column=0, padx=10, pady=10)

lbl_mensagem_tipo_usuario = tk.Label(janela_biblioteca, text="Selecione seu tipo de usuário:", font=("Arial", 14), bg="#C0C0C0")
lbl_mensagem_tipo_usuario.grid(row=3, column=0, padx=10, pady=10)
combo_tipo_usuario = tk.ttk.Combobox(janela_biblioteca, values=["Aluno", "Comunidade Geral"], width=30)
combo_tipo_usuario.grid(row=4, column=0, pady=10, padx=10)

def Aluno():
    lbl_mensagem_livro = tk.Label(janela_biblioteca, text="Selecione seu livro", font=("Arial", 14), bg="#C0C0C0")
    lbl_mensagem_livro.grid(row=5, column=0, padx=10, pady=10)
    combo_livro = tk.ttk.Combobox(janela_biblioteca, values=["Harry Potter", "Senhor dos Anéis", "Duna", "O Hobbit", "Don Quixote", "Alice no País das Maravilhas", "Livro Raro", "Livro Raro 2", "Livro Raro 3", "Livro Raro 4", "Outro"], width=30)
    combo_livro.grid(row=6, column=0, pady=10, padx=10)
def Comunidade_Geral():
    lbl_mensagem_livro = tk.Label(janela_biblioteca, text="Selecione seu livro", font=("Arial", 14), bg="#C0C0C0")
    lbl_mensagem_livro.grid(row=5, column=0, padx=10, pady=10)
    combo_livro = tk.ttk.Combobox(janela_biblioteca, values=["Harry Potter", "Senhor dos Anéis", "Duna", "O Hobbit", "Don Quixote", "Alice no País das Maravilhas", "Outro"], width=30)
    combo_livro.grid(row=6, column=0, pady=10, padx=10)
combo_tipo_usuario.bind("<<ComboboxSelected>>", lambda event: Aluno() if combo_tipo_usuario.get() == "Aluno" else Comunidade_Geral())

btn_enviar_mensagem = tk.Button(janela_biblioteca, text="Validar Empréstimo", font=("Arial", 14), bg="#A0B2F3", fg="white", command=bemvindo)
btn_enviar_mensagem.grid(row=10, column=0, padx=10, pady=10)

janela_biblioteca.mainloop()
