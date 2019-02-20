# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Andrey\Desktop\DocCompareApp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from Driver.docCompare1 import DocCompare
import time

class Ui_MainWindow(object):

    def __init__(self):
        self.docPath1 = ""
        self.docPath2 = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 40, 141, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 140, 141, 61))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 40, 141, 91))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 140, 141, 61))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 290, 461, 191))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.setDoc1)
        self.pushButton_3.clicked.connect(self.setDoc2)
        self.pushButton.clicked.connect(self.compare)

    def setDoc1(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Document", "", "Document Files (*.txt *docx *doc)")
        self.docPath1 = path
        filename = path.split("/")[-1]
        self.label.setText(filename)

    def setDoc2(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Document", "", "Document Files (*.txt *docx *doc)")
        self.docPath2 = path
        filename = path.split("/")[-1]
        self.label_2.setText(filename)

    def compare(self):
        self.listWidget.addItem("Comparison Started...")
        QtWidgets.QApplication.processEvents()

        comparison = DocCompare(self.docPath1, self.docPath2)
        start = time.time()
        comparison.run()
        end = time.time()

        value = comparison.lastComparison()
        value = round(value*100, 2)
        filename1 = self.label.text()
        filename2 = self.label_2.text()

        self.listWidget.addItem(str(filename2) + " matches " + (str(value)) + "% to "+str(filename1))
        self.listWidget.addItem("Approximate Execution time " + str(round(end-start)) + " seconds")
        self.listWidget.scrollToBottom()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Document Compare Tool"))
        self.pushButton.setText(_translate("MainWindow", "Compare"))
        self.pushButton_2.setText(_translate("MainWindow", "Select First Doc"))
        self.pushButton_3.setText(_translate("MainWindow", "Select Second Doc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

