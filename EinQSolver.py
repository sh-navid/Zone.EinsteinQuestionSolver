#By Navid Shamshirsaz

#what we have at all???
_h=["EN","SU","DN","NR","GR"]##human

_c=["GREEN","WHITE","RED","BLUE","YELLOW"]##color of houses

_p=["BIRD","HORSE","DOG","CAT","FISH"]##pet

_d=["BEER","MILK","COFFEE","TEA","UNKNOWN"]##drink

_s=["DH","PR","BL","BM","UNKNOWN2"]##sigaret

rules=[
    #MILK SHOULD BE IN CENTER HOUSE - DO THIS RULE SOMEWHERE ELSE
    #NR SHOULD N+BE IN FIRST HOUSE - DO THIS RULE SOMEWHERE ELSE
    "EN+RED",
    "SU+DOG",
    "DN+TEA",
    "GREEN+COFFEE",
    "GREEN=L|WHITE",
    "PM+BIRD",
    "YELLOW+DH",
    "BL=LR|CAT",#The house of whom smokes BL is Left or Right side of House with a CAT
    "HORSE=LR|DH",
    "BM+BEER",
    "GR+PR",
    "GR=LR|BLUE",
    "BL=LR|BEER",
]
