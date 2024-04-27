import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# create simple Dataframe 

data = {
    'Name': ['Aayush','Om','Patil','Prathmesh'],
    'Age' : ['18','19','17','18'],
    'Score':['60','80','50','90']
}

df = pd.DataFrame(data)

# st.dataframe() example
st.write("Displaying DataFrame using st.dataframe():")
st.dataframe(df)

#st.table() example
st.write("Displaying DataFrame using st.dataframe():")
st.dataframe(df)

# Generate random data for plotly chart
np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)

# st.plotly_chart() example
st.write("Displaying Plotly chart using st.plotly_chart():")
fig = px.scatter(x=x, y=y, title="Scatter Plot", labels={'x': 'X-axis', 'y': 'Y-axis'})
st.plotly_chart(fig)

# Sample data for st.map()
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

# st.map() example
st.write("Displaying map using st.map():")
st.map(map_data)

