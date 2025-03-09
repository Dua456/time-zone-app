# Import required libraries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# Apply custom CSS for styling
st.markdown(
    """
    <style>
    .subheader {
        font-size: 32px;
        font-weight: bold;
        color: green;
    }
    .black-header {
        color: black;
        font-size: 24px;
        font-weight: bold;
    }
    .result-container {
        background-color: black;
        color: white;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        margin-bottom: 5px;
        font-size: 20px;
        font-weight: bold;
    }
    .timezone-container {
        text-align: center;
        font-weight: bold;
    }
    div[data-baseweb="select"] > div {
        background-color: black !important;
        color: white !important;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create app title
st.title("🕰️ Time Zone Converter")

# Create a multi-select dropdown for choosing time zones
selected_timezone = st.multiselect("", TIME_ZONES, default=["UTC", "Asia/Karachi"])

# Display current time for selected time zones
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.markdown(f'<div class="result-container"><b>{tz}</b>: {current_time}</div>', unsafe_allow_html=True)

# Create section for time conversion
st.markdown('<div style="font-size: 24px; font-weight: bold;">🔄 Convert Time Between Timezones </div>', unsafe_allow_html=True)

# Create time input field with current time as default
current_time = st.time_input("", value=datetime.now().time())  

# Dropdown to select source timezone
st.markdown('<p class="subheader">🌍 From Time Zone</p>', unsafe_allow_html=True)
from_tz = st.selectbox("", TIME_ZONES, index=0, key="from_tz")

# Dropdown to select target timezone
st.markdown('<p class="subheader">🎯 To Time Zone</p>', unsafe_allow_html=True)
to_tz = st.selectbox("", TIME_ZONES, index=1, key="to_tz")

# Convert button
if st.button("🔁 Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.markdown(
        f'<div class="result-container" style="font-size: 22px; font-weight: bold;">⏳ Converted Time in {to_tz}: {converted_time}</div>',
        unsafe_allow_html=True
    )
