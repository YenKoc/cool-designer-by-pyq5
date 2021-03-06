from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login_Ui(object):
 def setupUi(self, login_Ui):
  login_Ui.setObjectName("login_Ui")
  login_Ui.resize(581, 533)
  self.gridLayoutWidget = QtWidgets.QWidget(login_Ui)
  self.gridLayoutWidget.setGeometry(QtCore.QRect(160, 330, 295, 141))
  self.gridLayoutWidget.setObjectName("gridLayoutWidget")
  self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
  self.gridLayout.setContentsMargins(0, 0, 0, 0)
  self.gridLayout.setObjectName("gridLayout")
  self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
  self.horizontalLayout_2.setObjectName("horizontalLayout_2")
  self.loginButton = QtWidgets.QPushButton(self.gridLayoutWidget)
  self.loginButton.setObjectName("loginButton")
  self.horizontalLayout_2.addWidget(self.loginButton)
  self.registerButton = QtWidgets.QPushButton(self.gridLayoutWidget)
  self.registerButton.setObjectName("registerButton")
  self.horizontalLayout_2.addWidget(self.registerButton)
  self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
  self.pushButton.setObjectName("pushButton")
  self.horizontalLayout_2.addWidget(self.pushButton)
  self.gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
  self.userlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
  self.userlineEdit.setObjectName("userlineEdit")
  self.gridLayout.addWidget(self.userlineEdit, 0, 1, 1, 1)
  self.userLabel = QtWidgets.QLabel(self.gridLayoutWidget)
  self.userLabel.setObjectName("userLabel")
  self.gridLayout.addWidget(self.userLabel, 0, 0, 1, 1)
  self.labelTip = QtWidgets.QLabel(self.gridLayoutWidget)
  self.labelTip.setObjectName("labelTip")
  self.gridLayout.addWidget(self.labelTip, 3, 1, 1, 1)
  self.pwdlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
  self.pwdlineEdit.setObjectName("pwdlineEdit")
  self.gridLayout.addWidget(self.pwdlineEdit, 1, 1, 1, 1)
  self.pwdlabel = QtWidgets.QLabel(self.gridLayoutWidget)
  self.pwdlabel.setObjectName("pwdlabel")
  self.gridLayout.addWidget(self.pwdlabel, 1, 0, 1, 1)
  self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
  self.comboBox.setObjectName("comboBox")
  self.comboBox.addItem("")
  self.comboBox.addItem("")
  self.comboBox.addItem("")
  self.comboBox.addItem("")
  self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
  self.label = QtWidgets.QLabel(self.gridLayoutWidget)
  self.label.setObjectName("label")
  self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
  self.label_2 = QtWidgets.QLabel(login_Ui)
  self.label_2.setGeometry(QtCore.QRect(-10, 0, 601, 321))
  self.label_2.setText("")
  self.label_2.setObjectName("label_2")

  self.retranslateUi(login_Ui)
  QtCore.QMetaObject.connectSlotsByName(login_Ui)

 def retranslateUi(self, login_Ui):
  _translate = QtCore.QCoreApplication.translate
  login_Ui.setWindowTitle(_translate("login_Ui", "Form"))
  self.loginButton.setText(_translate("login_Ui", "登 陆"))
  self.registerButton.setText(_translate("login_Ui", "注 册"))
  self.pushButton.setText(_translate("login_Ui", "找回密码"))
  self.userLabel.setText(_translate("login_Ui", " 账 户"))
  self.labelTip.setText(_translate("login_Ui", "密码或用户名错误"))
  self.pwdlabel.setText(_translate("login_Ui", " 密 码"))
  self.comboBox.setItemText(0, _translate("login_Ui", "财务管理员"))
  self.comboBox.setItemText(1, _translate("login_Ui", "信息管理员"))
  self.comboBox.setItemText(2, _translate("login_Ui", "停车场管理员"))
  self.comboBox.setItemText(3, _translate("login_Ui", "超级管理员"))
  self.label.setText(_translate("login_Ui", " 请选择"))