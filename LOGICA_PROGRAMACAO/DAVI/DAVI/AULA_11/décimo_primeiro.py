# Interface Gráfica com Tkinter

# O que é o Tkinter?
# O Tkinter é uma biblioteca de interface gráfica para Python que permite criar aplicativos com janelas, botões, rótulos e outros elementos visuais. Ele é uma das bibliotecas mais populares para desenvolvimento de interfaces gráficas em Python devido à sua simplicidade e facilidade de uso.

# Fundamentos do Tkinter:
# - Widgets: são os elementos visuais que compõem a interface gráfica, como botões, rótulos, campos de entrada, etc.
# - Layout: é a forma como os widgets são organizados na janela. O Tkinter oferece diferentes gerenciadores de layout, como pack, grid e place, para posicionar os widgets de maneira eficiente.
# - Eventos: são ações que ocorrem na interface gráfica, como cliques de mouse, pressionamento de teclas, etc. O Tkinter permite associar funções a esses eventos para criar interatividade na aplicação.
# - Loop principal: é o processo que mantém a janela aberta e responde a eventos. O método mainloop() é usado para iniciar esse loop.

# O que é callback?
# Callback é uma função que é passada como argumento para outra função e é chamada (ou "chamada de volta") em um momento específico, geralmente em resposta a um evento. No contexto do Tkinter, as funções de callback são usadas para definir o comportamento dos widgets quando eventos ocorrem, como cliques de botão ou entrada de texto. Por exemplo, quando um botão é clicado, a função de callback associada a esse evento é executada para realizar uma ação específica.

# Os componentes principais (widgets) do Tkinter são:
# - Tk - a classe principal que representa a janela principal da aplicação.
# - Label: para exibir texto ou imagens.
# - Button: para criar botões clicáveis.
# - Entry: para criar campos de entrada de texto.
# - Frame: para organizar outros widgets em uma estrutura hierárquica.

# Para criar uma interface gráfica com Tkinter, é necessário seguir os seguintes passos:
# 1. Importar a biblioteca Tkinter.
# 2. Criar uma janela principal (root).
# 3. Adicionar os widgets desejados à janela.
# 4. Iniciar o loop principal da interface gráfica para exibir a janela e responder a eventos.

# 0. Importar a biblioteca Tkinter
import tkinter as tk
from tkinter import messagebox

# 1. Criar a janela principal
janela = tk.Tk()
janela.title("Minha Primeira Janela em GUI")
janela.geometry("400x400")
janela.configure(bg="#aaecee")
# 2. Criar a função para o botão
def mostrar_mensagem():
    messagebox.showinfo("Sucesso", "Você clicou no botão! :) ")
# 3. Criar os componentes (widgets)
lbl_titulo_pagina = tk.Label(janela, text="Bem-vindo a aula de Interface Gráfica em Python!", font=("Arial", 14, "bold"))
btn_clique_ativar = tk.Button(janela, text="Clique aqui :)", font=("Arial", 14), bg="#a0baf3", fg="white", command=mostrar_mensagem)
btn_clicar_fechar = tk.Button(janela, text="Fechar aplicativo", command=janela.destroy)
lbl_titulo_pagina.grid(row=0, column=0, padx=10, pady=10)
btn_clique_ativar.grid(row=1, column=1, padx=15, pady=15)
btn_clicar_fechar.grid(row=2, column=1, padx=10, pady=10)
# 4. Posicionar os widgets na janela
# 5. Rodar interface gráfica
janela.mainloop()

# Como colocar uma imagem no background da janela?
# Para colocar uma imagem como plano de fundo (background) em uma janela do Tkinter, você pode usar o widget Canvas para desenhar a imagem na janela. Aqui está um exemplo de como fazer isso:
# 1. Importar a biblioteca Tkinter e PIL (Pillow) para manipulação de imagens
# 2. Criar a janela principal
# 3. Carregar a imagem usando PIL
# 4. Criar um widget Canvas e desenhar a imagem nele
# 5. Iniciar o loop principal da interface gráfica
