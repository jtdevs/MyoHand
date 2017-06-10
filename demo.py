#! /usr/bin/env python
import sys
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
rock = (M_pulgar,M_indice, m_medio, m_anular, M_menique)
obscene = (m_pulgar, m_indice, M_medio, m_anular, m_menique)

pwm=PWM(0x40)
pwm.setPWMFreq(50)

class PrintPoseListener(DeviceListener):
    def on_pose(self, pose):
        pose_type = PoseType(pose)
        print pose_type.name
    
        if(pose_type.name=="FIST"):
            self.Fist()
        
        if(pose_type.name=="REST"):
            self.Spread()
        
        if(pose_type.name=="WAVE_OUT"):
            self.Point()

        if(pose_type.name=="WAVE_IN"):
            self.Rock()

        if(pose_type.name=="DOUBLE_TAP"):
            self.Obscene()

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

    def Rock(self):
        global rock
        rock = (M_pulgar,M_indice, m_medio, m_anular, M_menique)
        pwm.setPWM(0,0,rock[0])
        pwm.setPWM(1,0,rock[1])
        pwm.setPWM(2,0,rock[2])
        pwm.setPWM(3,0,rock[3])
        pwm.setPWM(4,0,rock[4])
        time.sleep(0.5)

    def Obscene(self):
        global obscene
        obscene = (m_pulgar, m_indice, M_medio, m_anular, m_menique)
        pwm.setPWM(0,0,obscene[0])
        pwm.setPWM(1,0,obscene[1])
        pwm.setPWM(2,0,obscene[2])
        pwm.setPWM(3,0,obscene[3])
        pwm.setPWM(4,0,obscene[4])
        time.sleep(0.5)

    def Out(self):
        Myo().safely_disconnect()
    sys.exit()

print('Start Myo demo for Linux')
listener = PrintPoseListener()
myo = Myo()
myo.connect()
myo.add_listener(listener)
myo.vibrate(VibrationType.SHORT)
while True:
    myo.run()
