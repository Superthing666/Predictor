# ⏳ Time Pattern Engine 3.0

A powerful Streamlit-based tool for analyzing, predicting, and detecting anomalies in time-series biomedical or signal data using LSTM neural networks.

---

### 🚀 Features

- 📈 **Signal Visualization**: Upload and preview your time-series or biomedical signals.
- 🔮 **LSTM-Based Prediction**: Train a simple LSTM model to forecast signal patterns.
- ⚠️ **Anomaly Detection**: Identify abnormal signal patterns using standard deviation thresholds.
- 🧭 **User-Friendly Interface**: Clean UI with tabs, sliders, and live plots.
- 📦 **Streamlit Cloud Ready**: Just upload and deploy from GitHub!

---

### 📁 File Structure

```
time_pattern_engine/
├── app.py                 # Streamlit app with upgraded engine & UI
├── requirements.txt       # Clean dependencies list for Streamlit Cloud
```

---

### 🛠️ Setup & Deployment

#### ✅ Option 1: Run Locally
1. Clone this repo:
   ```bash
   git clone https://github.com/Superthing666/Dinosaur.git
   cd Dinosaur
   ```
2. Create a virtual environment and install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

#### 🚀 Option 2: Deploy on [Streamlit Cloud](https://streamlit.io/cloud)
1. Upload all files (`app.py`, `requirements.txt`) to a **public GitHub repo**
2. Create a new app on Streamlit Cloud:
   - **Repo:** Superthing666/Dinosaur
   - **Main file:** `app.py`
3. Click **Deploy** and wait for the app to spin up

---

### 📤 Input Data Format

- Upload a `.csv` file containing time-series or biomedical signals.
- Ensure there’s **at least one numeric column** (e.g., ECG, EEG, heart rate, etc.)

Example:

| time | signal |
|------|--------|
| 0.0  | 0.12   |
| 0.1  | 0.15   |
| 0.2  | 0.22   |

---

### 💡 Coming Soon

- 🔬 Real-time wearable data support
- 🧠 Predictive health risk modeling
- 🧬 Integration with large biomedical datasets

---

### 📜 License

MIT — free to use, modify, and share.

---

### 🧑‍🔬 Author

Built with curiosity by Superthing666  
Inspired by the idea of understanding time through signal patterns.