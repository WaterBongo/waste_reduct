from flask import Flask
import requests
from flask import request
app = Flask(__name__)
amazing_db = {'jamal': {'name': 'jamal', 'description': 'manager', 'company': 'apple', 'NASAQ': 'AAPL', 'location': 'cs', 'performance': 'wr', 'stock': {'one_month_ago': 170.73, 'one_week_ago': 171.48, 'today': 169.58}, 'financial_status': {'ebitda_margin': 33.16708492376473, 'grim': False, 'gross_profit_margin': 44.5886669900251, 'net_profit_margin': 25.568601193614377, 'operating_margin': 30.130591113266835}, 'stability': {'stability': 'true', 'explanation': "Apple is a company with strong business performance and financial stability which generally contributes to the job security of its employees. As for your position as a manager, it would widely depend on your performance and the specific department or project you are managing. However, given Apple's position in the industry and the importance of a managerial role, it can be considered that there is a level of job security."}}}
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

