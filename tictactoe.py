#COMEBACK PYTHON SOLVER
#fahhhhhhh

# k so ima plan ts out first bc i lowk dk how to code..

# start by using some data type to store a grid, or js go like oneone=0 onetwo = 0 and do it that way but thats lowk weird
grid = [[0, 0, 0], [0, 0, 0], 
        [0, 0, 0]]

isX = True
gamerunning = True
# print grid here
print("A ", grid[0][0], "  ", grid[0][1], "  ", grid[0][2])
print("B ", grid[1][0], "  ", grid[1][1], "  ", grid[1][2])
print("C ", grid[2][0], "  ", grid[2][1], "  ", grid[2][2])
print("0  1    2    3 ")
# while true start
while gamerunning:

#add a input field here, take inputs like a1 a2 b3 wait genuinely what is going on 

#interpret the input    WHATTTTT
    while True:
        move = input("Make your move ex: A1, B2, C3:  ")
        if len(move) == 2:
            valid = False
            letter= move[0].upper()
            if letter == "A" or letter == "B" or letter == "C": 
                moveletter = letter
            else: 
                print("invalid!")
                continue
            
# update board, check status

            if int(move[1]) == 1 or int(move[1]) == 2 or int(move[1]) == 3:
                movenumber = int(move[1]) - 1
            else:
                print("invalid!")
                continue
            if isX == True:
                isX = False
            else:
                isX = True
            if moveletter == "A":
                movelnumber = 0
            elif moveletter == "B":
                movelnumber = 1
            elif moveletter == "C":
                movelnumber = 2
            if isX == True:
                grid[movelnumber][movenumber] = "X"
            else:
                grid[movelnumber][movenumber] = "Y"
            print("A ", grid[0][0], "  ", grid[0][1], "  ", grid[0][2])
            print("B ", grid[1][0], "  ", grid[1][1], "  ", grid[1][2])
            print("C ", grid[2][0], "  ", grid[2][1], "  ", grid[2][2])
            print("0  1    2    3 ")
            for i in range (0, 2):
                if grid[i][0] == grid[i][1] == grid[i][2]:
                    if grid[i][0] == "Y":
                        print("Y WINS!")
                        gamerunning = False
                        break
                    if grid[i][0] == "X":
                        print ("X WINS!")
                        gamerunning = False
                        break
            for i in range (0, 2):
                if grid[0][i] == grid[1][i] == grid[2][i]:
                    if grid[0][i] == "Y":
                        print("Y WINS!")
                        gamerunning = False
                        break
                    if grid[0][i] == "X":
                        print ("X WINS!")
                        gamerunning = False
                        break
            if grid [0][0] == grid[1][1] == grid[2][2] or grid[2][0] == grid[1][1] == grid[0][2]:
                if grid[1][1] == "Y":
                    print("Y WINS!")
                    gamerunning = False
                    break
                if grid[1][1] == "X":
                    print("X WINS!")
                    gamerunning = False
                    break
            



    break
        
# im fried i need a break lapeace out