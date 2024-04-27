import streamlit as st

# st.sidebar() example
st.sidebar.title("Sidebar Title")
st.sidebar.write("This is a sidebar section.")
sidebar_option = st.sidebar.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])

# st.columns() example
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
    st.write("This is the first column.")

with col2:
    st.write("Column 2")
    st.write("This is the second column.")
    
# st.expander() example
with st.expander("Click to expand"):
    st.write("This is the content inside the expander.")
    st.write("You can put any content here, such as text, images, or widgets.")

# Advanced layout with combination of st.columns() and st.expander()
col1, col2 = st.columns([1, 2])
with col1:
    st.write("This column has a width ratio of 1.")
    st.write("It occupies one-third of the available width.")

with col2:
    with st.expander("Expand to see more"):
        st.write("This column has a width ratio of 2.")
        st.write("It occupies two-thirds of the available width.")
