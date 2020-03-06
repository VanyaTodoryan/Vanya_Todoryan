# -*- coding: utf-8 -*-
import telebot
import os
import pyautogui
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

bot = telebot.TeleBot("1007355603:AAHSvPhd1HlWQiYQ-4Cw7eEljqrnoQvZIyo")
while True:
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
	       bot.send_message(message.chat.id, "Введи якісь слова!")

    @bot.message_handler(func=lambda message: True)
    def name(message):
        global a
        off=["виключи","off","Виключи","OFF"]
        pause=["пауза","pause","Pause","Пауза"]
        a=(message.text)
        print(a)
        if a in off:
            bot.send_message(message.chat.id, "Ноутбук виключається!")
            os.system("shutdown -s")
        elif a in pause:
            bot.send_message(message.chat.id, "Пауза!")
            pyautogui.press('space')

    bot.polling()
