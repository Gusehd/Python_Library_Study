#API = 어플리케이션 프로그래밍 인터페이스
#API -> 개발자가 프로그램을 만들기 쉽게 도와준다는 개념
#API 1 => OPENWHEATHERMAP / 날씨 api

#모든 api들은 api 사용법 공식 문서가 있다. 잘 확인하고 어떤 것을 얻고 싶으면 어떻게 해라 를 확인하고 사용하면 된다.

import requests
import json

api_key = ""
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format("Seoul",api_key)

#url 주소는 항상 http:// 나 https://로 시작해야 한다.

data = requests.get(url)
data_dic = json.loads(data.text)
# json 데이터를 딕셔너리 자료형으로 변환해줌

print("현재날씨 : ", data_dic["weather"])

#딕셔너리 안의 리스트 안의 딕셔너리 이런식으로 구성이 되어있는 것을 볼 수 있다. 내가 원하는 정보를 해당하는 인덱스나
#키를 통해 뽑아내어 사용하면 된다.

#데이터 방식을 크게 2가지로 볼 수 있음 / csv 와 json 이다.
#csv -> 콤마로 값을 나타낸다 / json -> Javascript 객체 문법으로 구조화된 데이터를 표현하기 위한 문자 기반의 표준 포맷
#api 사이트들은 대부분 csv 혹은 json 으로 데이터를 포장해서 보내준다.

#공공데이터 포탈에서 다양한 api를 검색해서 사용할 수 있다.
#api 스토어도 있어 api 스토어를 이용해서 다양한 서비스를 만들 수 있다.

#json,dumps(loads된 딕셔너리 자료형 , indent="\t) 같이 파이썬 에서 제공하는 다양한 json 관련
#함수들을 통해서 불러온 데이터를 좀더 보기 좋게 할 수 있다.
#또 다양한 데이터 시각화 라이브러리를 통해서 불러온 데이터들을 시각화 할 수 있다. ex) 지도데이터 시각화 - folium