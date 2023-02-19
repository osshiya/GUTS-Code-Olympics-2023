s = [['+', '-', '+', '-', '+', '-', '+'], #One Way With No DeadEnd/ Case used

['|', ' ', ' ', ' ', ' ', ' ', '|'],

['+', ' ', '+', '-', '+', ' ', '+'],

['|', ' ', ' ', 'F', '|', ' ', '|'],

['+', '-', '+', '-', '+', ' ', '+'],

['|', '$', ' ', ' ', ' ', ' ', '|'],

['+', '-', '+', '-', '+', '-', '+']]

case2 = [['+', '-', '+', '-', '+', '-', '+'], #Two Way With 1 DeadEnd

['|', ' ', ' ', ' ', ' ', ' ', '|'],

['+', ' ', '+', '-', '+', ' ', '+'],

['|', ' ', ' ', 'F', '|', ' ', '|'],

['+', ' ', '+', '-', '+', '-', '+'],

['|', '$', ' ', ' ', ' ', ' ', '|'],

['+', '-', '+', '-', '+', '-', '+']]
t = 7
pos = []
path = ["=>"]
    
def check(s, pm, pn): #Check Around Snake's Pos Surroundings
    print ("DOWN:",s[pm+1][pn], s[pm+1][pn] == " ")
    print ("UP:",s[pm-1][pn])
    print ("R:",s[pm][pn+1])
    print ("L:",s[pm][pn-1])
    print(pm, pn)

def map(s, m, n): #Map out current in checkEmptySpace
    for m in range(len(s)):
        for n in range(t):
            print(s[m][n], end="")
        print("\n")

def checkFood(s, path, pm, pn):
    if s[pm+1][pn] == "F":
        return path.append("down")
    elif s[pm-1][pn] == "F":
        return path.append("up")
    elif s[pm][pn+1] == "F":
        return path.append("right")
    elif s[pm][pn-1] == "F":
        return path.append("left")
    else:
        return 0
    
def checkEmptySpace(s, path, pm, pn):
    # s[pm][pn] = "$" //Snake Current Position
    # map(s, pm, pn) //Snake Current Position on Map
    if checkFood(s, path, pm, pn) != 0:
        return path
    elif(s[pm][pn+1]) == " " and path[-1] != "left":
        s[pm][pn] = " "
        path.append("right")
        checkEmptySpace(s, path, pm, pn+1)
    elif(s[pm][pn-1]) == " " and path[-1] != "right":
        s[pm][pn] = " "
        path.append("left")
        checkEmptySpace(s, path, pm, pn-1)
    elif(s[pm-1][pn]) == " " and path[-1] != "down":
        s[pm][pn] = " "
        path.append("up")
        checkEmptySpace(s, path, pm-1, pn)
    elif(s[pm+1][pn]) == " " and path[-1] != "up":
        s[pm][pn] = " "
        path.append("down")
        checkEmptySpace(s, path, pm+1, pn)

    else:
        if path[-1] == "up":
            s[pm][pn] = " "
            path.append("down")
            checkEmptySpace(s, path, pm+1, pn)
        elif path[-1] == "down":
            s[pm][pn] = " "
            path.append("up")
            checkEmptySpace(s, path, pm-1, pn)
        elif path[-1] == "right":
            s[pm][pn] = " "
            path.append("left")
            checkEmptySpace(s, path, pm, pn-1)
        elif path[-1] == "left":
            s[pm][pn] = " "
            path.append("right")
            checkEmptySpace(s, path, pm, pn+1)
        else:
            # check(s, pm, pn) //Check Surrounding Elements
            exit()
    
# --------------------------------- Driver Code

for m in range(len(s)):
    for n in range(t):
        if(s[m][n] == "$"):
            pos.append(m)
            pos.append(n)
        print(s[m][n], end="") #Initial map
    print("\n")
checkEmptySpace(s, path, pos[0], pos[1])
print(*path)

