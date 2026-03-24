from tkinter import *
from tkinter import messagebox
from random import randrange

# =====================
# VARIÁVEIS
# =====================
board = []
buttons = []
modo = None  # "pvp" ou "pc"
jogador_atual = "O"

# =====================
# TABULEIRO
# =====================
def create_board():
    return [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9']
    ]

# =====================
# DESENHAR
# =====================
def draw_board():
    for i in range(3):
        for j in range(3):
            valor = board[i][j]
            if valor in ['X','O']:
                buttons[i][j]['text'] = valor
                buttons[i][j]['state'] = DISABLED
            else:
                buttons[i][j]['text'] = ""
                buttons[i][j]['state'] = NORMAL

# =====================
# VENCEDOR
# =====================
def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    cheio = True
    for linha in board:
        for valor in linha:
            if valor not in ['X','O']:
                cheio = False

    if cheio:
        return "Empate"

    return None

# =====================
# COMPUTADOR
# =====================
def computer_move():
    while True:
        r = randrange(3)
        c = randrange(3)
        if board[r][c] not in ['X','O']:
            board[r][c] = 'X'
            break

# =====================
# CLIQUE
# =====================
def player_move(i, j):
    global jogador_atual

    if board[i][j] in ['X','O']:
        return

    # jogador sempre O no modo PC
    board[i][j] = jogador_atual
    draw_board()

    resultado = check_winner()
    if resultado:
        end_game(resultado)
        return

    # modo vs pc
    if modo == "pc":
        computer_move()
        draw_board()

        resultado = check_winner()
        if resultado:
            end_game(resultado)

    # modo 2 jogadores
    else:
        jogador_atual = "X" if jogador_atual == "O" else "O"

# =====================
# FIM
# =====================
def end_game(resultado):
    if resultado == "Empate":
        messagebox.showinfo("Resultado", "Deu empate!")
    else:
        messagebox.showinfo("Resultado", f"{resultado} venceu!")

# =====================
# RESET
# =====================
def reset_game():
    global board, jogador_atual
    board = create_board()
    jogador_atual = "O"

    # 👇 garante regra do enunciado
    if modo == "pc":
        board[1][1] = 'X'

    draw_board()

# =====================
# ESCOLHER MODO
# =====================
def escolher_modo(m):
    global modo, board, jogador_atual
    modo = m
    board = create_board()
    jogador_atual = "O"

    frame_menu.pack_forget()
    frame_jogo.pack()

    # 👇 COMPUTADOR COMEÇA NO CENTRO
    if modo == "pc":
        board[1][1] = 'X'

    draw_board()

# =====================
# INTERFACE
# =====================
janela = Tk()
janela.title("Jogo da Velha")

# MENU
frame_menu = Frame(janela)
frame_menu.pack()

Label(frame_menu, text="Escolha o modo").pack(pady=10)

Button(frame_menu, text="2 Jogadores",
       command=lambda: escolher_modo("pvp")).pack(pady=5)

Button(frame_menu, text="Contra o PC",
       command=lambda: escolher_modo("pc")).pack(pady=5)

# JOGO
frame_jogo = Frame(janela)

for i in range(3):
    linha = []
    for j in range(3):
        b = Button(frame_jogo, text="", width=10, height=5,
                   command=lambda i=i, j=j: player_move(i,j))
        b.grid(row=i, column=j)
        linha.append(b)
    buttons.append(linha)

Button(frame_jogo, text="Resetar", command=reset_game)\
    .grid(row=3, column=0, columnspan=3, sticky="we")

janela.mainloop()