from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib
import warnings
import os
from enhancement import map_hours,gender, map_device, map_impact, addiction_map, place
warnings.filterwarnings("ignore")

app = Flask(__name__, static_folder='Images', static_url_path='/images')

model = joblib.load("final_model.pkl")

@app.route('/')
def index():
    return render_template('analysis.html')

@app.route('/images/<path:filename>')
def serve_images(filename):
    return app.send_static_file(f'../Images/{filename}')


@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        
        age_input = request.form['Age']
        gender_input = request.form['Gender']
        screen_time = request.form['screen_time']
        device_input = request.form['device']
        impact_input = request.form['impact']
        addiction_level = request.form['addiction_level']
        place_input = request.form['place']
        
        # Preprocess the input data
        age_input = int(age_input)
        gender_input = gender(gender_input)
        screen_time = map_hours(float(screen_time))
        device_input = map_device(device_input)
        impact_input = map_impact(impact_input)
        addiction_level_input = addiction_map(addiction_level)
        place_input = place(place_input)
        data = {
            'Age': age_input,
            'Gender': gender_input,
            'screen_time': screen_time,
            'device': device_input,
            'impact': impact_input,
            'place': place_input,
            'addiction_level': addiction_level_input
        }
        
        df = pd.DataFrame([data])
        
        prediction = model.predict(df)
        print(prediction)
        return render_template('index.html', data=prediction[0])

    return render_template('index.html', data=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)