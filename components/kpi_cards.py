import streamlit as st

# ----------------------------------------------------
# KPI CARDS
# ----------------------------------------------------
def display_kpi_cards(
        total_households,
        total_provinces,
        total_assistance,
        average_satisfaction,
):


    with st.container():

        st.subheader("📌 Key Performance Indicators")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Households",
                      f"{total_households:,}"
            )

        with col2:
            st.metric("Provinces",
                      f"{total_provinces:,}"
            )

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
