import streamlit as st
import pandas as pd
import joblib


model = joblib.load("mobile_price_model.pkl")

st.set_page_config(page_title="Mobile Price Predictor", layout="wide")

st.title("📱 Mobile Price Range Predictor")
st.write("Predict whether a mobile phone is Low, Medium, High, or Very High cost.")


st.sidebar.header("📡 Features (Yes / No)")

def yes_no(label):
    return 1 if st.sidebar.selectbox(label, ["No", "Yes"]) == "Yes" else 0

blue = yes_no("Bluetooth")
dual_sim = yes_no("Dual SIM")
four_g = yes_no("4G")
three_g = yes_no("3G")
touch_screen = yes_no("Touch Screen")
wifi = yes_no("WiFi")

st.header("🔋 Performance")

battery_power = st.slider("Battery Power (mAh)", 500, 2000, 1000)
clock_speed = st.slider("Clock Speed (GHz)", 0.5, 3.5, 1.5)
n_cores = st.slider("CPU Cores", 1, 8, 4)
ram = st.slider("RAM (MB)", 256, 8000, 2000)
talk_time = st.slider("Talk Time (hours)", 2, 30, 10)

st.header("📷 Camera")

fc = st.slider("Front Camera (MP)", 0, 20, 5)
pc = st.slider("Primary Camera (MP)", 0, 50, 12)

st.header("💾 Storage & Display")

int_memory = st.slider("Internal Memory (GB)", 2, 256, 64)
px_height = st.slider("Pixel Height", 200, 2000, 800)
px_width = st.slider("Pixel Width", 200, 2000, 1200)
sc_h = st.slider("Screen Height (cm)", 5, 20, 12)
sc_w = st.slider("Screen Width (cm)", 3, 15, 7)

st.header("⚙️ Physical Specs")

m_dep = st.slider("Mobile Depth (cm)", 0.1, 1.0, 0.5)
mobile_wt = st.slider("Weight (g)", 80, 250, 150)


sample = pd.DataFrame([{
    "battery_power": battery_power,
    "blue": blue,
    "clock_speed": clock_speed,
    "dual_sim": dual_sim,
    "fc": fc,
    "four_g": four_g,
    "int_memory": int_memory,
    "m_dep": m_dep,
    "mobile_wt": mobile_wt,
    "n_cores": n_cores,
    "pc": pc,
    "px_height": px_height,
    "px_width": px_width,
    "ram": ram,
    "sc_h": sc_h,
    "sc_w": sc_w,
    "talk_time": talk_time,
    "three_g": three_g,
    "touch_screen": touch_screen,
    "wifi": wifi
}])


price_labels = {
    0: "💰 Low Cost",
    1: "💰💰 Medium Cost",
    2: "💰💰💰 High Cost",
    3: "💎 Very High Cost"
}

st.markdown("---")

if st.button("🚀 Predict Price"):
    prediction = model.predict(sample)[0]
    st.success(f"Predicted Price Range: {price_labels[prediction]}")