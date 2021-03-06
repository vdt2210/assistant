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

path = EdgeChromiumDriverManager().install()
language='vi'

mouth = pyttsx3.init()
rate = mouth.getProperty('rate')
mouth.setProperty('rate', 175)
voices = mouth.getProperty('voices')
mouth.setProperty('voice', voices[1].id)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def speak(audio):
	print(open("./assistantname.ini", "r").readline() + ": " + audio)
	mouth.say(audio)
	mouth.runAndWait()

def getAudio():
	print("Listenning...")
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("{}: ".format(open("./username.ini", "r").readline()), end='')
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

def userSpeak():
	for i in range(3):
		user = getAudio()
		if user:
			return user.lower()
		elif i < 2:
			user = ""
			return user
	return

def greeting(name):
	name = open("./username.ini", "r").readline()
	hour = int(strftime('%H'))
	if hour < 12:
		speak("Good morning {}" .format(name))
	elif 12 <= hour < 18:
		speak("Good afternoon {}" .format(name))
	else:
		speak("Good evening {}" .format(name))
		
def stop():
	speak("See you later!")

def shutDownPC():
	speak("Are you sure you want me to turn off your PC?")
	user = userSpeak()
	if user == "yes":
		speak("I am shutting down your PC in 10 seconds")
		os.system('shutdown -s -t 10')
		countdown(mins=0, secs=7)
		speak("Goodbye")
	elif user == "no" or user == "":
		speak("Cancel action")
	else:
		speak("Canceled")

def restartPC():
	speak("Are you sure you want me to restart your PC?")
	user = userSpeak()
	if user == "yes":
		speak("Your PC will be restart in 10 seconds")
		os.system('shutdown -r -t 10')
		countdown(mins=0, secs=8)
	elif user == "no" or user == "":
		speak("Cancel action")
	else:
		speak("Canceled")

def logoutPC():
	speak("Are you sure you want to logout?")
	user = userSpeak()
	if user == "yes":
		speak("See you later")
		os.system('shutdown -l')
	elif user == "no" or user == "":
		speak("Cancel action")
	else:
		speak("Canceled")

def getTime(user):
	now = datetime.now()
	speak("Currently is " + now.strftime("%H:%M"))

def getDate(user):
	today = datetime.now()
	speak("Today is " + today.strftime("%A, %d/%m/%Y"))

def openApplication(user):
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
			speak("Open {}.exe".format(user))
			os.startfile(user +'.exe')
			# speak("Application not installed")
	except:
		speak("Sorry, I can't open this app")

def openWebsite(user):
	if "m???" in user or "??i ?????n" in user or "go to" in user or "open" in user:
		if "m???" in user:
			regEx = re.search('m??? (.+)', user)
		elif "??i ?????n" in user:
			regEx = re.search('??i ?????n (.+)', user)
		elif "open" in user:
			regEx = re.search('open (.+)', user)
		elif "go to" in user:
			regEx = re.search('go to (.+)', user)
	else:
		regEx = re.search('(.+)', user)
	if regEx:
		domain = regEx.group(1)
		url = 'https://www.' + domain
		webbrowser.open(url)
		speak("Go to {}" .format(domain))
		return True
	else:
		return False

def searchGoogle(user):
	if user == "searching for" or user == "t??m":
		speak("What do you want me to find?")
		user = userSpeak()
		if user == "cancel" or user == "h???y" or user == "":
			speak("Cancel searching")
		else:
			user = user.replace("", "")
			speak("Searching for " + user)
			webbrowser.open('https://www.google.com/search?q=' + user)
	else:
		if "t??m" in user:
			user = user.replace("t??m ", "")
		elif "searching for" in user:
			user = user.replace("searching for ", "")
		speak("Searching for " + user)
		webbrowser.open('https://www.google.com/search?q=' + user)

def searchYoutube(user):
	if user == "search on youtube" or user == "t??m video tr??n youtube":
		speak("What video you want me to find?")
		user = userSpeak()
		user = user.replace("", "")
		if user == "" or user == "cancel" or user == "h???y":
			speak("Cancel searching")
		else:
			speak("Searching for " + user)
			webbrowser.open('https://www.youtube.com/results?search_query=' + user)
	else:
		if "t??m video tr??n youtube" in user:
			user = user.replace("t??m video tr??n youtube ", "")
		elif "search on youtube" in user:
			user = user.replace("search on youtube ", "")
		speak("Searching for " + user)
		webbrowser.open('https://www.youtube.com/results?search_query=' + user)

def wiki(user):
	if user == "wikipedia" or user == "wiki":
		speak("What do you want me to find?")
		user = userSpeak()
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

# def sendEmail(user):
# 	speak('B???n g???i email cho ai nh???')
# 	recipient = userspeak()
# 	if 'y???n' in recipient:
# 		speak('N???i dung b???n mu???n g???i l?? g??')
# 		content = userspeak()
# 		mail = smtplib.SMTP('smtp.gmail.com', 587)
# 		mail.ehlo()
# 		mail.starttls()
# 		mail.login('luongngochungcntt@gmail.com', 'hung23081997')
# 		mail.sendmail('luongngochungcntt@gmail.com',
# 					  'hungdhv97@gmail.com', content.encode('utf-8'))
# 		mail.close()
# 		speak('Email c???a b???n v??a ???????c g???i. B???n check l???i email nh?? hihi.')
# 	else:
# 		speak('Bot kh??ng hi???u b???n mu???n g???i email cho ai. B???n n??i l???i ???????c kh??ng?')

def readNews():
	speak("What content you want to heard?")
	queue = userSpeak()
	params = {
		'apiKey': '30d02d187f7140faacf9ccd27a1441ad',
		"q": queue,
	}
	apiResult = requests.get('http://newsapi.org/v2/top-headlines?', params)
	apiResponse = apiResult.json()
	speak("Here what I found")
	for number, result in enumerate(apiResponse['articles'], start=1):
		print(f"""News no.{number}:\nTitle: {result['title']}\nDescription: {result['description']}\nLink: {result['url']}""")

def changeName(user):
	speak("What's your new name?")
	userName = input("Enter your new name: ")
	if userName == "":
		speak("Canceled")
	else:
		name = open("./username.ini","w+").write(userName)
		speak("Your new name is {}".format(userName))

def userInfo():
	userName = open("./username.ini", "r").readline()
	speak("Your name is {}".format(userName))

def assistantInfo(user):
	if "your name" in user:
		if os.path.exists('./assistantname.ini') == False:
			open("./assistantname.ini","w").write("Eva")
		else:
			pass
		aiName = open("./assistantname.ini","r").readline()
		speak("My name is {}".format(aiName))

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

def openWeatherMap(user):
	city = user
	if not city:
		pass
# https://api.openweathermap.org/data/2.5/weather?id=1566083&appid=ff1bc4683fc7325e9c57e586c20cc03e
	apiKey = "ff1bc4683fc7325e9c57e586c20cc03e"
	callUrl = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" + apiKey + "&q=" + city + "&units=metric"
	response = requests.get(callUrl)
	data = response.json()
	if data["cod"] != "404":
		cityRes = data["main"]
		currentTemperature = cityRes["temp"]
		currentHumidity = cityRes["humidity"]
		wthr = data["weather"]
		weatherDescription = wthr[0]["description"]
		content = """
		Currently in {city}
		{temp}??C with {description}
		Humidity is {humidity}%""".format(city = city, temp = currentTemperature, humidity = currentHumidity, description = weatherDescription)
		speak(content)
	else:
		pass

def currentWeather(user):
	if user == "th???i ti???t" or user == "weather" or user == "how is the weather" or user == "how's the weather":
		speak("Tell me city name?")
		try:
			user = userSpeak()
			user = user.replace("", "")
			openWeatherMap(user)
		except:
			if user == "" or user =="cancel":
				speak("I canceled that")
			else:
				speak("I can't find that city")
	else:
		if "th???i ti???t ???" in user:
			user = user.replace("th???i ti???t ??? ", "")
		elif "weather in" in user:
			user = user.replace("weather in ", "")
		elif "weather" in user:
			user = user.replace("weather ", "")
		elif "th???i ti???t" in user:
			user = user.replace("th???i ti???t ", "")
		openWeatherMap(user)

def currentVol():
	currentVol = str(round(volume.GetMasterVolumeLevelScalar() * 100))
	speak("Current volume is " + currentVol + "%")

def muteVol():
	volume.SetMute(1, None)
	speak("Volume is muted")

def unmuteVol():
	volume.SetMute(0, None)
	speak("Volume is unmuted")

def setVol():
	speak("How much?")
	user = int(userSpeak())
	scalarVolume = user/100
	volume.SetMasterVolumeLevelScalar(scalarVolume, None)
	currentVol = str(round(volume.GetMasterVolumeLevelScalar() * 100))
	speak("Set volume to " + currentVol + "%")

def assistant():
	if os.path.exists('./username.ini') == False or os.path.exists('./assistantname.ini') == False:
		open("./assistantname.ini","w").write("Eva")
		speak("Hi there! My name is {}. What your name?".format(open("./assistantname.ini","r").readline()))
		user = input("Enter your name: ")
		if user == "":
			userName = "User"
			speak("OK, I will call you " + userName)
		else:
			userName = user
		userName = open("./username.ini","w+").write(userName)
	if os.path.exists('./username.ini') and os.path.getsize('./username.ini') > 0:
		userName = open("./username.ini", "r").readline()
		aiName = open("./assistantname.ini","r").readline().lower()
		speak("Hello " + userName)
		while True:
			user = input("User type: ")
			# user = userspeak()
			if "hey " + open("./assistantname.ini","r").readline().lower() in user:
				if user == "hey {}".format(aiName):
					speak("Yes?")
					# user = userspeak()
					user = input("User type: ")
				elif "hey {}".format(aiName) in user:
					user = user.split("hey {} ".format(aiName))[-1]
				if not user or user == "":
					speak("Sorry, I don't heard anything?")
					pass
				elif "change my name" in user or "?????i t??n t??i" in user:
					changeName(user)
				elif "what's my name" in user:
					userInfo()
				elif "your name" in user:
					assistantInfo(user)
				elif "d???ng" in user or "t???m bi???t" in user or "bye" in user or user == "shut down":
					stop()
					break
				elif "c?? th??? l??m g??" in user or "what can you do" in user:
					help()
				elif user == "ch??o" or user == "hi" or user == "hello":
					greeting(userName)
					getDate(user)
					getTime(user)
				elif user == "shut down my pc":
					shutDownPC()
					if user == "no" or user == "":
						pass
					elif user == "yes":
						break
				elif user == "restart my pc":
					restartPC()
					break
				elif user == "logout my pc":
					logoutPC()
					break
				elif "time" in user:
					getTime(user)
				elif "today" in user:
					getDate(user)
				elif "m???" in user or "??i ?????n" in user or "go to" in user or "open" in user:
					if "." in user:
						openWebsite(user)
					else:
						user = user.split("open " and "m??? ")[-1]
						openApplication(user)
				elif "." in user:
					openWebsite(user)
				elif "t??m" in user or "searching for" in user:
					searchGoogle(user)
				# elif "email" in user or "mail" in user or "gmail" in user:
				# 	sendEmail(user)
				elif "th???i ti???t" in user or "weather" in user or "how is the weather" in user or "how's the weather" in user:
					currentWeather(user)
				elif "search on youtube" in user or "t??m video tr??n youtube" in user:
					searchYoutube(user)
				elif "news" in user:
					readNews()
				elif "wikipedia" in user or "wiki" in user:
					wiki(user)
				elif "??m l?????ng hi???n t???i" in user or "current volume" in user:
					currentVol()
				elif "t???t ??m l?????ng" in user or "mute volume" in user:
					muteVol()
				elif "b???t ??m l?????ng" in user or "unmute volume" in user:
					unmuteVol()
				elif "?????t ??m l?????ng" in user or "volume" in user:
					setVol()
				else:
					speak("Sorry, I can't understand")
			else:
				continue
assistant()