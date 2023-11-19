from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = 'b17be144b37ef728ebdc8e6d15564fea'

def weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key  
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        Temperature = data['main']['temp']
        Weather = data['weather'][0]['description']
        humidity = data['main']['humidity']
        return {
            'Temperature': Temperature,
            'Weather': Weather,
            'humidity': humidity
        }

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/city', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        result = weather(api_key, city)
    else:
        result = None
        city = None
    return render_template('compose.html', result=result, city=city)


if __name__=="__main__":
    app.run(debug=True)

