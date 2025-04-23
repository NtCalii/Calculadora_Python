import customtkinter as ctk # importando biblioteca
from Dominio import * # importando arquivo Dominio

# criando janela principal
janela = ctk.CTk()
janela.title("Calculadora Python")
janela.geometry("215x255")
janela.resizable(width=False, height=False)


# tela de resposta
resposta = ctk.CTkLabel(janela, text="", font=("arial bold", 28))
resposta.grid(row=0, column=0, pady=4, columnspan=4, sticky="e")


# criando botões numéricos
btn1 = ctk.CTkButton(janela, text="1", width=50, height=50, command=lambda: num_um(resposta))
btn1.grid(row=1, column=0, padx=2)

btn2 = ctk.CTkButton(janela, text="2", width=50, height=50, command=lambda: num_dois(resposta))
btn2.grid(row=1, column=1, padx=2)

btn3 = ctk.CTkButton(janela, text="3", width=50, height=50, command=lambda: num_tres(resposta))
btn3.grid(row=1, column=2, padx=2)

btn4 = ctk.CTkButton(janela, text="4", width=50, height=50, command=lambda: num_quatro(resposta))
btn4.grid(row=2, column=0, padx=2, pady=4)

btn5 = ctk.CTkButton(janela, text="5", width=50, height=50, command=lambda: num_cinco(resposta))
btn5.grid(row=2, column=1, padx=2, pady=4)

btn6 = ctk.CTkButton(janela, text="6", width=50, height=50, command=lambda: num_seis(resposta))
btn6.grid(row=2, column=2, padx=2, pady=4)

btn7 = ctk.CTkButton(janela, text="7", width=50, height=50, command=lambda: num_sete(resposta))
btn7.grid(row=3, column=0, padx=2)

btn8 = ctk.CTkButton(janela, text="8", width=50, height=50, command=lambda: num_oito(resposta))
btn8.grid(row=3, column=1, padx=2)

btn9 = ctk.CTkButton(janela, text="9", width=50, height=50, command=lambda: num_nove(resposta))
btn9.grid(row=3, column=2, padx=2)

btn0 = ctk.CTkButton(janela, text="0", width=50, height=50, command=lambda: num_zero(resposta))
btn0.grid(row=4, column=0, padx=2, pady=4)


# criando botões de operadores
btn_mais = ctk.CTkButton(janela, text="+", width=50, height=50, command=lambda: ope_mais(resposta))
btn_mais.grid(row=1, column=3, padx=2)

btn_menos = ctk.CTkButton(janela, text="-", width=50, height=50, command=lambda: ope_menos(resposta))
btn_menos.grid(row=2, column=3, padx=2)

btn_vezes = ctk.CTkButton(janela, text="X", width=50, height=50, command=lambda: ope_vezes(resposta))
btn_vezes.grid(row=3, column=3, padx=2)

btn_dividir = ctk.CTkButton(janela, text="/", width=50, height=50, command=lambda: ope_dividir(resposta))
btn_dividir.grid(row=4, column=3, padx=2)

btn_igual = ctk.CTkButton(janela, text="=", width=50, height=50, command=lambda: calcular(resposta))
btn_igual.grid(row=4, column=2, padx=2, pady=4)

btn_backspace = ctk.CTkButton(janela, text="←", width=50, height=50, command=lambda: backspace(resposta))
btn_backspace.grid(row=4, column=1, padx=2)


janela.mainloop() # inicializando janela
