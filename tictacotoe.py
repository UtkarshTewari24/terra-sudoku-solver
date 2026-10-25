#import tkinter
import tkinter as tk
from tkinter import messagebox
#set up variable
grid = [[0, 0, 0], [0,0,0],[0,0,0]]
isX = True
gamerunning = True
root = tk.Tk()
root.title("Tic Tac Toe")

start_frame=tk.Frame(root,bg=BG)
game_frame=tk.Frame(root,bg=BG)

# set up tkinter
tk.Label(start_frame, text="TIC TAC TOE", font=("Arial", 40, "bold"), bg=BG, fg="white").pack(pady=20)

turnbar = tk.Label(root, text="X's turn", font=("Arial", 20, "bold"),  fg="white")
status = tk.Label(root, text="X's turn", font=("Arial", 16), fg="white")
status.grid(row=1, column=0, columnspan=4, pady=10)
buttons = [[None, None, None],[None, None, None],[None, None, None] ]
#el labelos
tk.Label(root, text="A", font=("Arial", 20), fg="white").grid(row=2, column=0)
tk.Label(root, text="B", font=("Arial", 20), fg="white").grid(row=3, column=0)
tk.Label(root, text="C", font=("Arial", 20), fg="white").grid(row=4, column=0)
tk.Label(root, text="1", font=("Arial", 20), fg="white").grid(row=5, column=1)
tk.Label(root, text="2", font=("Arial", 20), fg="white").grid(row=5, column=2)
tk.Label(root, text="3", font=("Arial", 20), fg="white").grid(row=5, column=3)
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
                status.config(text="Y WINS!")
                gamerunning = False
                break
            #check if it's X
            if grid[i][0] == "X":
                status.config(text="X WINS!")
                gamerunning = False
                break
    #check if it's in a column and game is over
    for i in range(0, 3):
        #check column
        if grid[0][i] == grid[1][i] == grid[2][i]:
            #confirm Y
            if grid[0][i] == "Y":
                status.config(text="Y WINS!")
                gamerunning = False
                break
            #confirm X
            if grid[0][i] == "X":
                status.config(text="X WINS!")
                gamerunning = False
                break
        #btw i had a big bug here where all this code below to 88 was indented, causing nothing to work! 
        if grid [0][0] == grid[1][1] == grid [2][2] or grid[2][0] == grid[1][1] == grid[0][2]:
            if grid[1][1] == "Y":
                status.config(text="Y WINS!")
                gamerunning = False
                break
            elif grid[1][1] == "X":
                status.config(text="X WINS!")
                gamerunning = False
                break
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
                status.config(text="Y's Turn")
                turnbar.config(text="Y's Turn")
            else:
                isX = True
                status.config(text="X's Turn")
                turnbar.config(text="X's Turn")
def make_button(r,c):
    def on_click():
        click(r,c)
    b = tk.Button(root, text="", width=4, height=4, font=("Arial", 28), command=on_click)
    b.grid(row = r+2, column = c+1)
    buttons[r][c] = b

def reset():
    global isX, gamerunning
    isX = True
    gamerunning = True
    status.config(text="X's turn")
    turnbar.config(text="X's turn")
    for r in range(3):
        for c in range(3):
            grid[r][c] = 0
            buttons[r][c].config(text="")
for r in range(3):
    for x in range(3):
        make_button(r,x)
tk.Button(root, text="Restart", command=reset).grid(row=6, column=0, columnspan=4, pady=10)

root.mainloop()