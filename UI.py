import streamlit as st
import HD_model
import numpy as np

def main():
    st.title("Heart Health Predictor")

    # Create a form for user input

    sex_mapping = {"Male": 1, "Female": 0}
    fbs_mapping = {"Yes": 1,"No": 0}
    exang_mapping = {"Yes": 1,"No": 0} 

    with st.form("heart_form"):
        st.write("Fill in the following details:")
        age = st.slider("Age", 1, 100, 25)
        sex = st.radio("Sex", ["Male", "Female"])
        mapped_sex = sex_mapping.get(sex)
        cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
        trestbps = st.slider("Resting Blood Pressure", 90, 200, 120)
        chol = st.slider("Cholesterol", 100, 600, 200)
        fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
        mapped_fbs=fbs_mapping.get(fbs)
        restecg = st.selectbox("Resting Electrocardiographic Results", [0, 1, 2])
        thalach = st.slider("Maximum Heart Rate Achieved", 60, 220, 150)
        exang = st.radio("Exercise Induced Angina", ["No", "Yes"])
        mapped_exang = exang_mapping.get(exang)
        oldpeak = st.slider("ST Depression Induced by Exercise Relative to Rest", 0.0, 6.2, 0.0)
        slope = st.selectbox("Slope of the Peak Exercise ST Segment", [0, 1, 2])
        ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", [0, 1, 2, 3])
        thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

        submitted = st.form_submit_button("Predict")

    # Display the prediction result
    if submitted:
        st.subheader("Prediction Result:")
        input_data = (int(age),mapped_sex,int(cp),int(trestbps),int(chol),mapped_fbs,int(restecg),int(thalach),mapped_exang,float(oldpeak),int(slope),int(ca),int(thal))

        input_data_as_numpy_array= np.asarray(input_data)

        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = HD_model.model.predict(input_data_reshaped)

        if (prediction[0]== 0):
            st.write('The Person does not have a Heart Disease')
        else:
            st.write('The Person has Heart Disease')

if __name__ == "__main__":
    main()
