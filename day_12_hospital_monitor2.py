import streamlit as st
import random
import pandas as pd
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Multi-Patient Monitoring", layout="wide")
st.title("🏥 Multi-Patient Live Monitoring Dashboard")
st.write("Simulating live sensor data for multiple patients: Heart Rate, Temperature, Oxygen Level")

patients = ["Arun", "Meena", "John", "Priya", "Ravi"]

# --- Auto-refresh every 2 seconds ---
st_autorefresh(interval=2000, key="monitor_refresh")

# Initialize shared data in session_state
if "shared_data" not in st.session_state:
    st.session_state.shared_data = {p: {"hr": 0, "temp": 0, "ox": 0, "alert": ""} for p in patients}

# --- UI placeholders ---
placeholders = {}
for p in patients:
    placeholders[p] = {
        "container": st.container(),
        "hr_bar": None, "temp_bar": None, "ox_bar": None,
        "hr_text": None, "temp_text": None, "ox_text": None, "alert_text": None
    }
    with placeholders[p]["container"]:
        st.subheader(f"Patient: {p}")
        placeholders[p]["hr_bar"] = st.progress(0)
        placeholders[p]["temp_bar"] = st.progress(0)
        placeholders[p]["ox_bar"] = st.progress(0)
        placeholders[p]["hr_text"] = st.empty()
        placeholders[p]["temp_text"] = st.empty()
        placeholders[p]["ox_text"] = st.empty()
        placeholders[p]["alert_text"] = st.empty()

# --- Safe normalization ---
def safe_progress(value, min_val, max_val):
    norm = (value - min_val) / (max_val - min_val)
    return max(0.0, min(1.0, norm))

# --- Simulate sensor data and update UI ---
for p in patients:
    hr = random.randint(60, 110)
    temp = round(random.uniform(97, 101), 1)
    ox = random.randint(90, 100)

    alert_msg = ""
    if hr > 100:
        alert_msg += f"⚠️ HR High ({hr} bpm) "
    if temp > 100:
        alert_msg += f"🌡️ Temp High ({temp} °F) "
    if ox < 95:
        alert_msg += f"🩸 O2 Low ({ox}%)"

    st.session_state.shared_data[p] = {"hr": hr, "temp": temp, "ox": ox, "alert": alert_msg.strip()}

    placeholders[p]["hr_bar"].progress(safe_progress(hr, 60, 110))
    placeholders[p]["temp_bar"].progress(safe_progress(temp, 97, 101))
    placeholders[p]["ox_bar"].progress(safe_progress(ox, 90, 100))

    placeholders[p]["hr_text"].text(f"❤️ Heart Rate: {hr} bpm")
    placeholders[p]["temp_text"].text(f"🌡️ Temperature: {temp} °F")
    placeholders[p]["ox_text"].text(f"🩸 Oxygen Level: {ox}%")

    if alert_msg:
        placeholders[p]["alert_text"].error(alert_msg)
    else:
        placeholders[p]["alert_text"].success("🟢 All readings normal")
