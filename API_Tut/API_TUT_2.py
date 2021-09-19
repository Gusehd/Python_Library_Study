#API TUT 2
#PAPAGO API 활용하기

import json
import os
import sys
import urllib.request

api_id = ""
api_pw = ""

#파파고를 통해 번역기 api를 활용해본다.
#네이버에서 제공해준 예시 코드를 통해서 살펴본다.
#예시코드를 실행해보고 어떤 방식으로 돌아가는지 확인해보는 것도 api를 잘 사용할 수 있는 방법중 하나이다.

client_id = api_id # 개발자센터에서 발급받은 Client ID 값
client_secret = api_pw # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote("반갑습니다") # 번역할 문장이 들어가는 부분 만약 입력을 받아서 번역하고 싶다면
#input을 문자열로 받아서 실행하면 된다.

data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result = response_body.decode('utf-8')
    result_dic = json.loads(result) # json 형태니까 다시 딕셔너리 형태로 바꾸어줌
    print(result_dic["message"]["result"]["translatedText"]) # 딕셔너리 형태 안에서 번역문을 찾아 print 함
else:
    print("Error Code:" + rescode)

#파파고는 무료로 사용하는 하루 허용량이 10000글자 이다. 이런식으로 무료 api는 제한이 있는 경우가 있다.
#확인하고 사용해야 한다.
#무료라고 해도 다양한 기능과 좋은 기능이 많이 있는 API들이 많으니 찾아서 적재적소에 사용하면 된다.
#네이버 클라우드 플랫폼 역시 API 서비스가 모여있는 플랫폼 중 하나이다.

#Window 작업 스케줄러를 통한 프로그램 자동실행
#만들어 놓은 다양한 프로그램들을 window 작업 스케쥴러를 통해서 자동 실행할 수 있다.
#프로그램/스크립트 창에는 파이썬 인터프리터의 경로를 넣는다. 파이썬 프로젝트의 venv를 찾아서 연다.
#이후 스크립트라는 폴더에서 python.exe를 찾아서 선택한다. 우클릭 copy path를 통해서 path를 복사한다.
#absolute path를 가져와서 복사 붙여넣기 해준다. 인수옵션에는 내가 코딩한 파이썬 파일의 경로를 입력한다.
#시작위치에는 프로젝트 폴더의 위치 경로를 넣는다. 즉 파이썬 파일이 있는 위치를 넣어주면 된다.
#이후 트리거 편집에서 좀더 디테일한 설정을 할 수 있다.
