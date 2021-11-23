import os
import pyttsx3
import playsound
import speech_recognition as sr
import time
import sys
import fileinput
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import math
import smtplib
import psutil
import pyjokes
import pywhatkit as kit
import requests
import subprocess
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request as urllib2
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import translators as ts
path = EdgeChromiumDriverManager().install()
language='vi'
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
from datetime import datetime, date, time
from countdown import countdown
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import sys
import pyautogui as pg

mouth = pyttsx3.init()
rate = mouth.getProperty('rate')
mouth.setProperty('rate', 175)
voices = mouth.getProperty('voices')
mouth.setProperty('voice', voices[1].id)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def speak(audio):
	print("FVA: {}".format(audio))
	mouth.say(audio)
	mouth.runAndWait()

def get_audio():
    
	print("Listenning...")
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("User: ", end='')
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	try:
		try:
			user = r.recognize_google(audio, language='vi-VN')
		except:
			user = r.recognize_google(audio, language='en-EN')
		print(user)
	except:
		user = ""
		print(user)
	return user

def userspeak():
	for i in range(3):
		user = get_audio()
		if user:
			return user.lower()
		elif i < 2:
			user = ""
			return user
	return

def greeting(name):
	name = open("./username.ini", "r").readline()
	day_time = int(strftime('%H'))
	if day_time < 12:
		speak("Good morning {}" .format(name))
	elif 12 <= day_time < 18:
		speak("Good afternoon {}" .format(name))
	else:
		speak("Good evening {}" .format(name))
		
def stop():
	speak("See you later!")

def shutdownpc():
	speak("Are you sure you want me to turn off your PC?")
	user = userspeak()
	if user == "yes":
		speak("I am shutting down your PC in 10 seconds")
		os.system('shutdown -s -t 10')
		countdown(mins=0, secs=7)
		speak("Goodbye")
	elif user == "no" or user == "":
		speak("Cancel action")
	else:
		speak("Canceled")

def restartpc():
	speak("Are you sure you want me to restart your PC?")
	user = userspeak()
	if user == "yes":
		speak("Your PC will be restart in 10 seconds")
		os.system('shutdown -r -t 10')
		countdown(mins=0, secs=8)
	elif user == "no" or user == "":
		speak("Cancel action")
	else:
		speak("Canceled")

def logoutpc():
	speak("Are you sure you want to logout?")
	user = userspeak()
	if user == "yes":
		speak("See you later")
		os.system('shutdown -l')
	elif user == "no" or user == "":
		speak("Cancel action")
	else:
		speak("Canceled")

def get_time(user):
	now = datetime.now()
	speak("Currently is " + now.strftime("%H:%M"))

def get_date(user):
	today = datetime.now()
	speak("Today is " + today.strftime("%d/%m/%Y"))

def open_application(user):
	try:
		if "microsoft edge" in user:
			speak("Open Microsoft Edge")
			os.startfile('msedge.exe')
		elif "word" in user:
			speak("Open Microsoft Word")
			os.startfile('WINWORD.EXE')
		elif "windows explorer" in user:
			speak("Open Windows Explorer")
			os.startfile('explorer.exe')
		else:
			speak("Application not installed")
	except:
		speak("Sorry, I can't open this app")

def open_website(user):
	if "mở" in user or "đi đến" in user or "go to" in user or "open" in user:
		if "mở" in user:
			reg_ex = re.search('mở (.+)', user)
		elif "đi đến" in user:
			reg_ex = re.search('đi đến (.+)', user)
		elif "open" in user:
			reg_ex = re.search('open (.+)', user)
		elif "go to" in user:
			reg_ex = re.search('go to (.+)', user)
	else:
		reg_ex = re.search('(.+)', user)
	if reg_ex:
		domain = reg_ex.group(1)
		url = 'https://www.' + domain
		webbrowser.open(url)
		speak("Go to {}" .format(domain))
		return True
	else:
		return False

def search_google(user):
	if user == "searching for" or user == "tìm":
		speak("What do you want me to find?")
		user = userspeak()
		if user == "cancel" or user == "hủy" or user == "":
			speak("Cancel searching")
		else:
			user = user.replace("", "")
			speak("Searching for " + user)
			webbrowser.open('https://www.google.com/search?q=' + user)
	else:
		if "tìm" in user:
			user = user.replace("tìm ", "")
		elif "searching for" in user:
			user = user.replace("searching for ", "")
		speak("Searching for " + user)
		webbrowser.open('https://www.google.com/search?q=' + user)

def search_youtube(user):
	if user == "search on youtube" or user == "tìm video trên youtube":
		speak("What video you want me to find?")
		user = userspeak()
		user = user.replace("", "")
		if user == "" or user == "cancel" or user == "hủy":
			speak("Cancel searching")
		else:
			speak("Searching for " + user)
			webbrowser.open('https://www.youtube.com/results?search_query=' + user)
	else:
		if "tìm video trên youtube" in user:
			user = user.replace("tìm video trên youtube ", "")
		elif "search on youtube" in user:
			user = user.replace("search on youtube ", "")
		speak("Searching for " + user)
		webbrowser.open('https://www.youtube.com/results?search_query=' + user)

def wiki(user):
	if user == "wikipedia" or user == "wiki":
		speak("What do you want me to find?")
		user = userspeak()
		user = user.replace("", "")
		speak("According to Wikipedia. " + str(wikipedia.summary(str(user), sentences=2)))
		if user == "cancel" or user == "":
			speak("Ok, I canceled that")
		else:
			speak("Sorry! I can't find any matching result")
	else:
		try:
			if "wikipedia" in user:
				user = user.replace("wikipedia ", "")
			elif "wiki" in user:
				user = user.replace("wiki ", "")
			speak("According to Wikipedia. " + str(wikipedia.summary(str(user), sentences=2)))
		except:
			speak("Sorry! I can't find any matching result")

def send_email(user):
	speak('Bạn gửi email cho ai nhỉ')
	recipient = userspeak()
	if 'yến' in recipient:
		speak('Nội dung bạn muốn gửi là gì')
		content = userspeak()
		mail = smtplib.SMTP('smtp.gmail.com', 587)
		mail.ehlo()
		mail.starttls()
		mail.login('luongngochungcntt@gmail.com', 'hung23081997')
		mail.sendmail('luongngochungcntt@gmail.com',
					  'hungdhv97@gmail.com', content.encode('utf-8'))
		mail.close()
		speak('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')
	else:
		speak('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?')

def read_news():
	speak("What content you want to heard?")
	queue = userspeak()
	params = {
		'apiKey': '30d02d187f7140faacf9ccd27a1441ad',
		"q": queue,
	}
	api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
	api_response = api_result.json()
	speak("Here what I found")
	for number, result in enumerate(api_response['articles'], start=1):
		print(f"""News no.{number}:\nTitle: {result['title']}\nDescription: {result['description']}\nLink: {result['url']}""")

def changeName(user):
	speak("What's your new name?")
	name = input("Enter your new name: ")
	if name == "":
		speak("Canceled")
	else:
		name = open("./username.ini","w+").write(name)
		speak("Your new name is {}".format(name))

def userinfo():
	name = open("./username.ini", "r").readline()
	speak("Your name is {}".format(name))

def assistantinfo(user):
	if "your name" in user:
		if os.path.exists('./assistantname.ini') == False:
			open("./assistantname.ini","w").write("FVA")
		else:
			pass
		ainame = open("./assistantname.ini","r").readline()
		speak("My name is {}".format(ainame))
	# elif "your name stand for" in user:
	# 	speak("FVA stand for 'Female Voice Assistant'")

def help():
	speak("Here are commands I can do:"
    """
	1. Greeting
	2. Show date, time
	3. Go to website
	4. Open application
	5. Searching on Google, Youtube, Wikipedia
	6. Send email
	7. Weather
	9. Reading news
	10. System setting
 	And more in the future update""")

def openweathermap(user):
	city = user
	if not city:
		pass
	api_key = "283fdf84873609c06a47e26d1f53a248"
	call_url = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" + api_key + "&q=" + city + "&units=metric"
	response = requests.get(call_url)
	data = response.json()
	if data["cod"] != "404":
		city_res = data["main"]
		current_temperature = city_res["temp"]
		current_humidity = city_res["humidity"]
		wthr = data["weather"]
		weather_description = wthr[0]["description"]
		content = """
		Currently in {city}
		{temp}°C with {description}
		Humidity is {humidity}%""".format(city = city, temp = current_temperature, humidity = current_humidity, description = weather_description)
		speak(content)
	else:
		pass

def current_weather(user):
	if user == "thời tiết" or user == "weather" or user == "how is the weather" or user == "how's the weather":
		speak("Tell me city name?")
		try:
			user = userspeak()
			user = user.replace("", "")
			openweathermap(user)
		except:
			if user == "" or user =="cancel":
				speak("I canceled that")
			else:
				speak("I can't find that city")
	else:
		if "thời tiết ở" in user:
			user = user.replace("thời tiết ở ", "")
		elif "weather in" in user:
			user = user.replace("weather in ", "")
		elif "weather" in user:
			user = user.replace("weather ", "")
		elif "thời tiết" in user:
			user = user.replace("thời tiết ", "")
		openweathermap(user)

def curvol():
	currentvol = str(round(volume.GetMasterVolumeLevelScalar() * 100))
	speak("Current volume is " + currentvol + "%")

def mutevol():
	volume.SetMute(1, None)
	speak("Volume is muted")

def unmutevol():
	volume.SetMute(0, None)
	speak("Volume is unmuted")

def setvol():
	speak("How much?")
	user = int(userspeak())
	scalarVolume = user/100
	volume.SetMasterVolumeLevelScalar(scalarVolume, None)
	currentvol = str(round(volume.GetMasterVolumeLevelScalar() * 100))
	speak("Set volume to " + currentvol + "%")

def assistant():
	if os.path.exists('./username.ini') == False or os.stat('./username.ini').st_size == 0:
		speak("Hi there! My name is Eva. What your name?")
		name = input("Enter your name: ")
		if name == "":
			name = "User"
			speak("OK, I will call you " + name)
		else:
			name = name
		name = open("./username.ini","w+").write(name)
	if os.path.exists('./username.ini') and os.path.getsize('./username.ini') > 0:
		name = open("./username.ini", "r").readline()
		speak("Hello " + name)
		#speak("Hello " + name)
		while True:
			#user = input("User type: ")
			user = userspeak()
			if "eva" in user:
				if user == "eva":
					speak("Yes?")
					user = userspeak()
				elif "eva" in user:
					user = user.replace("eva ", "")
				if not user or user == "":
					speak("Sorry, I don't heard anything?")
					pass
				elif "change my name" in user or "đổi tên tôi" in user:
					changeName(user)
				elif "what's my name" in user:
					userinfo()
				elif "your name" in user:
					assistantinfo(user)
				elif "dừng" in user or "tạm biệt" in user or "bye" in user or user == "shut down":
					stop()
					break
				elif "có thể làm gì" in user or "what can you do" in user:
					help()
				elif user == "chào" or user == "hi" or user == "hello":
					greeting(name)
					get_date(user)
					get_time(user)
				elif user == "shut down my pc":
					shutdownpc()
					if user == "no" or user == "":
						pass
					elif user == "yes":
						break
				elif user == "restart my pc":
					restartpc()
					break
				elif user == "logout my pc":
					logoutpc()
					break
				elif "time" in user:
					get_time(user)
				elif "today" in user:
					get_date(user)
				elif "mở" in user or "đi đến" in user or "go to" in user or "open" in user:
					if "." in user:
						open_website(user)
					else:
						open_application(user)
				elif "." in user:
					open_website(user)
				elif "tìm" in user or "searching for" in user:
					search_google(user)
				elif "email" in user or "mail" in user or "gmail" in user:
					send_email(user)
				elif "thời tiết" in user or "weather" in user or "how is the weather" in user or "how's the weather" in user:
					current_weather(user)
				elif "search on youtube" in user or "tìm video trên youtube" in user:
					search_youtube(user)
				elif "news" in user:
					read_news()
				elif "wikipedia" in user or "wiki" in user:
					wiki(user)
				elif "âm lượng hiện tại" in user or "current volume" in user:
					curvol()
				elif "tắt âm lượng" in user or "mute volume" in user:
					mutevol()
				elif "bật âm lượng" in user or "unmute volume" in user:
					unmutevol()
				elif "đặt âm lượng" in user or "volume" in user:
					setvol()
				else:
					speak("Sorry, I can't understand")
			else:
				continue
assistant()