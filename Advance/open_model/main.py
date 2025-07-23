import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_squared_error

st.title("Custom AI Model Builder")

# --- Data Input ---
st.header("Input Your Data")
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
manual_data = st.text_area("Or paste CSV data here (with headers)")

# Load data
data = None
if uploaded_file:
    data = pd.read_csv(uploaded_file)
elif manual_data.strip():
    from io import StringIO
    data = pd.read_csv(StringIO(manual_data))

if data is not None:
    st.write("Preview:", data.head())
    cols = data.columns.tolist()
    target = st.selectbox("Select target column", cols)
    features = st.multiselect("Select features", [c for c in cols if c != target])

    problem_type = st.selectbox("Type of Problem", ["Classification", "Regression"])
    if st.button("Train Model"):
        X = data[features]
        y = data[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        if problem_type == "Classification":
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            st.write("Accuracy:", accuracy_score(y_test, preds))
        else:
            model = RandomForestRegressor()
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            st.write("Mean Squared Error:", mean_squared_error(y_test, preds))

        # Save model and features for prediction
        st.session_state["model"] = model
        st.session_state["features"] = features

# --- Try the Trained Model ---
if "model" in st.session_state and "features" in st.session_state:
    st.header("Test Your Model")
    test_input = {}
    for f in st.session_state["features"]:
        val = st.text_input(f"Enter {f} for prediction")
        test_input[f] = float(val) if val else 0
    if st.button("Predict"):
        X_pred = pd.DataFrame([test_input])
        prediction = st.session_state["model"].predict(X_pred)[0]
        st.write(f"Prediction: {prediction}")
