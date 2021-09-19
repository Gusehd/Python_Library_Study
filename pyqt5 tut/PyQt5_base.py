from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

#PyQt5의 기본 형태이다. 대부분 이 상태에서 살을 붙여 완성한다.

ui_file = "./myui.ui"
class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(ui_file,self)

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())