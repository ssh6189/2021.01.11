#Robot Parameter입력하는 GUI
import sys
import numpy
import math
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication

import Robot_Matrix as RoM

global X
global Y
global Z
global RX
global RY
global RZ
    
def Robot_Parameter():
    #UI파일 연결
    #단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
    form_class = uic.loadUiType("Robot_Parameter.ui")[0]

    #화면을 띄우는데 사용되는 Class 선언
    class WindowClass(QMainWindow, form_class) :
        def __init__(self) :
            global X
            global Y
            global Z
            global RX
            global RY
            global RZ

            super().__init__()
            self.setupUi(self)

            self.Finish.clicked.connect(self.send)

            self.Finish.clicked.connect(QCoreApplication.instance().quit)

        def send(self, text):
            global X
            global Y
            global Z
            global RX
            global RY
            global RZ

            X = float(self.lineEdit.text())
            Y = float(self.lineEdit_2.text())
            Z = float(self.lineEdit_3.text())
            RX = float(self.lineEdit_4.text())
            RY = float(self.lineEdit_5.text())
            RZ = float(self.lineEdit_6.text())

            if self.Degree.isChecked():
                RX = RX
                RY = RY
                RZ = RZ

            else:
                RX = math.degrees(RX)
                RY = math.degrees(RY)
                RZ = math.degrees(RZ)
        
    #if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    
    return RoM.robot_Mat(X, Y, Z, RX, RY, RZ)

if __name__ == "__main__" :
    Robot_Parameter()