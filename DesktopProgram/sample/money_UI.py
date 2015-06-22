# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'money_UI.ui'
#
# Created: Fri Jun 12 11:00:01 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from GetRateFunction import *
import sys
import images

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(393, 149)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/currency_dollar_green.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.OK = QtGui.QPushButton(self.centralwidget)
        self.OK.setGeometry(QtCore.QRect(160, 10, 75, 23))
        self.OK.setObjectName(_fromUtf8("OK"))
        self.CountryList = QtGui.QComboBox(self.centralwidget)
        self.CountryList.setGeometry(QtCore.QRect(10, 10, 141, 22))
        self.CountryList.setObjectName(_fromUtf8("CountryList"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/America.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon1, _fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/HongKong.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon2, _fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/England.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon3, _fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/Australia.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon4, _fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/Canada.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon5, _fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/Singapore.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon6, _fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/Swiss.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon7, _fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/Japan.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon8, _fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/Sweden.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon9, _fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/NewZealand.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon10, _fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/Thailand.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon11, _fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/Philippine.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon12, _fromUtf8(""))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/Indonesia.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon13, _fromUtf8(""))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/Euro.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon14, _fromUtf8(""))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/Korea.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon15, _fromUtf8(""))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/Vietnam.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon16, _fromUtf8(""))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/Malaysia.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon17, _fromUtf8(""))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/pic/China.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CountryList.addItem(icon18, _fromUtf8(""))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 371, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.title1 = QtGui.QLabel(self.groupBox)
        self.title1.setGeometry(QtCore.QRect(10, 20, 47, 12))
        self.title1.setAlignment(QtCore.Qt.AlignCenter)
        self.title1.setObjectName(_fromUtf8("title1_2"))
        self.title2 = QtGui.QLabel(self.groupBox)
        self.title2.setGeometry(QtCore.QRect(10, 50, 47, 12))
        self.title2.setAlignment(QtCore.Qt.AlignCenter)
        self.title2.setObjectName(_fromUtf8("title2_2"))
        self.result_buy = QtGui.QLabel(self.groupBox)
        self.result_buy.setGeometry(QtCore.QRect(80, 20, 47, 12))
        self.result_buy.setText(_fromUtf8(""))
        self.result_buy.setObjectName(_fromUtf8("result_buy_2"))
        self.result_sell = QtGui.QLabel(self.groupBox)
        self.result_sell.setGeometry(QtCore.QRect(80, 50, 47, 12))
        self.result_sell.setText(_fromUtf8(""))
        self.result_sell.setObjectName(_fromUtf8("result_sell_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 393, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "即時匯率查詢程式", None))
        self.OK.setText(_translate("MainWindow", "確定", None))
        self.CountryList.setItemText(0, _translate("MainWindow", "美金 (USD)", None))
        self.CountryList.setItemText(1, _translate("MainWindow", "港幣 (HKD)", None))
        self.CountryList.setItemText(2, _translate("MainWindow", "英鎊 (GBP)", None))
        self.CountryList.setItemText(3, _translate("MainWindow", "澳幣 (AUD)", None))
        self.CountryList.setItemText(4, _translate("MainWindow", "加拿大幣 (CAD)", None))
        self.CountryList.setItemText(5, _translate("MainWindow", "新加坡幣 (SGD)", None))
        self.CountryList.setItemText(6, _translate("MainWindow", "瑞士法郎 (CHF)", None))
        self.CountryList.setItemText(7, _translate("MainWindow", "日圓 (JPY)", None))
        self.CountryList.setItemText(8, _translate("MainWindow", "瑞典幣 (SEK)", None))
        self.CountryList.setItemText(9, _translate("MainWindow", "紐元 (NZD)", None))
        self.CountryList.setItemText(10, _translate("MainWindow", "泰幣 (THB)", None))
        self.CountryList.setItemText(11, _translate("MainWindow", "菲國比索 (PHP)", None))
        self.CountryList.setItemText(12, _translate("MainWindow", "印尼幣 (IDR)", None))
        self.CountryList.setItemText(13, _translate("MainWindow", "歐元 (EUR)", None))
        self.CountryList.setItemText(14, _translate("MainWindow", "韓元 (KRW)", None))
        self.CountryList.setItemText(15, _translate("MainWindow", "越南盾 (VND)", None))
        self.CountryList.setItemText(16, _translate("MainWindow", "馬來幣 (MYR)", None))
        self.CountryList.setItemText(17, _translate("MainWindow", "人民幣 (CNY)", None))
        self.groupBox.setTitle(_translate("MainWindow", "現金匯率", None))
        self.title1.setText(_translate("MainWindow", "買入", None))
        self.title2.setText(_translate("MainWindow", "賣出", None))
        self.OK.clicked.connect(self.getCountry)

    def getCountry(self):
        Value = self.CountryList.currentIndex()
        rate_list = GetInformation(Value)
        #print rate_list
        self.result_buy.setText(_translate("MainWindow", str(rate_list[0]), None))
        self.result_sell.setText(_translate("MainWindow", str(rate_list[1]), None))

    def closeEvent(self, event):
        print "User has clicked the red x on the main window"
        event.accept()

    

