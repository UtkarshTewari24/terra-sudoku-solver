#v3 gonna crash out
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
#ouu shii first function (lowk needed this) uh um hope this works idk i had this in my logic diagram hardcoded but its so much easier to just learn functions instead
def cands(used):
    out = []
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if n not in used:
            out.append(n)
    return out

if r1 == X:
    c = cands([r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r19, r20, r21, r28, r37, r46, r55, r64, r73])
    if len(c) == 1:
        r1 = c[0]
if r2 == X:
    c = cands([r1, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r19, r20, r21, r29, r38, r47, r56, r65, r74])
    if len(c) == 1:
        r2 = c[0]
if r3 == X:
    c = cands([r1, r2, r4, r5, r6, r7, r8, r9, r10, r11, r12, r19, r20, r21, r30, r39, r48, r57, r66, r75])
    if len(c) == 1:
        r3 = c[0]
if r4 == X:
    c = cands([r1, r2, r3, r5, r6, r7, r8, r9, r13, r14, r15, r22, r23, r24, r31, r40, r49, r58, r67, r76])
    if len(c) == 1:
        r4 = c[0]
if r5 == X:
    c = cands([r1, r2, r3, r4, r6, r7, r8, r9, r13, r14, r15, r22, r23, r24, r32, r41, r50, r59, r68, r77])
    if len(c) == 1:
        r5 = c[0]
if r6 == X:
    c = cands([r1, r2, r3, r4, r5, r7, r8, r9, r13, r14, r15, r22, r23, r24, r33, r42, r51, r60, r69, r78])
    if len(c) == 1:
        r6 = c[0]
if r8 == X:
    c = cands([r1, r2, r3, r4, r5, r6, r7, r9, r16, r17, r18, r25, r26, r27, r35, r44, r53, r62, r71, r80])
    if len(c) == 1:
        r8 = c[0]
if r10 == X:
    c = cands([r1, r2, r3, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r28, r37, r46, r55, r64, r73])
    if len(c) == 1:
        r10 = c[0]
if r11 == X:
    c = cands([r1, r2, r3, r10, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r29, r38, r47, r56, r65, r74])
    if len(c) == 1:
        r11 = c[0]
if r12 == X:
    c = cands([r1, r2, r3, r10, r11, r13, r14, r15, r16, r17, r18, r19, r20, r21, r30, r39, r48, r57, r66, r75])
    if len(c) == 1:
        r12 = c[0]
if r15 == X:
    c = cands([r4, r5, r6, r10, r11, r12, r13, r14, r16, r17, r18, r22, r23, r24, r33, r42, r51, r60, r69, r78])
    if len(c) == 1:
        r15 = c[0]
if r18 == X:
    c = cands([r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r25, r26, r27, r36, r45, r54, r63, r72, r81])
    if len(c) == 1:
        r18 = c[0]
if r19 == X:
    c = cands([r1, r2, r3, r10, r11, r12, r20, r21, r22, r23, r24, r25, r26, r27, r28, r37, r46, r55, r64, r73])
    if len(c) == 1:
        r19 = c[0]
if r20 == X:
    c = cands([r1, r2, r3, r10, r11, r12, r19, r21, r22, r23, r24, r25, r26, r27, r29, r38, r47, r56, r65, r74])
    if len(c) == 1:
        r20 = c[0]
if r21 == X:
    c = cands([r1, r2, r3, r10, r11, r12, r19, r20, r22, r23, r24, r25, r26, r27, r30, r39, r48, r57, r66, r75])
    if len(c) == 1:
        r21 = c[0]
if r23 == X:
    c = cands([r4, r5, r6, r13, r14, r15, r19, r20, r21, r22, r24, r25, r26, r27, r32, r41, r50, r59, r68, r77])
    if len(c) == 1:
        r23 = c[0]
if r25 == X:
    c = cands([r7, r8, r9, r16, r17, r18, r19, r20, r21, r22, r23, r24, r26, r27, r34, r43, r52, r61, r70, r79])
    if len(c) == 1:
        r25 = c[0]
if r29 == X:
    c = cands([r2, r11, r20, r28, r30, r31, r32, r33, r34, r35, r36, r37, r38, r39, r46, r47, r48, r56, r65, r74])
    if len(c) == 1:
        r29 = c[0]
if r30 == X:
    c = cands([r3, r12, r21, r28, r29, r31, r32, r33, r34, r35, r36, r37, r38, r39, r46, r47, r48, r57, r66, r75])
    if len(c) == 1:
        r30 = c[0]
if r32 == X:
    c = cands([r5, r14, r23, r28, r29, r30, r31, r33, r34, r35, r36, r40, r41, r42, r49, r50, r51, r59, r68, r77])
    if len(c) == 1:
        r32 = c[0]
if r34 == X:
    c = cands([r7, r16, r25, r28, r29, r30, r31, r32, r33, r35, r36, r43, r44, r45, r52, r53, r54, r61, r70, r79])
    if len(c) == 1:
        r34 = c[0]
if r35 == X:
    c = cands([r8, r17, r26, r28, r29, r30, r31, r32, r33, r34, r36, r43, r44, r45, r52, r53, r54, r62, r71, r80])
    if len(c) == 1:
        r35 = c[0]
if r36 == X:
    c = cands([r9, r18, r27, r28, r29, r30, r31, r32, r33, r34, r35, r43, r44, r45, r52, r53, r54, r63, r72, r81])
    if len(c) == 1:
        r36 = c[0]
if r37 == X:
    c = cands([r1, r10, r19, r28, r29, r30, r38, r39, r40, r41, r42, r43, r44, r45, r46, r47, r48, r55, r64, r73])
    if len(c) == 1:
        r37 = c[0]
if r39 == X:
    c = cands([r3, r12, r21, r28, r29, r30, r37, r38, r40, r41, r42, r43, r44, r45, r46, r47, r48, r57, r66, r75])
    if len(c) == 1:
        r39 = c[0]
if r40 == X:
    c = cands([r4, r13, r22, r31, r32, r33, r37, r38, r39, r41, r42, r43, r44, r45, r49, r50, r51, r58, r67, r76])
    if len(c) == 1:
        r40 = c[0]
if r41 == X:
    c = cands([r5, r14, r23, r31, r32, r33, r37, r38, r39, r40, r42, r43, r44, r45, r49, r50, r51, r59, r68, r77])
    if len(c) == 1:
        r41 = c[0]
if r42 == X:
    c = cands([r6, r15, r24, r31, r32, r33, r37, r38, r39, r40, r41, r43, r44, r45, r49, r50, r51, r60, r69, r78])
    if len(c) == 1:
        r42 = c[0]
if r43 == X:
    c = cands([r7, r16, r25, r34, r35, r36, r37, r38, r39, r40, r41, r42, r44, r45, r52, r53, r54, r61, r70, r79])
    if len(c) == 1:
        r43 = c[0]
if r45 == X:
    c = cands([r9, r18, r27, r34, r35, r36, r37, r38, r39, r40, r41, r42, r43, r44, r52, r53, r54, r63, r72, r81])
    if len(c) == 1:
        r45 = c[0]
if r46 == X:
    c = cands([r1, r10, r19, r28, r29, r30, r37, r38, r39, r47, r48, r49, r50, r51, r52, r53, r54, r55, r64, r73])
    if len(c) == 1:
        r46 = c[0]
if r47 == X:
    c = cands([r2, r11, r20, r28, r29, r30, r37, r38, r39, r46, r48, r49, r50, r51, r52, r53, r54, r56, r65, r74])
    if len(c) == 1:
        r47 = c[0]
if r48 == X:
    c = cands([r3, r12, r21, r28, r29, r30, r37, r38, r39, r46, r47, r49, r50, r51, r52, r53, r54, r57, r66, r75])
    if len(c) == 1:
        r48 = c[0]
if r50 == X:
    c = cands([r5, r14, r23, r31, r32, r33, r40, r41, r42, r46, r47, r48, r49, r51, r52, r53, r54, r59, r68, r77])
    if len(c) == 1:
        r50 = c[0]
if r52 == X:
    c = cands([r7, r16, r25, r34, r35, r36, r43, r44, r45, r46, r47, r48, r49, r50, r51, r53, r54, r61, r70, r79])
    if len(c) == 1:
        r52 = c[0]
if r53 == X:
    c = cands([r8, r17, r26, r34, r35, r36, r43, r44, r45, r46, r47, r48, r49, r50, r51, r52, r54, r62, r71, r80])
    if len(c) == 1:
        r53 = c[0]
if r57 == X:
    c = cands([r3, r12, r21, r30, r39, r48, r55, r56, r58, r59, r60, r61, r62, r63, r64, r65, r66, r73, r74, r75])
    if len(c) == 1:
        r57 = c[0]
if r59 == X:
    c = cands([r5, r14, r23, r32, r41, r50, r55, r56, r57, r58, r60, r61, r62, r63, r67, r68, r69, r76, r77, r78])
    if len(c) == 1:
        r59 = c[0]
if r61 == X:
    c = cands([r7, r16, r25, r34, r43, r52, r55, r56, r57, r58, r59, r60, r62, r63, r70, r71, r72, r79, r80, r81])
    if len(c) == 1:
        r61 = c[0]
if r62 == X:
    c = cands([r8, r17, r26, r35, r44, r53, r55, r56, r57, r58, r59, r60, r61, r63, r70, r71, r72, r79, r80, r81])
    if len(c) == 1:
        r62 = c[0]
if r63 == X:
    c = cands([r9, r18, r27, r36, r45, r54, r55, r56, r57, r58, r59, r60, r61, r62, r70, r71, r72, r79, r80, r81])
    if len(c) == 1:
        r63 = c[0]
if r64 == X:
    c = cands([r1, r10, r19, r28, r37, r46, r55, r56, r57, r65, r66, r67, r68, r69, r70, r71, r72, r73, r74, r75])
    if len(c) == 1:
        r64 = c[0]
if r67 == X:
    c = cands([r4, r13, r22, r31, r40, r49, r58, r59, r60, r64, r65, r66, r68, r69, r70, r71, r72, r76, r77, r78])
    if len(c) == 1:
        r67 = c[0]
if r70 == X:
    c = cands([r7, r16, r25, r34, r43, r52, r61, r62, r63, r64, r65, r66, r67, r68, r69, r71, r72, r79, r80, r81])
    if len(c) == 1:
        r70 = c[0]
if r71 == X:
    c = cands([r8, r17, r26, r35, r44, r53, r61, r62, r63, r64, r65, r66, r67, r68, r69, r70, r72, r79, r80, r81])
    if len(c) == 1:
        r71 = c[0]
if r72 == X:
    c = cands([r9, r18, r27, r36, r45, r54, r61, r62, r63, r64, r65, r66, r67, r68, r69, r70, r71, r79, r80, r81])
    if len(c) == 1:
        r72 = c[0]
if r74 == X:
    c = cands([r2, r11, r20, r29, r38, r47, r55, r56, r57, r64, r65, r66, r73, r75, r76, r77, r78, r79, r80, r81])
    if len(c) == 1:
        r74 = c[0]
if r76 == X:
    c = cands([r4, r13, r22, r31, r40, r49, r58, r59, r60, r67, r68, r69, r73, r74, r75, r77, r78, r79, r80, r81])
    if len(c) == 1:
        r76 = c[0]
if r77 == X:
    c = cands([r5, r14, r23, r32, r41, r50, r58, r59, r60, r67, r68, r69, r73, r74, r75, r76, r78, r79, r80, r81])
    if len(c) == 1:
        r77 = c[0]
if r78 == X:
    c = cands([r6, r15, r24, r33, r42, r51, r58, r59, r60, r67, r68, r69, r73, r74, r75, r76, r77, r79, r80, r81])
    if len(c) == 1:
        r78 = c[0]
if r79 == X:
    c = cands([r7, r16, r25, r34, r43, r52, r61, r62, r63, r70, r71, r72, r73, r74, r75, r76, r77, r78, r80, r81])
    if len(c) == 1:
        r79 = c[0]
if r80 == X:
    c = cands([r8, r17, r26, r35, r44, r53, r61, r62, r63, r70, r71, r72, r73, r74, r75, r76, r77, r78, r79, r81])
    if len(c) == 1:
        r80 = c[0]
if r81 == X:
    c = cands([r9, r18, r27, r36, r45, r54, r61, r62, r63, r70, r71, r72, r73, r74, r75, r76, r77, r78, r79, r80])
    if len(c) == 1:
        r81 = c[0]
#finger bleeding rn
row1 = str(r1) + str(r2) + str(r3) + str(r4) + str(r5) + str(r6) + str(r7) + str(r8) + str(r9)
row2 = str(r10) + str(r11) + str(r12) + str(r13) + str(r14) + str(r15) + str(r16) + str(r17) + str(r18)
row3 = str(r19) + str(r20) + str(r21) + str(r22) + str(r23) + str(r24) + str(r25) + str(r26) + str(r27)
row4 = str(r28) + str(r29) + str(r30) + str(r31) + str(r32) + str(r33) + str(r34) + str(r35) + str(r36)
row5 = str(r37) + str(r38) + str(r39) + str(r40) + str(r41) + str(r42) + str(r43) + str(r44) + str(r45)
row6 = str(r46) + str(r47) + str(r48) + str(r49) + str(r50) + str(r51) + str(r52) + str(r53) + str(r54)
row7 = str(r55) + str(r56) + str(r57) + str(r58) + str(r59) + str(r60) + str(r61) + str(r62) + str(r63)
row8 = str(r64) + str(r65) + str(r66) + str(r67) + str(r68) + str(r69) + str(r70) + str(r71) + str(r72)
row9 = str(r73) + str(r74) + str(r75) + str(r76) + str(r77) + str(r78) + str(r79) + str(r80) + str(r81)
#finger bled more
print(row1 + " " + row2 + " " + row3 + " " + row4 + " " + row5 + " " + row6 + " " + row7 + " " + row8 + " " + row9)

#note in post: WHY DOESNT THIS WORK I DONT UNDERSTAND I THINK I DID IT RIGHT BUT IT DOESNT WORK