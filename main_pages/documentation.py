import streamlit as st

def show():
    if st.button("Back to Main Page"):
        st.session_state.current_page = 'home'

    st.title("📘 Avi Analytics App Documentation")
    
    st.header("Introduction")
    st.write("Avi Analytics App is a simple and easy-to-use tool for analyzing and visualizing data. It helps users explore datasets, create charts, and gain insights without needing programming knowledge.")
    
    st.header("Features")
    st.markdown("""
    - **User-Friendly Interface** – No coding required.
    - **Data Visualization** – Create charts and graphs easily.
    - **Upload Your Data** – Supports common file formats like CSV.
    - **Customizable Settings** – Change themes and preferences.
    - **Fast & Lightweight** – Works smoothly on most computers.
    """)
    
    st.header("How to Use")
    
    st.subheader("1. Installation")
    st.write("Follow these steps to set up the app on your computer:")
    
    st.markdown("""
    1. **Download the app** from the official GitHub repository.
    2. **Install Python** (if not already installed) from [python.org](https://www.python.org/).
    3. **Install Required Packages** by running:
       ```bash
       pip install -r requirements.txt
       ```
    4. **Run the App** with:
       ```bash
       streamlit run App.py
       ```
       This will open the app in your web browser.
    """)
    
    st.subheader("2. Using the App")
    st.write("Explore the app through these sections:")
    st.markdown("""
    - **Home Page** – View the main dashboard.
    - **Upload Data** – Select and upload a CSV file.
    - **Visualizations** – Choose chart types to analyze data.
    - **Settings** – Change the theme and app preferences.
    """)
    
    st.header("Troubleshooting")
    st.write("If you face issues, try these solutions:")
    st.markdown("""
    - If the app doesn’t open, check that **Python** and **Streamlit** are installed.
    - If you get an error, run:
      ```bash
      pip install -r requirements.txt
      ```
    - Restart the app if changes don’t appear.
    """)
    
    st.header("Need Help?")
    st.write("For support or feedback, visit the GitHub repository or contact the developer.")

    st.title("License")
    st.markdown("""
    ### Custom License
    You are free to use and share this app for personal or educational purposes only.  
    **Commercial use, modification, or redistribution is strictly prohibited** without permission.  
    
    For full license text, see [LICENSE.txt](https://github.com/Abhish04/Avi-Analytics-App/blob/main/LICENSE.txt).  
    Contact: **abhishekpratap2004@gmail.com**
    """)
    
# if __name__ == "__main__":
#     show()
