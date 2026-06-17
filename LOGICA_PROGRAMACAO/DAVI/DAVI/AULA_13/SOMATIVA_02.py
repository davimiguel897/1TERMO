# Registro de Operador
# import tkinter as tk
# from tkinter import messagebox

# def registrar_operador():
#     nome_operador = entry_nome.get()
#     turno_operador = entry_turno.get()

#     if nome_operador and turno_operador:
#         messagebox.showinfo("Registro de Operador", f"Operador {nome_operador} registrado no turno {turno_operador}. Boa jornada!")
#     else:
#         messagebox.showwarning("Erro", "Por favor, preencha ambos os campos.")
# # Configuração da janela
# janela = tk.Tk()
# janela.title("Registro de Operador")
# janela.geometry("300x200")
# # Widgets
# label_nome = tk.Label(janela, text="Nome do Operador:")
# label_nome.pack(pady=5)
# entry_nome = tk.Entry(janela)
# entry_nome.pack(pady=5)
# label_turno = tk.Label(janela, text="Turno do Operador (Manhã, Tarde ou Noite):")
# label_turno.pack(pady=5)
# entry_turno = tk.Entry(janela)
# entry_turno.pack(pady=5)
# button_registrar = tk.Button(janela, text="Registrar", command=registrar_operador)
# button_registrar.pack(pady=10)
# button_fechar = tk.Button(janela, text="Fechar", command=janela.destroy)
# button_fechar.pack(pady=10) 
# janela.mainloop()


# 2: Calculo de Produção

# import tkinter as tk
# from tkinter import messagebox

# def registrar_peças():
#     peças_hora = entry_hora.get()
#     peças_turno = float(peças_hora) * 8 if peças_hora.isdigit() else None

#     if peças_hora and peças_turno is not None:
#         messagebox.showinfo("Calculo de Produção", f"Produção registrada: {peças_hora} peças na hora, {peças_turno} peças no turno.")
#     else:
#         messagebox.showwarning("Erro", "Por favor, preencha ambos os campos.")
# # Configuração da janela
# janela = tk.Tk()
# janela.title("Calculo de Produção")
# janela.geometry("300x200")
# # Widgets
# label_hora = tk.Label(janela, text="Peças produzidas na hora:")
# label_hora.pack(pady=5)
# entry_hora = tk.Entry(janela)
# entry_hora.pack(pady=5)
# button_registrar = tk.Button(janela, text="Registrar", command=registrar_operador)
# button_registrar.pack(pady=10)
# janela.mainloop()


# Conversor de Unidade

# import tkinter as tk
# from tkinter import messagebox

# def registrar_conversor():
#     bar = entry_bar.get()
#     psi = float(bar) * 14.5 if bar.isdigit() else None

#     if bar and psi is not None:
#         messagebox.showinfo("Conversor de Unidade", f"Pressão em Bar: {bar}. Quantidade em PSI: {psi}.")
#     else:
#         messagebox.showwarning("Erro", "Por favor, preencha o campo corretamente.")
# # Configuração da janela
# janela = tk.Tk()
# janela.title("Conversor de Unidade")
# janela.geometry("300x200")
# # Widgets
# label_hora = tk.Label(janela, text="Pressão em Bar:")
# label_hora.pack(pady=5)
# entry_bar = tk.Entry(janela)
# entry_bar.pack(pady=5)
# button_registrar = tk.Button(janela, text="Converter", command=registrar_conversor)
# button_registrar.pack(pady=10)
# button_fechar = tk.Button(janela, text="Fechar", command=janela.destroy)
# button_fechar.pack(pady=10) 
# janela.mainloop()


# Média de Qualidade

# import tkinter as tk
# from tkinter import messagebox

# def inspeçao_peça():
#     peça_nota1 = int(entry_nota1.get())
#     peça_nota2 = int(entry_nota2.get())
#     peça_nota3 = int(entry_nota3.get())
#     peças_media = peça_nota1 + peça_nota2 + peça_nota3 / 3 if peça_nota1 and peça_nota2 and peça_nota3 else None

#     if peça_nota1 and peça_nota2 and peça_nota3 and peças_media is not None:
#         messagebox.showinfo("Calculo de Produção", f"Média das notas: {peças_media}")
#     else:
#         messagebox.showwarning("Erro", "Por favor, preencha ambos os campos.")
# # Configuração da janela
# janela = tk.Tk()
# janela.title("Calculo de Produção")
# janela.geometry("300x300")
# # Widgets
# label_nota1 = tk.Label(janela, text="Nota 1:")
# label_nota1.pack(pady=5)
# entry_nota1 = tk.Entry(janela)
# entry_nota1.pack(pady=5)
# label_nota2 = tk.Label(janela, text="Nota 2:")
# label_nota2.pack(pady=5)
# entry_nota2 = tk.Entry(janela)
# entry_nota2.pack(pady=5)
# label_nota3 = tk.Label(janela, text="Nota 3:")
# label_nota3.pack(pady=5)
# entry_nota3 = tk.Entry(janela)
# entry_nota3.pack(pady=5)
# button_registrar = tk.Button(janela, text="Registrar", command=inspeçao_peça)
# button_registrar.pack(pady=10)
# button_fechar = tk.Button(janela, text="Fechar", command=janela.destroy)
# button_fechar.pack(pady=10) 
# janela.mainloop()


# 5: Termostato Inteligente
 
# import tkinter as tk
# from tkinter import messagebox

# def temperatura():
#     temperatura_atual = int(entry_temperatura.get())
#     if temperatura_atual < 40:
#         messagebox.showinfo("Termostato Inteligente", f"Temperatura em baixa carga")
#     elif temperatura_atual >= 40 and temperatura_atual <= 70:
#         messagebox.showinfo("Termostato Inteligente", f"Temperatura normal")
#     elif temperatura_atual > 70:
#         messagebox.showwarning("Termostato Inteligente", f"ALERTA: Resfriamento Ativado!")

# janela = tk.Tk()
# janela.title("Termostato Inteligente")
# janela.geometry("300x300")

# label_temperatura = tk.Label(janela, text="Digite a temperatura atual do equipamento:")
# label_temperatura.pack(pady=5)
# entry_temperatura = tk.Entry(janela)
# entry_temperatura.pack(pady=5)
# button_verificar = tk.Button(janela, text="Verificar Temperatura", command=temperatura)
# button_verificar.pack(pady=10)
# button_fechar = tk.Button(janela, text="Fechar", command=janela.destroy)
# button_fechar.pack(pady=10) 
# janela.mainloop()



# 6: Classificador de Lotes

# import tkinter as tk
# from tkinter import messagebox
        
# messagebox.showinfo("Classificador de Lotes", f"Escolha entre os produtos: (A) para Alimentos, (E) para Eletrônicos ou outro valor para Desconhecido.")
# def classificar_lote():
#     produto = entry_produto.get()
#     if produto == "A":
#         messagebox.showinfo("Produto", "Seu produto é um alimento!")
#     elif produto == "E":
#         messagebox.showinfo("Produto", "Seu produto é um eletrônico!")
#     else:
#         messagebox.showinfo("Produto", "Seu produto é desconhecido.")

# janela = tk.Tk()
# janela.title("Classificador de Lotes")
# janela.geometry("300x300")

# label_produto = tk.Label(janela, text="Digite o código do produto (A, E ou outro):")
# label_produto.pack(pady=5)
# entry_produto = tk.Entry(janela)
# entry_produto.pack(pady=5)


# button_classificar = tk.Button(janela, text="Classificar lote", command=classificar_lote)
# button_classificar.pack(pady=10)
# button_fechar = tk.Button(janela, text="Fechar", command=janela.destroy)
# button_fechar.pack(pady=10) 
# janela.mainloop()


# 7: Segurança de Operação

# import tkinter as tk
# from tkinter import messagebox
        
# messagebox.showinfo("Operação", f"Para ligar a máquina, digite o código (fechada) para o sensor e (desligado) para o botão de emergência")
# def maquina():
#     sensor_porta = entry_sensor_porta.get()
#     botao_emergencia = entry_botao_emergencia.get()
#     if sensor_porta == "fechado" and botao_emergencia == "desligado":
#         messagebox.showinfo("Máquina", "A máquina foi ligada com sucesso!")
#     else:
#         messagebox.showwarning("Erro", "Digite o comando certo!")

# janela = tk.Tk()
# janela.title("Classificador de Lotes")
# janela.geometry("300x300")

# label_sensor_porta = tk.Label(janela, text="Digite o comando:")
# label_sensor_porta.pack(pady=5)
# entry_sensor_porta = tk.Entry(janela)
# entry_sensor_porta.pack(pady=5)

# label_botao_emergencia = tk.Label(janela, text="Digite o comando:")
# label_botao_emergencia.pack(pady=5)
# entry_botao_emergencia = tk.Entry(janela)
# entry_botao_emergencia.pack(pady=5)


# button_classificar = tk.Button(janela, text="Executar comando", command=maquina)
# button_classificar.pack(pady=10)
# button_fechar = tk.Button(janela, text="Fechar", command=janela.destroy)
# button_fechar.pack(pady=10) 
# janela.mainloop()



# 8: Cálculo de Descarte:

# import tkinter as tk
# from tkinter import messagebox

# def calcular_descarte():
#     total_pecas = int(entry_total_pecas.get())
#     pecas_defeituosas = int(entry_pecas_defeituosas.get())
#     taxa_descarte = (pecas_defeituosas / total_pecas) * 100 if total_pecas > 0 else None

#     if taxa_descarte is not None:
#         if taxa_descarte > 5:
#             messagebox.showwarning("Cálculo de Descarte", f"Revisar Processo! Taxa de descarte: {taxa_descarte}%")
#         else:
#             messagebox.showinfo("Cálculo de Descarte", f"Processo Otimizado! Taxa de descarte: {taxa_descarte}%")
#     else:
#         messagebox.showwarning("Erro", "Por favor, preencha ambos os campos corretamente.")
# # Configuração da janela
# janela = tk.Tk()
# janela.title("Cálculo de Descarte")
# janela.geometry("300x200")
# # Widgets

# label_total_pecas = tk.Label(janela, text="Total de peças produzidas:")
# label_total_pecas.pack(pady=5)
# entry_total_pecas = tk.Entry(janela)
# entry_total_pecas.pack(pady=5)
# label_pecas_defeituosas = tk.Label(janela, text="Total de peças defeituosas:")
# label_pecas_defeituosas.pack(pady=5)
# entry_pecas_defeituosas = tk.Entry(janela)
# entry_pecas_defeituosas.pack(pady=5)
# button_calcular = tk.Button(janela, text="Calcular Descarte", command=calcular_descarte)
# button_calcular.pack(pady=10)
# button_fechar = tk.Button(janela, text="Fechar", command=janela.destroy)
# button_fechar.pack(pady=10)
# janela.mainloop()

# 9: Validação de Medida

# import tkinter as tk
# from tkinter import messagebox


# def medida():
#     medida_peça = float(entry_medida_peça.get())
#     if medida_peça < 9.8:
#         messagebox.showwarning("Medida", "A peça está abaixo da tolerância")
#     elif medida_peça > 9.8 and medida_peça < 10.2:
#         messagebox.showinfo("Medida", "A peça está dentro da tolerância")
#     elif medida_peça > 10.2:
#         messagebox.showwarning("Medida", "A peça está acima da tolerância.")

# janela = tk.Tk()
# janela.title("Validação de Medida")
# janela.geometry("300x200")
# label_medida_peça = tk.Label(janela, text="Digite a medida da peça em mm:")
# label_medida_peça.pack(pady=5)
# entry_medida_peça = tk.Entry(janela)
# entry_medida_peça.pack(pady=5)
# button_verificar = tk.Button(janela, text="Verificar Medida", command=medida)
# button_verificar.pack(pady=10)
# button_fechar = tk.Button(janela, text="Fechar", command=janela.destroy)
# button_fechar.pack(pady=10)
# janela.mainloop()

# 10: Contagem Regressiva

# import tkinter as tk
# from tkinter import messagebox

# def contagem_regressiva():
#     tempo = 10
#     for i in range(tempo, -1, -1):
#         label_contagem.config(text=f"Prensa ativada em: {i} segundos")
#         janela.update()
#         janela.after(1000)
#     messagebox.showinfo("Contagem Regressiva", "Prensa Ativada!")

# janela = tk.Tk()
# janela.title("Contagem Regressiva")
# janela.geometry("300x200")
# label_tempo = tk.Label(janela, text="A prensa será ativada em 10 segundos")
# label_tempo.pack(pady=5)
# button_iniciar = tk.Button(janela, text="Iniciar Contagem", command=contagem_regressiva)
# button_iniciar.pack(pady=10)
# label_contagem = tk.Label(janela, text="")
# label_contagem.pack(pady=5)
# button_fechar = tk.Button(janela, text="Fechar", command=janela.destroy)
# button_fechar.pack(pady=10)
# janela.mainloop()    

# 11: Soma de Produção (Acumulador)

# import tkinter as tk
# from tkinter import messagebox

# messagebox.showinfo("Soma de Produção", "Digite o peso das caixas. Digite 0 para finalizar e ver o total acumulado.")
# def somar_peso():
#     peso_total == entry_peso_total.get()
#     while True:
#         peso = float(entry_peso.get())
#         if peso == 0:
#             messagebox.showinfo("Soma de Produção", f"Peso total acumulado: {peso_total} kg")
#             break
#         peso_total += peso
# janela = tk.Tk()
# janela.title("Soma de Produção")
# janela.geometry("300x200")
# label_peso = tk.Label(janela, text="Digite o peso da caixa em kg:")
# label_peso.pack(pady=5)
# entry_peso = tk.Entry(janela)
# entry_peso.pack(pady=5)
# button_somar = tk.Button(janela, text="Adicionar Peso", command=somar_peso)
# entry_peso_total = tk.Label(janela)
# button_somar.pack(pady=10)
# button_fechar = tk.Button(janela, text="Fechar", command=janela.destroy)
# button_fechar.pack(pady=10)
# janela.mainloop()



# 13: Painel de Login

# import tkinter as tk
# from tkinter import messagebox

# def verificar_senha():
#     senha = entry_senha.get()
#     tentativas = 3
#     while tentativas > 0:
#         if senha == "admin123":
#             messagebox.showinfo("Login", "Acesso Permitido!")
#             return
#         else:
#             tentativas -= 1
#             messagebox.showwarning("Login", f"Acesso Negado! Tentativas restantes: {tentativas}")
#             if tentativas == 0:
#                 messagebox.showerror("Login", "Painel Bloqueado!")
#                 janela.destroy()
#             break
# janela = tk.Tk()
# janela.title("Painel de Login")
# janela.geometry("300x200")
# label_senha = tk.Label(janela, text="Digite a senha do supervisor:")
# label_senha.pack(pady=5)
# entry_senha = tk.Entry(janela)
# entry_senha.pack(pady=5)
# button_verificar = tk.Button(janela, text="Verificar Senha", command=verificar_senha)
# button_verificar.pack(pady=10)
# button_fechar = tk.Button(janela, text="Fechar", command=janela.destroy)
# button_fechar.pack(pady=10)
# janela.mainloop()


# 15: Relatório de Turno Completo

# import tkinter as tk
# from tkinter import messagebox

# TOTAL_PECAS = 5
# pecas_aprovadas = 0
# pecas_rejeitadas = 0
# peca_atual = 1


# def verificar_peca():
#     global pecas_aprovadas, pecas_rejeitadas, peca_atual

#     try:
#         diametro = float(entry_diametro.get())
#     except ValueError:
#         messagebox.showerror("Erro", "Digite um valor numérico válido para o diâmetro.")
#         return

#     if 19.9 <= diametro <= 20.1:
#         pecas_aprovadas += 1
#         messagebox.showinfo("Peça Aprovada", f"Peça {peca_atual} aprovada! Diâmetro: {diametro} mm")
#     else:
#         pecas_rejeitadas += 1
#         messagebox.showwarning("Peça Reprovada", f"Peça {peca_atual} reprovada! Diâmetro: {diametro} mm")

#     peca_atual += 1
#     entry_diametro.delete(0, tk.END)

#     if peca_atual > TOTAL_PECAS:
#         eficiencia = (pecas_aprovadas / TOTAL_PECAS) * 100
#         messagebox.showinfo(
#             "Relatório de Turno",
#             f"Total de peças aprovadas: {pecas_aprovadas}\n"
#             f"Peças rejeitadas: {pecas_rejeitadas}\n"
#             f"Eficiência do lote: {eficiencia:.2f}%"
#         )
#         button_verificar.config(state=tk.DISABLED)
#         label_status.config(text="Relatório finalizado.")
#     else:
#         label_status.config(text=f"Digitando peça {peca_atual} de {TOTAL_PECAS}")


# janela = tk.Tk()
# janela.title("Relatório de Turno Completo")
# janela.geometry("320x220")
# label_diametro = tk.Label(janela, text="Digite o diâmetro da peça em mm:")
# label_diametro.pack(pady=5)
# entry_diametro = tk.Entry(janela)
# entry_diametro.pack(pady=5)
# button_verificar = tk.Button(janela, text="Verificar Peça", command=verificar_peca)
# button_verificar.pack(pady=10)
# label_status = tk.Label(janela, text=f"Digitando peça {peca_atual} de {TOTAL_PECAS}")
# label_status.pack(pady=5)
# button_fechar = tk.Button(janela, text="Fechar", command=janela.destroy)
# button_fechar.pack(pady=10)
# janela.mainloop()
