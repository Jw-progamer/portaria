# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'porteiro/uis/main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(487, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.ip_trava = QtWidgets.QLabel(Form)
        self.ip_trava.setText("")
        self.ip_trava.setObjectName("ip_trava")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ip_trava)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.porta_trava = QtWidgets.QLabel(Form)
        self.porta_trava.setText("")
        self.porta_trava.setObjectName("porta_trava")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.porta_trava)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.iptxt = QtWidgets.QLineEdit(Form)
        self.iptxt.setObjectName("iptxt")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.iptxt)
        self.portatxt = QtWidgets.QLineEdit(Form)
        self.portatxt.setObjectName("portatxt")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.portatxt)
        self.verticalLayout.addLayout(self.formLayout)
        self.configBtn = QtWidgets.QPushButton(Form)
        self.configBtn.setObjectName("configBtn")
        self.verticalLayout.addWidget(self.configBtn)
        self.openBtn = QtWidgets.QPushButton(Form)
        self.openBtn.setObjectName("openBtn")
        self.verticalLayout.addWidget(self.openBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Portaria"))
        self.label.setText(_translate("Form", "Sistema de Portaria eletrônica"))
        self.label_2.setText(_translate("Form", "Endereço de rede da trava:"))
        self.label_3.setText(_translate("Form", "Porta de configuração da trava:"))
        self.label_4.setText(_translate("Form", "Endereço de rede:"))
        self.label_5.setText(_translate("Form", "Porta de configuração:"))
        self.configBtn.setText(_translate("Form", "Configurar Endereço"))
        self.openBtn.setText(_translate("Form", "Abrir portaria"))

