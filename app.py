import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

columns=['const', 'PLAN_COST', 'TOTAL_PLAN_QTY', 'TOTAL_PLAN_AMOUNT',
       'VOICE_CNT', 'VOICE_MINUTES_LOCAL', 'SMS_CNT', 'TOTALOCTETSUNIT1',
       'UNITS_MONEY']
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    #int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    payload = request.files['fileupload']
    #obs = pd.DataFrame([payload], columns=columns).astype(dtypes)
    #proba = pipeline.predict_proba(obs)[0, 1]
    #prediction = model.predict(obs)

    #output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Count of customer churns should be $ {}'.format(payload.isnull().sum().values.sum()))


if __name__ == "__main__":
    app.run(debug=True)
