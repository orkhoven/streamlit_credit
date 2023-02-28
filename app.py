import requests
import streamlit as st

# Define the URL for your FastAPI app
FASTAPI_URL = "https://orkun-credit.onrender.com/predict"

# Define a function to send requests to your FastAPI app and return the response
def get_prediction(features):
    response = requests.post(FASTAPI_URL, json=features)
    return response.json()

# Define your Streamlit app
def main():
    # Create a title for your app
    st.title("Credit Scoring")

    # Create a form to get user input
    form = st.form(key='my-form')
    age = form.number_input('Age', min_value=0, max_value=100)
    income = form.number_input('Income', min_value=0)
    loan_amount = form.number_input('Loan Amount', min_value=0)
    credit_score = form.number_input('Credit Score', min_value=300, max_value=850)
    submit_button = form.form_submit_button(label='Submit')

    # When the user submits the form, send a request to your FastAPI app and display the response
    if submit_button:
        features = {'age': age, 'income': income, 'loan_amount': loan_amount, 'credit_score': credit_score}
        prediction = get_prediction(features)
        st.write('Prediction:', prediction)

if __name__ == '__main__':
    main()