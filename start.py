import sys
import logging, netifaces, impacket, webbrowser
import MyUniversal as mu
import MyUtilities as mut
import re
from scapy.all import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from impacket import ImpactDecoder, ImpactPacket

def add_image(window) :
	label = QLabel(window)
	#painter = QtGui.QPainter()
	filename = mu.IMAGE_FOLDER+"main_back1.jpg"
	pixmap = QPixmap(filename)
	#pixmap.scaled(1000,1000)
	#painter.drawPixmap(QtCore.QPoint(1000,1000),pixmap)
	label.setPixmap(pixmap)
	label.setGeometry(QtCore.QRect(1,1,620,440))
	label.show()
	
	palet = QtGui.QPalette()
	palet.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
	banner = QLabel('Coded by Tony Stark', window)
	banner.setGeometry(QtCore.QRect(10,20,150,120))# x1,y1,x2,y2
	banner.move(15,15)
	banner.setPalette(palet)
	font = QtGui.QFont()
	font.setPointSize(10)
	banner.setFont(font)

class MyWindow(QtGui.QDialog):    # any super class is okay
	def __init__(self, parent=None):
		super(MyWindow, self).__init__(parent)
		#self.button = QtGui.QPushButton('Quit')
		layout = QtGui.QHBoxLayout()
		#layout.addWidget(self.button)
		self.resize(400,400)
		self.setLayout(layout)
		#self.button.move(70,370)
		#self.button.clicked.connect(self.create_child())
	def create_child(self):
		# here put the code that creates the new window and shows it.
		child = MyWindow(self)
		return child

def google_search(query):
	if len(query) < 1:
		return 
	query = "https://www.google.com/search?q=" + mut.urlify(query)
	webbrowser.get('firefox').open(query)

def youtube_search(query):
	if len(query) < 1:
		return 
	query = "https://www.youtube.com/results?q=" + mut.urlify(query)
	webbrowser.get('firefox').open(query)

def create(window):
	#add image
	add_image(window)
	
	#Google Search
	#input
	google_input = QLineEdit(window)
	google_input.move(50, 120)
	google_input.resize(280,25)
	#btn
	google_btn = QPushButton('Google Search', window)
	google_btn.setToolTip('Enter Query and click')
	google_btn.clicked.connect(lambda: google_search(str(google_input.text())))#query
	google_btn.resize(google_btn.sizeHint())
	google_btn.move(350, 120)
	
	#Youtube Search
	#input
	youtube_input = QLineEdit(window)
	youtube_input.move(50, 160)
	youtube_input.resize(280,25)
	#btn
	youtube_btn = QPushButton('Youtube Search', window)
	youtube_btn.setToolTip('Enter Query and click')
	youtube_btn.clicked.connect(lambda: youtube_search(str(youtube_input.text())))#query
	youtube_btn.resize(youtube_btn.sizeHint())
	youtube_btn.move(350, 160)
	

if __name__ == '__main__':
	# QApplication created only here.
	app = QtGui.QApplication([])
	window = MyWindow()
	window.resize(620,440) #(width,height)
	window.setWindowTitle("JARVIS Control Screen")
	
	create(window)
	
	window.show()
	app.exec_()
