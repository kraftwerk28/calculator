# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(240, 190)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.div_btn = QtWidgets.QPushButton(Form)
        self.div_btn.setGeometry(QtCore.QRect(0, 30, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.div_btn.setFont(font)
        self.div_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.div_btn.setObjectName("div_btn")
        self.mul = QtWidgets.QPushButton(Form)
        self.mul.setGeometry(QtCore.QRect(40, 30, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.mul.setFont(font)
        self.mul.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mul.setObjectName("mul")
        self.minus = QtWidgets.QPushButton(Form)
        self.minus.setGeometry(QtCore.QRect(80, 30, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.minus.setFont(font)
        self.minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minus.setObjectName("minus")
        self.two = QtWidgets.QPushButton(Form)
        self.two.setGeometry(QtCore.QRect(40, 70, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.two.setFont(font)
        self.two.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(Form)
        self.three.setGeometry(QtCore.QRect(80, 70, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.three.setFont(font)
        self.three.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.three.setObjectName("three")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(200, 30, 41, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setObjectName("pushButton_9")
        self.plus = QtWidgets.QPushButton(Form)
        self.plus.setGeometry(QtCore.QRect(120, 30, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.plus.setFont(font)
        self.plus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plus.setObjectName("plus")
        self.dot = QtWidgets.QPushButton(Form)
        self.dot.setGeometry(QtCore.QRect(160, 30, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.dot.setFont(font)
        self.dot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dot.setObjectName("dot")
        self.one = QtWidgets.QPushButton(Form)
        self.one.setGeometry(QtCore.QRect(0, 70, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.one.setFont(font)
        self.one.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.one.setObjectName("one")
        self.zero = QtWidgets.QPushButton(Form)
        self.zero.setGeometry(QtCore.QRect(120, 70, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.zero.setFont(font)
        self.zero.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zero.setObjectName("zero")
        self.pow = QtWidgets.QPushButton(Form)
        self.pow.setGeometry(QtCore.QRect(160, 70, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.pow.setFont(font)
        self.pow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pow.setObjectName("pow")
        self.four = QtWidgets.QPushButton(Form)
        self.four.setGeometry(QtCore.QRect(0, 110, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.four.setFont(font)
        self.four.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.four.setObjectName("four")
        self.five = QtWidgets.QPushButton(Form)
        self.five.setGeometry(QtCore.QRect(40, 110, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.five.setFont(font)
        self.five.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(Form)
        self.six.setGeometry(QtCore.QRect(80, 110, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.six.setFont(font)
        self.six.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.six.setObjectName("six")
        self.del_last = QtWidgets.QPushButton(Form)
        self.del_last.setGeometry(QtCore.QRect(120, 110, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.del_last.setFont(font)
        self.del_last.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.del_last.setObjectName("del_last")
        self.left_bracket = QtWidgets.QPushButton(Form)
        self.left_bracket.setGeometry(QtCore.QRect(160, 110, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.left_bracket.setFont(font)
        self.left_bracket.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_bracket.setObjectName("left_bracket")
        self.seven = QtWidgets.QPushButton(Form)
        self.seven.setGeometry(QtCore.QRect(0, 150, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.seven.setFont(font)
        self.seven.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(Form)
        self.eight.setGeometry(QtCore.QRect(40, 150, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.eight.setFont(font)
        self.eight.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(Form)
        self.nine.setGeometry(QtCore.QRect(80, 150, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.nine.setFont(font)
        self.nine.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nine.setObjectName("nine")
        self.deletebtn = QtWidgets.QPushButton(Form)
        self.deletebtn.setGeometry(QtCore.QRect(120, 150, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.deletebtn.setFont(font)
        self.deletebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deletebtn.setObjectName("deletebtn")
        self.right_bracket = QtWidgets.QPushButton(Form)
        self.right_bracket.setGeometry(QtCore.QRect(160, 150, 39, 36))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        self.right_bracket.setFont(font)
        self.right_bracket.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.right_bracket.setObjectName("right_bracket")
        self.display = QtWidgets.QLabel(Form)
        self.display.setGeometry(QtCore.QRect(0, 0, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(12)
        self.display.setFont(font)
        self.display.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.display.setIndent(50)
        self.display.setObjectName("display")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.div_btn.setText(_translate("Form", "/"))
        self.mul.setText(_translate("Form", "*"))
        self.minus.setText(_translate("Form", "-"))
        self.two.setText(_translate("Form", "2"))
        self.three.setText(_translate("Form", "3"))
        self.pushButton_9.setText(_translate("Form", "="))
        self.plus.setText(_translate("Form", "+"))
        self.dot.setText(_translate("Form", "."))
        self.one.setText(_translate("Form", "1"))
        self.zero.setText(_translate("Form", "0"))
        self.pow.setText(_translate("Form", "^"))
        self.four.setText(_translate("Form", "4"))
        self.five.setText(_translate("Form", "5"))
        self.six.setText(_translate("Form", "6"))
        self.del_last.setText(_translate("Form", "<-"))
        self.left_bracket.setText(_translate("Form", "("))
        self.seven.setText(_translate("Form", "7"))
        self.eight.setText(_translate("Form", "8"))
        self.nine.setText(_translate("Form", "9"))
        self.deletebtn.setText(_translate("Form", "DEL"))
        self.right_bracket.setText(_translate("Form", ")"))
        self.display.setText(_translate("Form", "0"))
