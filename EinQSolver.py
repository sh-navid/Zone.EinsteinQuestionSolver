#By Navid Shamshirsaz

import random
#what we have at all???
[#just for knowing - i do not use this
    ["EN", "SU", "DN", "NR", "GR"],  ##human
    ["GREEN", "WHITE", "RED", "BLUE", "YELLOW"],  ##color of houses
    ["BIRD", "HORSE", "DOG", "CAT", "FISH"],  ##pet
    ["BEER", "MILK", "COFFEE", "TEA", "UNKNOWN"],  ##drink
    ["DH", "PR", "BL", "BM", "PM"]  ##sigaret
]

rulesA = [
    #MILK SHOULD BE IN CENTER HOUSE - DO THIS RULE SOMEWHERE ELSE
    #NR SHOULD N+BE IN FIRST HOUSE - DO THIS RULE SOMEWHERE ELSE
    "0_EN+1_RED",
    "0_SU+2_DOG",
    "0_DN+3_TEA",
    "1_GREEN+3_COFFEE",
    "4_PM+2_BIRD",
    "1_YELLOW+4_DH",
    "4_BM+3_BEER",
    "0_GR+4_PR",
]

rulesB = [
    "4_BL=LR|2_CAT",  #The house of whom smokes BL is Left or Right side of House with a CAT
    "2_HORSE=LR|4_DH",
    "1_GREEN=L|1_WHITE",
    "0_GR=LR|1_BLUE",
    "4_BL=LR|3_BEER",
]


#make a case
def make():
    solution = [["NR", "", "", "", ""], ["", "", "", "", ""],
                ["", "", "", "MILK", ""], ["", "", "", "", ""],
                ["", "", "", "", ""]]
    return solution

def rnd(q):#q=5 -> return 0-4
    return random.randint(0, q) - 1 

s = []

def firstRules():
    global s
    s = make()
    counter = 0
    i = 0
    while True:  #0-4
        r = rulesA[i]
        while True:
            n = rnd(5)
            lIdx = int(r.split("+")[0].split("_")[0])
            lVal = r.split("+")[0].split("_")[1]
            rIdx = int(r.split("+")[1].split("_")[0])
            rVal = r.split("+")[1].split("_")[1]

            if s[n][lIdx] == "" and s[n][rIdx] == "":
                s[n][lIdx] = lVal
                s[n][rIdx] = rVal
                break
            else:
                counter += 1
                if (counter > 100):
                    print(lIdx, lVal, rIdx, rVal)
                    print("error - rematch")
                    return False
        i += 1
        if i == 8:
            break
    return True

#find a solution with defined rules
while True:
    ret = firstRules()
    if ret:
        break
    pass

for ss in s:
    print(ss)


#Fill empty cells
#human list is full - NR, DN, GR, EN, SU
#I should fill colors. YELLOW, RED and GREEN are selected. I should Select between BLUE and WHITE
remained=["BLUE","WHITE"]
while len(remained)>0:
    x=remained.pop();
    while True:
        n=rnd(5)
        if s[n][1]=="":
            s[n][1]=x
            break

remained=["HORSE","CAT","FISH"]
while len(remained)>0:
    x=remained.pop();
    while True:
        n=rnd(5)
        if s[n][2]=="":
            s[n][2]=x
            break

remained=["UNKNOWN"]
while len(remained)>0:
    x=remained.pop();
    while True:
        n=rnd(5)
        if s[n][3]=="":
            s[n][3]=x
            break

remained=["BL"]
while len(remained)>0:
    x=remained.pop();
    while True:
        n=rnd(5)
        if s[n][4]=="":
            s[n][4]=x
            break

print("________________")  
for ss in s:
    print(ss)