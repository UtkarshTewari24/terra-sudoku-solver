import random
import tkinter as tk
from tkinter import messagebox
#set up variable
GREEN = "#14CC55"
YELLOW = "#FFFF00"
GRAY = "#3a3a3c"
TILE = "#444444"
KEY = "#818384"
rank = {GRAY: 1, YELLOW: 2, GREEN: 3}
words = [
    "apple", "beach", "crane", "dream", "eagle",
    "flame", "grape", "house", "ivory", "joker",
    "knife", "lemon", "mouse", "night", "ocean",
    "plant", "queen", "river", "stone", "table",
    "under", "voice", "water", "youth", "zebra",
    "abuse", "brain", "charm", "dance", "earth",
    "faith", "giant", "happy", "image", "juice",
    "karma", "light", "magic", "noble", "orbit",
    "peace", "quiet", "radio", "smile", "train",
    "unity", "value", "world", "adore", "blaze",
    "candy", "delta", "enjoy", "frost", "globe",
    "honor", "input", "jelly", "kneel", "lucky",
    "march", "novel", "olive", "piano", "quirk",
    "roast", "sheep", "tiger", "ultra", "vivid",
    "wheat", "yield", "amber", "bloom", "cloud",
    "drift", "elbow", "fancy", "ghost", "ideal",
    "judge", "layer", "metal", "never", "panel",
    "ranch", "scale", "theme", "urban", "valid",
    "witch", "xenon", "young", "zesty"
]
grid = [[0, 0, 0], [0,0,0],[0,0,0]]
isX = True
gamerunning = True
you_wins = 0
ai_wins = 0
draws = 0
root = tk.Tk()
root.title("Tic Tac Toe")
BG = "#222222"
root.configure(bg=BG)
easy_mode = False
start_frame=tk.Frame(root,bg=BG)
game_frame=tk.Frame(root,bg=BG)

# set up tkinter
tk.Label(start_frame, text="TIC TAC TOE", font=("Arial", 40, "bold"), bg=BG, fg="white").pack(pady=20)

turnbar = tk.Label(root, text="Your turn", font=("Arial", 20, "bold"), bg=BG, fg="white")
turnbar.grid(row=0, column=0, columnspan=4, pady=5)
status = tk.Label(root, text="Your turn", font=("Arial", 16), bg=BG, fg="white")
status.grid(row=1, column=0, columnspan=4, pady=10)
buttons = [[None, None, None],[None, None, None],[None, None, None] ]
#el labelos
tk.Label(root, text="A", font=("Arial", 20), bg=BG, fg="white").grid(row=2, column=0)
tk.Label(root, text="B", font=("Arial", 20), bg=BG, fg="white").grid(row=3, column=0)
tk.Label(root, text="C", font=("Arial", 20), bg=BG, fg="white").grid(row=4, column=0)
tk.Label(root, text="1", font=("Arial", 20), bg=BG, fg="white").grid(row=5, column=1)
tk.Label(root, text="2", font=("Arial", 20), bg=BG, fg="white").grid(row=5, column=2)
tk.Label(root, text="3", font=("Arial", 20), bg=BG, fg="white").grid(row=5, column=3)

#i need helper functions here for inside of the ai thing like get_winner and is_full
def get_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[1][1]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[1][1]
    return None
        
def is_full(board):
    for i in range(3):
        for x in range(3):
            if board[i][x] == 0:
                return False
    return True



#i can add minimax here using what i thought abt before AOUDJWAOUDHAIOUFJWAIFWJOEIRWJARIAWJROIAWJDIOAWJFIAWo
def minimax(board, is_ai_turn):
    winner = get_winner(board)
    if winner == "Y":
        return 1
    if winner == "X":
        return -1
    elif is_full(board) == True:
        return 0
    if is_ai_turn == True:
        best = -100
        for i in range(3):
            for x in range(3):
                if board[i][x] == 0:
                    board[i][x] = "Y"
                    score = minimax(board, False)
                    board[i][x] = 0
                    if score>best:
                        best = score
        return best
    elif is_ai_turn == False:
        best = 100
        for r in range(3):
            for c in range(3):
                if board[r][c] == 0:
                    board[r][c] = "X"
                    score = minimax(board, True)
                    board[r][c] = 0
                    if score<best:
                        best = score
        return best






# add move picker here
def best_move():
    global grid
    best_score = -100
    best_spot = None
    for i in range(3):
        for x in range(3):
            if grid[i][x] == 0:
                grid[i][x] = "Y"
                score = minimax(grid, False)
                grid[i][x] = 0
                if score > best_score:
                    best_score = score
                    best_spot = (i, x)
    return best_spot
def random_move():
    empty = []
    for r in range(3):
        for c in range(3):
            if grid[r][c] == 0:
                empty.append((r,c))
    return random.choice(empty)
def toggle_mode():
    global easy_mode
    if easy_mode == True:
        easy_mode = False
        mode_button.config(text="Mode: Hard")
    else: 
        easy_mode = True
        mode_button.config(text="Mode: Easy")

def ai_turn():
    if gamerunning == True and isX == False:
        if easy_mode == True and random.random() < 0.5:
            spot = random_move()
        else: 
            spot = best_move()
        click(spot[0], spot[1])


#click function
def end_game(message, who):
    global gamerunning, you_wins, ai_wins, draws
    gamerunning = False
    if who == "X":
        you_wins = you_wins + 1
    elif who == "Y":
        ai_wins = ai_wins + 1
    else: draws = draws + 1
    score.config(text="you: " + str(you_wins) +"    AI:  " + str(ai_wins) + "   Draws:  " + str(draws))
    status.config(text=message)
    root.update()
    messagebox.showinfo("Game Over", message)




def click(movelnumber, movenumber):
    #globalify the variables so i can access them
    global isX, gamerunning
    #reject when game is over or click touched square
    if gamerunning == False or grid[movelnumber][movenumber] !=0:
        return
    #make a move on X
    if isX == True:
        grid[movelnumber][movenumber] = "X"
        buttons[movelnumber][movenumber].config(text="X")
    #make a move on Y
    else:
        grid[movelnumber][movenumber] = "Y"
        buttons[movelnumber][movenumber].config(text = "Y")
    #check rows for completion
    for i in range(0, 3):
        #check it
        if grid[i][0] == grid[i][1] == grid[i][2]:
            #check if it's Y
            if grid[i][0] == "Y":
                status.config(text="AI WINS!")
                gamerunning = False
                break
            #check if it's X
            if grid[i][0] == "X":
                status.config(text="YOU WIN!")
                gamerunning = False
                break
    #check if it's in a column and game is over
    for i in range(0, 3):
        #check column
        if grid[0][i] == grid[1][i] == grid[2][i]:
            #confirm Y
            if grid[0][i] == "Y":
                status.config(text="AI WINS!")
                gamerunning = False
                break
            #confirm X
            if grid[0][i] == "X":
                status.config(text="YOU WIN!")
                gamerunning = False
                break
        #btw i had a big bug here where all this code below to 88 was indented, causing nothing to work! 
    if grid [0][0] == grid[1][1] == grid [2][2] or grid[2][0] == grid[1][1] == grid[0][2]:
        if grid[1][1] == "Y":
            status.config(text="AI WINS!")
            gamerunning = False
        elif grid[1][1] == "X":
            status.config(text="YOU WIN!")
            gamerunning = False
    if gamerunning == True:
        gridFull = True
        for r in range(3):
            for c in range(3):
                if grid[r-1][c-1] == 0:
                    gridFull = False
        if gridFull == True:
            status.config(text="It's a draw :(")
        elif isX == True:
            isX = False
            status.config(text="AI's Turn")
            turnbar.config(text="AI's Turn")
        else:
            isX = True
            status.config(text="Your Turn")
            turnbar.config(text="Your Turn")
        #trigger AI from click
        if gamerunning == True and isX == False:
            root.after(300, ai_turn)
    winner = get_winner(grid)
    if winner == "X":
        end_game("YOU WIN!", "X")
    elif winner == "Y":
        end_game("AI WINS!", "Y")
    elif is_full(grid):
        end_game("It's a draw :(", None)

def make_button(r,c):
    #make it so you can only click during human turn bc this algo lowk gonna take like 2 seconds
    def on_click(event):
        if isX == True:
            click(r,c)
    cell = tk.Frame(root, width=100, height=100, bg="#444444")
    cell.grid(row=r+2, column=c+1, padx=3, pady=3)
    lbl=tk.Label(cell, text="", font=("Arial", 40), bg="#444444", fg="white")
    lbl.place(relx=0.5, rely=0.5, anchor="center")
    cell.bind("<Button-1>", on_click)
    lbl.bind("<Button-1>", on_click)
    buttons[r][c] = lbl
def reset():
    global isX, gamerunning
    isX = True
    gamerunning = True
    status.config(text="Your turn")
    turnbar.config(text="Your turn")
    for r in range(3):
        for c in range(3):
            grid[r][c] = 0
            buttons[r][c].config(text="")
for r in range(3):
    for x in range(3):
        make_button(r,x)
tk.Button(root, text="Restart", command=reset).grid(row=6, column=0, columnspan=4, pady=10)
score = tk.Label(root, text="you: 0   AI:    0    Draws: 0", font=("Arial", 16), bg=BG, fg="white")
score.grid(row=7, column=0, columnspan=4, pady=5)
mode_button = tk.Button(root, text="Mode; Hard", command=toggle_mode)
mode_button.grid(row=8, column=0, columnspan=4, pady=5)
tk.Label(start_frame, text="Play against AI!", font=("Arial", 16), bg=BG, fg="white").pack(pady=5)
tk.Label(start_frame, text="You are X, the AI is Y.", font=("Arial", 14), bg=BG, fg="white").pack(pady=5)

def start_game():
    start_frame.place_forget()
    reset()
def show_start():
    wordle_frame.place_forget()
    start_frame.place(x=0, y=0, relwidth=1, relheight=1)
    start_frame.tkraise()
wordle_frame = tk.Frame(root,bg=BG)
secret=""
row=0
tk.Label(wordle_frame, text="WORDLE", font=("Arial", 28, "bold"), bg=BG, fg="white").pack(pady=10)
msg = tk.Label(wordle_frame, text="guess the word", font=("Arial", 14), bg=BG, fg="white")
msg.pack()
tile_frame = tk.Frame(wordle_frame, bg=BG)
tile_frame.pack(pady=10)
tiles=[]
for r in range(6):
    tile_row=[]
    for c in range(5):
        t= tk.Label(tile_frame, text="", width=2, font=("Arial", 22, "bold"), bg=TILE, fg="white")
        t.grid(row=r, column=c, padx=3, pady=3)
        tile_row.append(t)
    tiles.append(tile_row)
entry=tk.Entry(wordle_frame, font=("Arial", 20), width=8, justify="center")
entry.pack(pady=5)

def new_wordle():
    global secret, row
    secret = random.choice(words)
    row = 0
    msg.config(text="guess the word")
    entry.delete(0, tk.END)
    for r in range(6):
        for c in range(5):
            tiles[r][c].config(text="", bg=TILE)
def guess(event=None):
    global row
    if row ==6:
        return
    word = entry.get().lower()
    if len(word) != 5:
        msg.config(text="Need 5 letters")
        return
    for i in range(5):
        if word[i] == secret[i]:
            color = GREEN
        elif word[i] in secret:
            color = YELLOW
        else:
            color = GRAY
        tiles[row][i].config(text=word[i].upper(), bg=color)
    entry.delete(0, tk.END)
    if word == secret:
        msg.config(text="NICE!")
        row=6
    elif row == 5:
        msg.config(text="the word was" + secret)
        row = 6
    else: 
        row = row+1
entry.bind("<Return>", guess)
tk.Button(wordle_frame, text="Guess", command=guess).pack(pady=3)
tk.Button(wordle_frame, text="New Word", command=new_wordle).pack(pady=3)
tk.Button(wordle_frame, text="Back to Menu", command=show_start).pack(pady=3)

def show_wordle():
    start_frame.place_forget()
    wordle_frame.place(x=0, y=0, relwidth=1, relheight=1)
    wordle_frame.tkraise()
    new_wordle()
    entry.focus()

tk.Button(start_frame, text="Tic Tac Toe", font=("Arial", 20), command=start_game).pack(pady=10)
tk.Button(start_frame, text="Wordle", font=("Arial", 20), command = show_wordle).pack(pady=10)
tk.Button(root, text="Menu", command=show_start).grid(row=9, column=0, columnspan=4, pady=5)
show_start()

root.mainloop()

#shit what else can i add? 
#WORDLE! 