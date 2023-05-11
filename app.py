from flask.helpers import url_for
import numpy as np
import pandas as pd
from flask import Flask, request, render_template, redirect
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pickle', 'rb'))


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        gender_Male = int(request.form['gender'])
        age = int(request.form['age'])
        hypertension_1 = int(request.form['hypertension'])
        heart_disease_1 = int(request.form['disease'])
        ever_married_Yes = int(request.form['married'])
        work = int(request.form['work'])
        Residence_type_Urban =int( request.form['residence'])
        avg_glucose_level = float(request.form['avg_glucose_level'])
        bmi = float(request.form['bmi'])
        smoking = int(request.form['smoking'])
        work_type_Never_worked=0
        work_type_Private=0
        work_type_Self_employed=0
        work_type_children=0
        if(work==1):
           work_type_Never_worked=1
        elif work==2: 
            work_type_Private=1
        elif work==3:
            work_type_Self_employed=1
        elif work==4:
            work_type_children=1
        smoking_status_formerly_smoked=0
        smoking_status_never_smoked	=0
        smoking_status_smokes=0
        if smoking==1:
            smoking_status_formerly_smoked=1
        elif smoking==2:
            smoking_status_never_smoked	=1
        elif smoking==3:
            smoking_status_smokes=1
            

        input_features = [age	,avg_glucose_level,	bmi	,gender_Male,hypertension_1,	heart_disease_1,ever_married_Yes,	work_type_Never_worked,	work_type_Private,	work_type_Self_employed,	work_type_children	,Residence_type_Urban,	smoking_status_formerly_smoked,smoking_status_never_smoked	,smoking_status_smokes]

        features_value = [np.array(input_features)]
        features_name = ['age'	,'avg_glucose_level',	'bmi'	,'gender_Male'	,'hypertension_1',	'heart_disease_1','ever_married_Yes',	'work_type_Never_worked',	'work_type_Private',	'work_type_Self-employed',	'work_type_children'	,'Residence_type_Urban',	'smoking_status_formerly smoked','smoking_status_never smoked'	,'smoking_status_smokes']


        df = pd.DataFrame(features_value, columns=features_name)
        print(df)
        prediction = model.predict(df)[0]
        print(prediction)
        if prediction == 1:
            return render_template('index.html', prediction_text='Patient has stroke risk')
        else:
            return render_template('index.html', prediction_text='Congratulations, patient does not have stroke risk')

        # return render_template('index.html', prediction_text='Patient has {}'.format(df))


if __name__ == "__main__":
    app.run()
