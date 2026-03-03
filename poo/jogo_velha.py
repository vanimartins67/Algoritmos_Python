import random

# ========================
#  JOGO DA VELHA - PYTHON
# ========================

def criar_tabuleiro():
    return ['1','2','3','4','5','6','7','8','9']

def mostrar_tabuleiro(tabuleiro):
    print()
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print()

def verificar_vencedor(tabuleiro, simbolo):
    combinacoes = [
        [0,1,2],[3,4,5],[6,7,8],  # linhas
        [0,3,6],[1,4,7],[2,5,8],  # colunas
        [0,4,8],[2,4,6]           # diagonais
    ]
    for combo in combinacoes:
        if tabuleiro[combo[0]] == tabuleiro[combo[1]] == tabuleiro[combo[2]] == simbolo:
            return True
    return False

def tabuleiro_cheio(tabuleiro):
    return all(casa in ['X', 'O'] for casa in tabuleiro)

def posicoes_livres(tabuleiro):
    return [i for i, casa in enumerate(tabuleiro) if casa not in ['X', 'O']]

def jogada_humano(tabuleiro, simbolo, nome):
    while True:
        try:
            escolha = int(input(f"{nome} ({simbolo}), escolha uma posição (1-9): "))
            if 1 <= escolha <= 9:
                posicao = escolha - 1
                if tabuleiro[posicao] not in ['X', 'O']:
                    tabuleiro[posicao] = simbolo
                    break
                else:
                    print("Essa posição já está ocupada! Tente outra.")
            else:
                print("Digite um número entre 1 e 9!")
        except ValueError:
            print("Digite apenas números!")

# ---- NÍVEIS DE DIFICULDADE ----

def jogada_facil(tabuleiro, simbolo):
    """Fácil: joga aleatoriamente em qualquer posição livre"""
    livres = posicoes_livres(tabuleiro)
    escolha = random.choice(livres)
    tabuleiro[escolha] = simbolo
    print(f"Computador jogou na posição {escolha + 1}")

def jogada_medio(tabuleiro, simbolo):
    """Médio: tenta ganhar ou bloquear, mas às vezes joga aleatório"""
    adversario = 'X' if simbolo == 'O' else 'O'
    livres = posicoes_livres(tabuleiro)

    # Tenta ganhar
    for pos in livres:
        tabuleiro[pos] = simbolo
        if verificar_vencedor(tabuleiro, simbolo):
            print(f"Computador jogou na posição {pos + 1}")
            return
        tabuleiro[pos] = str(pos + 1)  # desfaz a jogada

    # Tenta bloquear o adversário
    for pos in livres:
        tabuleiro[pos] = adversario
        if verificar_vencedor(tabuleiro, adversario):
            tabuleiro[pos] = simbolo  # bloqueia
            print(f"Computador jogou na posição {pos + 1}")
            return
        tabuleiro[pos] = str(pos + 1)  # desfaz a jogada

    # 50% de chance de jogar aleatório, senão prefere centro/cantos
    if random.random() < 0.5:
        escolha = random.choice(livres)
    else:
        preferidos = [4, 0, 2, 6, 8]  # centro e cantos
        escolha = next((p for p in preferidos if p in livres), random.choice(livres))

    tabuleiro[escolha] = simbolo
    print(f"Computador jogou na posição {escolha + 1}")

def minimax(tabuleiro, eh_maximizando, simbolo_ia):
    """
    Algoritmo Minimax: calcula recursivamente a melhor jogada.
    Retorna +10 se a IA ganhar, -10 se perder, 0 se empatar.
    """
    simbolo_humano = 'X' if simbolo_ia == 'O' else 'O'

    if verificar_vencedor(tabuleiro, simbolo_ia):
        return 10
    if verificar_vencedor(tabuleiro, simbolo_humano):
        return -10
    if tabuleiro_cheio(tabuleiro):
        return 0

    livres = posicoes_livres(tabuleiro)

    if eh_maximizando:
        melhor = -100
        for pos in livres:
            tabuleiro[pos] = simbolo_ia
            melhor = max(melhor, minimax(tabuleiro, False, simbolo_ia))
            tabuleiro[pos] = str(pos + 1)
        return melhor
    else:
        melhor = 100
        for pos in livres:
            tabuleiro[pos] = simbolo_humano
            melhor = min(melhor, minimax(tabuleiro, True, simbolo_ia))
            tabuleiro[pos] = str(pos + 1)
        return melhor

def jogada_dificil(tabuleiro, simbolo):
    """Difícil: usa minimax para nunca perder"""
    livres = posicoes_livres(tabuleiro)
    melhor_pontuacao = -100
    melhor_pos = livres[0]

    for pos in livres:
        tabuleiro[pos] = simbolo
        pontuacao = minimax(tabuleiro, False, simbolo)
        tabuleiro[pos] = str(pos + 1)
        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_pos = pos

    tabuleiro[melhor_pos] = simbolo
    print(f"Computador jogou na posição {melhor_pos + 1}")

def jogada_computador(tabuleiro, simbolo, dificuldade):
    if dificuldade == 1:
        jogada_facil(tabuleiro, simbolo)
    elif dificuldade == 2:
        jogada_medio(tabuleiro, simbolo)
    else:
        jogada_dificil(tabuleiro, simbolo)

# ---- MODOS DE JOGO ----

def modo_dois_jogadores():
    print("\n=== MODO 2 JOGADORES ===")
    nome1 = input("Nome do Jogador 1 (X): ").strip() or "Jogador 1"
    nome2 = input("Nome do Jogador 2 (O): ").strip() or "Jogador 2"

    tabuleiro = criar_tabuleiro()
    jogadores = [(nome1, 'X'), (nome2, 'O')]
    turno = 0

    while True:
        mostrar_tabuleiro(tabuleiro)
        nome, simbolo = jogadores[turno % 2]
        jogada_humano(tabuleiro, simbolo, nome)

        if verificar_vencedor(tabuleiro, simbolo):
            mostrar_tabuleiro(tabuleiro)
            print(f"🎉 {nome} GANHOU! Parabéns!")
            break

        if tabuleiro_cheio(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("🤝 EMPATE! Boa partida!")
            break

        turno += 1

def escolher_dificuldade():
    print("\nEscolha a dificuldade:")
    print("1 - Fácil   (computador joga aleatório)")
    print("2 - Médio   (computador tenta ganhar/bloquear)")
    print("3 - Difícil (computador nunca perde!)")
    while True:
        opcao = input("Dificuldade (1/2/3): ").strip()
        if opcao in ['1', '2', '3']:
            nomes = {'1': 'Fácil', '2': 'Médio', '3': 'Difícil'}
            print(f"Dificuldade selecionada: {nomes[opcao]}")
            return int(opcao)
        print("Digite 1, 2 ou 3!")

def modo_vs_computador():
    print("\n=== MODO VS COMPUTADOR ===")
    nome = input("Seu nome: ").strip() or "Jogador"
    dificuldade = escolher_dificuldade()

    tabuleiro = criar_tabuleiro()

    while True:
        mostrar_tabuleiro(tabuleiro)
        jogada_humano(tabuleiro, 'X', nome)

        if verificar_vencedor(tabuleiro, 'X'):
            mostrar_tabuleiro(tabuleiro)
            print(f"🎉 {nome} GANHOU! Incrível!")
            break

        if tabuleiro_cheio(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("🤝 EMPATE! Boa partida!")
            break

        jogada_computador(tabuleiro, 'O', dificuldade)

        if verificar_vencedor(tabuleiro, 'O'):
            mostrar_tabuleiro(tabuleiro)
            print("🤖 O COMPUTADOR GANHOU! Tente de novo!")
            break

        if tabuleiro_cheio(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("🤝 EMPATE! Boa partida!")
            break

def menu_principal():
    while True:
        print("\n============================")
        print("      JOGO DA VELHA 🎮")
        print("============================")
        print("1 - 2 Jogadores")
        print("2 - Vs Computador")
        print("3 - Sair")
        print("============================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            modo_dois_jogadores()
        elif opcao == '2':
            modo_vs_computador()
        elif opcao == '3':
            print("Até mais! 👋")
            break
        else:
            print("Opção inválida! Digite 1, 2 ou 3.")
            continue

        jogar_novamente = input("\nJogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            print("Até mais! 👋")
            break

if __name__ == "__main__":
    menu_principal()