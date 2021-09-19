from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import urllib.request as req
from bs4 import BeautifulSoup
from PyQt5.QtGui import *

#PyQt5의 기본 형태이다. 대부분 이 상태에서 살을 붙여 완성한다.

ui_file = "./movie.ui"
#ui에서 라벨에는 텍스트와 이미지 모두 띄울수 있다. 그래서 이미지의 크기를 확실히 알아야 한다.
#그래야 라벨의 크기를 알맞게 설정해놓을 수 있다.
#이미지 크기를 확인하는 방법은 웹 사이트에서 검사 소스에서 확인하면 해당 픽셀 크기를 알려준다.


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(ui_file,self)

        self.button.clicked.connect(self.crawling)
        #버튼클릭 함수를 만들어서 연결한다. 버튼을 누르면 크롤링 함수가 동작하도록 한다.

    def crawling(self):
        code = req.urlopen("http://www.cgv.co.kr/movies/")
        soup = BeautifulSoup(code , "html.parser")
        title = soup.select("div.sect-movie-chart strong.title")
        poster_image = soup.select("span.thumb-image > img")

        for i in range(len(title)):
            img_url = poster_image[i].attrs["src"]
            data = req.urlopen(img_url).read()

            # 이미지를 띄우기 위해서는 QPixmap이라는 객체를 사용해야 한다.

            pixmap = QPixmap()
            pixmap.loadFromData(data)

            # self.img1.setPixmap(pixmap) 이런식으로 하면 이미지1 라벨에 이미지가 들어갈 것이다.
            # 이 역시 getattr을 이용해서 표현해주자
            # 해보니 이미지가 확대되어 나타낸다. 즉 원 크기와 확대 비율 역시 정해주어야 한다.
            # 픽셀 단위를 맞추어주기 위해서 pixmap.scaled를 사용한다.

            pixmap = pixmap.scaled(185, 260)

            getattr(self, "img{}".format(i + 1)).setPixmap(pixmap)
            getattr(self, "text{}".format(i+1)).setText(title[i].string)

        #1, 2, 3 .. 은 text1,2,3.. 으로 포맷팅이 안된다. 해당되는 리스트를 만들어서 활용해도 된다.
        #아니면 다른 제공되는 함수를 사용해도 된다. 바로 getattr(self, ) 인데 변수이름에도
        #문자열 포맷팅을 사용할 수 있도록 해주는 함수이다. 인자 첫번째 즉 self 자리에는 앞쪽에
        #나오는 변하지 않는 객체의 이름이나 속성을 나타낸다.



QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())