def Aula1():
    print("Ola mundo \n Quebra de linha "),
    print("Olá", "Mundo", "oi", sep="-")
    print("Olá", "Mundo", "oi", sep="\n")

    pais = "Italia"
    type(pais)
    qtd = 4
    type(qtd)
    print(pais, "tem ", qtd, "estados")

    print("R$ {:.2f}".format(1.989085))
    print("R$ {:08.2f}".format(1.989085))

    print("R$ {:2d}/{:2d}".format(19, 11))
