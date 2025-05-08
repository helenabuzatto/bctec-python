# fase 1
resposta = "sim"
pergunta = "?"
while pergunta != resposta:
    pergunta = (input("Você deseja continuar a jornada? (sim/não): "))
    if pergunta != resposta:
        print("Resposta inválida para avançar. Tente novamente!")
print("Portal aberto! Você pode seguir em frente.")

# fase 2
y = 1
x = int(input("Quantos degraus tem a escada? "))
degrau = int(input("Informe um número de degrau aleatório: "))
while y <= x:
    if y != degrau:
        print(f"Estou no degrau {y}")
    elif y == degrau:
        print(f"Estou no degrau que você escolheu, degrau {y}")
    y += 1
print("Você chegou no topo da escada!")

# fase 3
for x in range (1,11):
    y = int(input("Quantas pedras foram coletadas? "))
    print(f"Ponto de coleta {x} - número de pedras coletadas: {y}")
    x += 1
print("O número total de pedras luminosas foram coletadas!")

# fase 4
tab = 1
while tab <= 5:
    print(tab)
    mult = 1
    while mult <= 10:
        conta = tab * mult
        print (f"{tab}*{mult}={conta}")
        mult += 1
    tab += 1

# fase 6
chave = 3
t_chave = -1
while chave != t_chave:
    t_chave = int(input("Digite o número da chave (entre 1 e 10): "))

    if chave == t_chave:
        print ("Você acertou a chave!")
        codigo = 9
        t_codigo = -1
        while codigo != t_codigo:
            t_codigo = int(input("Digite o código de segurança (entre 1 e 10): "))
            print("Código incorreto. Tente novamente.")
        if codigo==t_codigo:
            print("Você acertou o código!")
    else:
        print ("Chave incorreta. Tente novamente.")
print("Cofre aberto com sucesso! Tesouro liberado!")

# fase 7
x = 100
y = 1
encontrado=False
while x >= 0 and encontrado==False:
    while y <= 100 and encontrado==False:
        if x + 2 * y == 150:
            encontrado = True
            print(f"Equilíbrio encontrado: x = {x} e y = {y}")
        y += 1
    x -= 1

# fase 8
x = 100
y = 1
portal_aberto = False

while x > 0 and not portal_aberto:
    while y <= 100 and not portal_aberto:
        if abs(x - y) < 5 and (x * y > 3000):
            print(f"O portal se abriu com x = {x} e y = {y}")
            portal_aberto = True
        else:
            y += 1
    x -= 1

# fase 9

energia = 100
constelacao = 1
while energia > 0 and constelacao <= 10:
    print (f"Constelação: {constelacao}")
    
    gemas=int(input("Quantas gemas foram coletadas? "))

    if gemas >= 5:
        energia_usada = gemas * 2
        energia = energia - energia_usada
        if constelacao == 10:
            print("Você completou a missão! Visitou as 10 constelações!")
        else:
            if energia <= 0:
                print("Sua energia acabou. Você não pode coletar mais gemas")
            else:
                print ("Você avançou para a próxima constelação.")
        print(f"Energia restante: {energia}")
        constelacao += 1
    else:
        print("Você coletou poucas gemas. Procure por mais.")
    
# fase 10

forca = 100
resistencia = 50
camada = 3

while forca > 0 and camada > 0:
    print(f"Camada: {camada}")
    ataque=int(input("Qual a força que você vai atacar? (núm. inteiro): "))
    forca -= 5

    if ataque % 3 != 0:
        resistencia -= 10
        print ("Ataque bem-sucedido!")
        print(f"Força restante: {forca} ; Resistencia da armadura: {resistencia}")
    else:
        print("O ataque falhou! Tente novamente.")
        print(f"Força restante: {forca} ; Resistencia da armadura: {resistencia}")

    if resistencia == 0:
        print("Você quebrou a proteção!")
        camada -= 1
        resistencia = 50

    if forca == 0 and camada != 0:
        print("Você perdeu toda sua força. Recomece.")
    
    if forca >=0 and camada == 0:
        print("Você concluiu a batalha!")

        


        

