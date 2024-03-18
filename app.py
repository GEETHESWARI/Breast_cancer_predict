import numpy as np
import pandas as pd
from flask import Flask, render_template,request
import pickle


app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def valuepredictor(to_predict_list):
    to_predict=np.array(to_predict_list).reshape(1,12)
    loaded_model=pickle.load(open('classifier.pkl','rb'))
    result=loaded_model.predict(to_predict)
    return result[0]

@app.route('/streamlit_result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float,to_predict_list))
        print(to_predict_list)
        result = valuepredictor(to_predict_list)
        
        if float(result)==1:
          result='We  inform you that from our analysis indicates the patient  the presence of malignant breast cancer'
        else:  
          result='Our assessment reveals that there is no evidence of malignant breast cancer'

           
        return render_template('result.html',result= result)

if __name__ == "__main__": 

        app.run(debug=True)
        app.config['TEMPLATES_AUTO_RELOAD']=True           

