from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import os

#PyQt5의 기본 형태이다. 대부분 이 상태에서 살을 붙여 완성한다.

ui_file = "./mycal.ui"
class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(ui_file,self)

        self.equalbutton.clicked.connect(self.calculate)
        #버튼클릭 함수를 만들어서 연결한다.

    def calculate(self):
        equation = self.inputbox.text()
        #계산기를 만들어서 계산식을 받아도 그냥 문자열로 인식한다.
        #그래서 파이썬에서 제공하는 eval() 함수를 사용한다.
        #문자열 형태의 수식을 eval()안에 넣기만 하면 그냥 계산을 해주는 함수이다.
        result = eval(equation)
        history_text = "{}\n= {}\n".format(equation, result)
        #히스토리 텍스트를 통해 보기좋게 바꾼 형태이다. 그냥 result를 넣어도 상관없다.
        self.history.append(history_text)

        #self.history.append(history_text) 에서 setText를 사용하면 전에것은 지워지고
        #새로운 것만 나오게 된다.

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())