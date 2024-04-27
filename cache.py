import streamlit as st

# Define a function that performs expensive computation
@st.cache
def expensive_computation(x):
    # Assume this computation takes a long time
    result = x ** 2
    return result

# Main Streamlit app code
st.title("Caching Example")

# Call the expensive computation function with a value
input_value = st.slider("Select a value", 0, 100, 50)
result = expensive_computation(input_value)

# Display the result
st.write(f"Result of the expensive computation: {result}")