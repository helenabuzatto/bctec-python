# Fase 1 do jogo
escolha = input("Você quer entrar na Câmara das escolhas, sim  ou não? ")
print(escolha)

if(escolha == "sim"):
       print("borá lá!")
else:
    print("volte para fase das variáveis!")


# Fase 2 do jogo
numero = int(input("Quantas chaves mágicas você coletou?:"))
print (numero)

if(numero == 3):
    print("Portão de bronze aberto!")
elif (numero == 5):
    print("Portão de prata aberto!")
elif(numero == 7):
    print("Portão de ouro aberto!")
else:
    print("Número incorreto de chaves. Portão permanece fechado.")

# Fase 3 do jogo
nivel = numero*20
print(nivel)
print("Verificando níveis de força")

if (nivel > 5):
    print ("Níveis aceitáveis de força")
else:
    print ("Precisa estudar mais para melhorar seus níveis de força")


# Fase 4 do jogo
caminho=input("Escolha um caminho: floresta, caverna ou rio: ")

if(caminho == "floresta"):
    print("Você foi atacado por robôs-programadores. Volte ao início.")
elif(caminho == "caverna"):
    print("Você encontrou um enigma lógico!")
elif(caminho == "rio"):
    print("Você atravessou com sucesso para a próxima fase!")
else:
    print("Caminho inválido. Tente novamente")

# Fase 5 do jogo
senha_secreta = 7
senha_tentativa = int(input("Tente adivinhar a senha entre 1 e 10: "))

if(senha_tentativa == senha_secreta):
    print("Senha correta! Cofre aberto.")
elif(senha_tentativa<senha_secreta):
    print("Senha muito baixa")
else:
    print("Senha muito alta")

# Fase 6 do jogo
temperatura = float(input("Digite a temperatura atual: "))

if (temperatura < 15):
    print("Muito frio! Robô congelado.")
elif (temperatura <= 25):
    print("Temperatura ideal. Robô funcionando.")
else:
    print("Muito quente! Robô superaquecido.")
