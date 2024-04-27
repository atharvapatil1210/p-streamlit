import streamlit as st

# Initialize session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Increase counter when button is clicked
if st.button('Increment'):
    st.session_state.counter += 1

# Display the counter value
st.write('Counter:', st.session_state.counter)


if 'counter' not in st.session_state:
    st.session_state.counter = 00
    
if st.button('Decreament'):
    st.session_state.counter -= 1
