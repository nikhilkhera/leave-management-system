# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'employee.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from fire import db,auth
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import string


class Ui_EmployeeWindow(object):
    def __init__(self,message1):
        
        self.eidf=message1
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.user_by_mngr_ssn=db.child("users").order_by_child("mngr_ssn").equal_to(self.eidf).get()
        try:
            self.a1=self.user_by_mngr_ssn.val()
            self.ec=1
        except Exception:
            self.a1={}
            self.ec=0
        print(self.a1)
        self.n=[key for key in self.a1.keys()]


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 664)
        MainWindow.setMinimumSize(QtCore.QSize(951, 664))
        MainWindow.setMaximumSize(QtCore.QSize(951, 664))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-60, -60, 1091, 711))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("background3.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.background.raise_()
        self.empid_lb = QtWidgets.QLabel(self.centralwidget)
        self.empid_lb.setGeometry(QtCore.QRect(300, 70, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.empid_lb.setFont(font)
        self.empid_lb.setObjectName("empid_lb")
        self.name_lb1 = QtWidgets.QLabel(self.centralwidget)
        self.name_lb1.setGeometry(QtCore.QRect(20, 120, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.name_lb1.setFont(font)
        self.name_lb1.setObjectName("name_lb1")
        self.eid_lb1 = QtWidgets.QLabel(self.centralwidget)
        self.eid_lb1.setGeometry(QtCore.QRect(20, 160, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.eid_lb1.setFont(font)
        self.eid_lb1.setObjectName("eid_lb1")
        self.eid1 = QtWidgets.QLabel(self.centralwidget)
        self.eid1.setGeometry(QtCore.QRect(130, 160, 651, 22))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.eid1.setFont(font)
        self.eid1.setObjectName("eid1")
        self.phone_lb1 = QtWidgets.QLabel(self.centralwidget)
        self.phone_lb1.setGeometry(QtCore.QRect(20, 240, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.phone_lb1.setFont(font)
        self.phone_lb1.setObjectName("phone_lb1")
        self.addr_lb1 = QtWidgets.QLabel(self.centralwidget)
        self.addr_lb1.setGeometry(QtCore.QRect(20, 200, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.addr_lb1.setFont(font)
        self.addr_lb1.setObjectName("addr_lb1")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 0, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(160, 300, 621, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(790, 120, 20, 141))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.name1 = QtWidgets.QLineEdit(self.centralwidget)
        self.name1.setGeometry(QtCore.QRect(130, 120, 651, 22))
        self.name1.setText("")
        self.name1.setObjectName("name1")
       
        self.addr1 = QtWidgets.QLineEdit(self.centralwidget)
        self.addr1.setGeometry(QtCore.QRect(130, 200, 651, 22))
        self.addr1.setObjectName("addr1")
        self.phone1 = QtWidgets.QLineEdit(self.centralwidget)
        self.phone1.setGeometry(QtCore.QRect(130, 240, 651, 22))
        self.phone1.setObjectName("phone1")
        self.edit = QtWidgets.QPushButton(self.centralwidget)
        self.edit.setGeometry(QtCore.QRect(820, 120, 111, 51))
        self.edit.setObjectName("edit")
        self.editstatus = QtWidgets.QLabel(self.centralwidget)
        self.editstatus.setGeometry(QtCore.QRect(820, 180, 131, 16))
        self.editstatus.setText("")
        self.editstatus.setObjectName("editstatus")
        self.phone_lb2 = QtWidgets.QLabel(self.centralwidget)
        self.phone_lb2.setGeometry(QtCore.QRect(10, 510, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.phone_lb2.setFont(font)
        self.phone_lb2.setObjectName("phone_lb2")
        self.addr_lb2 = QtWidgets.QLabel(self.centralwidget)
        self.addr_lb2.setGeometry(QtCore.QRect(10, 470, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.addr_lb2.setFont(font)
        self.addr_lb2.setObjectName("addr_lb2")
        self.eid2 = QtWidgets.QLineEdit(self.centralwidget)
        self.eid2.setGeometry(QtCore.QRect(120, 430, 661, 22))
        self.eid2.setObjectName("eid2")
        self.phone2 = QtWidgets.QLineEdit(self.centralwidget)
        self.phone2.setGeometry(QtCore.QRect(120, 510, 661, 22))
        self.phone2.setObjectName("phone2")
        self.name2 = QtWidgets.QLineEdit(self.centralwidget)
        self.name2.setGeometry(QtCore.QRect(120, 390, 661, 22))
        self.name2.setText("")
        self.name2.setObjectName("name2")
        self.eid_lb2 = QtWidgets.QLabel(self.centralwidget)
        self.eid_lb2.setGeometry(QtCore.QRect(10, 430, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.eid_lb2.setFont(font)
        self.eid_lb2.setObjectName("eid_lb2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(820, 450, 131, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(790, 390, 20, 141))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.name_lb2 = QtWidgets.QLabel(self.centralwidget)
        self.name_lb2.setGeometry(QtCore.QRect(10, 390, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.name_lb2.setFont(font)
        self.name_lb2.setObjectName("name_lb2")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(820, 390, 111, 51))
        self.add.setObjectName("add")
        self.addr2 = QtWidgets.QLineEdit(self.centralwidget)
        self.addr2.setGeometry(QtCore.QRect(120, 470, 661, 22))
        self.addr2.setObjectName("addr2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 310, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(420, 60, 131, 31))
        self.comboBox.setObjectName("comboBox")
        self.select = QtWidgets.QPushButton(self.centralwidget)
        self.select.setGeometry(QtCore.QRect(600, 60, 111, 31))
        self.select.setObjectName("select")
        self.select.setText("Select")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(800, 10, 131, 28))
        self.reset.setObjectName("reset")
        self.reset.setText("Reset Leave Balance")
        self.resets = QtWidgets.QLabel(self.centralwidget)
        self.resets.setGeometry(QtCore.QRect(820, 40, 131, 16))
        self.resets.setObjectName("resets")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 951, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
    

        self.reset.clicked.connect(self.clickedreset)
        self.coboxitems(self.n)
        if (self.ec==1):
            self.select.clicked.connect(self.clickedselect)
        self.edit.clicked.connect(self.clickededit)
        self.add.clicked.connect(self.clickedadd)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.empid_lb.setText(_translate("MainWindow", "EMPLOYEE ID :"))
        self.name_lb1.setText(_translate("MainWindow", "NAME :  "))
        self.eid_lb1.setText(_translate("MainWindow", "EMAIL ID :"))
        self.phone_lb1.setText(_translate("MainWindow", "PHONE NO. :"))
        self.addr_lb1.setText(_translate("MainWindow", "ADDRESS :"))
        self.label_3.setText(_translate("MainWindow", "EMPLOYEE DETAILS"))
        self.edit.setText(_translate("MainWindow", "EDIT"))
        self.phone_lb2.setText(_translate("MainWindow", "PHONE NO. :"))
        self.addr_lb2.setText(_translate("MainWindow", "ADDRESS :"))
        self.eid_lb2.setText(_translate("MainWindow", "EMAIL ID :"))
        self.name_lb2.setText(_translate("MainWindow", "NAME :  "))
        self.add.setText(_translate("MainWindow", "ADD"))
        self.label_4.setText(_translate("MainWindow", "ADD EMPLOYEE"))
    
    def coboxitems(self,lis):
        for i in range(len(lis)):
            self.comboBox.addItem(lis[i])
    def clickedselect(self):
        self.eids=self.comboBox.currentText()
        print(self.eids)
        self.users_by_key=db.child("users").child(self.eids).get()
        self.a=self.users_by_key.val()
        print(self.a)
        self.addf=self.a['address']
        self.namef=self.a['name']
        self.phonef=self.a['phone_no']
        self.email=self.a['email']
        self.name1.setText(self.namef)
        self.eid1.setText(self.email)
        self.phone1.setText(self.phonef)
        self.addr1.setText(self.addf)
        self.editstatus.setText("")
    def clickededit(self):
        try:
            data1 = {
                    "users/"+self.eids+"/name": self.name1.text(),            
                    "users/"+self.eids+"/address": self.addr1.text(),
                    "users/"+self.eids+"/phone_no": self.phone1.text(),
                    }   
            db.update(data1)
            self.editstatus.setText("Edit Successful")
        except Exception:
            self.editstatus.setText("Edit failed")
    def clickedadd(self):
        try:
            self.nextssn=db.child("nextssn").get().val()
            auth.create_user_with_email_and_password(self.eid2.text(),self.randomString(8))
            data2={
                    "email":self.eid2.text(),
                    "name":self.name2.text(),
                    "address": self.addr2.text(),
                    "phone_no": self.phone2.text(),
                    "mngr_ssn":self.eidf,
                    "pen_req_made": 0,
                    "pen_req_rec": 0,
                    "casual_bl": 10,
                    "priv_bl":10,
                    "sick_bl":10,
                    "wfh_bl":10            
                } 
            db.child("users").child(str(self.nextssn)).set(data2)
            self.n.append(str(self.nextssn))
            self.comboBox.addItem(str(self.nextssn)) 
            self.nextssn=self.nextssn+1
            auth.send_password_reset_email(self.eid2.text())
            db.update({"nextssn":self.nextssn})
            self.label_2.setText("add successful")
            self.defaulttxt()
        except Exception :
            self.label_2.setText("add failed")
            
    def randomString(self,stringLength=8):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))   

    def defaulttxt(self):
        self.name2.setText("")
        self.addr2.setText("")
        self.eid2.setText("")
        self.phone2.setText("")
    
    def clickedreset(self):
        for key in self.n:
            print(key)
            self.resets.setText("It might take some time")
            data={
                  
                    "users/"+key+"/casual_bl": 10,            
                    "users/"+key+"/priv_bl": 10,
                    "users/"+key+"/wfh_bl": 10,
                    "users/"+key+"/sick_bl": 10
                }
            db.update(data)
        self.resets.setText("Balance updated")
        

        