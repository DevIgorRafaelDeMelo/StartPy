numero_secreto = 23

print("Acerto o numero")

numero = input("Digite um numero ")

print("Voce digitou :", numero)

if (numero_secreto == int(numero)):
    print("Acertou")
else:
    if (int(numero) > numero_secreto):
        print("Voce errou o seu chute foi maior que o numero secreto")
    else:
        print("Voce errou o seu chute foi menor que o numero secreto")

print("Fim de jogo !!!")
