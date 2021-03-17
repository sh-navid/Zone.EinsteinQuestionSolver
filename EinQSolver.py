#By Navid Shamshirsaz
#IF YOU NEED COMMENTS IN ENGLISH JUST COMMENT ON ONE OF MY ACCOUNTS OR SUBMIT AN ISSUE
#نوشته شده توسط نوید شمشیرساز

import random
#
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

#فکر کنم فارسی کامنت بزارم بهتره - خودم هم گیج شدم دارم چکار میکنم
#انیشتین یک سری قوانین مشخص کرده بود
#من این قوانین رو به سه دسته تقسیم بندی کرده بودم
#دسته اول اونایی بودن که ثابت بودن
#مثلا صاحب خونه وسطی همیشه شیر میخوره
#یا فرد نروژی همواره تو خونه اوله
#سری دوم قوانین ایتمهایی بود که تو یک خونه مشترکن
#مثلا مرد انگلیسی تو خونه قرمز خواهد بود
#خب حالا سری سوم قوانین مونده اما اول نیازه تا جاهای خالی تو راه حل پر بشن
#خیلی خب این تابع به من کمک میکنه جاهای خالی رو پر کنم
#اوکی الان فارسی نوشتم خودم بیشتر فهمیدم دارم چکار میکنم
#باید تو سبک کامنت نوشتن یکم تجدید نظر کنم
def filler(remained_data_to_fill_empty_cells,colomn_to_fill):
    #remained_data_to_fill_empty_cells=["BLUE","WHITE"]
    while len(remained_data_to_fill_empty_cells)>0:
        x=remained_data_to_fill_empty_cells.pop();
        while True:
            n=rnd(5)
            if s[n][colomn_to_fill]=="":
                s[n][colomn_to_fill]=x
                break


#Fill empty cells
#human list is full - NR, DN, GR, EN, SU
#I should fill colors. YELLOW, RED and GREEN are selected. I should Select between BLUE and WHITE
filler(["BLUE","WHITE"],1)
filler(["HORSE","CAT","FISH"],2)
filler(["UNKNOWN"],3)
filler(["BL"],4)

print("________________")  
for ss in s:
    print(ss)