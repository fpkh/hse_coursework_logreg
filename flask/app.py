from flask import Flask, render_template, request, flash
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
app.secret_key = '1'

model = pickle.load(open('models/model.pkl', 'rb'))
THRESHOLD = 0.25

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    features = model.named_steps['classifier'].feature_names_in_
    augmented = pd.DataFrame(columns=features)

    input = {}
    ok_keys = ['age', 'sex', 'credit_amount', 'duration']
    for key, value in request.form.items():
        if key in ok_keys:
            input[key] = int(value)
        else:
            input[value] = 1

    input = {i:input[i] for i in input if i != 'dummy'}
    print(input)

    augmented = pd.concat([augmented, pd.DataFrame(input, index=[0])], ignore_index=True).fillna(0)

    prediction = model.predict_proba(augmented)
    print(prediction)
    if (np.where(model.predict_proba(augmented)[:,1] > THRESHOLD, 1, 0)[0] == 1):
        return render_template('predict.html', predict_content="Denied", predict_value="probability of default: {}".format(round(prediction[:,1][0], 2)), predict_threshold="threshold: {}".format(THRESHOLD))
    
    return render_template('predict.html', predict_content="Granted", predict_value="probability of default: {}".format(round(prediction[:,1][0], 2)), predict_threshold="threshold: {}".format(THRESHOLD))


if __name__=='__main__':
    app.run()