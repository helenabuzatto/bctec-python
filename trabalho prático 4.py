import pandas as pd
import random

df = pd.read_csv("partidas_futebol_sem_gols.csv", sep=';', nrows=15)

for indice, linha in df.iterrows():
    time_casa = linha["TimeCasa"]
    time_fora = linha["TimeFora"]
    rodada = linha["Rodada"]

    print (f"Rodada: {rodada}")

    # PARTE 1
    # 1) SIMULAÇÃO
    
    limite_forca_casa = random.randint(1, 100)
    for forca_casa in range(1, limite_forca_casa + 1): 
        forca_casa += 1
    gols_casa = forca_casa // 10

    limite_forca_fora = random.randint(1, 100)
    for forca_fora in range(1, limite_forca_fora + 1):
        forca_fora += 1
    gols_fora = forca_fora // 10

    print(f"{time_casa} {gols_casa} x {gols_fora} {time_fora}")

    if gols_casa>gols_fora:
        print(f"Time vencedor: {time_casa}")
    elif gols_casa==gols_fora:
        print ("Empate.")
    else:
        print(f"Time vencedor: {time_fora}")

    # PARTE 2
    # 1) APROVEITAMENTO

    chutes_casa = linha["Chutes_Casa"]
    chutes_fora = linha["Chutes_Fora"]

    if chutes_casa>0:
        aproveitamento_casa = (gols_casa/chutes_casa)*100
        print (f"Aproveitamento ofensivo {time_casa}: {aproveitamento_casa:.0f}%")
    
    if chutes_fora>0:
        aproveitamento_fora = (gols_fora/chutes_fora)*100
        print (f"Aproveitamento ofensivo {time_fora}: {aproveitamento_fora:.0f}%")
    
    # 2) AGRESSIVIDADE

    faltas_casa = linha["Faltas_Casa"]
    faltas_fora = linha["Faltas_Fora"]
    ca_casa = linha["CA_Casa"]
    cv_casa = linha ["CV_Casa"]
    ca_fora = linha["CA_Fora"]
    cv_fora = linha ["CV_Fora"]

    agressividade_casa = (faltas_casa + 2)*(ca_casa + 3)*cv_casa
    agressividade_fora = (faltas_fora + 2)*(ca_fora + 3)*cv_fora

    if agressividade_casa>agressividade_fora:
        print (f"Mais agressivo: {time_casa} com {agressividade_casa} pontos de agressividade")
    elif agressividade_casa<agressividade_fora:
        print (f"Mais agressivo: {time_fora} com {agressividade_fora} pontos de agressividade")
    else:
        print (f"Agressividades iguais: ({time_casa}: {agressividade_casa} e {time_fora}: {agressividade_fora}")

    # 3) ESCANTEIOS

    escanteios_casa = linha ["Escanteios_Casa"]
    escanteios_fora = linha ["Escanteios_Fora"]

    diferenca_de_escanteios = abs(escanteios_casa - escanteios_fora)
    if escanteios_casa>escanteios_fora:
        print (f"{time_casa} teve mais escanteios. Diferença de {diferenca_de_escanteios} escanteios.")
    elif escanteios_casa<escanteios_fora:
        print (f"{time_fora} teve mais escanteios. Diferença de {diferenca_de_escanteios} escanteios.")
    else:
        print (f"Os dois times tiveram a mesma quantidade de escanteios.")

    # 4) PRESSA OFENSIVA

    impedimentos_casa = linha["Impedimentos_Casa"]
    impedimentos_fora = linha["Impedimentos_Fora"]

    ipo_casa = impedimentos_casa/(chutes_casa + escanteios_casa + 1)
    ipo_fora = impedimentos_fora/(chutes_fora + escanteios_fora + 1)

    if ipo_casa>ipo_fora:
        print (f"{time_casa} se precipitou mais ao atacar. Com Índice de Pressa Ofensiva de {ipo_casa:.2f}")
    elif ipo_casa<ipo_fora:    
        print (f"{time_fora} se precipitou mais ao atacar. Com Índice de Pressa Ofensiva de {ipo_fora:.2f}")
    else:
        print (f"Os dois apresentam Índice de Pressa Ofensiva iguais. {time_casa}: {ipo_casa:.2f} e {time_fora}: {ipo_fora:.2f}")

    # PARTE 3 - SIMULAÇÃO DE PRESSÃO TÁTICA

    limite_de_pressao_casa = random.randint(50, 150)
    limite_de_pressao_fora = random.randint(50, 150)

    pressao_tatica_casa = 0
    pressao_tatica_fora = 0

    contador_casa = 0
    contador_fora = 0

    while pressao_tatica_casa<=limite_de_pressao_casa:
        pressao_tatica_casa += (escanteios_casa*1.5) + (chutes_casa*1.2) - (faltas_casa*0.5)
        contador_casa += 1
    print (f"{time_casa} teve pressão tática de {pressao_tatica_casa:.2f} com {contador_casa} ciclos de ataque")

    while pressao_tatica_fora<=limite_de_pressao_fora:
        pressao_tatica_fora += (escanteios_fora*1.5) + (chutes_fora*1.2) - (faltas_fora*0.5)
        contador_fora +=1
    print (f"{time_fora} teve pressão tática de {pressao_tatica_fora:.2f} com {contador_fora} ciclos de ataque")

