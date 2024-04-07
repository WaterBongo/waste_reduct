from flask import Flask
from flask import request
app = Flask(__name__)
amazing_db = {}
@app.route('/gatodb',methods=['POST','GET'])
def hello():
    if request.method == 'GET':
        data = request.json
        print(data)
        name = data['name']
        if name not in amazing_db:
            amazing_db[name] = data
        print(amazing_db)
        return 'Hello, World!'
    else:
        return 'Hello, World!'
if __name__ == '__main__':
    app.run('0.0.0.0',port=8052)