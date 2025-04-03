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
            "name": "E-Commerce Sales Data Analysis",
            "image": "img\e_commerce.jpg",
            "path": "e_commerce"
        },
        "Category 2": {
            "name": "Food Price Analysis",
            "image": "img\india_food_prices.jpg",
            "path": "food_prices"
        },
        "Category 3": {
            "name": "Other Datasets",
            "image": "https://www.bing.com/ck/a?!&&p=66550ab90be1d214119ba8e4d72da032c56c04e6e383543d7533cbee8aee9424JmltdHM9MTc0MzYzODQwMA&ptn=3&ver=2&hsh=4&fclid=385b4511-ca1f-6178-0ffd-5795cbad60aa&u=a1L2ltYWdlcy9zZWFyY2g_cT1pbWFnZXMmaWQ9RUVDRkJCN0Y0MzIwOTIxNTcxQTUzOURCNDU5Q0FDRkU5RDFFQzI0MiZGT1JNPUlRRlJCQQ&ntb=1",
            "path": ""
        },
        "Category 4": {
            "name": "Dataset 4",
            "image": "https://www.bing.com/ck/a?!&&p=66550ab90be1d214119ba8e4d72da032c56c04e6e383543d7533cbee8aee9424JmltdHM9MTc0MzYzODQwMA&ptn=3&ver=2&hsh=4&fclid=385b4511-ca1f-6178-0ffd-5795cbad60aa&u=a1L2ltYWdlcy9zZWFyY2g_cT1pbWFnZXMmaWQ9RUVDRkJCN0Y0MzIwOTIxNTcxQTUzOURCNDU5Q0FDRkU5RDFFQzI0MiZGT1JNPUlRRlJCQQ&ntb=1",
            "path": ""
        },
    }

    # Create a grid layout for the categories
    cols = st.columns(2)

    for i, (category, details) in enumerate(categories.items()):
        with cols[i % 2]:  # Alternate between columns
            # Check if the image URL is valid (optional)
            if details["image"]:
                st.image(details["image"], caption=category, width=500, use_container_width=False)
            else:
                st.warning(f"No image available for {category}.")
            
            if st.button(f"Explore {details['name']}"):
                # Set the current page in session state
                st.session_state.current_page = details['path']
                  

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
elif st.session_state.current_page == 'e_commerce':
    try:
        from data_analytics_templates import e_commerce
        e_commerce.show()
    except ImportError:
        st.error("e_commerce module could not be imported.")
elif st.session_state.current_page == 'food_prices':
    try:
        from data_analytics_templates import food_prices
        food_prices.show()
    except ImportError:
        st.error("food_prices module could not be imported.")
else:
    st.error("Page not found.")
