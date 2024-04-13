# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 594)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.videoWidget = QVideoWidget(self.centralwidget)
        self.videoWidget.setGeometry(QtCore.QRect(0, 0, 801, 441))
        self.videoWidget.setObjectName("videoWidget")
        self.playOrPauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.playOrPauseButton.setGeometry(QtCore.QRect(10, 500, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.playOrPauseButton.setFont(font)
        self.playOrPauseButton.setObjectName("playOrPauseButton")
        self.openVideoFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.openVideoFileButton.setGeometry(QtCore.QRect(690, 500, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.openVideoFileButton.setFont(font)
        self.openVideoFileButton.setObjectName("openVideoFileButton")
        self.openCaptionFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.openCaptionFileButton.setGeometry(QtCore.QRect(580, 500, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.openCaptionFileButton.setFont(font)
        self.openCaptionFileButton.setObjectName("openCaptionFileButton")
        self.durationSlider = QtWidgets.QSlider(self.centralwidget)
        self.durationSlider.setGeometry(QtCore.QRect(170, 510, 341, 22))
        self.durationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.durationSlider.setObjectName("durationSlider")
        self.durationLabel = QtWidgets.QLabel(self.centralwidget)
        self.durationLabel.setGeometry(QtCore.QRect(520, 500, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.durationLabel.setFont(font)
        self.durationLabel.setObjectName("durationLabel")
        self.speakerLabel = QtWidgets.QLabel(self.centralwidget)
        self.speakerLabel.setGeometry(QtCore.QRect(10, 450, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.speakerLabel.setFont(font)
        self.speakerLabel.setObjectName("speakerLabel")
        self.textLabel = QtWidgets.QLabel(self.centralwidget)
        self.textLabel.setGeometry(QtCore.QRect(180, 450, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textLabel.setFont(font)
        self.textLabel.setObjectName("textLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "專題"))
        self.playOrPauseButton.setText(_translate("MainWindow", "播放/暫停"))
        self.openVideoFileButton.setText(_translate("MainWindow", "選擇影片"))
        self.openCaptionFileButton.setText(_translate("MainWindow", "選擇字幕"))
        self.durationLabel.setText(_translate("MainWindow", "00:00"))
        self.speakerLabel.setText(_translate("MainWindow", "Speaker"))
        self.textLabel.setText(_translate("MainWindow", "Text"))
from PyQt5.QtMultimediaWidgets import QVideoWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
