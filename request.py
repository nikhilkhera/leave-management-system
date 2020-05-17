# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'request.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from fire import db
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RequestWindow(object):
    def __init__(self,message1,message2):
        self.eidf=message1
        self.mngridf=message2
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.leave_by_ssn=db.child("leaves").order_by_child("ssn").equal_to(self.eidf).get()
        try:
            self.a1=self.leave_by_ssn.val()
            self.ec=1
        except Exception:
            self.a1={}
            self.ec=0
        self.n=[key for key in self.a1.keys()]
        print(self.n)

        self.user_by_ssn=db.child("users").child(self.eidf).get()
        self.a2=self.user_by_ssn.val()
        self.priv_bl=self.a2['priv_bl']
        self.sick_bl=self.a2['sick_bl']
        self.wfh_bl=self.a2['wfh_bl']
        self.casual_bl=self.a2['casual_bl']
        self.pen_req_made1=self.a2['pen_req_made']



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 664)
        MainWindow.setMinimumSize(QtCore.QSize(951, 664))
        MainWindow.setMaximumSize(QtCore.QSize(951, 664))
        MainWindow.setSizeIncrement(QtCore.QSize(951, 664))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-60, -60, 1091, 711))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("background3.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.background.raise_()
        self.typelv_cbox = QtWidgets.QComboBox(self.centralwidget)
        self.typelv_cbox.setGeometry(QtCore.QRect(450, 310, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.typelv_cbox.setFont(font)
        self.typelv_cbox.setObjectName("typelv_cbox")
        self.typelv_cbox.addItem("")
        self.typelv_cbox.addItem("")
        self.typelv_cbox.addItem("")
        self.typelv_cbox.addItem("")
        self.tol_lb = QtWidgets.QLabel(self.centralwidget)
        self.tol_lb.setGeometry(QtCore.QRect(280, 310, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.tol_lb.setFont(font)
        self.tol_lb.setObjectName("tol_lb")
        self.sd_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.sd_2.setGeometry(QtCore.QRect(450, 360, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.sd_2.setFont(font)
        self.sd_2.setObjectName("sd_2")
        self.balv = QtWidgets.QLabel(self.centralwidget)
        self.balv.setGeometry(QtCore.QRect(810, 310, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.balv.setFont(font)
        self.balv.setObjectName("balv")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 350, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 400, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.td_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.td_2.setGeometry(QtCore.QRect(450, 410, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.td_2.setFont(font)
        self.td_2.setText("")
        self.td_2.setObjectName("td_2")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(370, 480, 141, 61))
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit.setObjectName("submit")
        self.submit_status = QtWidgets.QLabel(self.centralwidget)
        self.submit_status.setGeometry(QtCore.QRect(370, 560, 331, 16))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(8)
        self.submit_status.setFont(font)
        self.submit_status.setText("")
        self.submit_status.setObjectName("submit_status")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(120, 250, 691, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.rlv_lb = QtWidgets.QLabel(self.centralwidget)
        self.rlv_lb.setGeometry(QtCore.QRect(360, 250, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.rlv_lb.setFont(font)
        self.rlv_lb.setObjectName("rlv_lb")
        self.lvid_lb = QtWidgets.QLabel(self.centralwidget)
        self.lvid_lb.setGeometry(QtCore.QRect(290, 60, 101, 31))
        self.lvid_lb.setObjectName("lvid_lb")
        self.lvid = QtWidgets.QComboBox(self.centralwidget)
        self.lvid.setGeometry(QtCore.QRect(450, 60, 241, 31))
        self.lvid.setObjectName("lvid")
        self.select1 = QtWidgets.QPushButton(self.centralwidget)
        self.select1.setGeometry(QtCore.QRect(720, 60, 141, 30))
        self.select1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select1.setObjectName("select1")
        self.select1.setText("select")
        self.sd_lb1 = QtWidgets.QLabel(self.centralwidget)
        self.sd_lb1.setGeometry(QtCore.QRect(290, 130, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.sd_lb1.setFont(font)
        self.sd_lb1.setObjectName("sd_lb1")
        self.td_lb1 = QtWidgets.QLabel(self.centralwidget)
        self.td_lb1.setGeometry(QtCore.QRect(290, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.td_lb1.setFont(font)
        self.td_lb1.setObjectName("td_lb1")
        self.status_lb1 = QtWidgets.QLabel(self.centralwidget)
        self.status_lb1.setGeometry(QtCore.QRect(290, 220, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.status_lb1.setFont(font)
        self.status_lb1.setObjectName("status_lb1")
        self.lv_type_lb1 = QtWidgets.QLabel(self.centralwidget)
        self.lv_type_lb1.setGeometry(QtCore.QRect(290, 90, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lv_type_lb1.setFont(font)
        self.lv_type_lb1.setObjectName("lv_type_lb1")
        self.typelv = QtWidgets.QLabel(self.centralwidget)
        self.typelv.setGeometry(QtCore.QRect(450, 100, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.typelv.setFont(font)
        self.typelv.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.typelv.setObjectName("typelv")
        self.sd_1 = QtWidgets.QLabel(self.centralwidget)
        self.sd_1.setGeometry(QtCore.QRect(450, 140, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.sd_1.setFont(font)
        self.sd_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sd_1.setObjectName("sd_1")
        self.td_1 = QtWidgets.QLabel(self.centralwidget)
        self.td_1.setGeometry(QtCore.QRect(450, 180, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.td_1.setFont(font)
        self.td_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.td_1.setObjectName("td_1")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(450, 220, 391, 30))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.status.setFont(font)
        self.status.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.status.setObjectName("status")
        self.rq_lv_lb = QtWidgets.QLabel(self.centralwidget)
        self.rq_lv_lb.setGeometry(QtCore.QRect(340, 0, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.rq_lv_lb.setFont(font)
        self.rq_lv_lb.setObjectName("rq_lv_lb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 951, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.bal = QtWidgets.QPushButton(self.centralwidget)
        self.bal.setGeometry(QtCore.QRect(710, 310, 93, 31))
        self.bal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bal.setObjectName("bal")
        self.bal.setText("Balance :")
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.coboxitems(self.n)
        if(self.ec==1):
            self.select1.clicked.connect(self.clickedselect1)
        self.submit.clicked.connect(self.clickedsumbit)
        self.bal.clicked.connect(self.clickedbal)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.typelv_cbox.setItemText(0, _translate("MainWindow", "Sick leave"))
        self.typelv_cbox.setItemText(1, _translate("MainWindow", "Casual leave"))
        self.typelv_cbox.setItemText(2, _translate("MainWindow", "Privilege leave"))
        self.typelv_cbox.setItemText(3, _translate("MainWindow", "Work from home"))
        self.tol_lb.setText(_translate("MainWindow", "Type of leave :"))
        self.label.setText(_translate("MainWindow", "Starting date :"))
        self.label_4.setText(_translate("MainWindow", "Total days :"))
        self.submit.setText(_translate("MainWindow", "SUBMIT"))
        self.rlv_lb.setText(_translate("MainWindow", "REQUEST LEAVE"))
        self.lvid_lb.setText(_translate("MainWindow", "Leave ID :"))
        self.sd_lb1.setText(_translate("MainWindow", "Starting date :"))
        self.td_lb1.setText(_translate("MainWindow", "Total days :"))
        self.status_lb1.setText(_translate("MainWindow", "Status :"))
        self.lv_type_lb1.setText(_translate("MainWindow", "Type of Leave :"))
        self.typelv.setText(_translate("MainWindow", "none"))
        self.sd_1.setText(_translate("MainWindow", "none"))
        self.td_1.setText(_translate("MainWindow", "none"))
        self.status.setText(_translate("MainWindow", "none"))
        self.rq_lv_lb.setText(_translate("MainWindow", "REQUESTED LEAVE"))

    def coboxitems(self,lis):
        lis.reverse()
        for i in range(len(lis)):
            self.lvid.addItem(lis[i])
    def clickedselect1(self):
        self.lvidf=self.lvid.currentText()
        print(self.lvidf)
        self.users_by_lvid=db.child("leaves").child(self.lvidf).get()
        self.a=self.users_by_lvid.val()
        print(self.a)
        self.start_datef=self.a['start_date']
        self.statusf=self.a['status']
        self.total_daysf=self.a['total_days']
        self.typef=self.a['type']
        print("000000000000000000000000000000000000")
        self.sd_1.setText(self.start_datef)
        self.status.setText(self.statusf)
        self.td_1.setText(str(self.total_daysf))
        self.typelv.setText(self.typef)

    def clickedsumbit(self) :
        try:
            self.nextlvid=db.child("nextlvid").get().val()
            self.start_datef1=self.sd_2.text()
            self.typef1=self.typelv_cbox.currentText()
            self.total_daysf1=int(self.td_2.text())
            self.balance=self.switch(self.typef1)-self.total_daysf1
        
            if(self.balance>=0):
            
                if(self.typef1=="Casual leave"):
                    self.casual_bl=self.balance
                elif(self.typef1=="Privilege leave"):
                    self.priv_bl=self.balance
                elif(self.typef1=="Work from home"):
                    self.wfh_bl=self.balance
                elif(self.typef1=="Sick leave"):
                    self.sick_bl=self.balance
                else:
                    print("Error ")

                self.pen_req_made1=self.pen_req_made1+1
                self.pen_req_rec1=db.child("users").child(self.mngridf).child("pen_req_rec").get().val()
                self.pen_req_rec1=self.pen_req_rec1+1
                
                
                
                data1 = {
                        "users/"+self.mngridf+"/pen_req_rec":self.pen_req_rec1,
                        "users/"+self.eidf+"/pen_req_made":self.pen_req_made1,
                        "users/"+self.eidf+"/casual_bl": self.casual_bl,            
                        "users/"+self.eidf+"/priv_bl": self.priv_bl,
                        "users/"+self.eidf+"/wfh_bl": self.wfh_bl,
                        "users/"+self.eidf+"/sick_bl": self.sick_bl
                        }   
                data2={
                        "mngr_ssn":self.mngridf,
                        "ssn": self.eidf,
                        "start_date":self.start_datef1,
                        "status": "pending",
                        "total_days":self.total_daysf1,
                        "type": self.typef1           
                        } 
                db.child("leaves").child(str(self.nextlvid)).set(data2)
                self.lvid.addItem(str(self.nextlvid)) 
                self.nextlvid=self.nextlvid+1
                db.update({"nextlvid":self.nextlvid})
                db.update(data1)
                self.submit_status.setText("leave request submitted")
                self.balv.setText("")
                if(self.ec==0):
                    self.ec=1
                    self.select1.clicked.connect(self.clickedselect1)

            else:
                print("insufficient leave balance")
                self.submit_status.setText("insufficient leave balance")
        except Exception :
            self.submit_status.setText("leave request failed")

    def switch(self,lv):
        switcher={ "Casual leave" : self.casual_bl,
                    "Privilege leave": self.priv_bl,
                    "Work from home": self.wfh_bl,
                    "Sick leave": self.sick_bl
                }
        return switcher[lv]

    def clickedbal(self):
        self.typef1=self.typelv_cbox.currentText()
        self.balancev= self.switch(self.typef1)
        self.balv.setText(str(self.balancev))
    
    def updateleaves(self):
        self.priv_bl=self.a2['priv_bl']
        self.sick_bl=self.a2['sick_bl']
        self.wfh_bl=self.a2['wfh_bl']
        self.casual_bl=self.a2['casual_bl']
        
        
        
        
