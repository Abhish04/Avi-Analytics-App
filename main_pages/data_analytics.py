import streamlit as st



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
            "name": "e_commerce",
            "image": "img/e_commerce.jpg"
        },
        "Category 2": {
            "name": "Food Price Analysis",
            "image": "img/india_food_prices.jpg"
        },
        "Category 3": {
            "name": "Other Datasets",
            "image": "img/image1.jpg"
        },
        "Category 4": {
            "name": "Dataset 4",
            "image": "img/linked_bg.png"
        },
    }

    # Create a grid layout for the categories
    cols = st.columns(2)

    for i, (category, details) in enumerate(categories.items()):
        with cols[i % 2]:  # Alternate between columns
            # Check if the image URL is valid (optional)
            if details["image"]:
                st.image(details["image"], caption=category, use_container_width=True)
            else:
                st.warning(f"No image available for {category}.")
            
            if st.button(f"Explore {details['name']}"):
                # Set the current page in session state
                st.session_state.current_page = {details["name"]}
                  

#if __name__ == "__main__":
#    data_analytics()




    
# Page routing
if st.session_state.current_page == 'home':
    try:
        import App
        App.show_home()
    except ImportError:
        st .error("Data analysis module could not be imported.")   
elif st.session_state.current_page == 'data_analysis':
    try:
        show()
    except ImportError:
        st .error("Data analysis module could not be imported.")
elif st.session_state.current_page == 'E-Commerce Sales Data Analysis':
    try:
        from data_analytics_templates import e_commerce
        e_commerce.show()
    except ImportError:
        st.error("e_commerce module could not be imported.")
elif st.session_state.current_page == 'Food Price Analysis':
    try:
        from data_analytics_templates import food_prices
        food_prices.show()
    except ImportError:
        st.error("food_prices module could not be imported.")
else:
    st.error("Page not found.")
