# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assign.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from fire import db
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AssignWindow(object):
    def __init__(self,message1):
        self.eidf=message1
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.leave_by_ssn=db.child("leaves").order_by_child("mngr_ssn").equal_to(self.eidf).get()
        self.leave_by_pen=db.child("leaves").order_by_child("status").equal_to("pending").get()
        try:
            self.a1=self.leave_by_ssn.val()       
            self.a2=self.leave_by_pen.val()
            self.a=set( self.a1.keys() ) & set( self.a2.keys() )
            print(self.a)
            self.ec=1
        except Exception:
            self.a={}
            self.ec=0
        self.n1=[key for key in self.a]
        print(self.n1)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(954, 667)
        MainWindow.setMinimumSize(QtCore.QSize(954, 664))
        MainWindow.setMaximumSize(QtCore.QSize(954, 667))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-60, -60, 1091, 711))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("background3.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.background.raise_()
        self.lvid_cbox = QtWidgets.QComboBox(self.centralwidget)
        self.lvid_cbox.setGeometry(QtCore.QRect(460, 170, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lvid_cbox.setFont(font)
        self.lvid_cbox.setObjectName("lvid_cbox")
        self.select1 = QtWidgets.QPushButton(self.centralwidget)
        self.select1.setGeometry(QtCore.QRect(640, 170, 141, 30))
        self.select1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select1.setObjectName("select1")
        self.select1.setText("select")
        self.lvid_lb = QtWidgets.QLabel(self.centralwidget)
        self.lvid_lb.setGeometry(QtCore.QRect(270, 170, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lvid_lb.setFont(font)
        self.lvid_lb.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lvid_lb.setObjectName("lvid_lb")
        self.sta = QtWidgets.QLabel(self.centralwidget)
        self.sta.setGeometry(QtCore.QRect(314, 540, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.sta.setFont(font)
        self.sta.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sta.setObjectName("sta")
        self.sd_lb = QtWidgets.QLabel(self.centralwidget)
        self.sd_lb.setGeometry(QtCore.QRect(270, 290, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.sd_lb.setFont(font)
        self.sd_lb.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sd_lb.setObjectName("sd_lb")
        self.td_lb = QtWidgets.QLabel(self.centralwidget)
        self.td_lb.setGeometry(QtCore.QRect(270, 330, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.td_lb.setFont(font)
        self.td_lb.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.td_lb.setObjectName("td_lb")
        
        self.empname_lb = QtWidgets.QLabel(self.centralwidget)
        self.empname_lb.setGeometry(QtCore.QRect(270, 220, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.empname_lb.setFont(font)
        self.empname_lb.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.empname_lb.setObjectName("empname_lb")
        self.empname = QtWidgets.QLabel(self.centralwidget)
        self.empname.setGeometry(QtCore.QRect(470, 220, 431, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.empname.setFont(font)
        self.empname.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.empname.setObjectName("empname")
        self.sd = QtWidgets.QLabel(self.centralwidget)
        self.sd.setGeometry(QtCore.QRect(470, 300, 431, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.sd.setFont(font)
        self.sd.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sd.setObjectName("sd")
        self.td = QtWidgets.QLabel(self.centralwidget)
        self.td.setGeometry(QtCore.QRect(470, 340, 461, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.td.setFont(font)
        self.td.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.td.setObjectName("td")
        self.ty = QtWidgets.QLabel(self.centralwidget)
        self.ty.setGeometry(QtCore.QRect(470, 385, 461, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.ty.setFont(font)
        self.ty.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ty.setObjectName("ty")
        self.ty.setText("none")
        self.ty_lb = QtWidgets.QLabel(self.centralwidget)
        self.ty_lb.setGeometry(QtCore.QRect(270, 370, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.ty_lb.setFont(font)
        self.ty_lb.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ty_lb.setObjectName("td_ly")
        self.ty_lb.setText("Leave Type:")
        self.empid_lb = QtWidgets.QLabel(self.centralwidget)
        self.empid_lb.setGeometry(QtCore.QRect(270, 250, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.empid_lb.setFont(font)
        self.empid_lb.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.empid_lb.setObjectName("empid_lb")
        self.empid = QtWidgets.QLabel(self.centralwidget)
        self.empid.setGeometry(QtCore.QRect(470, 260, 431, 20))
        self.empid.setMinimumSize(QtCore.QSize(431, 0))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.empid.setFont(font)
        self.empid.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.empid.setObjectName("empid")
        self.accept = QtWidgets.QPushButton(self.centralwidget)
        self.accept.setGeometry(QtCore.QRect(310, 470, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.accept.setFont(font)
        self.accept.setObjectName("accept")
        self.reject = QtWidgets.QPushButton(self.centralwidget)
        self.reject.setGeometry(QtCore.QRect(430, 470, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.reject.setFont(font)
        self.reject.setObjectName("reject")
        self.manage_lb = QtWidgets.QLabel(self.centralwidget)
        self.manage_lb.setGeometry(QtCore.QRect(320, 20, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.manage_lb.setFont(font)
        self.manage_lb.setObjectName("manage_lb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 954, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        if(self.ec==1):
            self.coboxitems(self.n1)
            self.select1.clicked.connect(self.clickedselect1)
            self.accept.clicked.connect(self.clickedaccept)
            self.reject.clicked.connect(self.clickedreject)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lvid_lb.setText(_translate("MainWindow", "Select leave id:"))
        self.sd_lb.setText(_translate("MainWindow", "Starting date:"))
        self.td_lb.setText(_translate("MainWindow", "Total days:"))
        self.empname_lb.setText(_translate("MainWindow", "Employee name:"))
        self.empname.setText(_translate("MainWindow", "none"))
        self.sd.setText(_translate("MainWindow", "none"))
        self.td.setText(_translate("MainWindow", "none"))
        self.empid_lb.setText(_translate("MainWindow", "Employee ID:"))
        self.empid.setText(_translate("MainWindow", "none"))
        self.accept.setText(_translate("MainWindow", "ACCEPT"))
        self.reject.setText(_translate("MainWindow", "REJECT"))
        self.manage_lb.setText(_translate("MainWindow", "MANAGE LEAVE"))

    def coboxitems(self,arr):
            for i in range(len(arr)):
                self.lvid_cbox.addItem(arr[i])
            self.count=self.lvid_cbox.count()
    def clickedselect1(self):
        if (self.count!=0):
            self.lvids=self.lvid_cbox.currentText()
            print(self.lvids)
            self.leave_by_id=db.child("leaves").child(self.lvids).get()
            self.v=self.leave_by_id.val()
            print(self.v)
            self.start_datef=self.v['start_date']
            self.total_daysf=self.v['total_days']
            self.typef=self.v['type']
            self.ssnf=self.v['ssn']
            self.enamef=db.child("users").child(self.ssnf).child("name").get().val()
            print("00000000000000000000000000000000000000")
            self.sd.setText(self.start_datef)
            self.td.setText(str(self.total_daysf))
            self.ty.setText(self.typef)
            self.empname.setText(self.enamef)
            self.empid.setText(self.ssnf)

    def clickedaccept(self):
        self.pen_lvm=db.child("users").child(self.ssnf).child("pen_req_made").get().val()
        self.pen_lvm=self.pen_lvm-1
        self.pen_lvr=db.child("users").child(self.eidf).child("pen_req_rec").get().val()
        self.pen_lvr=self.pen_lvr-1
        print("00000000000000000000000000000000000000000000000")
        data1={
                "leaves/"+self.lvids+"/status":"accepted",
                 "users/"+self.ssnf+"/pen_req_made":self.pen_lvm,
                "users/"+self.eidf+"/pen_req_rec":self.pen_lvr
            }
        db.update(data1)
        self.sta.setText("Request Accepted")
        self.delitem(self.lvids)

    def delitem(self,leave_id):
        if(self.count==0):
            self.sta.setText("no leave assigned") 
        index = self.lvid_cbox.findText(leave_id, QtCore.Qt.MatchFixedString)
        self.lvid_cbox.removeItem(index)
        self.sd.setText("none")
        self.td.setText("none")
        self.ty.setText("none")
        self.empid.setText("none")
        self.empname.setText("none")
        self.count=self.lvid_cbox.count()  
        


    def clickedreject(self):
        self.pen_lvm1=db.child("users").child(self.ssnf).child("pen_req_made").get().val()
        self.pen_lvm1=self.pen_lvm1-1
        self.pen_lvr1=db.child("users").child(self.eidf).child("pen_req_rec").get().val()
        self.pen_lvr1=self.pen_lvr1-1
        self.casual_bl=db.child("users").child(self.ssnf).child("casual_bl").get().val()
        self.priv_bl=db.child("users").child(self.ssnf).child("priv_bl").get().val()
        self.wfh_bl=db.child("users").child(self.ssnf).child("wfh_bl").get().val()
        self.sick_bl=db.child("users").child(self.ssnf).child("sick_bl").get().val()
        

        print("111111111111111111111111111111111111111111111111111")
            
        if(self.typef=="Casual leave"):
            self.casual_bl=self.casual_bl+self.total_daysf
        elif(self.typef=="Privilege leave"):
            self.priv_bl=self.priv_bl+self.total_daysf
        elif(self.typef=="Work from home"):
            self.wfh_bl=self.wfh_bl+self.total_daysf
        elif(self.typef=="Sick leave"):
            self.sick_bl=self.sick_bl+self.total_daysf
        else:
            print("Error ")
    
        data2 = {
                    "users/"+self.eidf+"/pen_req_rec":self.pen_lvr1,
                    "users/"+self.ssnf+"/pen_req_made":self.pen_lvm1,
                    "users/"+self.ssnf+"/casual_bl": self.casual_bl,            
                    "users/"+self.ssnf+"/priv_bl": self.priv_bl,
                    "users/"+self.ssnf+"/wfh_bl": self.wfh_bl,
                    "users/"+self.ssnf+"/sick_bl": self.sick_bl,
                    "leaves/"+self.lvids+"/status":"rejected",
                }
        db.update(data2)
        self.sta.setText("Request rejected")
        self.delitem(self.lvids)

