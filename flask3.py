from flask import Flask
import requests
from flask import request
app = Flask(__name__)
amazing_db = {}
@app.route("/")
def helll():
    return "hello, world!"
@app.route('/gatodb',methods=['POST'])
def hello():
    if request.method == 'POST':
        data = request.json
        print(data)
        name = data['name']
        if name not in amazing_db:
            amazing_db[name] = data
        print(amazing_db)
        return 'Hello, World!'

@app.route('/get/<name>')
def get(name):
    return amazing_db[name]
if __name__ == '__main__':
    app.run('0.0.0.0',port=8052)

