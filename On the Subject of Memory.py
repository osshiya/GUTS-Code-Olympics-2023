n = 4
stages = 5
lst =  [[1,3,2,4,1], [3,1,2,4,3], [2,3,4,1,2], [2,1,4,3,1], [4,1,2,3,4]]

def byPos(lst, i, buttonp):
    return lst[i][buttonp]

def byLabel(lst, i, buttonx):
    for j in range(n):
        if lst[i][j] == buttonx:
            return j 

for i in range(stages):
    # for j in range(n):

    p = lst[i][n]

    if i == 0: #stage 1
        if p == 1 or p == 2:
            button1p = 1 #2nd pos
            button1 = byPos(lst, i, button1p)
        elif p ==3:
            button1p = 2 #3nd pos
            button1 = byPos(lst, i, button1p)
        elif p ==4:
            button1p = 3 #4nd pos
            button1 = byPos(lst, i, button1p)
        print (button1)

    elif i == 1: #stage 2
        if p == 1:
            button2 = 4
            button2p = byLabel(lst, i, button2)
        elif p ==3:
            button2p = 0 #1st pos
            button2 = byPos(lst, i, button2p)
        elif p==2 or p ==4:
            button2p = button1p
            button2 = byPos(lst, i, button2p)
        print (button2)

    elif i == 2: #stage 3
        if p == 1:
            button3 = button2
            button3p = byLabel(lst, i, button3)
        elif p == 2:
            button3 = button1
            button3p = byLabel(lst, i, button3)
        elif p ==3:
            button3p = 2
            button3 = byPos(lst, i, button3p)
        elif p ==4:
            button3 = 4 #button labelled 4
            button3p = byLabel(lst, i, button3)
        print (button3)

    elif i == 3: #stage 4
        if p == 1:
            button4p = button1p
            button4 = byPos(lst, i, button4p)
        elif p == 2:
            button4p = 1
            button4 = byPos(lst, i, button4p)
        elif p ==3 or p== 4:
            button4p = button2p
            button4 = byPos(lst, i, button4p)
        print(button4)

    elif i == 4: #stage 5
        if p == 1:
            button5p = button1p
            button5 = byPos(lst, i, button5p)
        elif p == 2:
            button5p = button2p
            button5 = byPos(lst, i, button5p)
        elif p ==3:
            button5p = button3p
            button5 = byPos(lst, i, button5p)
        elif p ==4:
            button5p = button4p            
            button5 = byPos(lst, i, button5p)
        print(button5)
