import streamlit as st
import pandas as pd
import joblib
import os

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Network Intrusion Detection",
    page_icon="🛡️",
    layout="wide"
)

# --------------------------------------------------
# Load Model and Preprocessor
# --------------------------------------------------

@st.cache_resource
def load_models():
    model = joblib.load("models/xgb_model.pkl")
    preprocessor = joblib.load("models/preprocessor.pkl")
    return model, preprocessor


model, preprocessor = load_models()

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🛡️ Network Intrusion Detection System")

st.markdown(
    """
    ### Machine Learning Based Network Intrusion Detection

    This application uses a trained **XGBoost classification model**
    to identify whether network traffic is **Normal** or represents an
    **Attack**.

    **Dataset:** UNSW-NB15  
    **Model:** XGBoost  
    **Task:** Binary Network Traffic Classification
    """
)

st.divider()

# --------------------------------------------------
# Model Information
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model", "XGBoost")

with col2:
    st.metric("Accuracy", "86.98%")

with col3:
    st.metric("Recall", "97.71%")

st.divider()

# --------------------------------------------------
# File Upload
# --------------------------------------------------

st.subheader("📂 Upload Network Traffic Data")

st.write(
    "Upload a CSV file containing the network traffic features "
    "used by the trained model."
)

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

# --------------------------------------------------
# Prediction
# --------------------------------------------------

if uploaded_file is not None:

    try:

        data = pd.read_csv(uploaded_file)

        st.success("CSV file uploaded successfully!")

        st.subheader("📋 Uploaded Data")

        st.dataframe(
            data.head(10),
            use_container_width=True
        )

        # Get the features expected by the preprocessor
        expected_features = list(preprocessor.feature_names_in_)

        missing_features = [
            feature for feature in expected_features
            if feature not in data.columns
        ]

        if missing_features:

            st.error(
                "The uploaded CSV is missing required features."
            )

            st.write("Missing features:")

            st.code(
                "\n".join(missing_features)
            )

        else:

            # Keep only the features required by the model
            input_data = data[expected_features]

            # Apply preprocessing
            transformed_data = preprocessor.transform(input_data)

            # Generate predictions
            predictions = model.predict(transformed_data)

            # Convert predictions to readable labels
            result = data.copy()

            result["Prediction"] = [
                "Attack" if prediction == 1 else "Normal"
                for prediction in predictions
            ]

            # Prediction probabilities
            probabilities = model.predict_proba(
                transformed_data
            )

            result["Attack Probability"] = (
                probabilities[:, 1] * 100
            ).round(2)

            # --------------------------------------------------
            # Results
            # --------------------------------------------------

            st.subheader("🔍 Detection Results")

            result_counts = result["Prediction"].value_counts()

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Normal Traffic",
                    int(result_counts.get("Normal", 0))
                )

            with col2:
                st.metric(
                    "Detected Attacks",
                    int(result_counts.get("Attack", 0))
                )

            st.dataframe(
                result,
                use_container_width=True
            )

            # --------------------------------------------------
            # Download Results
            # --------------------------------------------------

            csv = result.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="⬇️ Download Prediction Results",
                data=csv,
                file_name="intrusion_detection_results.csv",
                mime="text/csv"
            )

    except Exception as e:

        st.error(
            "An error occurred while processing the uploaded file."
        )

        st.exception(e)

else:

    st.info(
        "👆 Upload a CSV file to start intrusion detection."
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Machine Learning Based Network Intrusion Detection | "
    "UNSW-NB15 | XGBoost"
)
