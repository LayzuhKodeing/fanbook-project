from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://Hano_LX:TG0707@cluster0.shs7hsb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.fanmsg.insert_one(doc)
    return jsonify({'msg':'POST request!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    msg_list = list(db.fanmsg.find({},{'_id': False}))
    return jsonify({'messages': msg_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)