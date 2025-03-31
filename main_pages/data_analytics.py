import streamlit as st


# Page navigation function
def navigate_to(page):
    st.session_state.current_page = page


# Main function to run the app
def show():
    from data_analytics_templates import e_commerce
    from data_analytics_templates import food_prices
    
    
    #st.set_page_config(page_title="Dataset Categories", layout="wide")
    st.title("📊 Dataset Categories")


    # Define categories of datasets with images
    categories = {
        "Category 1": {
            "name": "E-Commerce Sales Data Analysis",
            "image": "img/e_commerce.png",  # Fixed typo in the image path
            "path": "e_commerce"  # Adjusted path to be relative
        },
        "Category 2": {
            "name": "Food Price Analysis",
            "image": "img/food_prices.png",  # Adjusted path to be relative
            "path": "food_prices"  # Adjusted path to be relative
        },
        "Category 3": {
            "name": "Other Datasets",
            "image": "https://via.placeholder.com/150.png?text=Category+3",
            "path": ""  # No path for this category
        },
        "Category 4": {
            "name": "Dataset 4",
            "image": "https://via.placeholder.com/150.png?text=Category+4",
            "path": ""  # No path for this category
        },
    }

    # Create a grid layout for the categories
    cols = st.columns(2)

    for i, (category, details) in enumerate(categories.items()):
        with cols[i % 2]:  # Alternate between columns
            st.image(details["image"], caption=details["name"])  # Use details["name"] for caption
            if st.button(f"Explore {details['name']}"):
                if details["path"]:  # Check if the path is not empty
                    navigate_to(details["path"])  # Navigate to the actual path
                else:
                    st.warning("No path available for this category.")

#if __name__ == "__main__":
#    data_analytics()

    if st.button("Back to Main Page"):
        st.session_state.current_page = 'home'
