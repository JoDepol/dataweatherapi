from flask import Flask, render_template,request
import requests
import time
import os

app = Flask(__name__)

picfolder = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = picfolder

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def api_route():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'bh.jpg')
    if request.method == 'POST':
        city = request.form['city']
        r = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=359dd3fd6b6be34a7511ca2e4dd42f28")
        data = r.json()
        temp = round(data['main']['temp'] - 273.15)
        temp_min = round(data['main']['temp_min']- 273.15)
        temp_max = round(data['main']['temp_max']- 273.15)
        country = (data['sys']['country'])
        pressure = (data['main']['pressure'])
        humidity = (data['main']['humidity'])
        wind = (data['wind']['speed'])
        sunrise = time.strftime('%I:%M:%p', time.gmtime(data['sys']['sunrise']-21600))
        sunset = time.strftime('%I:%M:%p', time.gmtime(data['sys']['sunset']-21600))
        long = (data['coord']['lon'])
        lat = (data['coord']['lat'])
        return render_template("results.html", temp_min=temp_min, temp_max=temp_max, country=country, city=city, temp=temp, humidity=humidity, wind=wind, pressure=pressure, sunset=sunset, sunrise=sunrise, long=long, lat=lat)

    return render_template('indes.html', user_image=pic1)

if __name__ == '__main__':
    app.run(debug=True, port=8080,)
