#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TEST.ui'
#
# Created: Mon Feb  1 11:38:43 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!


from Adafruit_PWM_Servo_Driver import PWM
import time

from PyQt4 import QtCore, QtGui

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

m = 250
M = 550

valmax = 800
valmin = 100

m_pulgar = m
M_pulgar = M

m_indice = m
M_indice = M

m_medio = m
M_medio = M

m_anular = m 
M_anular = M 

m_menique = m
M_menique = M



fist = (m_pulgar,m_indice,m_medio,m_anular,m_menique)
spread = (M_pulgar,M_indice,M_medio,M_anular,M_menique)
point = (m_pulgar,M_indice,m_medio,m_anular,m_menique)

pwm=PWM(0x40)
pwm.setPWMFreq(50)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(340, 220)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)

        self.verticalSlider = QtGui.QSlider(Form)
        self.verticalSlider.setMaximum(180)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))

        self.verticalSlider_2 = QtGui.QSlider(Form)
        self.verticalSlider_2.setMaximum(180)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName(_fromUtf8("verticalSlider_2"))

        self.verticalSlider_3 = QtGui.QSlider(Form)
        self.verticalSlider_3.setMaximum(180)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName(_fromUtf8("verticalSlider_3"))

        self.verticalSlider_4 = QtGui.QSlider(Form)
        self.verticalSlider_4.setMaximum(180)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName(_fromUtf8("verticalSlider_4"))


        self.verticalSlider_5 = QtGui.QSlider(Form)
        self.verticalSlider_5.setMaximum(180)
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName(_fromUtf8("verticalSlider_5"))

        self.verticalLayout.addWidget(self.verticalSlider)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.verticalSlider_3)
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_2.addWidget(self.label_8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_3.addWidget(self.verticalSlider_4)
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_3.addWidget(self.label_9)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.verticalLayout_4.addWidget(self.verticalSlider_2)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_4.addWidget(self.label_7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.verticalLayout_5.addWidget(self.verticalSlider_5)
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_5.addWidget(self.label_10)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        self.spinBox = QtGui.QSpinBox(Form)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.setMaximum(valmax)
        self.spinBox.setMinimum(valmin)
        self.spinBox.setValue(M)

        self.spinBox_2 = QtGui.QSpinBox(Form)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_2.setMaximum(valmax)
        self.spinBox_2.setMinimum(valmin)
        self.spinBox_2.setValue(m)

        self.spinBox_3 = QtGui.QSpinBox(Form)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.spinBox_3.setMaximum(valmax)
        self.spinBox_3.setMinimum(valmin)
        self.spinBox_3.setValue(M)

        self.spinBox_4 = QtGui.QSpinBox(Form)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.spinBox_4.setMaximum(valmax)
        self.spinBox_4.setMinimum(valmin)
        self.spinBox_4.setValue(m)

        self.spinBox_5 = QtGui.QSpinBox(Form)
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.spinBox_5.setMaximum(valmax)
        self.spinBox_5.setMinimum(valmin)
        self.spinBox_5.setValue(M)

        self.spinBox_6 = QtGui.QSpinBox(Form)
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.spinBox_6.setMaximum(valmax)
        self.spinBox_6.setMinimum(valmin)
        self.spinBox_6.setValue(m)

        self.spinBox_7 = QtGui.QSpinBox(Form)
        self.spinBox_7.setObjectName(_fromUtf8("spinBox_7"))
        self.spinBox_7.setMaximum(valmax)
        self.spinBox_7.setMinimum(valmin)
        self.spinBox_7.setValue(M)

        self.spinBox_8 = QtGui.QSpinBox(Form)
        self.spinBox_8.setObjectName(_fromUtf8("spinBox_8"))
        self.spinBox_8.setMaximum(valmax)
        self.spinBox_8.setMinimum(valmin)
        self.spinBox_8.setValue(m)

        self.spinBox_9 = QtGui.QSpinBox(Form)
        self.spinBox_9.setObjectName(_fromUtf8("spinBox_9"))
        self.spinBox_9.setMaximum(valmax)
        self.spinBox_9.setMinimum(valmin)
        self.spinBox_9.setValue(M)

        self.spinBox_10 = QtGui.QSpinBox(Form)
        self.spinBox_10.setObjectName(_fromUtf8("spinBox_10"))
        self.spinBox_10.setMaximum(valmax)
        self.spinBox_10.setMinimum(valmin)
        self.spinBox_10.setValue(m)



        self.horizontalLayout_2.addWidget(self.spinBox)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)        
        self.horizontalLayout_4.addWidget(self.spinBox_3)        
        self.horizontalLayout_4.addWidget(self.spinBox_5)        
        self.horizontalLayout_4.addWidget(self.spinBox_7)        
        self.horizontalLayout_4.addWidget(self.spinBox_9)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))        
        self.horizontalLayout_3.addWidget(self.spinBox_2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addWidget(self.spinBox_4)     
        self.horizontalLayout_5.addWidget(self.spinBox_6)      
        self.horizontalLayout_5.addWidget(self.spinBox_8)       
        self.horizontalLayout_5.addWidget(self.spinBox_10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.verticalSlider_4, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_9.setNum)
        QtCore.QObject.connect(self.verticalSlider_4, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Medio)

        QtCore.QObject.connect(self.verticalSlider_5, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_10.setNum)
        QtCore.QObject.connect(self.verticalSlider_5, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Menique)

        QtCore.QObject.connect(self.verticalSlider_3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_8.setNum)
        QtCore.QObject.connect(self.verticalSlider_3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Indice)

        QtCore.QObject.connect(self.verticalSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_7.setNum)
        QtCore.QObject.connect(self.verticalSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Anular)

        QtCore.QObject.connect(self.verticalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_6.setNum)
        QtCore.QObject.connect(self.verticalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Pulgar)

        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.setM_pulgar)
        QtCore.QObject.connect(self.spinBox_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.setm_pulgar)

        QtCore.QObject.connect(self.spinBox_3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.setM_indice)
        QtCore.QObject.connect(self.spinBox_4, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.setm_indice)

        QtCore.QObject.connect(self.spinBox_5, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.setM_medio)
        QtCore.QObject.connect(self.spinBox_6, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.setm_medio)

        QtCore.QObject.connect(self.spinBox_9, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.setM_menique)
        QtCore.QObject.connect(self.spinBox_10, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.setm_menique)

        QtCore.QObject.connect(self.spinBox_7, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.setM_anular)
        QtCore.QObject.connect(self.spinBox_8, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.setm_anular)

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Spread)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Fist)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Point)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Spread", None))
        self.pushButton_2.setText(_translate("Form", "Fist", None))
        self.pushButton_3.setText(_translate("Form", "Point", None))
        self.label_5.setText(_translate("Form", "Pulgar", None))
        self.label_6.setText(_translate("Form", "0", None))
        self.label.setText(_translate("Form", "Indice", None))
        self.label_8.setText(_translate("Form", "0", None))
        self.label_2.setText(_translate("Form", "Medio", None))
        self.label_9.setText(_translate("Form", "0", None))
        self.label_3.setText(_translate("Form", "Anular", None))
        self.label_7.setText(_translate("Form", "0", None))
        self.label_4.setText(_translate("Form", "Meñique", None))
        self.label_10.setText(_translate("Form", "0", None))

    def setm_pulgar(self):
        global m_pulgar
        m_pulgar = self.spinBox_2.value()
        print "m_pulgar = ",m_pulgar

    def setM_pulgar(self):
        global M_pulgar
        M_pulgar = self.spinBox.value()
        print "M_pulgar = ",M_pulgar

    def setm_indice(self):
        global m_indice
        m_indice = self.spinBox_4.value()
        print "m_indice = ",m_indice

    def setM_indice(self):
        global M_indice
        M_indice = self.spinBox_3.value()
        print "M_indice = ",M_indice

    def setm_medio(self):
        global m_medio
        m_medio = self.spinBox_6.value()
        print "m_medio = ",m_medio

    def setM_medio(self):
        global M_medio
        M_medio = self.spinBox_5.value()
        print "M_medio = ",M_medio

    def setm_anular(self):
        global m_anular
        m_anular = self.spinBox_8.value()
        print "m_anular = ",m_anular

    def setM_anular(self):
        global M_anular
        M_anular = self.spinBox_7.value()
        print "M_anular = ",M_anular

    def setm_menique(self):
        global m_menique
        m_menique = self.spinBox_10.value()
        print "m_menique = ",m_menique

    def setM_menique(self):
        global M_menique
        M_menique = self.spinBox_9.value()
        print "M_menique = ",M_menique


    def Hello(self):
        print "Hello World"

    def Fist(self):
        global fist
        fist = (m_pulgar,m_indice,m_medio,m_anular,m_menique)
        #print fist[0],fist[1],fist[2],fist[3],fist[4]
	pwm.setPWM(0,0,fist[0])
        pwm.setPWM(1,0,fist[1])
        pwm.setPWM(2,0,fist[2])
        pwm.setPWM(3,0,fist[3])
        pwm.setPWM(4,0,fist[4])
        time.sleep(1)

    def Spread(self):
        global spread
        spread = (M_pulgar,M_indice,M_medio,M_anular,M_menique)
        #print spread[0],spread[1],spread[2],spread[3],spread[4]
	pwm.setPWM(0,0,spread[0])
        pwm.setPWM(1,0,spread[1])
        pwm.setPWM(2,0,spread[2])
        pwm.setPWM(3,0,spread[3])
        pwm.setPWM(4,0,spread[4])
        time.sleep(1)

    def Point(self):
        global point
        point = (m_pulgar,M_indice,m_medio,m_anular,m_menique)
        #print point[0],point[1],point[2],point[3],point[4]
	pwm.setPWM(0,0,point[0])
        pwm.setPWM(1,0,point[1])
        pwm.setPWM(2,0,point[2])
        pwm.setPWM(3,0,point[3])
        pwm.setPWM(4,0,point[4])
        time.sleep(1)	

    def Pulgar(self):
        x1 = self.verticalSlider.value()
        pwm_pulgar = (M_pulgar-m_pulgar)*x1/180 + m_pulgar
        #print "pwm_pulgar = ", pwm_pulgar
	pwm.setPWM(0,0,pwm_pulgar)

    def Indice(self):
        x2= self.verticalSlider_3.value()
        pwm_indice = (M_indice-m_indice)*x2/180 + m_indice
        #print "pwm_indice = ", pwm_indice
	pwm.setPWM(1,0,pwm_indice)

    def Medio(self):
        x3= self.verticalSlider_4.value()
        pwm_medio = (M_medio-m_medio)*x3/180 + m_medio
        #print "pwm_medio = ", pwm_medio
	pwm.setPWM(2,0,pwm_medio)


    def Anular(self):
        x4= self.verticalSlider_2.value()
        pwm_anular = (M_anular-m_anular)*x4/180 + m_anular
        #print "pwm_anular = ", pwm_anular
	pwm.setPWM(3,0,pwm_anular)


    def Menique(self):
        x5= self.verticalSlider_5.value()
        pwm_menique = (M_menique-m_menique)*x5/180 + m_menique
        #print "pwm_menique = ", pwm_menique
	pwm.setPWM(4,0,pwm_menique)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

