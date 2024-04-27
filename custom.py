import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="My Custom Streamlit App",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",  # "centered" or "wide"
    initial_sidebar_state="collapsed"  # "auto" or "collapsed"
)
#page_title: Sets the title of your Streamlit app.
#page_icon: Sets the favicon for your Streamlit app (can be an emoji).
#layout: Sets the layout of the app ("centered" or "wide").
#initial_sidebar_state: Sets the initial state of the sidebar ("auto" or "collapsed").

# Markdown for custom styling
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
        }
        .css-1l02zno {
            font-size: 18px;
            color: #333333;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit elements
st.title("Customizing Appearance")
st.write("This is a Streamlit app with customized appearance.")
st.button("Click me")

