import streamlit as st

from utils.filters import apply_filters
from utils.load_data import load_data
from utils.calculations import (
    get_total_households,
    get_total_provinces,
    get_total_assistance,
    get_average_satisfaction,
)

# ----------------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------------

st.set_page_config(
    page_title="Humanitarian Monitoring Dashboard",
    page_icon="📊",
    layout="wide"
)

# ----------------------------------------------------
# LOAD DATA
# ----------------------------------------------------

df = load_data()

# filters

filtered_df = apply_filters(df)
# ----------------------------------------------------
# KPI CALCULATIONS
# ----------------------------------------------------

total_households = get_total_households(filtered_df)
total_provinces = get_total_provinces(filtered_df)
total_assistance = get_total_assistance(filtered_df)
average_satisfaction = get_average_satisfaction(filtered_df)

# ----------------------------------------------------
# PAGE TITLE
# ----------------------------------------------------

st.title("📊 Humanitarian Monitoring Dashboard")
st.success("Dataset loaded successfully!")

# ----------------------------------------------------
# KPI CARDS
# ----------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Households", total_households)

with col2:
    st.metric("Provinces", total_provinces)

with col3:
    st.metric(
        "Total Assistance",
        f"${total_assistance:,.0f}"
    )

with col4:
    st.metric(
        "Avg Satisfaction",
        f"{average_satisfaction:.1f}"
    )

# ----------------------------------------------------
# DATA INFORMATION
# ----------------------------------------------------

st.write(f"Rows: {filtered_df.shape[0]}")
st.write(f"Columns: {filtered_df.shape[1]}")

# ----------------------------------------------------
# DATA TABLE
# ----------------------------------------------------

st.dataframe(
    filtered_df,
    width="stretch"
)