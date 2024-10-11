from flask import Flask, render_template, request
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler, FunctionTransformer
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
import sys
import os
sys.path.append(os.path.abspath('../Model'))
from LinearRegressionModel import MyModel
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

cars = pd.read_csv('data\Cleaned_Car_data.csv')
model = pickle.load(open('data\LinearRegressionModel.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    companies = sorted(cars['car_name'].apply(lambda x: x.split(" ")[0]).unique())
    car_models = sorted(cars['car_name'].unique())
    year = sorted(cars['manufacture'].unique(), reverse=True)
    fuel_type = cars['fuel_type'].unique()
    seats = sorted(cars['Seats'].unique())
    transmission = cars['transmission'].unique()
    ownership = sorted(cars['ownership'].unique())

    return render_template('index.html', companies=companies, car_models=car_models, years=year, fuel_types=fuel_type,
                           seats=seats, transmission=transmission, ownership=ownership)

@app.route('/predict', methods=['POST'])
def predict():
    car_name = request.form.get('car_model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    transmission = request.form.get('transmission')
    seats = int(request.form.get('seats'))
    ownership = int(request.form.get('ownership'))
    engine = cars[cars['car_name'] == str(car_name)]['engine'].iloc[0]
    kms_driven = float(request.form.get('kms_driven'))
    print(car_name, kms_driven, fuel_type, transmission, ownership, year, engine, seats)

    transmission_list = cars[cars['car_name'] == str(car_name)]['transmission'].unique()
    if len(transmission_list) == 1:
        transmission=(transmission_list[0])

    prediction = model.predict(pd.DataFrame(
        columns=['car_name', 'kms_driven', 'fuel_type', 'transmission', 'ownership', 'manufacture', 'engine', 'Seats'],
        data=np.array([car_name, kms_driven, fuel_type, transmission, ownership, year, engine, seats]).reshape(1, 8)))
    return str(int(prediction[0]))

if __name__ == '__main__':
    app.run()