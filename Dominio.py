# controla se o último clique foi "="
resultado_mostrado = False


# funções numéricos
def num_um(resposta):
    global resultado_mostrado
    if resultado_mostrado == True:
        resposta.configure(text="")
        resultado_mostrado = False
    resposta.configure(text=resposta.cget("text") + "1")

def num_dois(resposta):
    global resultado_mostrado
    if resultado_mostrado == True:
        resposta.configure(text="")
        resultado_mostrado = False
    resposta.configure(text=resposta.cget("text") + "2")

def num_tres(resposta):
    global resultado_mostrado
    if resultado_mostrado == True:
        resposta.configure(text="")
        resultado_mostrado = False
    resposta.configure(text=resposta.cget("text") + "3")

def num_quatro(resposta):
    global resultado_mostrado
    if resultado_mostrado == True:
        resposta.configure(text="")
        resultado_mostrado = False
    resposta.configure(text=resposta.cget("text") + "4")

def num_cinco(resposta):
    global resultado_mostrado
    if resultado_mostrado == True:
        resposta.configure(text="")
        resultado_mostrado = False
    resposta.configure(text=resposta.cget("text") + "5")

def num_seis(resposta):
    global resultado_mostrado
    if resultado_mostrado == True:
        resposta.configure(text="")
        resultado_mostrado = False
    resposta.configure(text=resposta.cget("text") + "6")

def num_sete(resposta):
    global resultado_mostrado
    if resultado_mostrado == True:
        resposta.configure(text="")
        resultado_mostrado = False
    resposta.configure(text=resposta.cget("text") + "7")

def num_oito(resposta):
    global resultado_mostrado
    if resultado_mostrado == True:
        resposta.configure(text="")
        resultado_mostrado = False
    resposta.configure(text=resposta.cget("text") + "8")

def num_nove(resposta):
    global resultado_mostrado
    if resultado_mostrado == True:
        resposta.configure(text="")
        resultado_mostrado = False
    resposta.configure(text=resposta.cget("text") + "9")

def num_zero(resposta):
    global resultado_mostrado
    if resultado_mostrado == True:
        resposta.configure(text="")
        resultado_mostrado = False
    resposta.configure(text=resposta.cget("text") + "0")


# funções de operadores
def ope_mais(resposta):
    resposta.configure(text=resposta.cget("text") + "+")

def ope_menos(resposta):
    resposta.configure(text=resposta.cget("text") + "-")

def ope_vezes(resposta):
    resposta.configure(text=resposta.cget("text") + "*")

def ope_dividir(resposta):
    resposta.configure(text=resposta.cget("text") + "/")

def calcular(resposta):
    global resultado_mostrado
    try:
        expressao = resposta.cget("text")
        resultado = eval(expressao)
        resposta.configure(text=str(resultado))
        resultado_mostrado = True
    except:
        resposta.configure(text="ERRO!")
        resultado_mostrado = True

def backspace(resposta):
    global resultado_mostrado
    try:
        texto_atual = resposta.cget("text")
        resposta.configure(text=texto_atual[:-1])
    except:
        resposta.configure(text="ERRO!")
        resultado_mostrado = True

