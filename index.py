import random
import os
erros = 0
sorteado = random.randrange(0,100)
jogador = int(input("Digite seu número: "))

while(sorteado != jogador):
    os.system('cls')
    if(sorteado > jogador):
        print("ERRO, o número e maior")
    elif(sorteado < jogador):
        print("ERRO, o número e menor")
    erros+=1
    jogador = int(input("Digite seu número: "))
print("Número " + str(jogador) + ", você acertou em " + str(erros+1) + " tentativas")