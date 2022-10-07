#Aluna: Deisiane Prata Cuellar
#Curso: Análise e Desenvolvimento de Sistemas

import random

def separador():
    # Fazer quebras de linhas  
    print('~' * 65)

def IniciarCopo():
    # 3 tipos de dados - 13 dados ao total

    dVerde = ("CPCTPC", "Verde")
    dAmarelo = ("TPCTPC", "Amarelo")
    dVermelho = ("TPTCPT", "Vermelho")

    return [
        dVerde,dVerde,dVerde,dVerde,dVerde,dVerde,
        dAmarelo, dAmarelo, dAmarelo, dAmarelo,
        dVermelho,dVermelho,dVermelho
    ]

def PegarDados(DadosSorteados, Copo):
    # Retirar os dados se ainda tiver dados no Copo
    while (len(DadosSorteados) < 3 and len(Copo) > 0):
        dadoAtual = random.choice(Copo)
        RemoverDado(dadoAtual, Copo)
        DadosSorteados.append(dadoAtual)

def RemoverDado(dadoAtual, Copo):
    # Remove o dado do copo
    Copo.remove(dadoAtual)

def LancarDados(dados, DadosNaMao, DadosNaMesa):
    # Lança os dados

    input("\nAperte ENTER para lançar os dados: ")
    DadosResultado = []
    DadosNaMao.clear()

    for dadoAtual in dados:
        # Escolhe a face do dado
        faceAtual = random.choice(dadoAtual[0])

        DadosResultado.append((dadoAtual[1], faceAtual))

        if (faceAtual == "C"):
            DadosNaMesa.append(dadoAtual)
        elif (faceAtual == "P"):
            DadosNaMao.append(dadoAtual)
        else:
            DadosNaMesa.append(dadoAtual)

    return DadosResultado

def MostrarDadosSorteados(DadosResultado):
    print("\nO resultado dos dados foram:")

    for dadoAtual in DadosResultado:
        print(f"{dadoAtual}")

def Pontuacao(DadosResultado, CerebrosTotais, TirosTotais):
    # Reseta a pontuacao dos dados a cada nova tentativa
    cerebros = 0
    passos = 0
    tiros = 0

    for dadoAtual in DadosResultado:
        faceAtual = dadoAtual[1]

        if (faceAtual == "C"):
            cerebros = cerebros + 1
        elif (faceAtual == "P"):
            passos = passos + 1
        else:
            tiros = tiros + 1

    # Adiciona cérebros aos pontos totais do jogador
    CerebrosTotais = CerebrosTotais + cerebros

    # Contabiliza os tiros
    TirosTotais = TirosTotais + tiros

    print(f"\nNessa rodada:")
    print(f"Você comeu: {cerebros} Cérebro(s).")
    print(f"Você conseguiu: {passos} Passo(s).")
    print(f"Você levou: {tiros} Tiro(s)\n")

    print("Sua Pontuação Total:")
    print(f"Cerebros Totais: {CerebrosTotais}")
    print(f"Tiros Totais: {TirosTotais}\n")

    return CerebrosTotais, TirosTotais

def MostrarDados(dados):
    verdes = sum(dado[1] == 'Verde' for dado in dados)
    amarelos = sum(dado[1] == 'Amarelo' for dado in dados)
    vermelhos = sum(dado[1] == 'Vermelho' for dado in dados)

    print(f"{verdes} Verdes, {amarelos} Amarelos, {vermelhos} Vermelhos")



#Boas Vindas ao Jogo
separador()
print("{:^15}Bem Vindo ao Jogo Zombie Dice!!\n".format(" "))
print("{:^10}Devore cérebros. Não leve um tiro na cabeça!!".format(" "))
separador()

# Decidir quantos jogadores irão jogar
qtdJogadores = 0

while (qtdJogadores < 2):
    
    qtdJogadores = int(input("Informe a quantidade de 2 ou + jogadores: \n"))
    if (qtdJogadores< 2): print("Está faltando a quantidade de jogadores necessários para iniciar o jogo.\n")

ListaJogadores = []

# Preencher o nome dos jogadores

for i in range(qtdJogadores):
    nomeJogador = input("Digite o nome do jogador " + str(i+1) + ": ")
    ListaJogadores.append(nomeJogador)

separador()
print("O Jogador que falar “Céééééérebros” da maneira mais zumbi possível "
      "irá iniciar!!")

# Decidir a ordem dos jogadores
random.shuffle(ListaJogadores)

print("\nUau "+str(ListaJogadores[0])+"! Você imitou muito bem um zumbi!\n")

print("Portanto, a sequência de turno dos jogadores será: \n\n"+str(ListaJogadores))

separador()
print("\n*REGRAS*: \n - Cada um dos dados representa uma pobre vítima a ser atacada. "
      "\n - O jogo é composto por um tubo que armazena 13 dados de 6 faces."
      "\n - Os dados irão possuir 3 símbolos: \n Cérebro (Ganha Pontos), Tiros (Perde o Jogo se levar 3 tiros) e Passos (Jogar dados novamente).")

separador()
print("\n......Loading......\n")

Copo = IniciarCopo()

# Começa uma nova rodada
TirosParaPerder = 3
PontosParaGanhar = 13
FimDejogo = False

#Preencher a lista dos pontos

ListaPontos = []

for j in range(qtdJogadores):
    ListaPontos.append(0)

while (FimDejogo == False):
    for j in range(qtdJogadores):

        # Começa um novo turno
        print("-->", str(ListaJogadores[j])+ " <-- É A SUA VEZ DE JOGAR ")

        # Reseta a lista dos dados a cada turno
        DadosSorteados = []
        DadosNaMao = []
        DadosNaMesa = []

        TirosTotais = 0

        continuar = "s"
        while (continuar == "s"):
            # Mantem na lista dos DadosSorteados os dados de Passos que ficaram na mao
            DadosSorteados = DadosNaMao.copy()

            PegarDados(DadosSorteados, Copo)
            DadosResultado = LancarDados(DadosSorteados, DadosNaMao, DadosNaMesa)

            # Mostra os dados e as pontuações
            separador()
            MostrarDadosSorteados(DadosResultado)
            
            pontuacao = Pontuacao(DadosResultado, ListaPontos[j], TirosTotais)
            ListaPontos[j] = pontuacao[0]
            TirosTotais = pontuacao[1]
            
            # Contabiliza os dados restantes
            print(f"Sobrou {len(Copo)} dados no Copo")
            MostrarDados(Copo)

            print(f"Sobrou {len(DadosNaMao)} dados na Mão")
            MostrarDados(DadosNaMao)
            DadosDisponiveis = len(Copo) + len(DadosNaMao)

            separador()
            # Verifica os TirosTotais
            if (TirosTotais >= TirosParaPerder):

                # Jogador perdeu, reseta pontos do jogador
                ListaPontos[j] = 0
                print(">>>>> Jogador ~" + str(ListaJogadores[j]) + "~ perdeu, os pontos voltaram para 0 <<<\n")
                continuar = "n"
            elif (DadosDisponiveis > 0):

                # Solicita se o jogador quer continuar na rodada
                continuar = "x"
                while (continuar != "s" and continuar != "n"):
                    continuar = input("Quer continuar tentando a sorte? (s ou n): ").lower()
            else:
                print("Não tem mais dados disponíveis no copo e na mão")
                continuar = "n"

            if (continuar != "s" or TirosTotais >= TirosParaPerder):

                # Volta os dados da mesa e da mão para o copo
                Copo = Copo + DadosNaMesa
                Copo = Copo + DadosNaMao

                # Verifica se o jogador atual é o ultimo jogador da rodada
                if (j == (qtdJogadores-1)):
                    MaiorPontuacao = 0
                    print("\nResultado dessa rodada:")
                    for nJogador in range(qtdJogadores):
                        print(f"'{ListaJogadores[nJogador]}': {ListaPontos[nJogador]} Pontos")

                        # Verifica se alguém tem 13 pontos ou mais
                        if (ListaPontos[nJogador] >= PontosParaGanhar and ListaPontos[nJogador] > MaiorPontuacao):
                            MaiorPontuacao = ListaPontos[nJogador]
                            Ganhador = ListaJogadores[nJogador]

                    # Força o fim do jogo
                    if (MaiorPontuacao >= PontosParaGanhar):
                        print("\nJogador '" + str(Ganhador) + "' Ganhou com "+str(MaiorPontuacao)+" Pontos!")
                        FimDejogo = True

print("### FIM DE JOGO ###")


