def Aula2():
    numero_secreto = 23

    print("Acerto o numero")
    numero = input("Digite um numero")
    print("Voce digitou :", numero)
    if (numero_secreto == int(numero)):
        print("Acertou")
    else:
        print("Errou")

    print("Fim de jogo !!!")
