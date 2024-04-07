from flask import Flask
from flask import request
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.timeseries import TimeSeries
import datetime,requests
from transformers import pipeline

app = Flask(__name__)
info_used = {
}

pipe = pipeline("text-classification", model="mr8488/distilroberta-finetuned-financial-news-sentiment-analysis-v2")


# Financial data for the company
# Calculation functions
def calculate_gross_profit_margin(data):
    return (int(data["grossProfit"]) / int(data["totalRevenue"])) * 100

def calculate_operating_margin(data):
    return (int(data["operatingIncome"]) / int(data["totalRevenue"])) * 100

def calculate_net_profit_margin(data):
    return (int(data["netIncome"]) / int(data["totalRevenue"])) * 100


def calculate_ebitda_margin(data):
    return (int(data["ebitda"] )/int( data["totalRevenue"])) * 100



# Perform calculations

# Simple interpretive logic

@app.route("/stock/<stock>")
def stock(stock):

    ts = TimeSeries(key='8S8UVXUIR5WZP5P9', output_format='pandas')

    # Get daily historical data
    daily_data, meta_data = ts.get_daily(symbol=stock, outputsize='full')

    # Calculate the date of one month ago and one week ago
    one_month_ago = (datetime.datetime.now() - datetime.timedelta(days=30)).date()
    one_week_ago =  (datetime.datetime.now() - datetime.timedelta(days=7)).date()

    # Extract the closing prices for the most recent data on or before one month and one week ago
    price_one_month_ago = daily_data[daily_data.index.date <= one_month_ago]['4. close'][0]
    price_one_week_ago = daily_data[daily_data.index.date <= one_week_ago]['4. close'][0]
    #show the price of today
    price_today = daily_data['4. close'][0]
    print('Price today: ', daily_data['4. close'][0])
    print('Price one month ago: ', price_one_month_ago)
    print('Price one week ago: ', price_one_week_ago)
    

    return{
        "today": daily_data['4. close'][0],
        "one_month_ago": price_one_month_ago,
        "one_week_ago": price_one_week_ago
    }

@app.route("/news/<company>")
def news(company):
    data = requests.get(f'https://newsapi.org/v2/everything?q={company}&from=2024-03-07&sortBy=publishedAt&apiKey=6900242d44ec47839ca83eb1a31f32dd&language=en')
    
    descriptions = []
    for i in data['articles']:
        if not (i["description"] == "[Removed]" or i["description"] == None):
            descriptions.append(i["description"])
    
    results = pipe(descriptions)
    sum = 0
    cnt = 0
    for res in results:
        if res["label"] == "positive":
            sum += res["score"]
            cnt+=1
        elif res["label"] == "negative":
            sum -= res["score"]
            cnt+=1

    sum/=cnt
    
    label = "positive" if sum >= 0.0 else "negative"    
    confidence = abs(sum)

    return {
        "label": label,
        "confidence": confidence
    }

@app.route("/financial_status/<stock>")
def financial_status(stock):
    url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={stock}&apikey=EDSFR9WCYS1QI8P6'
    r = requests.get(url)
    data = r.json()
    print(data)
    financial_data = data['annualReports'][0]
    gross_profit_margin = calculate_gross_profit_margin(financial_data)
    operating_margin = calculate_operating_margin(financial_data)
    net_profit_margin = calculate_net_profit_margin(financial_data)
    ebitda_margin = calculate_ebitda_margin(financial_data)
    grim = None

    if gross_profit_margin > 20 and net_profit_margin > 10:
        print( "The company is likely in good financial health.")
        grim = False
    else:
            print("The company is likely in poor financial health.")
            grim = True
    return {
        "gross_profit_margin": gross_profit_margin,
        "operating_margin": operating_margin,
        "net_profit_margin": net_profit_margin,
        "ebitda_margin": ebitda_margin,
        "grim":grim
    }

@app.route("/product_stabilitiy/<company>/<app>/<nasaq>")
def stability(company,app,nasaq):
    he = '{\n  "model": "mistral",\n  "prompt":"'

    company_overview = requests.get(f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={nasaq}&apikey=9AQBP48DOAXMBGC1").json()['Description']
    prompt = f'I currently work at {company}, the product i work on is {app}, do i have a stable position? a brief description of {company} {company_overview} response in a json where one key is stability and the value is either true or false and another key called explnation and explain why or why not there is no job security'

    he = he+prompt
    he+='"\n,"stream":false }'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
    response = requests.post('http://100.111.60.93:11434/api/generate', headers=headers, data=he)
    print(response.json())
    return response.json()


if __name__ == '__main__':
    app.run('0.0.0.0',port=8080)


#https://newsapi.org/v2/everything?q=tesla&from=2024-03-07&sortBy=publishedAt&apiKey=API_KEY
#https://newsapi.org/v2/everything?q=apple&from=2024-03-07&sortBy=publishedAt&apiKey=6900242d44ec47839ca83eb1a31f32dd
#https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=6900242d44ec47839ca83eb1a31f32dd

#https://newsapi.org/v2/everything?q=apple&from=2024-03-07&sortBy=publishedAt&apiKey=6900242d44ec47839ca83eb1a31f32dd&language=en
