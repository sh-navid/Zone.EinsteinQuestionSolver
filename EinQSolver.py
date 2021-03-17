#By Navid Shamshirsaz

import random
#what we have at all???
_0 = ["EN", "SU", "DN", "NR", "GR"]  ##human
_1 = ["GREEN", "WHITE", "RED", "BLUE", "YELLOW"]  ##color of houses
_2 = ["BIRD", "HORSE", "DOG", "CAT", "FISH"]  ##pet
_3 = ["BEER", "MILK", "COFFEE", "TEA", "UNKNOWN"]  ##drink
_4 = ["DH", "PR", "BL", "BM", "UNKNOWN2"]  ##sigaret

rulesA = [
    #MILK SHOULD BE IN CENTER HOUSE - DO THIS RULE SOMEWHERE ELSE
    #NR SHOULD N+BE IN FIRST HOUSE - DO THIS RULE SOMEWHERE ELSE
    "0_EN+1_RED",
    "0_SU+2_DOG",
    "0_DN+3_TEA",
    "1_GREEN+3_COFFEE",
    "4_BM+2_BIRD",
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
    solution = [
        ["NR", "", "", "", ""], 
        ["", "", "", "", ""],
        ["", "", "", "MILK", ""], 
        ["", "", "", "", ""],
        ["", "", "", "", ""]
        ]
    return solution


s = make()


def firstRules():
    global s
    s = make()
    counter = 0
    i=0
    while True:  #0-4
        r = rulesA[i]
        while True:
            n = random.randint(0, 5) - 1
            #(1-5)-1 => (0-4)
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
        i+=1
        if i==8:
            break
    return True


while True:
    ret = firstRules()
    if ret:
        break
    pass

for ss in s:
    print(ss)

counter = 0
for i in range(0, 5):  #0-4

    pass
