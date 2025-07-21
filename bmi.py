import streamlit as st

st.title("BMI Calculator")
st.header("This is my bmi calculator")
st.text("This bmi calculator can help you to know your body weights and the sign it provides to help you to come out and take some regular preventive steps.")

weight = st.number_input("Enter your weight (kg)", min_value= 1)
height = st.number_input("Enter your height (feet)", min_value=1.0)

if st.button("Calulate BMI"):
    # height_m = height/100
    bmi = weight/(((height/3.28)) **2)
    st.header(f"Your bmi is: {bmi}")
    
    if bmi < 16:
        st.error("You are Extremely Underweight")
        
    if 16 <= bmi < 18.5:
        st.warning("You are Underweight")
        
    if 18.5 <= bmi  < 25:
        st.success("You are healthy")
        
    if 25 <= bmi < 30:
        st.info("You are overweight")
        
    if bmi >= 30:
        st.error("You are Extremely overweight")
        
    
