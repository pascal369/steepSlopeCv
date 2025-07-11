# -*- coding: utf-8 -*-
import os
import sys
import Import
import Spreadsheet
import DraftVecUtils
import Sketcher
import PartDesign
import FreeCAD as App
import FreeCADGui as Gui

from PySide import QtGui
from PySide import QtUiTools
from PySide import QtCore

class Ui_Dialog(object):
    #print('aaaaaaa')
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 625)
        Dialog.move(1000, 0)

        #水平機長
        self.label_sita = QtGui.QLabel('slopeAngle(θ)',Dialog)
        self.label_sita.setGeometry(QtCore.QRect(30, 13, 100, 22))
        self.le_sita = QtGui.QLineEdit('85',Dialog)
        self.le_sita.setGeometry(QtCore.QRect(180, 10, 60, 20))
        self.le_sita.setAlignment(QtCore.Qt.AlignCenter)
        #揚程
        self.label_H = QtGui.QLabel('liftingHight(H)',Dialog)
        self.label_H.setGeometry(QtCore.QRect(30, 38, 100, 22))
        self.le_H = QtGui.QLineEdit(Dialog)
        self.le_H.setGeometry(QtCore.QRect(180, 35, 60, 20))
        self.le_H.setAlignment(QtCore.Qt.AlignCenter)
        #テール部長
        self.label_l1 = QtGui.QLabel('tailLength(l1)',Dialog)
        self.label_l1.setGeometry(QtCore.QRect(30, 63, 100, 22))
        self.le_l1 = QtGui.QLineEdit(Dialog)
        self.le_l1.setGeometry(QtCore.QRect(180, 60, 60, 20))
        self.le_l1.setAlignment(QtCore.Qt.AlignCenter)
        #テール部高
        self.label_h1 = QtGui.QLabel('tailHight(h1)',Dialog)
        self.label_h1.setGeometry(QtCore.QRect(30, 88, 100, 22))
        self.le_h1 = QtGui.QLineEdit(Dialog)
        self.le_h1.setGeometry(QtCore.QRect(180, 85, 60, 20))
        self.le_h1.setAlignment(QtCore.Qt.AlignCenter)

        #ヘッド部長
        self.label_l2 = QtGui.QLabel('headLength(l2)',Dialog)
        self.label_l2.setGeometry(QtCore.QRect(30, 113, 100, 22))
        self.le_l2 = QtGui.QLineEdit(Dialog)
        self.le_l2.setGeometry(QtCore.QRect(180, 110, 60, 20))
        self.le_l2.setAlignment(QtCore.Qt.AlignCenter)
         #ヘッド部高
        self.label_h2 = QtGui.QLabel('headHight(h2)',Dialog)
        self.label_h2.setGeometry(QtCore.QRect(30, 138, 100, 22))
        self.le_h2 = QtGui.QLineEdit(Dialog)
        self.le_h2.setGeometry(QtCore.QRect(180, 135, 60, 20))
        self.le_h2.setAlignment(QtCore.Qt.AlignCenter)
         #ヘッドポストポジション
        self.label_x2 = QtGui.QLabel('headPosition',Dialog)
        self.label_x2.setGeometry(QtCore.QRect(30, 163, 100, 22))
        self.le_x2 = QtGui.QLineEdit('0',Dialog)
        self.le_x2.setGeometry(QtCore.QRect(180, 160, 60, 20))
        self.le_x2.setAlignment(QtCore.Qt.AlignCenter)
        #図形
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 225, 320, 400))
        self.label_6.setText("")
        
        base=os.path.dirname(os.path.abspath(__file__))
        joined_path = os.path.join(base, "steepSlopeCv.png")
        self.label_6.setPixmap(QtGui.QPixmap(joined_path))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")


        #作成
        self.pushButton = QtGui.QPushButton('create',Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 200, 50, 22))
        #更新
        self.pushButton2 = QtGui.QPushButton('update',Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(100, 200, 50, 22))
        #Import
        self.pushButton3 = QtGui.QPushButton('Import',Dialog)
        self.pushButton3.setGeometry(QtCore.QRect(170, 200, 50, 22))
        
        #self.le_C.setText('5000')
        QtCore.QObject.connect(self.pushButton3, QtCore.SIGNAL("pressed()"), self.setParts)
        QtCore.QObject.connect(self.pushButton2, QtCore.SIGNAL("pressed()"), self.update)
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("pressed()"), self.create)
        #QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "600B Steep Slope Conveyor", None))
        
    def setParts(self):
        global shtSptAssy
        global stair
        selection = Gui.Selection.getSelection()
        if selection:
             selected_object = selection[0]
             if selected_object.TypeId == "App::Part":
                 parts_group = selected_object
                 for obj in parts_group.Group:
                     if obj.Label == "shtStpAssy":
                         shtSptAssy = obj
                     

        
        self.le_sita.setText(shtSptAssy.getContents('sita'))  
        self.le_H.setText(shtSptAssy.getContents('H0'))  
        self.le_l1.setText(shtSptAssy.getContents('l1')) 
        self.le_l2.setText(shtSptAssy.getContents('l2')) 
        self.le_h1.setText(shtSptAssy.getContents('h1'))   
        self.le_h2.setText(shtSptAssy.getContents('h2'))  
        self.le_x2.setText(shtSptAssy.getContents('xp2'))  
        H0=self.le_H.text()  
      

    def update(self):
         sita=self.le_sita.text()
         H0=self.le_H.text()
         l1=self.le_l1.text()
         l2=self.le_l2.text()
         h1=self.le_h1.text()
         h2=self.le_h2.text()
         xp2=self.le_x2.text()

         shtSptAssy.set('sita',str(sita))
         shtSptAssy.set('H0',str(H0))
         shtSptAssy.set('l1',str(l1))
         shtSptAssy.set('l2',str(l2))
         shtSptAssy.set('h1',str(h1))
         shtSptAssy.set('h2',str(h2))
         shtSptAssy.set('xp2',str(xp2))

         App.ActiveDocument.recompute()
        
    
    def create(self): 
         fname='steepSlopeCv.FCStd'
         base=os.path.dirname(os.path.abspath(__file__))
         joined_path = os.path.join(base, fname) 

         try:
            Gui.ActiveDocument.mergeProject(joined_path)
         except:
            doc=App.newDocument()
            Gui.ActiveDocument.mergeProject(joined_path)
         Gui.SendMsgToActiveView("ViewFit")   
         
class main():
        d = QtGui.QWidget()
        d.ui = Ui_Dialog()
        d.ui.setupUi(d)
        d.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        d.show() 
        #script_window = Gui.getMainWindow().findChild(QtGui.QDialog, 'd') 
        #script_window.setWindowFlags(script_window.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)            