# 웹서버 프로그램 웹 브라우저에서 http://localhost:5000/로 접속하면 
# index.html을 실행하고 버튼을 이용하여 LED 작동시킴

from flask import Flask, request
from flask import render_template
import random

app = Flask(__name__)
def p(num):
    print("수 = "+ num)
def s(result):
    print("합계 = "+ result) 

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/random")                       # index.html에서 이 주소를 접속하여 해당 함수를 실행
def rand():
    try:
        while(1):
            global num ,result
            num = random.randrange(1, 5000)
            result =+ num
        print("수 = "+ num)
        print("합계 = "+ result) 
        return "0k"                           # 함수가 'ok'문자열을 반환함
    except :
        return "fail"

if __name__ == "__main__":
    app.run(host="0.0.0.0")