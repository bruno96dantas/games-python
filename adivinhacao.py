print("*** Bem vindo ao jogo de Adivinhação ***")
print("*** Regras do Jogo ***")
print("Vôce precisa adivinhar qual o valor no número secreto, que está entre 0 e 100.")

numero_secreto = 42

chute_str = input("Digite o valor do seu chute:")
print("Você chutou: ", chute_str)
chute = int(chute_str)

# Condições
acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto


if (acertou):
    print("Parabéns! Você acertou!!")
else:
    if (maior):
        print("O seu chute foi maior do que o número secreto!")
    elif(menor):
        print("O seu chute foi menor do que o número secreto!")

print("Fim de jogo!")
