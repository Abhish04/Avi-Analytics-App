import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    mean_squared_error, r2_score, confusion_matrix, silhouette_score
)
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC, SVR
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans
from xgboost import XGBClassifier, XGBRegressor
from lightgbm import LGBMClassifier, LGBMRegressor
import matplotlib.pyplot as plt
import seaborn as sns


def show():
    st.title("🤖 Machine Learning Playground")
    st.markdown("Upload your dataset and explore machine learning models")

    # File upload
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
        
            st.success("Dataset loaded successfully!")
            st.subheader("Data Preview")
            st.dataframe(df.head())

            # Column selection
            cols = df.columns.tolist()
            problem_type = st.selectbox("Select problem type:", ["Classification", "Regression", "Clustering"])

            if problem_type == "Clustering":
                feature1 = st.selectbox("Select first feature column", cols)
                feature2 = st.selectbox("Select second feature column", cols)
            else:
                feature = st.selectbox("Select feature column", cols)
                target = st.selectbox("Select target column", cols)

            # Data preprocessing
            st.subheader("Data Preprocessing")
            handle_nan = st.radio("Handle missing values:", 
                                ["Drop missing values", "Impute with mean/median"])
        
            scale_features = st.checkbox("Scale features (recommended for SVM, Logistic Regression)")

            # Model selection
            st.subheader("Model Selection")
            models = {
                "Classification": {
                    "Logistic Regression": LogisticRegression(),
                    "Decision Tree": DecisionTreeClassifier(),
                    "Random Forest": RandomForestClassifier(),
                    "SVM": SVC(),
                    "K-Nearest Neighbors": KNeighborsClassifier(),
                    "Naive Bayes": GaussianNB(),
                    "XGBoost": XGBClassifier(),
                    "LightGBM": LGBMClassifier()
                },
                "Regression": {
                    "Linear Regression": LinearRegression(),
                    "Decision Tree": DecisionTreeRegressor(),
                    "Random Forest": RandomForestRegressor(),
                    "SVM": SVR(),
                    "K-Nearest Neighbors": KNeighborsRegressor(),
                    "XGBoost": XGBRegressor(),
                    "LightGBM": LGBMRegressor()
                },
                "Clustering": {
                    "K-Means Clustering": KMeans()
                }
            }
    
            selected_model = st.selectbox("Choose a model", list(models[problem_type].keys()))
    
            # Train-test split
            test_size = st.slider("Test set size (%)", 10, 40, 20) / 100
            random_state = st.number_input("Random state", 42)
    
            if st.button("Train Model"):
                # Handle missing values
                if handle_nan == "Drop missing values":
                    if problem_type == "Clustering":
                        df_clean = df[[feature1, feature2]].dropna()
                    else:
                        df_clean = df[[feature, target]].dropna()
                else:
                    if problem_type == "Clustering":
                        df_clean = df[[feature1, feature2]].fillna(df.median())
                    else:
                        df_clean = df[[feature, target]].fillna(df.median())

                # Split data
                if problem_type == "Clustering":
                    X = df_clean[[feature1, feature2]]
                    y = None
                else:
                    X = df_clean[[feature]]
                    y = df_clean[target]

                # Check valid dataset
                if len(X) < 10 or (y is not None and len(y) < 10):
                    st.error("Not enough data to train the model. Please ensure your dataset has sufficient entries.")
                    st.stop()

                # Scale features if selected
                if scale_features:
                    scaler = StandardScaler()
                    X = scaler.fit_transform(X)

                # Train-test split
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

                # Model training
                model = models[problem_type][selected_model]
                if problem_type == "Clustering":
                    model.fit(X)
                    labels = model.predict(X)
                    silhouette = silhouette_score(X, labels)
                    st.success(f"Model trained successfully! Silhouette Score: {silhouette:.2f}")

                    # Visualization
                    plt.figure(figsize=(10, 6))
                    sns.scatterplot(x=X[feature1], y=X[feature2], hue=labels, palette='viridis')
                    plt.title("K-Means Clustering Results")
                    plt.xlabel(feature1)
                    plt.ylabel(feature2)
                    st.pyplot(plt)

                else:
                    model.fit(X_train, y_train)
                    y_pred = model.predict(X_test)

                    # Evaluation metrics
                    if problem_type == "Classification":
                        accuracy = accuracy_score(y_test, y_pred)
                        precision = precision_score(y_test, y_pred, average='weighted')
                        recall = recall_score(y_test, y_pred, average='weighted')
                        f1 = f1_score(y_test, y_pred, average='weighted')
                        st.success(f"Model trained successfully! Accuracy: {accuracy:.2f}, Precision: {precision:.2f}, Recall: {recall:.2f}, F1 Score: {f1:.2f}")

                        # Confusion matrix
                        cm = confusion_matrix(y_test, y_pred)
                        plt.figure(figsize=(8, 6))
                        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
                        plt.title("Confusion Matrix")
                        plt.xlabel("Predicted")
                        plt.ylabel("Actual")
                        st.pyplot(plt)

                    else:  # Regression
                        mse = mean_squared_error(y_test, y_pred)
                        r2 = r2_score(y_test, y_pred)
                        st.success(f"Model trained successfully! MSE: {mse:.2f}, R²: {r2:.2f}")
    
                        # Scatter plot
                        plt.figure(figsize=(10, 6))
                        plt.scatter(y_test, y_pred)
                        plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
                        plt.xlabel("Actual")
                        plt.ylabel("Predicted")
                        plt.title("Regression Results")
                        st.pyplot(plt)

        except Exception as e:
            st.error(f"An error occurred: {e}")



