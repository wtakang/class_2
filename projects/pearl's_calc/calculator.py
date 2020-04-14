# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 384)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_n2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_n2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_n2.setObjectName("pushButton_n2")
        self.gridLayout_2.addWidget(self.pushButton_n2, 4, 1, 1, 1)
        self.pushButton_n5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_n5.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_n5.setObjectName("pushButton_n5")
        self.gridLayout_2.addWidget(self.pushButton_n5, 3, 1, 1, 1)
        self.pushButton_pow = QtWidgets.QPushButton(Dialog)
        self.pushButton_pow.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_pow.setObjectName("pushButton_pow")
        self.gridLayout_2.addWidget(self.pushButton_pow, 0, 1, 1, 1)
        self.pushButton_n3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_n3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_n3.setObjectName("pushButton_n3")
        self.gridLayout_2.addWidget(self.pushButton_n3, 4, 2, 1, 1)
        self.pushButton_mr = QtWidgets.QPushButton(Dialog)
        self.pushButton_mr.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_mr.setObjectName("pushButton_mr")
        self.gridLayout_2.addWidget(self.pushButton_mr, 1, 2, 1, 1)
        self.pushButton_n8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_n8.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_n8.setObjectName("pushButton_n8")
        self.gridLayout_2.addWidget(self.pushButton_n8, 2, 1, 1, 1)
        self.pushButton_n4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_n4.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_n4.setObjectName("pushButton_n4")
        self.gridLayout_2.addWidget(self.pushButton_n4, 3, 0, 1, 1)
        self.pushButton_ac = QtWidgets.QPushButton(Dialog)
        self.pushButton_ac.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_ac.setObjectName("pushButton_ac")
        self.gridLayout_2.addWidget(self.pushButton_ac, 1, 0, 1, 1)
        self.pushButton_mod = QtWidgets.QPushButton(Dialog)
        self.pushButton_mod.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_mod.setObjectName("pushButton_mod")
        self.gridLayout_2.addWidget(self.pushButton_mod, 0, 2, 1, 1)
        self.pushButton_n7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_n7.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_n7.setObjectName("pushButton_n7")
        self.gridLayout_2.addWidget(self.pushButton_n7, 2, 0, 1, 1)
        self.pushButton_n9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_n9.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_n9.setObjectName("pushButton_n9")
        self.gridLayout_2.addWidget(self.pushButton_n9, 2, 2, 1, 1)
        self.pushButton_m = QtWidgets.QPushButton(Dialog)
        self.pushButton_m.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_m.setObjectName("pushButton_m")
        self.gridLayout_2.addWidget(self.pushButton_m, 1, 1, 1, 1)
        self.pushButton_div = QtWidgets.QPushButton(Dialog)
        self.pushButton_div.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_div.setObjectName("pushButton_div")
        self.gridLayout_2.addWidget(self.pushButton_div, 1, 3, 1, 1)
        self.pushButton_mul = QtWidgets.QPushButton(Dialog)
        self.pushButton_mul.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.gridLayout_2.addWidget(self.pushButton_mul, 2, 3, 1, 1)
        self.pushButton_pos = QtWidgets.QPushButton(Dialog)
        self.pushButton_pos.setMaximumSize(QtCore.QSize(91, 16777215))
        self.pushButton_pos.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_pos.setObjectName("pushButton_pos")
        self.gridLayout_2.addWidget(self.pushButton_pos, 0, 0, 1, 1)
        self.pushButton_n1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_n1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_n1.setObjectName("pushButton_n1")
        self.gridLayout_2.addWidget(self.pushButton_n1, 4, 0, 1, 1)
        self.pushButton_flo = QtWidgets.QPushButton(Dialog)
        self.pushButton_flo.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_flo.setObjectName("pushButton_flo")
        self.gridLayout_2.addWidget(self.pushButton_flo, 0, 3, 1, 1)
        self.pushButton_n0 = QtWidgets.QPushButton(Dialog)
        self.pushButton_n0.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_n0.setObjectName("pushButton_n0")
        self.gridLayout_2.addWidget(self.pushButton_n0, 5, 0, 1, 1)
        self.pushButton_pc = QtWidgets.QPushButton(Dialog)
        self.pushButton_pc.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_pc.setObjectName("pushButton_pc")
        self.gridLayout_2.addWidget(self.pushButton_pc, 5, 1, 1, 1)
        self.pushButton_n6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_n6.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_n6.setObjectName("pushButton_n6")
        self.gridLayout_2.addWidget(self.pushButton_n6, 3, 2, 1, 1)
        self.pushButton_sub = QtWidgets.QPushButton(Dialog)
        self.pushButton_sub.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.gridLayout_2.addWidget(self.pushButton_sub, 3, 3, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout_2.addWidget(self.pushButton_add, 4, 3, 1, 1)
        self.pushButton_eq = QtWidgets.QPushButton(Dialog)
        self.pushButton_eq.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Cambria\";\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_eq.setObjectName("pushButton_eq")
        self.gridLayout_2.addWidget(self.pushButton_eq, 5, 2, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_n2.setText(_translate("Dialog", "2"))
        self.pushButton_n5.setText(_translate("Dialog", "5"))
        self.pushButton_pow.setText(_translate("Dialog", "pow"))
        self.pushButton_n3.setText(_translate("Dialog", "3"))
        self.pushButton_mr.setText(_translate("Dialog", "MR"))
        self.pushButton_n8.setText(_translate("Dialog", "8"))
        self.pushButton_n4.setText(_translate("Dialog", "4"))
        self.pushButton_ac.setText(_translate("Dialog", "AC"))
        self.pushButton_mod.setText(_translate("Dialog", "mod"))
        self.pushButton_n7.setText(_translate("Dialog", "7"))
        self.pushButton_n9.setText(_translate("Dialog", "9"))
        self.pushButton_m.setText(_translate("Dialog", "M"))
        self.pushButton_div.setText(_translate("Dialog", "÷"))
        self.pushButton_mul.setText(_translate("Dialog", "*"))
        self.pushButton_pos.setText(_translate("Dialog", "pos"))
        self.pushButton_n1.setText(_translate("Dialog", "1"))
        self.pushButton_flo.setText(_translate("Dialog", "floor"))
        self.pushButton_n0.setText(_translate("Dialog", "0"))
        self.pushButton_pc.setText(_translate("Dialog", "%"))
        self.pushButton_n6.setText(_translate("Dialog", "6"))
        self.pushButton_sub.setText(_translate("Dialog", "-"))
        self.pushButton_add.setText(_translate("Dialog", "+"))
        self.pushButton_eq.setText(_translate("Dialog", "="))
