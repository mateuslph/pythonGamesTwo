def jogar_adivinhacao():

    import random

    print("******************************")
    print("bem vindo ao jogo adivinhação!")
    print("******************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) nivel facil (2) médio (3) difícil")

    nivel = int(input("Defina o nível: "))
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digited o seu número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100 !!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Você errou, o seu chute foi maior do que seu nuemro secreto")
            elif (menor):
                print("Você errou, o seu chute foi menor do que o numero secreto")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
    print("Fim de Jogo!!")


    # print("\n")
    # nome = "Nico"
    # sobrenome = "Steppat"
    # print(nome, sobrenome, sep="")

    # print("R$ {}".format(1.59)) #interpolcao de strings com uso das chaves e function ".format()"
    # print("R$ {}".format(1.5902))
    # print("R$ {:f}".format(1.5902))
    # print("R$ {:.2f}".format(1.5902))
    # print("R$ {:7.2f}".format(1.5902))
    # print("R$ {:07.2f}".format(1.5902))
    # print("digito {:07d}".format(4))
    # print("data: {:02d}/{:02d}".format(9,11))
if (__name__ == "__main__"):
    jogar_adivinhacao()