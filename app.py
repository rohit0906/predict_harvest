import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    out={0:'Alive', 1:'Damage due to other causes', 2:'Damage due to Pesticides'}
    if final_features[0][3]!=3 and prediction[0]==2:
        prediction[0]=1;

    output=out[prediction[0]]

    return render_template('index.html', prediction_text=' {}'.format(output))



if __name__ == "__main__":
    app.run(debug=True)