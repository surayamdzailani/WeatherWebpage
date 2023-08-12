from flask import Flask, render_template,request
from weather import main as get_weather
from weather import get_weather_condition

#setup flask resource
app = Flask(__name__)

#this is only single page application so all the action will only been run and display in single route

@app.route('/', methods=['GET','POST'])
def index():
	data = None
	if request.method == 'POST':
		city = request.form['cityName']
		state = request.form['stateName']
		country = request.form['countryName']
		data = get_weather(city,state,country)
	return render_template('index.html', data = data) #return render template in order to dipaly our html page so make sure to store the html inside templates folder




if __name__ == '__main__':
	app.run(debug=True)
