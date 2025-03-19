# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/open_files_dialog.ui'
#
# Created: Thu Oct 31 15:38:50 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(657, 151)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ctLineEdit = QtWidgets.QLineEdit(Dialog)
        self.ctLineEdit.setObjectName("ctLineEdit")
        self.horizontalLayout.addWidget(self.ctLineEdit)
        self.ctPushButton = QtWidgets.QPushButton(Dialog)
        self.ctPushButton.setObjectName("ctPushButton")
        self.horizontalLayout.addWidget(self.ctPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.duraLineEdit = QtWidgets.QLineEdit(Dialog)
        self.duraLineEdit.setObjectName("duraLineEdit")
        self.horizontalLayout_2.addWidget(self.duraLineEdit)
        self.duraPushButton = QtWidgets.QPushButton(Dialog)
        self.duraPushButton.setObjectName("duraPushButton")
        self.horizontalLayout_2.addWidget(self.duraPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Open)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", "Open CT and dura..."))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", "CT volume"))
        self.ctLineEdit.setPlaceholderText(QtCore.QCoreApplication.translate("Dialog", "path to co-registered CT head scan"))
        self.ctPushButton.setText(QtCore.QCoreApplication.translate("Dialog", "Browse..."))
        self.label_2.setText(QtCore.QCoreApplication.translate("Dialog", "Dura mesh"))
        self.duraLineEdit.setPlaceholderText(QtCore.QCoreApplication.translate("Dialog", "path to dura surface mesh"))
        self.duraPushButton.setText(QtCore.QCoreApplication.translate("Dialog", "Browse..."))