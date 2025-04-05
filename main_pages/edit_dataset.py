import streamlit as st
import pandas as pd

def show():
    if st.button("Back to Main Page"):
        st.session_state.current_page = 'home'


    st.title("📊 Dataset Manager")
    
    # upload file
    uploaded_file = st.sidebar.file_uploader("CHOOSE YOUR FILE:", type=["csv","xlsx"])


    if uploaded_file is not None:
        #read the file
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)
            else:
                st.error("Invalid file type, Please upload CSV or Excel file.")
        except Exception as e:
            st.error(f"Error reading file: {e}")
        
        # Input for number of rows to view
        num_rows = st.number_input("Enter number of rows to display", min_value=1, max_value=len(df), value=5)
        st.dataframe(df.head(num_rows))
        
        # Rename columns
        st.subheader("Rename Columns")
        new_column_names = {}
        for col in df.columns:
            new_col_name = st.text_input(f"Rename '{col}' to:", value=col)
            new_column_names[col] = new_col_name
        
        if st.button("Rename Columns"):
            df.rename(columns=new_column_names, inplace=True)
            st.session_state["df"] = df
            st.success("Columns renamed successfully!")
        
        # Delete row option
        st.subheader("Delete a Row")
        row_to_delete = st.number_input("Enter row index to delete", min_value=0, max_value=len(df)-1, step=1)
        if st.button("Delete Row"):
            df = df.drop(index=row_to_delete).reset_index(drop=True)
            st.session_state["df"] = df
            st.success("Row deleted successfully!")
        
        # Add new row
        st.subheader("Add a New Row")
        new_data = {}
        for col in df.columns:
            new_data[col] = st.text_input(f"Enter value for {col}", key=f"add_{col}")
        
        if st.button("Add Row"):
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            st.session_state["df"] = df
            st.success("New row added successfully!")
        
        # Display updated dataframe
        st.subheader("Updated Dataset")
        st.dataframe(df)
        
        # Download updated dataset
        st.subheader("Download Updated Dataset")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", csv, "updated_dataset.csv", "text/csv")

# if __name__ == "__main__":
#     show()


# # Button to download the PDF
#         if st.button("Download Report as PDF"):
#             pdf_file = save_as_pdf(html_content)
#             with open(pdf_file, "rb") as f:
#                 st.download_button("Click here to download", f, file_name="dataset_analysis.pdf", mime="application/pdf")