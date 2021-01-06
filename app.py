from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbmyproject  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


db.diary_breast.insert_one({'time1': '7:00', 'time2': '7:40', 'location' : '왼쪽', 'memo' : '트름을 10분만에 함'})
db.diary_breast.insert_one({'time1': '9:00', 'time2': '9:40', 'location' : '오른쪽', 'memo' : '귀저기 갈음(소변)'})
db.diary_breast.insert_one({'time1': '11:00', 'time2': '11:20', 'location' : '오른쪽', 'memo' : '먹다 잠듬'})
db.diary_breast.insert_one({'time1': '15:00', 'time2': '15:45', 'location' : '왼쪽', 'memo' : '오래자서 그런지 오랫동안 먹네'})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)