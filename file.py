import streamlit as st
import pandas as pd

# File Upload
st.title("File Upload and Download Example")

# Display file uploader widget
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# If file is uploaded
if uploaded_file is not None:
    # Read uploaded CSV file
    df = pd.read_csv(uploaded_file)
    # Display DataFrame
    st.write("Uploaded DataFrame:")
    st.write(df)

    # File Download
    st.write("Download your uploaded file:")
    # Convert DataFrame to CSV string
    csv_string = df.to_csv(index=False)
    # Create a button for downloading the CSV file
    st.download_button(label="Download CSV", data=csv_string, file_name='uploaded_file.csv', mime='text/csv')
