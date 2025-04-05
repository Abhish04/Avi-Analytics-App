import streamlit as st

def show():
    if st.button("Back to Main Page"):
        st.session_state.current_page = 'home'


    st.title("⚙️ Settings")
    
    # Initialize session state for settings
    if 'theme' not in st.session_state:
        st.session_state.theme = "Light"
    # if 'version' not in st.session_state:
    #     st.session_state.version = "1.0.0"
    if 'notifications' not in st.session_state:
        st.session_state.notifications = True
    if 'refresh_rate' not in st.session_state:
        st.session_state.refresh_rate = 10
    
    # Title Input
    st.header("Avi Analytics App")
    
    # Theme Selection
    theme = st.selectbox("Select Theme", ["Light", "Dark"], index=["Light", "Dark"].index(st.session_state.theme))
    
    # Version
    st.write("1.0.0.0")
    
    # Notifications Toggle
    notifications = st.checkbox("Enable Notifications", st.session_state.notifications)
    
    # Data Refresh Interval
    refresh_rate = st.slider("Data Refresh Interval (seconds)", 1, 60, st.session_state.refresh_rate)
    
    # Save Settings
    if st.button("Save Settings"):
        st.session_state.theme = theme
        st.session_state.notifications = notifications
        st.session_state.refresh_rate = refresh_rate
        st.success("Settings saved successfully! Reload the page to see changes.")
    
# if __name__ == "__main__":
#     show()