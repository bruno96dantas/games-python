import random


def jogar():
    print("****************************************")
    print("*** Bem vindo ao jogo de Adivinhação ***")
    print("****************************************\n")
    print("*** Regras do Jogo ***")
    print("Vôce precisa adivinhar qual o valor no número secreto, que está entre 1 à 100.\n")

    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))

        chute_str = input("Digite o valor do seu chute:")
        print("Você chutou: ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        # Condições
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Parabéns! Você acertou!!")
            break
        else:
            if maior:
                print("O seu chute foi maior do que o número secreto!")
            elif menor:
                print("O seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim de jogo!")


if __name__ == "__main__":
    jogar()
