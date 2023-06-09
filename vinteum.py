import random
jogador1 = random.randint(1,4)
bot = random.randint(1,4)
botf = bot
cartas = 0
roleta = 0
parar = False
pararj = False
jogada = ""
while True:
    if pararj == False:
        if jogador1 > 21:
            break
        print(f"Você tem {jogador1} pontos")
        if cartas == 0:
            print(f"Seu adversário tem {botf} pontos\n")
        else:
            if cartas == 1:
                print(f"Seu adversário tem {botf} pontos, com {cartas} carta secreta\n")
            else:
                print(f"Seu adversário tem {botf} pontos, com {cartas} cartas secretas\n")
        jogada = input("Comprar mais (s/n)?")
    else:
        print(f"Seu adversário tem {botf} pontos, com {cartas} cartas secretas\n")
    if jogada.lower() == "n":
        pararj = True
    elif jogada.lower() == "s":
        jogador1 += random.randint(1,4)
    else:
        print("Comando inválido")
    if bot < 18:
        bot += random.randint(1,4)
        cartas += 1
    elif bot == 18 and parar == False:
        roleta = random.randint(1,3)
        if str(roleta) in "12":
            bot += random.randint(1, 4)
            cartas += 1
        else:
            parar = True
    elif bot == 19 and parar == False:
        roleta = random.randint(1,4)
        if str(roleta) in "1":
            bot += random.randint(1, 4)
            cartas += 1
        else:
            parar = True
    elif bot == 20 and parar == False:
        roleta = random.randint(1,7)
        if str(roleta) in "1":
            bot += random.randint(1, 4)
            cartas += 1
        parar = True
    elif parar == True and pararj == True:
        break
if jogador1 < 22 and bot < 22:
    if jogador1 > bot:
        print("Você venceu!\n")
    elif jogador1 < bot:
        print("Você perdeu!\n")
    elif jogador1 == bot:
        print("Empate!\n")
    else:
        print("Resultado desconhecido")
elif jogador1 > 21 or bot > 21:
    if jogador1 > 21 and bot > 21:
        print("Empate!\n")
    elif jogador1 > 21 and bot < 22:
        print("Você perdeu!\n")
    elif jogador1 < 22 and bot > 21:
        print("Você venceu!")
    else:
        print("Resultado desconhecido")
elif jogador1 == 21 and bot == 21:
    print("Empate!")
print(f"Você: {jogador1} pontos\nAdversário: {bot} pontos")


