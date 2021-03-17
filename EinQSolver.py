#By Navid Shamshirsaz

import random
#what we have at all???
_h=["EN","SU","DN","NR","GR"]##human

_c=["GREEN","WHITE","RED","BLUE","YELLOW"]##color of houses

_p=["BIRD","HORSE","DOG","CAT","FISH"]##pet

_d=["BEER","MILK","COFFEE","TEA","UNKNOWN"]##drink

_s=["DH","PR","BL","BM","UNKNOWN2"]##sigaret

rulesA=[
    #MILK SHOULD BE IN CENTER HOUSE - DO THIS RULE SOMEWHERE ELSE
    #NR SHOULD N+BE IN FIRST HOUSE - DO THIS RULE SOMEWHERE ELSE
    "EN+RED",
    "SU+DOG",
    "DN+TEA",
    "GREEN+COFFEE",
    "PM+BIRD",
    "YELLOW+DH",
    "BM+BEER",
    "GR+PR",
]

rulesB=[
    "BL=LR|CAT",#The house of whom smokes BL is Left or Right side of House with a CAT
    "HORSE=LR|DH",
    "GREEN=L|WHITE",
    "GR=LR|BLUE",
    "BL=LR|BEER",
]

#make a case
def make():
    solution=[
        ["NR","","","",""],
        ["","","","",""],
        ["","","MILK","",""],
        ["","","","",""],
        ["","","","",""]
    ]
    return solution

s=make()
for r in rulesA:
    n=random.randint(0, 5)-1;#(1-5)-1 => (0-4)
    



