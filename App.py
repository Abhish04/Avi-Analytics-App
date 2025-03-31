import streamlit as st


# Set page config
st.set_page_config(
    page_title="My App",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .category-block {
        padding: 20px;
        border-radius: 10px;
        margin: 10px;
        background-color: #f0f2f6;
        transition: all 0.3s;
    }
    .category-block:hover {
        transform: scale(1.02);
        box-shadow: 0 0 8px #d6d6d6;
    }
    .category-title {
        font-size: 1.4em;
        font-weight: bold;
        color: #2c3e50;
    }
    .category-description {
        font-size: 0.9em;
        color: #7f8c8d;
    }
    </style>
    """, unsafe_allow_html=True)

# Main page content
def home():
    st.title("Welcome to My App! 🌟")
    st.markdown("""
    ### Explore different sections using the categories below
    Select a category to get started with specific functionalities.
    """)

    # Create columns for category layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="category-block">' +
                    '<div class="category-title">📊 Data Analysis</div>' +
                    '<div class="category-description">Explore data visualization and statistical analysis tools</div>' +
                    '</div>', 
                    unsafe_allow_html=True)
        st.page_link("main_pages/data_analytics.py", label="Go to Data Analysis", icon="🏠")

    with col2:
        st.markdown('<div class="category-block">' +
                    '<div class="category-title">🤖 Machine Learning</div>' +
                    '<div class="category-description">Train and evaluate machine learning models</div>' +
                    '</div>', 
                    unsafe_allow_html=True)
        st.page_link("main_pages/machine_learning.py", label="Machine Learning", icon="🏠")

    with col3:
        st.markdown('<div class="category-block">' +
                    '<div class="category-title">📈 Forecasting</div>' +
                    '<div class="category-description">Time series analysis and prediction tools</div>' +
                    '</div>', 
                    unsafe_allow_html=True)
        st.page_link("main_pages/data_analytics.py", label="Go to Data Analysis", icon="🏠")

    # Additional Tools
    st.markdown("---")
    st.markdown("### Additional Tools")
    
    col4, col5 = st.columns(2)
    with col4:
        st.markdown('<div class="category-block">' +
                    '<div class="category-title">⚙️ Settings</div>' +
                    '<div class="category-description">Configure application settings</div>' +
                    '</div>', 
                    unsafe_allow_html=True)
        st.page_link("main_pages/data_analytics.py", label="Go to Data Analysis", icon="🏠")

    with col5:
        st.markdown('<div class="category-block">' +
                    '<div class="category-title">📚 Documentation</div>' +
                    '<div class="category-description">User  guides and API references</div>' +
                    '</div>', 
                    unsafe_allow_html=True)
        st.page_link("main_pages/data_analytics.py", label="Go to Data Analysis", icon="🏠")

if __name__ == "__main__":
    home()
