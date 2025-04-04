import streamlit as st

# Initialize session state key if not already set
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# Page navigation function
def navigate_to(page):
    st.session_state.current_page = page

# Main function to run the app
def show():
    if st.button("Back to Main Page"):
        st.session_state.current_page = 'home'

    # st.set_page_config(page_title="Dataset Categories", layout="wide")
    st.title("📊 Dataset Categories")

    # Define categories of datasets with images
    categories = {
        "Category 1": {
            "name": "E-Commerce Sales Analysis",
            "image": "img/e_commerce.jpg"
        },
        "Category 2": {
            "name": "Food Price Analysis",
            "image": "img/india_food_prices.jpg"
        }
        # "Category 3": {
        #     "name": "Other Datasets",
        #     "image": "img/image1.jpg"
        # },
        # "Category 4": {
        #     "name": "Dataset 4",
        #     "image": "img/linked_bg.png"
        # }
    }

    # Create a grid layout for the categories
    cols = st.columns(2)

    for i, (category, details) in enumerate(categories.items()):
        with cols[i % 2]:  # Alternate between columns
            # Check if the image URL is valid (optional)
            if details["image"]:
                st.image(details["image"], use_container_width=True)
            else:
                st.warning(f"No image available for {category}.")
            
            if st.button(f"Explore {details['name']}"):
                # Set the current page in session state
                st.session_state.current_page = details["name"]
            
            st.write("------------------------------------------------------------------------------------------")
