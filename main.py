import os
import time
from time import sleep
import smtplib
from gtts import gTTS
from playsound import playsound
import pyttsx3

import assistantui
from assistantui import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import  *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QTimer,QDate,QTime
from PyQt5 import uic
import webbrowser as web
import assistantfunctions
import sys

mouth = pyttsx3.init()
rate = mouth.getProperty('rate')
mouth.setProperty('rate', 175)
voices = mouth.getProperty('voices')
mouth.setProperty('voice', voices[1].id)

def speak(audio):
	print("FVA: {}".format(audio))
	mouth.say(audio)
	mouth.runAndWait()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        assistantui.Ui_MainWindow()
        assistantfunctions.assistant()

startExe = MainThread()

class Ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.startTask()
        self.gui.shutdownButton.clicked.connect(self.shutdown)
        self.gui.helpButton.clicked.connect(self.help)
    
    def startTask(self):        
        self.gui.label = QtGui.QMovie("./pic/main_circle.gif")
        self.gui.maingif.setMovie(self.gui.label)
        self.gui.label.start()
        
        self.show()
        
    def shutdown(self):
        sys.exit()
        
    def help(self):
        assistantfunctions.help()
        
app = QApplication(sys.argv)
window = Ui()
window.show()
exit(app.exec_())