import random

numero_secreto = round(random.random() * 100)
tentatival_total = 1

while (tentatival_total < 4):
    print("Acerte o numero")
    print("Voce está na sua {} tentativa".format(tentatival_total))
    print("Tentativa", tentatival_total)
    numero = input("Digite um numero de 1 a 100")
    print("Voce digitou :", numero)

    if (int(numero) < 1 or int(numero) > 100):
        print("Numero de ve ser entre 1 e 100 ")
        continue
    if (numero_secreto == int(numero)):
        print("Acertou")
        break

    else:
        if (int(numero) > numero_secreto):
            print("Voce errou o seu chute foi maior que o numero secreto")
        else:
            print("Voce errou o seu chute foi menor que o numero secreto")

    tentatival_total = tentatival_total + 1

print("{1} de {0} !!!".format("jogo", "fim"))
