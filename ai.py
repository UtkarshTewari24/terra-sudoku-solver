#here i aim to create an AI for the user to play against
# #COMEBACK PYTHON SOLVER
#fahhhhhhh


    

# k so ima plan ts out first bc i lowk dk how to code..

# start by using some data type to store a grid, or js go like oneone=0 onetwo = 0 and do it that way but thats lowk weird
grid = [[0, 0, 0], [0, 0, 0], 
        [0, 0, 0]]
aifirstx = False
isX = True
gamerunning = True
# print grid here
print("A ", grid[0][0], "  ", grid[0][1], "  ", grid[0][2])
print("B ", grid[1][0], "  ", grid[1][1], "  ", grid[1][2])
print("C ", grid[2][0], "  ", grid[2][1], "  ", grid[2][2])
print("0  1    2    3 ")












def bestnextmove():
    global grid, isX, aifirstx

# Strategy: (i saw a video about this when i was younger but dont fully remember how to do it so logic puzzle timeee)
#1. look at empty squares
#2. for every square go through each combination of next squares until you find one with the least probability of you losing
#repeat
#how to do 2? 
#find indexes of squares that aren't filled
# will this js be hella recursion? hmmmmmm idk if hella nested loops is good but idt theres any other way
#is there a way to adjustively recurse.. ?? 
#i guess ill make a function called is valid and then call that to verify and if it is then i return and go back and run again and again, how will i keep count tho? 
#yo i might be dumb
#WAIT doesnt this way like reduce the ability to do forced sequences with complexity?
#this might be hard.. 

# OH MY GOD
# btw i been working on paper for the last like 30 mins
#BRO I CAN CALL THE FUNCTION INTO ITSELF HOLY SHIT
#ballright i got it
#essentially +1 +0 and -1 are win draw and lose going through each possible scenario, we go for the highest number.
#i've been logic puzzling and rethinking this again and again and this is the only way that works according to all the brute forcing i have done 
#get winner function to check


#is board full function to check

#minimax function (we get the score of a board), it should take in the board and whether it is AI's turn or not)
# does AI's imagined turn, if its ai's turn. it does that math and it calculates the score if we take minimax of the same board but it is human's turn
#does humans imagined turn work, we do the same thing as the old one

# hopefully i figure this out more as i go through it... i want to make it work with tk tho so new file time, this step took fOREVER























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