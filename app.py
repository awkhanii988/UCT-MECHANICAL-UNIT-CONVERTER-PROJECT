import streamlit as st

# Title
st.title("⚙️ Mechanical Unit Converter")

# Unit categories
categories = {
    "Force": {
        "units": {"Newton": 1, "Kilonewton": 1000, "Pound-force": 4.44822}
    },
    "Pressure": {
        "units": {"Pascal": 1, "Bar": 100000, "PSI": 6894.76}
    },
    "Energy": {
        "units": {"Joule": 1, "Kilojoule": 1000, "Calorie": 4.184, "BTU": 1055.06}
    },
    "Power": {
        "units": {"Watt": 1, "Kilowatt": 1000, "Horsepower": 745.7}
    },
    "Torque": {
        "units": {"Newton-meter": 1, "Pound-foot": 1.35582}
    },
    "Length": {
        "units": {"Meter": 1, "Millimeter": 0.001, "Centimeter": 0.01, "Inch": 0.0254, "Foot": 0.3048}
    }
}

# Select category
category = st.selectbox("Select Category", list(categories.keys()))

# Select units
from_unit = st.selectbox("From Unit", list(categories[category]["units"].keys()))
to_unit = st.selectbox("To Unit", list(categories[category]["units"].keys()))

# Input value
value = st.number_input("Enter value", min_value=0.0, format="%.6f")

# Conversion
if st.button("Convert"):
    base_value = value * categories[category]["units"][from_unit]
    converted_value = base_value / categories[category]["units"][to_unit]
    st.success(f"{value} {from_unit} = {converted_value:.6f} {to_unit}")
