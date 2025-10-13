import streamlit as st
import pandas as pd
import random
import time
import altair as alt

# ------------------ PAGE SETTINGS ------------------
st.set_page_config(page_title="Hospital Sensor Live Monitoring", layout="wide")

st.title("🏥 Advanced Hospital Sensor Live Monitoring")
st.write("Live simulation of Heart Rate, Temperature, and Blood Pressure with smooth color curves (updates every 2 seconds).")

REFRESH_EVERY_SECONDS = 2

# ------------------ INITIAL DATA SETUP ------------------
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Time", "Heart Rate", "Temperature", "Blood Pressure"])

if "run" not in st.session_state:
    st.session_state.run = False

# ------------------ BUTTON CONTROLS ------------------
col1, col2 = st.columns(2)
if col1.button("▶️ Start Monitoring"):
    st.session_state.run = True
if col2.button("⏹️ Stop Monitoring"):
    st.session_state.run = False

# ------------------ DATA GENERATION FUNCTION ------------------
def generate_data():
    t = time.strftime("%H:%M:%S")
    hr = random.randint(60, 110)
    temp = round(random.uniform(36.0, 38.5), 1)
    bp = random.randint(110, 140)

    new = pd.DataFrame([[t, hr, temp, bp]], columns=["Time", "Heart Rate", "Temperature", "Blood Pressure"])
    st.session_state.data = pd.concat([st.session_state.data, new]).tail(30)
    return hr, temp, bp

# ------------------ MAIN MONITORING LOOP ------------------
if st.session_state.run:
    hr, temp, bp = generate_data()

    # Display current metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("💓 Heart Rate (bpm)", hr)
    c2.metric("🌡️ Temperature (°C)", temp)
    c3.metric("🩸 Blood Pressure (mmHg)", bp)

    # Prepare data for chart
    df_melt = st.session_state.data.melt("Time", var_name="Sensor", value_name="Value")

    chart = (
        alt.Chart(df_melt)
        .mark_line(point=True)
        .encode(
            x=alt.X("Time", sort=None, axis=alt.Axis(labelAngle=-45)),
            y="Value",
            color=alt.Color("Sensor", scale=alt.Scale(range=["red", "orange", "blue"])),
            strokeWidth=alt.value(3)
        )
        .properties(height=400)
    )

    st.altair_chart(chart, use_container_width=True)
    st.info("🟢 Monitoring live... (updates every 2 seconds)")

    time.sleep(REFRESH_EVERY_SECONDS)
    st.rerun()

else:
    st.info("⏸️ Click ▶️ *Start Monitoring* to begin live simulation.")
