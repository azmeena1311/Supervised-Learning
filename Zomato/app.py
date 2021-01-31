import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle


app = Flask(__name__)

filename = 'zomato_linear.pkl'
model = pickle.load(open(filename, 'rb'))



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():

	if request.method == 'POST':

		online_order = int(request.form['online_order'])
		book_table = int(request.form['book_table'])
		votes = int(request.form['votes'])
		location = int(request.form['location'])
		rest_type = int(request.form['rest_type'])
		cuisines = int(request.form['cuisines'])
		cost = int(request.form['cost'])
		menu_item = int(request.form['menu_item'])


		data = np.array([[online_order,book_table,votes,location,rest_type,cuisines,cost,menu_item]])
		data = scalar.transform(data)
		output = model.predict(data)[0].round(2)


		return render_template('index.html',prediction = my_prediction)

	if __name__ == '__main__':
		app.run(debug=True)
