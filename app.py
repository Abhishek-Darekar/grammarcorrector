import streamlit as st
from gramcorrector import correct,correct_ginger
st.title("Grammar Correction app")

input_text=st.text_area("Enter your text here")
output=st.button("correct")
if output:
    sub=correct_ginger(input_text)
    preprocess_text=sub["result"]
    st.write(correct(preprocess_text))