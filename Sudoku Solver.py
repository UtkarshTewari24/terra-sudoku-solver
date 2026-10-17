# sudoku solver v2

X = 0  # empty spot

# row 1
r1 = X
r2 = X
r3 = X
r4 = X
r5 = X
r6 = X
r7 = 9
r8 = X
r9 = 7

# row 2
r10 = X
r11 = X
r12 = X
r13 = 4
r14 = 2
r15 = X
r16 = 1
r17 = 8
r18 = X

# row 3
r19 = X
r20 = X
r21 = X
r22 = 7
r23 = X
r24 = 5
r25 = X
r26 = 2
r27 = 6

# row 4
r28 = 1
r29 = X
r30 = X
r31 = 9
r32 = X
r33 = 4
r34 = X
r35 = X
r36 = X

# row 5
r37 = X
r38 = 5
r39 = X
r40 = X
r41 = X
r42 = X
r43 = X
r44 = 4
r45 = X

# row 6
r46 = X
r47 = X
r48 = X
r49 = 5
r50 = X
r51 = 7
r52 = X
r53 = X
r54 = 9

# row 7
r55 = 9
r56 = 2
r57 = X
r58 = 1
r59 = X
r60 = 8
r61 = X
r62 = X
r63 = X

# row 8
r64 = X
r65 = 3
r66 = 4
r67 = X
r68 = 5
r69 = 9
r70 = X
r71 = X
r72 = X

# row 9
r73 = 5
r74 = X
r75 = 7
r76 = X
r77 = X
r78 = X
r79 = X
r80 = X
r81 = X

# pick a number not already in the row or column
def pick(row, col):
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if n not in row:
            if n not in col:
                return n
    return 0

# first pass genuine wall of if statements, i no use copy paste or ai autofill so its gg para me

if r1 == X:
    r1 = pick([r1, r2, r3, r4, r5, r6, r7, r8, r9], [r1, r10, r19, r28, r37, r46, r55, r64, r73])
if r2 == X:
    r2 = pick([r1, r2, r3, r4, r5, r6, r7, r8, r9], [r2, r11, r20, r29, r38, r47, r56, r65, r74])
if r3 == X:
    r3 = pick([r1, r2, r3, r4, r5, r6, r7, r8, r9], [r3, r12, r21, r30, r39, r48, r57, r66, r75])
if r4 == X:
    r4 = pick([r1, r2, r3, r4, r5, r6, r7, r8, r9], [r4, r13, r22, r31, r40, r49, r58, r67, r76])
if r5 == X:
    r5 = pick([r1, r2, r3, r4, r5, r6, r7, r8, r9], [r5, r14, r23, r32, r41, r50, r59, r68, r77])
if r6 == X:
    r6 = pick([r1, r2, r3, r4, r5, r6, r7, r8, r9], [r6, r15, r24, r33, r42, r51, r60, r69, r78])
if r8 == X:
    r8 = pick([r1, r2, r3, r4, r5, r6, r7, r8, r9], [r8, r17, r26, r35, r44, r53, r62, r71, r80])
if r10 == X:
    r10 = pick([r10, r11, r12, r13, r14, r15, r16, r17, r18], [r1, r10, r19, r28, r37, r46, r55, r64, r73])
if r11 == X:
    r11 = pick([r10, r11, r12, r13, r14, r15, r16, r17, r18], [r2, r11, r20, r29, r38, r47, r56, r65, r74])
if r12 == X:
    r12 = pick([r10, r11, r12, r13, r14, r15, r16, r17, r18], [r3, r12, r21, r30, r39, r48, r57, r66, r75])
if r15 == X:
    r15 = pick([r10, r11, r12, r13, r14, r15, r16, r17, r18], [r6, r15, r24, r33, r42, r51, r60, r69, r78])
if r18 == X:
    r18 = pick([r10, r11, r12, r13, r14, r15, r16, r17, r18], [r9, r18, r27, r36, r45, r54, r63, r72, r81])
if r19 == X:
    r19 = pick([r19, r20, r21, r22, r23, r24, r25, r26, r27], [r1, r10, r19, r28, r37, r46, r55, r64, r73])
if r20 == X:
    r20 = pick([r19, r20, r21, r22, r23, r24, r25, r26, r27], [r2, r11, r20, r29, r38, r47, r56, r65, r74])
if r21 == X:
    r21 = pick([r19, r20, r21, r22, r23, r24, r25, r26, r27], [r3, r12, r21, r30, r39, r48, r57, r66, r75])
if r23 == X:
    r23 = pick([r19, r20, r21, r22, r23, r24, r25, r26, r27], [r5, r14, r23, r32, r41, r50, r59, r68, r77])
if r25 == X:
    r25 = pick([r19, r20, r21, r22, r23, r24, r25, r26, r27], [r7, r16, r25, r34, r43, r52, r61, r70, r79])
if r29 == X:
    r29 = pick([r28, r29, r30, r31, r32, r33, r34, r35, r36], [r2, r11, r20, r29, r38, r47, r56, r65, r74])
if r30 == X:
    r30 = pick([r28, r29, r30, r31, r32, r33, r34, r35, r36], [r3, r12, r21, r30, r39, r48, r57, r66, r75])
if r32 == X:
    r32 = pick([r28, r29, r30, r31, r32, r33, r34, r35, r36], [r5, r14, r23, r32, r41, r50, r59, r68, r77])
if r34 == X:
    r34 = pick([r28, r29, r30, r31, r32, r33, r34, r35, r36], [r7, r16, r25, r34, r43, r52, r61, r70, r79])
if r35 == X:
    r35 = pick([r28, r29, r30, r31, r32, r33, r34, r35, r36], [r8, r17, r26, r35, r44, r53, r62, r71, r80])
if r36 == X:
    r36 = pick([r28, r29, r30, r31, r32, r33, r34, r35, r36], [r9, r18, r27, r36, r45, r54, r63, r72, r81])
if r37 == X:
    r37 = pick([r37, r38, r39, r40, r41, r42, r43, r44, r45], [r1, r10, r19, r28, r37, r46, r55, r64, r73])
if r39 == X:
    r39 = pick([r37, r38, r39, r40, r41, r42, r43, r44, r45], [r3, r12, r21, r30, r39, r48, r57, r66, r75])
if r40 == X:
    r40 = pick([r37, r38, r39, r40, r41, r42, r43, r44, r45], [r4, r13, r22, r31, r40, r49, r58, r67, r76])
if r41 == X:
    r41 = pick([r37, r38, r39, r40, r41, r42, r43, r44, r45], [r5, r14, r23, r32, r41, r50, r59, r68, r77])
if r42 == X:
    r42 = pick([r37, r38, r39, r40, r41, r42, r43, r44, r45], [r6, r15, r24, r33, r42, r51, r60, r69, r78])
if r43 == X:
    r43 = pick([r37, r38, r39, r40, r41, r42, r43, r44, r45], [r7, r16, r25, r34, r43, r52, r61, r70, r79])
if r45 == X:
    r45 = pick([r37, r38, r39, r40, r41, r42, r43, r44, r45], [r9, r18, r27, r36, r45, r54, r63, r72, r81])
if r46 == X:
    r46 = pick([r46, r47, r48, r49, r50, r51, r52, r53, r54], [r1, r10, r19, r28, r37, r46, r55, r64, r73])
if r47 == X:
    r47 = pick([r46, r47, r48, r49, r50, r51, r52, r53, r54], [r2, r11, r20, r29, r38, r47, r56, r65, r74])
if r48 == X:
    r48 = pick([r46, r47, r48, r49, r50, r51, r52, r53, r54], [r3, r12, r21, r30, r39, r48, r57, r66, r75])
if r50 == X:
    r50 = pick([r46, r47, r48, r49, r50, r51, r52, r53, r54], [r5, r14, r23, r32, r41, r50, r59, r68, r77])
if r52 == X:
    r52 = pick([r46, r47, r48, r49, r50, r51, r52, r53, r54], [r7, r16, r25, r34, r43, r52, r61, r70, r79])
if r53 == X:
    r53 = pick([r46, r47, r48, r49, r50, r51, r52, r53, r54], [r8, r17, r26, r35, r44, r53, r62, r71, r80])
if r57 == X:
    r57 = pick([r55, r56, r57, r58, r59, r60, r61, r62, r63], [r3, r12, r21, r30, r39, r48, r57, r66, r75])
if r59 == X:
    r59 = pick([r55, r56, r57, r58, r59, r60, r61, r62, r63], [r5, r14, r23, r32, r41, r50, r59, r68, r77])
if r61 == X:
    r61 = pick([r55, r56, r57, r58, r59, r60, r61, r62, r63], [r7, r16, r25, r34, r43, r52, r61, r70, r79])
if r62 == X:
    r62 = pick([r55, r56, r57, r58, r59, r60, r61, r62, r63], [r8, r17, r26, r35, r44, r53, r62, r71, r80])
if r63 == X:
    r63 = pick([r55, r56, r57, r58, r59, r60, r61, r62, r63], [r9, r18, r27, r36, r45, r54, r63, r72, r81])
if r64 == X:
    r64 = pick([r64, r65, r66, r67, r68, r69, r70, r71, r72], [r1, r10, r19, r28, r37, r46, r55, r64, r73])
if r67 == X:
    r67 = pick([r64, r65, r66, r67, r68, r69, r70, r71, r72], [r4, r13, r22, r31, r40, r49, r58, r67, r76])
if r70 == X:
    r70 = pick([r64, r65, r66, r67, r68, r69, r70, r71, r72], [r7, r16, r25, r34, r43, r52, r61, r70, r79])
if r71 == X:
    r71 = pick([r64, r65, r66, r67, r68, r69, r70, r71, r72], [r8, r17, r26, r35, r44, r53, r62, r71, r80])
if r72 == X:
    r72 = pick([r64, r65, r66, r67, r68, r69, r70, r71, r72], [r9, r18, r27, r36, r45, r54, r63, r72, r81])
if r74 == X:
    r74 = pick([r73, r74, r75, r76, r77, r78, r79, r80, r81], [r2, r11, r20, r29, r38, r47, r56, r65, r74])
if r76 == X:
    r76 = pick([r73, r74, r75, r76, r77, r78, r79, r80, r81], [r4, r13, r22, r31, r40, r49, r58, r67, r76])
if r77 == X:
    r77 = pick([r73, r74, r75, r76, r77, r78, r79, r80, r81], [r5, r14, r23, r32, r41, r50, r59, r68, r77])
if r78 == X:
    r78 = pick([r73, r74, r75, r76, r77, r78, r79, r80, r81], [r6, r15, r24, r33, r42, r51, r60, r69, r78])
if r79 == X:
    r79 = pick([r73, r74, r75, r76, r77, r78, r79, r80, r81], [r7, r16, r25, r34, r43, r52, r61, r70, r79])
if r80 == X:
    r80 = pick([r73, r74, r75, r76, r77, r78, r79, r80, r81], [r8, r17, r26, r35, r44, r53, r62, r71, r80])
if r81 == X:
    r81 = pick([r73, r74, r75, r76, r77, r78, r79, r80, r81], [r9, r18, r27, r36, r45, r54, r63, r72, r81])

# try again with the updated board (i might cry)

if r1 == X:
    r1 = pick([r1, r2, r3, r4, r5, r6, r7, r8, r9], [r1, r10, r19, r28, r37, r46, r55, r64, r73])
if r2 == X:
    r2 = pick([r1, r2, r3, r4, r5, r6, r7, r8, r9], [r2, r11, r20, r29, r38, r47, r56, r65, r74])
if r3 == X:
    r3 = pick([r1, r2, r3, r4, r5, r6, r7, r8, r9], [r3, r12, r21, r30, r39, r48, r57, r66, r75])
if r4 == X:
    r4 = pick([r1, r2, r3, r4, r5, r6, r7, r8, r9], [r4, r13, r22, r31, r40, r49, r58, r67, r76])
if r5 == X:
    r5 = pick([r1, r2, r3, r4, r5, r6, r7, r8, r9], [r5, r14, r23, r32, r41, r50, r59, r68, r77])
if r6 == X:
    r6 = pick([r1, r2, r3, r4, r5, r6, r7, r8, r9], [r6, r15, r24, r33, r42, r51, r60, r69, r78])
if r8 == X:
    r8 = pick([r1, r2, r3, r4, r5, r6, r7, r8, r9], [r8, r17, r26, r35, r44, r53, r62, r71, r80])
if r10 == X:
    r10 = pick([r10, r11, r12, r13, r14, r15, r16, r17, r18], [r1, r10, r19, r28, r37, r46, r55, r64, r73])
if r11 == X:
    r11 = pick([r10, r11, r12, r13, r14, r15, r16, r17, r18], [r2, r11, r20, r29, r38, r47, r56, r65, r74])
if r12 == X:
    r12 = pick([r10, r11, r12, r13, r14, r15, r16, r17, r18], [r3, r12, r21, r30, r39, r48, r57, r66, r75])
if r15 == X:
    r15 = pick([r10, r11, r12, r13, r14, r15, r16, r17, r18], [r6, r15, r24, r33, r42, r51, r60, r69, r78])
if r18 == X:
    r18 = pick([r10, r11, r12, r13, r14, r15, r16, r17, r18], [r9, r18, r27, r36, r45, r54, r63, r72, r81])
if r19 == X:
    r19 = pick([r19, r20, r21, r22, r23, r24, r25, r26, r27], [r1, r10, r19, r28, r37, r46, r55, r64, r73])
if r20 == X:
    r20 = pick([r19, r20, r21, r22, r23, r24, r25, r26, r27], [r2, r11, r20, r29, r38, r47, r56, r65, r74])
if r21 == X:
    r21 = pick([r19, r20, r21, r22, r23, r24, r25, r26, r27], [r3, r12, r21, r30, r39, r48, r57, r66, r75])
if r23 == X:
    r23 = pick([r19, r20, r21, r22, r23, r24, r25, r26, r27], [r5, r14, r23, r32, r41, r50, r59, r68, r77])
if r25 == X:
    r25 = pick([r19, r20, r21, r22, r23, r24, r25, r26, r27], [r7, r16, r25, r34, r43, r52, r61, r70, r79])
if r29 == X:
    r29 = pick([r28, r29, r30, r31, r32, r33, r34, r35, r36], [r2, r11, r20, r29, r38, r47, r56, r65, r74])
if r30 == X:
    r30 = pick([r28, r29, r30, r31, r32, r33, r34, r35, r36], [r3, r12, r21, r30, r39, r48, r57, r66, r75])
if r32 == X:
    r32 = pick([r28, r29, r30, r31, r32, r33, r34, r35, r36], [r5, r14, r23, r32, r41, r50, r59, r68, r77])
if r34 == X:
    r34 = pick([r28, r29, r30, r31, r32, r33, r34, r35, r36], [r7, r16, r25, r34, r43, r52, r61, r70, r79])
if r35 == X:
    r35 = pick([r28, r29, r30, r31, r32, r33, r34, r35, r36], [r8, r17, r26, r35, r44, r53, r62, r71, r80])
if r36 == X:
    r36 = pick([r28, r29, r30, r31, r32, r33, r34, r35, r36], [r9, r18, r27, r36, r45, r54, r63, r72, r81])
if r37 == X:
    r37 = pick([r37, r38, r39, r40, r41, r42, r43, r44, r45], [r1, r10, r19, r28, r37, r46, r55, r64, r73])
if r39 == X:
    r39 = pick([r37, r38, r39, r40, r41, r42, r43, r44, r45], [r3, r12, r21, r30, r39, r48, r57, r66, r75])
if r40 == X:
    r40 = pick([r37, r38, r39, r40, r41, r42, r43, r44, r45], [r4, r13, r22, r31, r40, r49, r58, r67, r76])
if r41 == X:
    r41 = pick([r37, r38, r39, r40, r41, r42, r43, r44, r45], [r5, r14, r23, r32, r41, r50, r59, r68, r77])
if r42 == X:
    r42 = pick([r37, r38, r39, r40, r41, r42, r43, r44, r45], [r6, r15, r24, r33, r42, r51, r60, r69, r78])
if r43 == X:
    r43 = pick([r37, r38, r39, r40, r41, r42, r43, r44, r45], [r7, r16, r25, r34, r43, r52, r61, r70, r79])
if r45 == X:
    r45 = pick([r37, r38, r39, r40, r41, r42, r43, r44, r45], [r9, r18, r27, r36, r45, r54, r63, r72, r81])
if r46 == X:
    r46 = pick([r46, r47, r48, r49, r50, r51, r52, r53, r54], [r1, r10, r19, r28, r37, r46, r55, r64, r73])
if r47 == X:
    r47 = pick([r46, r47, r48, r49, r50, r51, r52, r53, r54], [r2, r11, r20, r29, r38, r47, r56, r65, r74])
if r48 == X:
    r48 = pick([r46, r47, r48, r49, r50, r51, r52, r53, r54], [r3, r12, r21, r30, r39, r48, r57, r66, r75])
if r50 == X:
    r50 = pick([r46, r47, r48, r49, r50, r51, r52, r53, r54], [r5, r14, r23, r32, r41, r50, r59, r68, r77])
if r52 == X:
    r52 = pick([r46, r47, r48, r49, r50, r51, r52, r53, r54], [r7, r16, r25, r34, r43, r52, r61, r70, r79])
if r53 == X:
    r53 = pick([r46, r47, r48, r49, r50, r51, r52, r53, r54], [r8, r17, r26, r35, r44, r53, r62, r71, r80])
if r57 == X:
    r57 = pick([r55, r56, r57, r58, r59, r60, r61, r62, r63], [r3, r12, r21, r30, r39, r48, r57, r66, r75])
if r59 == X:
    r59 = pick([r55, r56, r57, r58, r59, r60, r61, r62, r63], [r5, r14, r23, r32, r41, r50, r59, r68, r77])
if r61 == X:
    r61 = pick([r55, r56, r57, r58, r59, r60, r61, r62, r63], [r7, r16, r25, r34, r43, r52, r61, r70, r79])
if r62 == X:
    r62 = pick([r55, r56, r57, r58, r59, r60, r61, r62, r63], [r8, r17, r26, r35, r44, r53, r62, r71, r80])
if r63 == X:
    r63 = pick([r55, r56, r57, r58, r59, r60, r61, r62, r63], [r9, r18, r27, r36, r45, r54, r63, r72, r81])
if r64 == X:
    r64 = pick([r64, r65, r66, r67, r68, r69, r70, r71, r72], [r1, r10, r19, r28, r37, r46, r55, r64, r73])
if r67 == X:
    r67 = pick([r64, r65, r66, r67, r68, r69, r70, r71, r72], [r4, r13, r22, r31, r40, r49, r58, r67, r76])
if r70 == X:
    r70 = pick([r64, r65, r66, r67, r68, r69, r70, r71, r72], [r7, r16, r25, r34, r43, r52, r61, r70, r79])
if r71 == X:
    r71 = pick([r64, r65, r66, r67, r68, r69, r70, r71, r72], [r8, r17, r26, r35, r44, r53, r62, r71, r80])
if r72 == X:
    r72 = pick([r64, r65, r66, r67, r68, r69, r70, r71, r72], [r9, r18, r27, r36, r45, r54, r63, r72, r81])
if r74 == X:
    r74 = pick([r73, r74, r75, r76, r77, r78, r79, r80, r81], [r2, r11, r20, r29, r38, r47, r56, r65, r74])
if r76 == X:
    r76 = pick([r73, r74, r75, r76, r77, r78, r79, r80, r81], [r4, r13, r22, r31, r40, r49, r58, r67, r76])
if r77 == X:
    r77 = pick([r73, r74, r75, r76, r77, r78, r79, r80, r81], [r5, r14, r23, r32, r41, r50, r59, r68, r77])
if r78 == X:
    r78 = pick([r73, r74, r75, r76, r77, r78, r79, r80, r81], [r6, r15, r24, r33, r42, r51, r60, r69, r78])
if r79 == X:
    r79 = pick([r73, r74, r75, r76, r77, r78, r79, r80, r81], [r7, r16, r25, r34, r43, r52, r61, r70, r79])
if r80 == X:
    r80 = pick([r73, r74, r75, r76, r77, r78, r79, r80, r81], [r8, r17, r26, r35, r44, r53, r62, r71, r80])
if r81 == X:
    r81 = pick([r73, r74, r75, r76, r77, r78, r79, r80, r81], [r9, r18, r27, r36, r45, r54, r63, r72, r81])

# print the board shitttt my fingers finna hurt

row1 = str(r1) + str(r2) + str(r3) + str(r4) + str(r5) + str(r6) + str(r7) + str(r8) + str(r9)
row2 = str(r10) + str(r11) + str(r12) + str(r13) + str(r14) + str(r15) + str(r16) + str(r17) + str(r18)
row3 = str(r19) + str(r20) + str(r21) + str(r22) + str(r23) + str(r24) + str(r25) + str(r26) + str(r27)
row4 = str(r28) + str(r29) + str(r30) + str(r31) + str(r32) + str(r33) + str(r34) + str(r35) + str(r36)
row5 = str(r37) + str(r38) + str(r39) + str(r40) + str(r41) + str(r42) + str(r43) + str(r44) + str(r45)
row6 = str(r46) + str(r47) + str(r48) + str(r49) + str(r50) + str(r51) + str(r52) + str(r53) + str(r54)
row7 = str(r55) + str(r56) + str(r57) + str(r58) + str(r59) + str(r60) + str(r61) + str(r62) + str(r63)
row8 = str(r64) + str(r65) + str(r66) + str(r67) + str(r68) + str(r69) + str(r70) + str(r71) + str(r72)
row9 = str(r73) + str(r74) + str(r75) + str(r76) + str(r77) + str(r78) + str(r79) + str(r80) + str(r81)

print(row1 + " " + row2 + " " + row3 + " " + row4 + " " + row5 + " " + row6 + " " + row7 + " " + row8 + " " + row9)
#my pinky finger genuinely hurts when i press enter or move it outside its lowk stuck to my ring finger like i aint even kidding send help and allat still ts doesnt work im genuinely finna crash out bro