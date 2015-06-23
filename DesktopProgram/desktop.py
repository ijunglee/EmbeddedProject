# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desktop.ui'
#
# Created: Tue Jun 23 08:34:31 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import serial
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class MyThread(QtCore.QThread):
    updated = QtCore.pyqtSignal(str)

    def run( self ):
        # do some functionality
        #for i in range(10000):
        #    self.updated.emit(str(i))
        #ser = serial.Serial(port='/dev/rfcomm0',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=0)
        #ser.open()
        ser = serial.Serial('/dev/rfcomm0', 9600)
        #ser.flushInput()
        #ser.flushOutput()
        while 1:
            get = ser.readline()
            strreturn = get.replace("\n","")
            getnum = strreturn.replace("A:","")
            #time.sleep(.1)
            print getnum
            #print type(getnum)
            #time.sleep(0.5)
            self.updated.emit(getnum)
            
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(326, 383)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self._thread = MyThread(self)
        self._thread.updated.connect(self.updateText)
        
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 179, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 150, 54, 51))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 201, 16))
        self.label_3.setMaximumSize(QtCore.QSize(208, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 150, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 230, 181, 31))
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(90)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 210, 201, 16))
        self.label_4.setMaximumSize(QtCore.QSize(208, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lcdNumber_2 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(10, 300, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber_2.setFont(font)
        self.lcdNumber_2.setAutoFillBackground(False)
        self.lcdNumber_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 280, 201, 16))
        self.label_5.setMaximumSize(QtCore.QSize(208, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Goal = QtGui.QLabel(self.centralwidget)
        self.Goal.setGeometry(QtCore.QRect(120, 310, 54, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Goal.setFont(font)
        self.Goal.setText(_fromUtf8(""))
        self.Goal.setObjectName(_fromUtf8("Goal"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(180, 350, 127, 26))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_7.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(13, 39, 291, 87))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.NanmeTitle = QtGui.QLabel(self.widget1)
        self.NanmeTitle.setMaximumSize(QtCore.QSize(34, 23))
        self.NanmeTitle.setObjectName(_fromUtf8("NanmeTitle"))
        self.horizontalLayout_2.addWidget(self.NanmeTitle)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget1)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(148, 0))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.widget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.spinBox = QtGui.QSpinBox(self.widget1)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_6.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.OK_button = QtGui.QPushButton(self.widget1)
        self.OK_button.setObjectName(_fromUtf8("OK_button"))
        self.horizontalLayout_3.addWidget(self.OK_button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.OK_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.clear)
        QtCore.QObject.connect(self.OK_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lcdNumber.update)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self._thread.start)
        QtCore.QObject.connect(self.progressBar, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber_2.update)
        QtCore.QObject.connect(self.lcdNumber_2, QtCore.SIGNAL(_fromUtf8("overflow()")), self.Goal.clear)
        QtCore.QObject.connect(self.OK_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.spinBox.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.spinBox.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lcdNumber.showMinimized)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.progressBar.showMinimized)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lcdNumber_2.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #self.pushbutton.clicked.connect(self._thread.start)
    def updateText( self, text ):
        self.label_6.setText(text)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Daily Rehabilitation Tracking", None))
        self.label_2.setText(_translate("MainWindow", "Personal Information", None))
        self.pushButton.setText(_translate("MainWindow", "Start", None))
        self.label_3.setText(_translate("MainWindow", "Your latest maximum angle", None))
        self.label_4.setText(_translate("MainWindow", "Current Angle", None))
        self.label_5.setText(_translate("MainWindow", "Times of reaching the maximum", None))
        self.pushButton_2.setText(_translate("MainWindow", "Save", None))
        self.pushButton_3.setText(_translate("MainWindow", "Restart", None))
        self.NanmeTitle.setText(_translate("MainWindow", "Name", None))
        self.label_6.setText(_translate("MainWindow", "Goal", None))
        self.OK_button.setText(_translate("MainWindow", "OK", None))


