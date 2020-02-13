# -*- coding: utf-8 -*-
# 程式 11-4 (Python 3 version)

from firebase import firebase
db_url = 'https://cgenkfust.firebaseio.com'
fdb = firebase.FirebaseApplication(db_url, None)

while True:
    inv_lotto = dict()
    inv_month = input('請輸入開獎月份(例：201707，輸入-1結束):')
    if int(inv_month) == -1 :
        break
    exist_data = fdb.get('/invlotto/'+inv_month, None)
    if exist_data != None:
        print("該月份已有資料，請重新輸入")
        continue
    inv_lotto['p1000w'] = input('請輸入特別獎1000萬號碼：')
    inv_lotto['p200w'] = input('請輸入特獎200萬號碼：')
    inv_lotto['p20w'] = list()
    while True:
        p20w = input('請輸入頭獎20萬號碼（輸入-1結束）：')
        if int(p20w) == -1:
            break
        inv_lotto['p20w'].append(p20w)
    inv_lotto['p200'] = list()
    while True:
        p200 = input('請輸入增開六獎號碼（輸入-1結束)：')
        if int(p200) == -1:
            break
        inv_lotto['p200'].append(p200)
    print("以下是您輸入的內容：")
    print("開獎月份:", inv_month)
    print("1000萬特別獎:", inv_lotto['p1000w'])
    print("200萬特獎:", inv_lotto['p200w'])
    print("20萬頭獎:", end="")
    for n in inv_lotto['p20w']:
        print(n + "  ", end="")
    print("\n200元增開六獎:", end="")
    for n in inv_lotto['p200']:
        print(n + "  ", end="")
    ans = input("\n是否寫入Firebase網路資料庫？(y/n)")
    if ans == 'y' or ans == 'Y':
        fdb.post('/invlotto/' + inv_month, inv_lotto)