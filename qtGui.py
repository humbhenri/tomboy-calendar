# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtGui.ui'
#
# Created: Mon Jan 11 13:26:59 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(379, 251)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout = QtGui.QGridLayout(Frame)
        self.gridLayout.setObjectName("gridLayout")
        self.calendarWidget = QtGui.QCalendarWidget(Frame)
        self.calendarWidget.setMinimumDate(QtCore.QDate(1752, 9, 14))
        self.calendarWidget.setMaximumDate(QtCore.QDate(3000, 12, 31))
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 0, 0, 1, 4)
        self.searchEdit = QtGui.QLineEdit(Frame)
        self.searchEdit.setObjectName("searchEdit")
        self.gridLayout.addWidget(self.searchEdit, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(73, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.aboutButton = QtGui.QPushButton(Frame)
        self.aboutButton.setObjectName("aboutButton")
        self.gridLayout.addWidget(self.aboutButton, 1, 2, 1, 1)
        self.quitButton = QtGui.QPushButton(Frame)
        self.quitButton.setObjectName("quitButton")
        self.gridLayout.addWidget(self.quitButton, 1, 3, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Tomboy", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutButton.setText(QtGui.QApplication.translate("Frame", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("Frame", "Quit", None, QtGui.QApplication.UnicodeUTF8))

