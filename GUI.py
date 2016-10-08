#! /usr/bin/env python
import sys
import signal
from PyQt4 import QtCore, QtGui
from Adafruit_PWM_Servo_Driver import PWM
import time

from myo import Myo
from vibration_type import VibrationType
from device_listener import DeviceListener
from pose_type import PoseType


m = 250
M = 550

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

def signal_handler(signal, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

class PrintPoseListener(DeviceListener):
    def on_pose(self, pose):
        pose_type = PoseType(pose)
        print pose_type.name
	if(pose_type.name=="FIST"):
		self.Fist()
	if(pose_type.name=="REST"):
		self.Spread()
	
        if(pose_type.name=="WAVE_IN"):
                self.Point()

        if(pose_type.name=="WAVE_OUT"):
                self.Point()

	if(pose_type.name=="DOUBLE_TAP"):
		self.Out()

    def Fist(self):
        global fist
        fist = (m_pulgar,m_indice,m_medio,m_anular,m_menique)
        #print fist[0],fist[1],fist[2],fist[3],fist[4]
        pwm.setPWM(0,0,fist[0])
        pwm.setPWM(1,0,fist[1])
        pwm.setPWM(2,0,fist[2])
        pwm.setPWM(3,0,fist[3])
        pwm.setPWM(4,0,fist[4])
        time.sleep(0.5)

    def Spread(self):
        global spread
        spread = (M_pulgar,M_indice,M_medio,M_anular,M_menique)
        #print spread[0],spread[1],spread[2],spread[3],spread[4]
        pwm.setPWM(0,0,spread[0])
        pwm.setPWM(1,0,spread[1])
        pwm.setPWM(2,0,spread[2])
        pwm.setPWM(3,0,spread[3])
        pwm.setPWM(4,0,spread[4])
        time.sleep(0.5)

    def Point(self):
        global point
        point = (m_pulgar,M_indice,m_medio,m_anular,m_menique)
        #print point[0],point[1],point[2],point[3],point[4]
        pwm.setPWM(0,0,point[0])
        pwm.setPWM(1,0,point[1])
        pwm.setPWM(2,0,point[2])
        pwm.setPWM(3,0,point[3])
        pwm.setPWM(4,0,point[4])
        time.sleep(0.5)

    def Out(self):
        Myo().safely_disconnect()
	sys.exit() 




class Ui_Myo_Window(QtGui.QWidget):

    def setupMyo_Window(self, Myo_Window):

        Myo_Window.setWindowTitle("Myo")
        Myo_Window.resize(320, 220)

        self.gridLayout = QtGui.QGridLayout(Myo_Window)

        btn = QtGui.QPushButton("Connect", self)
        btn.clicked.connect(self.start_myo)
        
        
           
        
        self.gridLayout.addWidget(btn, 1, 0, 1, 1)
        

    def Activate_Hand(self,state):
        if state == QtCore.Qt.Checked:
            Act = 1
            
            print "checked" , Act
        else:
            
            Act = 0
            print "unchecked", Act

        

    def start_myo(self):

        print('Start Myo for Linux')
        listener = PrintPoseListener()
        myo = Myo()

        try:
            myo.connect()
            myo.add_listener(listener)
            myo.vibrate(VibrationType.SHORT)
            while True:
                myo.run()


        except KeyboardInterrupt:
            pass
        except ValueError as ex:
            print(ex)
        finally:
            myo.safely_disconnect()
            print('Finished.')




if __name__ == '__main__':          

    app = QtGui.QApplication(sys.argv)
    Myo_Window = QtGui.QWidget()
    window = Ui_Myo_Window()
    window.setupMyo_Window(Myo_Window)
    Myo_Window.show()
    sys.exit(app.exec_())


