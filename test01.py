"""
#これはテストです.
#関数を呼び出す際は、defで関数を設定してその後ろに書く必要がある
"""
import calendar
#asで名前を定義できる
import random as r

def sum(a,b):
    c = a + b
    return c

def calcTax(value):
    tax = 1.08
    return value*tax

def printHelloWorld():
    print("Hello,world!")


sum("OK","Google")
print( sum("Hi","\tAlexa") )

#文字と数字の連結は数字をstrで囲む
print("税込み価格は"+str(calcTax(1000)))

#文字と数字の連結は　,　で区切っても良いが多少の空白が発生する
print("税込み価格は",calcTax(2000))

printHelloWorld()

#calendar.TextCalendarで週の始めを日曜から始める
cal = calendar.TextCalendar(calendar.SUNDAY)
#prmonth()で2018年11月のカレンダーを取得しprintする
cal.prmonth(2019,2)

#カレンダーをHTML形式で表示
htmlCal = calendar.HTMLCalendar(calendar.SUNDAY)
print(htmlCal.formatmonth(2019,2))

print("ランダム(0-100)=="+str(r.random()*100))
