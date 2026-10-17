#v4
# hopefully algo works now, then i can start working on smth new. been tuning this last 2 days...             

X = 0

       
r1 = X
r2 = X
r3 = X
r4 = X
r5 = X
r6 = X
r7 = 9
r8 = X
r9 = 7

       
r10 = X
r11 = X
r12 = X
r13 = 4
r14 = 2
r15 = X
r16 = 1
r17 = 8
r18 = X

       
r19 = X
r20 = X
r21 = X
r22 = 7
r23 = X
r24 = 5
r25 = X
r26 = 2
r27 = 6

       
r28 = 1
r29 = X
r30 = X
r31 = 9
r32 = X
r33 = 4
r34 = X
r35 = X
r36 = X

       
r37 = X
r38 = 5
r39 = X
r40 = X
r41 = X
r42 = X
r43 = X
r44 = 4
r45 = X

       
r46 = X
r47 = X
r48 = X
r49 = 5
r50 = X
r51 = 7
r52 = X
r53 = X
r54 = 9

       
r55 = 9
r56 = 2
r57 = X
r58 = 1
r59 = X
r60 = 8
r61 = X
r62 = X
r63 = X

       
r64 = X
r65 = 3
r66 = 4
r67 = X
r68 = 5
r69 = 9
r70 = X
r71 = X
r72 = X

       
r73 = 5
r74 = X
r75 = 7
r76 = X
r77 = X
r78 = X
r79 = X
r80 = X
r81 = X

board = [
    r1, r2, r3, r4, r5, r6, r7, r8, r9,
    r10, r11, r12, r13, r14, r15, r16, r17, r18,
    r19, r20, r21, r22, r23, r24, r25, r26, r27,
    r28, r29, r30, r31, r32, r33, r34, r35, r36,
    r37, r38, r39, r40, r41, r42, r43, r44, r45,
    r46, r47, r48, r49, r50, r51, r52, r53, r54,
    r55, r56, r57, r58, r59, r60, r61, r62, r63,
    r64, r65, r66, r67, r68, r69, r70, r71, r72,
    r73, r74, r75, r76, r77, r78, r79, r80, r81,
]

given = []
for i in range(81):
    if board[i] == 0:
        given.append(0)
    else:
        given.append(1)

def check_everything(b):
                                                    

           
    g = [b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

           
    g = [b[9], b[10], b[11], b[12], b[13], b[14], b[15], b[16], b[17]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

           
    g = [b[18], b[19], b[20], b[21], b[22], b[23], b[24], b[25], b[26]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

           
    g = [b[27], b[28], b[29], b[30], b[31], b[32], b[33], b[34], b[35]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

           
    g = [b[36], b[37], b[38], b[39], b[40], b[41], b[42], b[43], b[44]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

           
    g = [b[45], b[46], b[47], b[48], b[49], b[50], b[51], b[52], b[53]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

           
    g = [b[54], b[55], b[56], b[57], b[58], b[59], b[60], b[61], b[62]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

           
    g = [b[63], b[64], b[65], b[66], b[67], b[68], b[69], b[70], b[71]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

           
    g = [b[72], b[73], b[74], b[75], b[76], b[77], b[78], b[79], b[80]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[0], b[9], b[18], b[27], b[36], b[45], b[54], b[63], b[72]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[1], b[10], b[19], b[28], b[37], b[46], b[55], b[64], b[73]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[2], b[11], b[20], b[29], b[38], b[47], b[56], b[65], b[74]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[3], b[12], b[21], b[30], b[39], b[48], b[57], b[66], b[75]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[4], b[13], b[22], b[31], b[40], b[49], b[58], b[67], b[76]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[5], b[14], b[23], b[32], b[41], b[50], b[59], b[68], b[77]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[6], b[15], b[24], b[33], b[42], b[51], b[60], b[69], b[78]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[7], b[16], b[25], b[34], b[43], b[52], b[61], b[70], b[79]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[8], b[17], b[26], b[35], b[44], b[53], b[62], b[71], b[80]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[0], b[1], b[2], b[9], b[10], b[11], b[18], b[19], b[20]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[3], b[4], b[5], b[12], b[13], b[14], b[21], b[22], b[23]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[6], b[7], b[8], b[15], b[16], b[17], b[24], b[25], b[26]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[27], b[28], b[29], b[36], b[37], b[38], b[45], b[46], b[47]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[30], b[31], b[32], b[39], b[40], b[41], b[48], b[49], b[50]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[33], b[34], b[35], b[42], b[43], b[44], b[51], b[52], b[53]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[54], b[55], b[56], b[63], b[64], b[65], b[72], b[73], b[74]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[57], b[58], b[59], b[66], b[67], b[68], b[75], b[76], b[77]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    g = [b[60], b[61], b[62], b[69], b[70], b[71], b[78], b[79], b[80]]
    for i in range(9):
        for j in range(9):
            if i != j:
                if g[i] != 0:
                    if g[i] == g[j]:
                        return False

    return True

                         
pos = 0
going_back = False
steps = 0

while pos >= 0 and pos < 81:
    steps = steps + 1
                              
    if given[pos] == 1:
        if going_back == True:
            pos = pos - 1
        else:
            pos = pos + 1
        continue
    going_back = False
    board[pos] = board[pos] + 1
    if board[pos] > 9:
                                                         
        board[pos] = 0
        going_back = True
        pos = pos - 1
        continue
                                                   
    copy = []
    for k in range(81):
        copy.append(board[k])
    if check_everything(copy) == True:
        pos = pos + 1

                    

if pos < 0:
    print("no solution found :(")
else:
    row1 = str(board[0]) + str(board[1]) + str(board[2]) + str(board[3]) + str(board[4]) + str(board[5]) + str(board[6]) + str(board[7]) + str(board[8])
    row2 = str(board[9]) + str(board[10]) + str(board[11]) + str(board[12]) + str(board[13]) + str(board[14]) + str(board[15]) + str(board[16]) + str(board[17])
    row3 = str(board[18]) + str(board[19]) + str(board[20]) + str(board[21]) + str(board[22]) + str(board[23]) + str(board[24]) + str(board[25]) + str(board[26])
    row4 = str(board[27]) + str(board[28]) + str(board[29]) + str(board[30]) + str(board[31]) + str(board[32]) + str(board[33]) + str(board[34]) + str(board[35])
    row5 = str(board[36]) + str(board[37]) + str(board[38]) + str(board[39]) + str(board[40]) + str(board[41]) + str(board[42]) + str(board[43]) + str(board[44])
    row6 = str(board[45]) + str(board[46]) + str(board[47]) + str(board[48]) + str(board[49]) + str(board[50]) + str(board[51]) + str(board[52]) + str(board[53])
    row7 = str(board[54]) + str(board[55]) + str(board[56]) + str(board[57]) + str(board[58]) + str(board[59]) + str(board[60]) + str(board[61]) + str(board[62])
    row8 = str(board[63]) + str(board[64]) + str(board[65]) + str(board[66]) + str(board[67]) + str(board[68]) + str(board[69]) + str(board[70]) + str(board[71])
    row9 = str(board[72]) + str(board[73]) + str(board[74]) + str(board[75]) + str(board[76]) + str(board[77]) + str(board[78]) + str(board[79]) + str(board[80])
    print(row1 + " " + row2 + " " + row3 + " " + row4 + " " + row5 + " " + row6 + " " + row7 + " " + row8 + " " + row9)
