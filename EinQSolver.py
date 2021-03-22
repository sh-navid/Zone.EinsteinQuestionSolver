#By Navid Shamshirsaz
#github.com/sh-navid
#IF YOU NEED COMMENTS IN ENGLISH JUST TELL ME ON ONE OF MY ACCOUNTS OR SUBMIT AN ISSUE
#نوشته شده توسط نوید شمشیرساز

import random
#خب تصمیم گرفتم همون فارسی توضیح بدم خودم هم گیج نشم دارم چی مینویسم
#این کل برداشت من از جملات انیشتین هست
#فکر نمیکنم چیزی رو جا انداخته باشم
#من با این دیتا بصورت مستقیم کاری ندارم فقط بصورت کلی میخوام بدونم پارامترها چی هستن
[
    ["EN", "SU", "DN", "NR", "GR"],  ##ادم ها و ملیتشون
    ["GREEN", "WHITE", "RED", "BLUE", "YELLOW"],  ##رنگ خونه ها
    ["BIRD", "HORSE", "DOG", "CAT", "FISH"],  ##حیوانات خانگی
    ["BEER", "MILK", "COFFEE", "TEA",
     "UNKNOWN"],  ##نوشیدنی ها، یدونه مشخص نبود اصلا
    ["DH", "PR", "BL", "BM", "PM"]  ##برند سیگارها
]

#خب این اولین لیست قوانینه که میگه هر 2 ایتم چطور با هم در ارتباط هستن
rulesA = [
    #خونه وسطی شیر میخوره و همینطور خونه اول صاحبش مرد نروژیه
    #این 2 تا قانون رو تو لیست قانون های اینجا نمیزارم - بعدا تو تابع
    #ساختن هار-کد کردم - اونجوری بهتره به نظرم
    #تو این قواعد اعداد به معنای ستونهای راه حلی که میسازیم هستن
    #الان از جمله پایین منظورم اینه - مرد انگلیسی تو خونه قرمز قرار داره
    #و تو لیست راه حلها ملیت این مرد در ستون شماره 0 و رنگ خونش در
    #ستون شماره 1 باید قرار بگیره
    "0_EN+1_RED",
    "0_SU+2_DOG",
    "0_DN+3_TEA",
    "1_GREEN+3_COFFEE",
    "4_PM+2_BIRD",
    "1_YELLOW+4_DH",
    "4_BM+3_BEER",
    "0_GR+4_PR"
]

#این لیست دوم قوانین
#این لیست هم پارسر نداره میخوام خودم تک تک بررسیشون کنم. فقط جهت اطلاع نوشتم
[
    "4_BL=LR|2_CAT",  #خونه ای که بلندز میکشه سمت چپ یا راست خونه ای قرار داره که گربه داره
    "2_HORSE=LR|4_DH",  #خونه ای که اسب داره سمت راست یا چپ خونه ای قرار داره که دان-هیل میکشه
    "1_GREEN=L|1_WHITE",  #خانه سبز سمت چپ خانه سفید قرار دارد
    "0_GR=LR|1_BLUE",
    "4_BL=LR|3_BEER"
]


#ساخت یک راه حل اولیه
def make():
    solution = [["NR", "", "", "", ""], ["", "", "", "", ""],
                ["", "", "", "MILK", ""], ["", "", "", "", ""],
                ["", "", "", "", ""]]
    return solution


def rnd(q):  #q=5 -> return 0-4
    return random.randint(0, q) - 1


#یک راه حل خالی ساختم
s = []


#با این تابع یه راه حل رو با توجه به لیست اول قوانین پر میکنم
#یعنی یک سری مکان کاندید انتحاب و پیدا میکنم که معلوم نیست
#آیا مکان درستی هستن یا نه - خب این بعدا معلوم میشه
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

def find(item,column):
    for idx in range(0,5):
        if s[idx][column]==item:
            return idx
    return "ERROR"
        

PROGRAM_ENDED=False
while not PROGRAM_ENDED:
    #یک راه حل اولیه با قوانین اول تعریف شده
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
    def filler(remained_data_to_fill_empty_cells, colomn_to_fill):
        #remained_data_to_fill_empty_cells=["BLUE","WHITE"]
        while len(remained_data_to_fill_empty_cells) > 0:
            x = remained_data_to_fill_empty_cells.pop()
            while True:
                n = rnd(5)
                if s[n][colomn_to_fill] == "":
                    s[n][colomn_to_fill] = x
                    break


    #خب با لیست اول قوانین یک راه حل ساختم حالا باید اینجا جاهای خالی رو پر کنم
    #با توجه به شرایط نقاط کاندید برای خونه های سبز، قرمز و زرد مشخص شده بود
    #دو خونه باقی مونده بود که باید آبی یا سفید باشد
    filler(["BLUE", "WHITE"], 1)
    filler(["HORSE", "CAT", "FISH"], 2)
    filler(["UNKNOWN"], 3)
    filler(["BL"], 4)

    print("________________")
    for ss in s:
        print(ss)

    #خب حالا لیست شرایط دوم رو باید بررسی کنم
    #اگر تمام شرایط دوم برقرار بود این راه حل درسته اگر نه باید از اول یه راه حل بسازم
    #این خیلی بهینه نیست ولی بزار اول یه راه حل بدست بیارم
    #الان برام سوال شده ایا این مساله ممکنه دو یا چند راه حل داشته باشه ؟؟

    #چند روزی حوصله نداشتم بنویسمش تا امروز
    #3/22/2021

    rowA=find("BL",4);
    rowB=find("CAT",2);
    if abs(rowA-rowB) !=1:
        PROGRAM_ENDED=False
        continue

    rowA=find("HORSE",2);
    rowB=find("DH",4);
    if abs(rowA-rowB) !=1:
        PROGRAM_ENDED=False
        continue

    PROGRAM_ENDED=True