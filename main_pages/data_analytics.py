import streamlit as st

# Main function to run the app
def main():
    st.set_page_config(page_title="Dataset Categories", layout="wide")
    st.title("📊 Dataset Categories")

    # Define categories of datasets with images
    categories = {
        "Category 1": {
            "name": "E-Commerce Sales Data Analysis",
            "image": "https://via.placeholder.com/150.png?text=Category+1",
            "path": ""
        },
        "Category 2": {
            "name": "Food Price Analysis",
            "image": "https://via.placeholder.com/150.png?text=Category+2",
            "path": ""
        },
        "Category 3": {
            "name": "Other Datasets",
            "image": "https://via.placeholder.com/150.png?text=Category+3",
            "path": ""
        },
        "Category 4": {
            "name": "Dataset 4",
            "image": "https://via.placeholder.com/150.png?text=Category+4",
            "path": ""
        },
    }

    # Create a grid layout for the categories
    cols = st.columns(2)

    for i, (category, details) in enumerate(categories.items()):
        with cols[i % 2]:  # Alternate between columns
            st.image(details["image"], caption=category, use_column_width=True)
            if st.button(f"Explore {details['name']}"):
                navigate_to("path")

if __name__ == "__main__":
    main()
