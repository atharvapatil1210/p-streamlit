import streamlit as st
# # Basic usage of st.button()
# if st.button("Click me"):
#     st.write("`Buttton Clicked`")
    
# Basic usage of st.text_input()
name = st.text_input("Enter your name ", "John Doe")
st.write(f"Hello , {name}!")

# Basic usage of st.slider()
age = st.slider("Select your age",0,100,25)
st.write(f"Your age is : {age}")

# Basic usage of st.selectbox()
options = ["Option 1", "Option 2", "Option 3"]
selected_option = st.selectbox("Select an option", options)
st.write(f"You selected: {selected_option}")

st.write("Advanced Example:")
button_clicked = st.button("Click me")
if button_clicked:
    name = st.text_input("Enter your name", "John Doe")
    age = st.slider("Select your age", 0, 100, 25)
    options = ["Option 1", "Option 2", "Option 3"]
    selected_option = st.selectbox("Select an option", options)
    st.write(f"Hello, {name}! Your age is {age}. You selected: {selected_option}")
