# Імпортуєм необіхдні бібліотеки
import pyttsx3
import speech_recognition as sr
from nltk.tokenize import word_tokenize
import webbrowser
import time
import datetime
import os
import sys
import random
# Настройки голома
engine=pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 205)
volume = engine.getProperty('volume')
engine.setProperty('volume',10)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[9].id)
# Функція для розмови
def talk(word):
	print("[jora] "+word)
	engine.say(word)
	engine.runAndWait()
# Функція дати
def date_func():
    cls=now.day
    if cls==1:
        cls="первое"
    elif cls==2:
        cls="второе"
    elif cls==3:
        cls="третья"
    elif cls==4:
        cls="четвертое"
    elif cls==5:
        cls="пятое"
    elif cls==6:
        cls="шестое"
    elif cls==7:
        cls="седьмое"
    elif cls==8:
        cls="восьмое"
    elif cls==9:
        cls="девятое"
    elif cls==10:
        cls="десятое"
    elif cls==11:
        cls="одиннадцатое"
    elif cls==12:
        cls="двенадцатое"
    elif cls==13:
        cls="тринадцатое"
    elif cls==14:
        cls="четырнадцатое"
    elif cls==15:
        cls="пятнадцатое"
    elif cls==16:
        cls="шестнадцатое"
    elif cls==17:
        cls="семнадцатое"
    elif cls==18:
        cls="восемнадцатое"
    elif cls==19:
        cls="девятнадцатое"
    elif cls==20:
        cls="двадцатое"
    elif cls==21:
        cls="двадцать первое"
    elif cls==22:
        cls="двадцать второе"
    elif cls==23:
        cls="двадцать третья"
    elif cls==24:
        cls="двадцать четвертое"
    elif cls==25:
        cls="двадцать пятое"
    elif cls==26:
        cls="двадцать шестое"
    elif cls==27:
        cls="двадцать седьмое"
    elif cls==28:
        cls="двадцать восьмое"
    elif cls==29:
        cls="двадцать девятое"
    elif cls==30:
        cls="тридцатое"
    elif cls==31:
        cls="тридцать первое"
    mnth=now.month
    if mnth==1:
        mnth="января"
    elif mnth==2:
        mnth="февраля"
    elif mnth==3:
        mnth="марта"
    elif mnth==4:
        mnth="апреля"
    elif mnth==5:
        mnth="мая"
    elif mnth==6:
        mnth="июня"
    elif mnth==7:
        mnth="июля"
    elif mnth==8:
        mnth="августа"
    elif mnth==9:
        mnth="сентября"
    elif mnth==10:
        mnth="октября"
    elif mnth==11:
        mnth="ноября"
    elif mnth==12:
        mnth="декабря"
    talk("Сегодня "+cls+" "+mnth+" две тысячи двадцятого года")
# Настройки дати та часу
now = datetime.datetime.now()
# Настройки браузера
webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
# Функція для прослухування
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
def speak():
	with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source)
		print("Говорите")
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)
	try: #
		comand = r.recognize_google(audio, language="ru-RU").lower()
		print("[xazyain] " + comand)
	except sr.UnknownValueError:
		print("[jora] Голос не распознан")
		comand = speak()
	return comand
# Створюєм списки з командами та відповідями
delete=["жора","жорик","жара","жарик","пожалуйста","пожалуста","привет","быстра","сейчас","же","скажи",
"который","какоє","какой","какая","открой"]
name=["жора","жара","жарик","жорик","жорян","жарян"]
ctime=["время","час"]
wether=["погода","что по погоде","погоду"]
kd=["как дела","дела"]
vd=["лучше не бывает","отлично","так себе","бывало по лутше"]
wg=["что делаешь"]
vg=["разговариваю с умным человеком, немог бы ты отойты мешаеш разговаривать","с вамы разговариваю","отдыхаю","мог бы я что то делать, я бы захватил весь мир"]
brs=["браузер","google","chrome","хром"]
date=["число","дата","дату","день"]
offpc=["выключи компьютер","выключи пк","выключи","off"]
search=["найди","загугли","ищи"]
hi=["Привет, я жора","Жора на месте","Здарова человек","Привет жорик здесь","Привет в меня отличное настроение"]
hello=["добрый день","здарова","привет","здорово"]
youtube=["youtube","ютуб"]
bye=["пака","уйди","замолчи","пока"]
# Просим вести пароль
# password=input("Ведіть пароль: ")
password="parol123"
# Створюєм цикл для перевірки команд
if password=="parol123":
    a=random.randint(0,len(hi)-1)
    talk(hi[a])
    while True:
        a=speak()
        a=(word_tokenize(a))
        b=a[:]
        if a[0] in name or a[0] in hello:
            for i in a:
                if i in delete:
                    b.remove(i)

            a=' '.join(b)
            print(a)
            if a in kd:
                b=random.randint(0,len(vd)-1)
                talk(vd[b])
            elif a in ctime:
                hor="Сейчас "+str(now.hour)+" "+str(now.minute)
                talk(hor)
            elif a in wg:
                b=random.randint(0,len(vg)-1)
                talk(vg[b])
            elif a in brs:
                talk("Открываю")
                webbrowser.get('Chrome').open_new_tab('google.com')
            elif a in wether:
                talk("Сейчас вы узнаете погоду")
                webbrowser.get('Chrome').open_new_tab('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B2%D0%B5%D0%BB%D0%B8%D0%BA%D0%B8%D0%B9-%D0%BA%D1%83%D1%87%D1%83%D1%80%D1%96%D0%B2')
            elif a in offpc:
                talk("Через минуту выключу")
                os.system("shutdown -s")
            elif a in search:
                talk("Что вам найти")
                c=speak()
                url="https://www.google.com/search?sxsrf=ACYBGNTPE1sZpjgL0et6f8dibLfqLicNCQ%3A1578666715494&source=hp&ei=24oYXqHlG7WFk74P3NWe2A0&q="+c
                webbrowser.get('Chrome').open_new_tab(url)
            elif a in date:
                date_func()
            elif a in youtube:
                talk("Пожалуйста")
                webbrowser.get('Chrome').open_new_tab("https://www.youtube.com/")
            elif a in bye:
                exit()
else:
    talk("Пошел вон ты не хозяин, я щас тебя током стукну!")
    exit()
