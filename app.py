from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('diabetic_rf.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods = ['GET','POST'])
def predict():

    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = prediction[0]
    if output == 0:
        return render_template('home.html', prediction_text = 'Diabetes : No')
    else:
        return render_template('home.html', prediction_text = 'Diabetes : Yes')

if __name__ == '__main__':
    app.run(debug = True)

"""
Pregnancies = request.form['Pregnancies']
    Glucose = request.form['Glucose']
    BloodPressure = request.form['BloodPressure']
    SkinThickness = request.form['SkinThickness']
    Insulin = request.form['Insulin']
    BMI = request.form['BMI']
    DiabetesPedigreeFunction = request.form['Diabetes_Pedigree_Function']
    Age = request.form['Age']
    return render_template('home.html', prediction_text = Pregnancies)
    """