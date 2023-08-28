import random

Random_Number = round(random.random() * 100)

print("Adivinhe o numero")

print("Selecione a dificuldade")
print("1 : Facil")
print("2 : Medio")
print("3 : Dificil")

Dificuldade_Jogo = int(input())

if (Dificuldade_Jogo == 1):
    Numero_Tentativas = 10
elif (Dificuldade_Jogo == 2):
    Numero_Tentativas = 5
else:
    Numero_Tentativas = 3

print("\n" * 130)
Play_Game = "S"

while (Play_Game == "S"):
    Tentativa = 0
    while (Numero_Tentativas > 0):
        Tentativa = Tentativa + 1
        print("Tentativa :", Tentativa)
        print("Digite um numero de 1 a 100 e acerte !!!")
        Numero_Entrada = int(input())

        print("\n" * 130)
        if (Numero_Entrada == Random_Number):
            print("Voce acertou 0 Numero que é :", Random_Number)
            break
        if (Numero_Entrada < Random_Number):
            print("O Numero é Maior")
        else:
            print("O Numero é Menor")

        Numero_Tentativas = Numero_Tentativas - 1

    print("Deseja jogar novamente ? S/N")
    Play_Game = input("")
