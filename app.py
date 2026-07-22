import streamlit as st

from charts.charts import ( households_by_province,
                            households_by_gender,
                            households_by_sector,
                            households_by_survey_round,
                            assistance_by_province,
                            assistance_by_sector,
                            assistance_by_ip,
                            average_satisfaction_by_province,
                            average_hh_by_province,
                            average_food_security_score_by_province,
                            average_wash_access_score_by_province,
                            assessments_by_month,
                            total_assistance_by_month, avg_satisfaction_by_month

                            )
from utils.filters import apply_filters
from utils.load_data import load_data
from utils.calculations import (
    get_total_households,
    get_total_provinces,
    get_total_assistance,
    get_average_satisfaction,
)
from components.kpi_cards import display_kpi_cards


# ----------------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------------

st.set_page_config(
    page_title="Humanitarian Monitoring Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# LOAD DATA
# ----------------------------------------------------

df = load_data()

# filters

filtered_df = apply_filters(df)
# ----------------------------------------------------
# KPI CALCULATIONS, now they use filtered_df instead of df
# ----------------------------------------------------

total_households = get_total_households(filtered_df)
total_provinces = get_total_provinces(filtered_df)
total_assistance = get_total_assistance(filtered_df)
average_satisfaction = get_average_satisfaction(filtered_df)

# ----------------------------------------------------
# PAGE TITLE
# ----------------------------------------------------

st.title("🌍 MEAL International Dashobard")

st.markdown(
    """
    This dashboard provides monitoring insights from humanitarian interventions,
    including household demographics, assistance distribution,
    beneficiary satisfaction, and outcome trends.
    """
)

st.success("Dataset loaded successfully!")


# ----------------------------------------------------
# Displaying KPI cards:
# ----------------------------------------------------

display_kpi_cards(
    total_households,
    total_provinces,
    total_assistance,
    average_satisfaction
)



tab_analysis, tab_trends, tab_data = st.tabs(
    [
        "📊 Analysis",
        "⏳ Trends",
        "📋 Data"
    ]
)


with tab_analysis:

    # ----------------------------------------------------
    # Distribution Charts:
    # ----------------------------------------------------
    st.divider()
    with st.container():
        st.subheader("📊 Distribution Analysis")

        province_fig = households_by_province(filtered_df)
        gender_fig = households_by_gender(filtered_df)

        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(
                province_fig,
                width="stretch"
            )

        with col2:
            st.plotly_chart(
                gender_fig,
                width="stretch"
            )

        sector_fig = households_by_sector(filtered_df)
        survey_round_fig = households_by_survey_round(filtered_df)

        col1, col2 = st.columns(2)

        with col1:
            st.plotly_chart(
                sector_fig,
                width="stretch"
            )

        with col2:
            st.plotly_chart(
                survey_round_fig,
                width="stretch"
            )


    # ----------------------------------------------------
    # Totals Charts:
    # ----------------------------------------------------
    st.divider()
    with st.container():

        st.subheader("💰 Assistance Analysis")

        assistance_province = assistance_by_province(filtered_df)
        assistance_ip = assistance_by_ip(filtered_df)
        assistance_setor = assistance_by_sector(filtered_df)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.plotly_chart(
                assistance_province,
                width="stretch"
            )

        with col2:
            st.plotly_chart(
                assistance_ip,
                width="stretch"
            )

        with col3:
            st.plotly_chart(
                assistance_setor,
                width="stretch"

            )



    # ----------------------------------------------------
    # Average Charts:
    # ----------------------------------------------------
    st.divider()
    with st.container():
        st.subheader("📈 Average Indicators")

        avg_satisfaction = average_satisfaction_by_province(filtered_df)
        avg_hh = average_hh_by_province(filtered_df)
        avg_wash = average_wash_access_score_by_province(filtered_df)
        avg_food = average_food_security_score_by_province(filtered_df)


        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.plotly_chart(
                avg_satisfaction,
                width="stretch"
            )

        with col2:
            st.plotly_chart(
                avg_hh,
                width="stretch"
            )

        with col3:
            st.plotly_chart(
                avg_wash,
                width="stretch"
            )

        with col4:
            st.plotly_chart(
                avg_food,
                width="stretch"
            )



with tab_trends:
    # ----------------------------------------------------
    # Trend Charts:
    # ----------------------------------------------------
    st.divider()
    with st.container():
        st.subheader("⏳ Time Trends")

        month_assess = assessments_by_month(filtered_df)
        total_assess = total_assistance_by_month(filtered_df)
        avg_satisfaction_month = avg_satisfaction_by_month(filtered_df)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.plotly_chart(
                month_assess,
                width="stretch"

            )


        with col2:
            st.plotly_chart(
                total_assess,
                width="stretch"
            )


        with col3:
            st.plotly_chart(
                avg_satisfaction_month,
                width="stretch"

            )


with tab_data:
    # ----------------------------------------------------
    # DATA INFORMATION
    # ----------------------------------------------------

    st.write(f"Rows: {filtered_df.shape[0]}")
    st.write(f"Columns: {filtered_df.shape[1]}")

    # ----------------------------------------------------
    # DATA TABLE
    # ----------------------------------------------------
    st.divider()
    with st.container():
        st.subheader("📋 Filtered Dataset")
        st.dataframe(
            filtered_df,
            width="stretch"
        )