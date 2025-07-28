
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# ------------------- Title ------------------- #
st.set_page_config(page_title="Signal Classifier Dashboard", layout="wide")
st.title("📊 Signal Classifier & Anomaly Detector")

# ------------------- Sidebar ------------------- #
st.sidebar.header("Upload & Settings")
uploaded_file = st.sidebar.file_uploader("Upload CSV file with signal data", type=["csv"])

# ------------------- Example Data ------------------- #
def generate_sample_data():
    np.random.seed(42)
    X = np.linspace(0, 10, 1000)
    signal = np.sin(X) + 0.1 * np.random.randn(1000)
    labels = (signal > 0).astype(int)
    df = pd.DataFrame({"time": X, "signal": signal, "label": labels})
    return df

# ------------------- Load or Generate Data ------------------- #
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = generate_sample_data()
    st.sidebar.info("Using example data. Upload your own to replace it.")

# ------------------- Visualization ------------------- #
st.subheader("📈 Signal Overview")
st.line_chart(df[["signal"]])

# ------------------- Anomaly Detection ------------------- #
st.subheader("🚨 Anomaly Detection")
threshold = st.slider("Z-score threshold", min_value=1.0, max_value=5.0, value=2.5)
df['z_score'] = (df['signal'] - df['signal'].mean()) / df['signal'].std()
df['anomaly'] = (np.abs(df['z_score']) > threshold).astype(int)
st.write("Detected Anomalies (in red):")

fig, ax = plt.subplots(figsize=(10, 3))
ax.plot(df['time'], df['signal'], label='Signal')
ax.scatter(df['time'][df['anomaly'] == 1], df['signal'][df['anomaly'] == 1], color='red', label='Anomaly')
ax.legend()
st.pyplot(fig)

# ------------------- Classification ------------------- #
st.subheader("🧠 Signal Classification")
features = ['signal']

X = df[features]
y = df['label'] if 'label' in df.columns else (df['signal'] > 0).astype(int)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

st.write("Classification Report:")
st.text(classification_report(y_test, y_pred))

st.write("Confusion Matrix:")
st.write(confusion_matrix(y_test, y_pred))
