import pyautogui
import time
import pyttsx3
import speech_recognition as sr

shrp=["больше","шрифт больше","увелич шрифт","боишся","бойся"]
shrm=["меньше","шрифт мешьше","уменш шрифт"]
vt=["весь","текст","выдели"]
delete=["удали",'delete']
text=["веди текст","какой то текст","случайный текст","жора текст","жара текст"]

engine=pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 205)
volume = engine.getProperty('volume')
engine.setProperty('volume',10)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[9].id)
def talk(word):
	print("[jora] "+word)
	engine.say(word)
	engine.runAndWait()
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
while True:
	a=speak()
	if a in shrp:
		pyautogui.hotkey('ctrl','lshift','!')
	elif a in vt:
		pyautogui.hotkey('ctrl','a')
	elif a in shrm:
		pyautogui.hotkey('ctrl','lshift','(')
	elif a in delete:
		pyautogui.press('delete')
	elif a in text:
		pyautogui.typewrite("""Hello world! I random text!
Privet mir!
Bye!""",interval=0.2)
