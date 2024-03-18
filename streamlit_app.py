import streamlit as st
import numpy as np
import pickle

# Load your trained model (classifier.pkl)
loaded_model = pickle.load(open("C:/Desktop/Desktop/ML_Breast Cancer/classifier.pkl", 'rb'))

def breastcancer_predict(input_data):
    to_predict = np.array(input_data).reshape(1, 12)
    result = loaded_model.predict(to_predict)
    print(result)
    
    if (result[0]==1):
        return "Our analysis indicates the presence of malignant breast cancer."
    else:
        return "Our assessment reveals no evidence of malignant breast cancer(Benign)."
        


def main():
    
    # Giving title
    st.title("Breast Cancer Prediction App")
    
   
       
       
    radius_mean=st.text_input('Radius Mean')
       
    texture_mean=st.text_input('Texture Mean')
       
    smoothness_mean=st.text_input('Smoothness Mean')
       
    compactness_mean=st.text_input('Compactness Mean')
       
    symmetry_mean=st.text_input('Symmetry Mean')
       
    fractal_dimension_mean=st.text_input('Fractionam Dimesion Mean')
       
    radius_se=st.text_input('Radius Standard Error')
       
    texture_se=st.text_input('Texture Standard Error')
       
    smoothness_se=st.text_input('Smoothness Standard Error')
       
    compactness_se=st.text_input('Compactness Standard Error')
       
    symmetry_se =st.text_input('Symmetry Standard Error')
       
    fractal_dimension_se =st.text_input('Fractional Dimension Standard Error')
    
    
    #  Prediction
    
    diagnosis=''
    
    # Creating a button
    
    if st.button('Breast Cancer Prediction'):
        
        diagnosis=breastcancer_predict([radius_mean,  texture_mean, smoothness_mean,
       compactness_mean, symmetry_mean, fractal_dimension_mean,
       radius_se, texture_se, smoothness_se, compactness_se,
       symmetry_se, fractal_dimension_se])
        
    st.success(diagnosis)
    
    
if __name__=='__main__':
    main()        
        
    
    
       
       
       
       
       
       
    
    
    
    
    
    