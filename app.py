from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbvideo  # 'dbvideo'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## HTML을 주는 부분
@app.route('/write')
def write():
    return render_template('write.html')


## API 역할을 하는 부분
@app.route('/video', methods=['POST'])
def write_review():
    title_receive = request.form['title_give']
    description_receive = request.form['description_give']
    vm_receive = request.form['vm_give']

    video_data = {
        'title': title_receive,
        'description': description_receive,
        'vm': vm_receive
    }
    db.videos.insert_one(video_data)
    return jsonify({'result': 'success', 'msg': '성공적으로 등록되었습니다.'})


@app.route('/video_get', methods=['GET'])
def read_reviews():
    videos = list(db.videos.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'videos': videos})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)