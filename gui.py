# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Mar 12 15:17:08 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from main import *


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

	def change_label():
		# stores name input in filename
		input_file = '{}'.format(self.txt_name_input.text())
		main(input_file)

        # close the interface
        def close_it():
            QtCore.QCoreApplication.instance().quit()


        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(400,150)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.txt_name_input = QtGui.QLineEdit(self.centralWidget)
        self.txt_name_input.setObjectName(_fromUtf8("txt_name_input"))
        self.gridLayout.addWidget(self.txt_name_input, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.btn_close = QtGui.QPushButton(self.centralWidget)
        self.btn_close.setObjectName(_fromUtf8("btn_close"))
        QtCore.QObject.connect(self.btn_close, QtCore.SIGNAL(_fromUtf8("clicked()")), close_it)


        self.gridLayout.addWidget(self.btn_close, 3, 1, 1, 1)
        self.btn_search = QtGui.QPushButton(self.centralWidget)
        self.btn_search.setObjectName(_fromUtf8("btn_search"))
	# change label example
        QtCore.QObject.connect(self.btn_search, QtCore.SIGNAL(_fromUtf8("clicked()")), change_label)


        self.gridLayout.addWidget(self.btn_search, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 651, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Facebook Visualiser", None))
        self.label.setText(_translate("MainWindow", "Enter File Name", None))
        self.btn_close.setText(_translate("MainWindow", "Close", None))
        self.btn_search.setText(_translate("MainWindow", "Search", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

