from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.minyoung


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=["POST"])
def search():
    q = request.form["q"]
    url = f"https://www.youtube.com/results?search_query={q}"



@app.route('/mydietpage')
def mydietpage():
    return render_template('mydietpage.html')

# @app.route('api/list', methods=['GET'])
# def show_workout():

# @app.route('api/list', metohods=['POST'])
# def