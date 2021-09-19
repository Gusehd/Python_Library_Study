#엑셀 데이터로 엑셀에 차트 그리기
import openpyxl
from openpyxl.chart import  Reference, Series, LineChart

cp = ["LG전자","삼성전자","현대자동차"]

for i in cp:
    book = openpyxl.load_workbook("./file/2017년_광고비_{}.xlsx".format(i))
    sheet = book.active

    #차트 만들기
    chart = LineChart()
    #chart = BarChart() / 이런식으로 바 차트로 바꾸어도 되고 , 파이 차트도 위쪽에 import 만 해주면 다 사용 가능하다.

    chart.title = "{} 월별 광고비".format(i)
    value = Reference(sheet, range_string="Sheet1!C2:C13")
    #range_string 에는 어디부터 어디까지 이용할지 범위를 적는다.
    #특이한 점은 엑셀의 sheet 이름을 앞에 적어주어야 한다는 점이다.
    #실제로 엑셀가서 특정 sheet의 셀을 보면 위처럼 !가 섞여서 표현되고 있다.

    vs = Series(value, title=sheet["C1"].value)
    chart.append(vs)
    #시리즈 함수에 넣어야 차트에 사용할 수 있는 상태로 변한다.
    #타이틀에는 각 셀들의 이름들을 사용하게 된다.

    sheet.add_chart(chart, "J1")
    #엑셀 파일에서 어디쯤에 차트를 그릴건지 정하는 함수이다.
    #시작 위치를 정해주면 된다.

    book.save("./file/2017년_광고비_2번파일예시{}.xlsx".format(i))
