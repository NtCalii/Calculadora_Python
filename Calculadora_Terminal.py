# Calculadora feita no terminal

# função para limpar a tela, de forma gambiarra
def limpatela():
    print("\n" * 10)

# deixa o programa ativo
while True:
    # para pegar explicar como funciona e pegar o input
    print("+ para adição, - para subtração, * para vezes, / para divisão, ( ) para preferência.\n"
          "Exemplo: 23*3+(10/4)-7\n"
          "Digite a conta matématica que você quer fazer: ", end="")
    conta = input()

    # para calcular
    try:
        print(eval(conta))
    except:
        print("ERRO!")

    # verificar se o usuário quer continuar
    continuar = input("Deseja continuar [S/N]: ").upper().strip()
    while continuar not in "SN":
        print("Por favor, digite 'S' para Sim ou 'N' para Não.")
        continuar = input("Deseja continuar [S/N]: ").upper().strip()

    # limpa a tela do terminal
    limpatela()

    # para encerrar o programa
    if continuar == "N":
        print("Programa encerrado!")
        break
# FIM
