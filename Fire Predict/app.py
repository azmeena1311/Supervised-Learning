import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle


app = Flask(__name__)

filename = 'forest-fire-prediction.pkl'
model = pickle.load(open(filename, 'rb'))




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():

	if request.method == 'POST':

		oxygen = int(request.form['oxygen'])
		temperature = int(request.form['temperature'])
		humidity = int(request.form['humidity'])


		data = np.array([[oxygen,temperature,humidity]])
		output = model.predict_proba(data)[0][0].round(2)

		if output > 80:
			return render_template('index.html', prediction_text='You are at high risk')
		elif output>40 or output<70:
			return render_template('index.html', prediction_text='You are at Moderate risk')
		else:
			return render_template('index.html', prediction_text='You are at Low risk')

			


if __name__ == "__main__":
    app.run(debug=True)