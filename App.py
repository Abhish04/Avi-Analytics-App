import streamlit as st

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

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

# Page navigation function
def navigate_to(page):
    st.session_state.current_page = page

# Main page content
def show_home():
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
        if st.button("Go to Data Analysis", key="data_analysis"):
            navigate_to("data_analysis")

    with col2:
        st.markdown('<div class="category-block">' +
                    '<div class="category-title">🤖 Machine Learning</div>' +
                    '<div class="category-description">Train and evaluate machine learning models</div>' +
                    '</div>', 
                    unsafe_allow_html=True)
        if st.button("Go to Machine Learning", key="machine_learning"):
            navigate_to("machine_learning")

    with col3:
        st.markdown('<div class="category-block">' +
                    '<div class="category-title">📈 Forecasting</div>' +
                    '<div class="category-description">Time series analysis and prediction tools</div>' +
                    '</div>', 
                    unsafe_allow_html=True)
        if st.button("Go to Forecasting", key="forecasting"):
            navigate_to("forecasting")

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
        if st.button("Go to Settings", key="settings"):
            navigate_to("settings")

    with col5:
        st.markdown('<div class="category-block">' +
                    '<div class="category-title">📚 Documentation</div>' +
                    '<div class="category-description">User  guides and API references</div>' +
                    '</div>', 
                    unsafe_allow_html=True)
        if st.button("Go to Documentation", key="documentation"):
            navigate_to("documentation")

# Page routing
if st.session_state.current_page == 'home':
    show_home()
elif st.session_state.current_page == 'data_analysis':
    try:
        from main_pages import data_analytics as da
        da.show()
    except ImportError:
        st .error("Data analysis module could not be imported.")
elif st.session_state.current_page == 'machine_learning':
    try:
        from main_pages import machine_learning as ml
        ml.show()
    except ImportError:
        st.error("Machine learning module could not be imported.")
elif st.session_state.current_page == 'forecasting':
    try:
        from main_pages import forecasting as fc
        fc.show()
    except ImportError:
        st.error("Forecasting module could not be imported.")
elif st.session_state.current_page == 'settings':
    try:
        from main_pages import settings as stg
        stg.show()
    except ImportError:
        st.error("Settings module could not be imported.")
elif st.session_state.current_page == 'documentation':
    try:
        from main_pages import documentation as doc
        doc.show()
    except ImportError:
        st.error("Documentation module could not be imported.")
else:
    st.error("Page not found.")
