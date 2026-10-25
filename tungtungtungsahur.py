#import tkinter
import tkinter as tk
from tkinter import messagebox
#set up variable
grid = [[0, 0, 0], [0,0,0],[0,0,0]]
isX = True
gamerunning = True
root = tk.Tk()
root.title("Tic Tac Toe")
BG = "#222222"

start_frame=tk.Frame(root,bg=BG)
game_frame=tk.Frame(root,bg=BG)

# set up tkinter
tk.Label(start_frame, text="TIC TAC TOE", font=("Arial", 40, "bold"), bg=BG, fg="white").pack(pady=20)

turnbar = tk.Label(root, text="Your turn", font=("Arial", 20, "bold"),  fg="white")
turnbar.grid(row=0, column=0, columnspan=4, pady=5)
status = tk.Label(root, text="Your turn", font=("Arial", 16), fg="white")
status.grid(row=1, column=0, columnspan=4, pady=10)
buttons = [[None, None, None],[None, None, None],[None, None, None] ]
#el labelos
tk.Label(root, text="A", font=("Arial", 20), fg="white").grid(row=2, column=0)
tk.Label(root, text="B", font=("Arial", 20), fg="white").grid(row=3, column=0)
tk.Label(root, text="C", font=("Arial", 20), fg="white").grid(row=4, column=0)
tk.Label(root, text="1", font=("Arial", 20), fg="white").grid(row=5, column=1)
tk.Label(root, text="2", font=("Arial", 20), fg="white").grid(row=5, column=2)
tk.Label(root, text="3", font=("Arial", 20), fg="white").grid(row=5, column=3)

#i need helper functions here for inside of the ai thing like get_winner and is_full
def get_winner(board):
    for i in range(0, 3):
            #check column
    #check rows for completion
        for i in range(0, 3):
            #check it
            if board[i][0] == board[i][1] == board[i][2] != 0:
                #check if it's Y
                return board[i][0]
        #check if it's in a column and game is over
        for i in range(0, 3):
            #check column
            if board[0][i] == board[1][i] == board[2][i] != 0:
                #confirm Y
                return board[0][i]
            #btw i had a big bug here where all this code below to 88 was indented, causing nothing to work! 
            if board [0][0] == board[1][1] == board [2][2] != 0 or board[2][0] == board[1][1] == board[0][2] != 0:
                return board[1][1]
        
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

def ai_turn():
    if gamerunning == True and isX == False:
        spot = best_move()
        click(spot[0], spot[1])
#click function
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

root.mainloop()