from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbmyproject  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/diary', methods=['POST'])
def write_diary():
    # title_receive로 클라이언트가 준 title 가져오기
    currentDate_receive = request.form['currentDate_give']
    # author_receive로 클라이언트가 준 author 가져오기
    startTime_receive = request.form['startTime_give']
    # review_receive로 클라이언트가 준 review 가져오기
    endTime_receive = request.form['endTime_give']
    way_receive = request.form['way_give']
    comment_receive = request.form['comment_give']

    # DB에 삽입할 review 만들기
    diary = {
        'currentDate': currentDate_receive,
        'startTime': startTime_receive,
        'endTime': endTime_receive,
        'way': way_receive,
        'comment': comment_receive
    }
    # reviews에 review 저장하기
    db.diaries.insert_one(diary)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'msg': '성공적으로 작성되었습니다.'})


@app.route('/diary', methods=['GET'])
def read_diary():
    # 1. DB에서 리뷰 정보 모두 가져오기
    diaries = list(db.diaries.find({}, {'_id': 0}))
    # 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'diaries': diaries})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

