#By Navid Shamshirsaz

#what we have at all???

_h=["EN","SU","DN","NR","GR"]##human

_c=["GREEN","WHITE","RED","BLUE","YELLOW"]##color of houses

_p=["BIRD","HORSE","DOG","CAT","FISH"]##pet

_d=["BEER","MILK","COFFEE","TEA","UNKNOWN"]##drink

_s=["DH","PR","BL","PM","UNKNOWN2"]##sigaret

print(_h)

#Rules

rules=[
    #MILK SHOULD BE IN CENTER HOUSE - DO THIS RULE SOMEWHERE ELSE
    #NR SHOULD N+BE IN FIRST HOUSE - DO THIS RULE SOMEWHERE ELSE
    "EN+RED",
    "SU+DOG",
    "DN+TEA",
    "GREEN+COFFEE",
    "GREEN=|WHITE|-1",
    "PM+BIRD",
    "YELLOW+DH",
    
]
