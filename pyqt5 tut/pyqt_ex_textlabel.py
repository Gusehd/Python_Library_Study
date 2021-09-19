from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import os

#PyQt5의 기본 형태이다. 대부분 이 상태에서 살을 붙여 완성한다.

ui_file = "./myui.ui"
class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(ui_file,self)

        #문자버튼을 눌렀을 때 텍스트 라벨에 글자가 나오도록 하는 기능
        #버튼의 오브젝트 이름을 확인해야 한다. 디자이너로 가서 오브젝트 네임을 왼쪽 에서 확인한다.

        self.pushButton.clicked.connect(self.buttonClicked)
        #이후 버튼클릭 함수를 만들어서 연결한다.

    def buttonClicked(self):
        result = self.lineEdit.text()
        #글자를 입력하는 오브젝트 이름이 라인에디트라 이렇게 했다. 이런식으로
        #오브젝트 이름을 보면서 해야한다.
        self.label.setText(result)
        #위처럼 하면 라벨 오브젝트에 result를 텍스트로 띄우게 된다.

QApplication.setStyle("fusion")
#창의 테마를 결정한다. 이것 때문에 나중에 문제가 생기는 경우도 있어 추가했다.
#퓨전의 경우에는 맥과 윈도우를 섞은 스타일이다. 다양한 스타일이 존재한다.
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())