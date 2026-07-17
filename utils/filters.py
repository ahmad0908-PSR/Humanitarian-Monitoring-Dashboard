import streamlit as st

def apply_filters(df):
    """
    creates the sidebar filters and returns the filtered datafrome.

    """
    # this is the sidebar:
    st.sidebar.header("Filters:")


    # Province Options:
    province_options = ['All'] + sorted(df["province"].unique().tolist())
    # province drop down:
    selected_province = st.sidebar.selectbox("Province", province_options)
    # Filtering:
    if selected_province == "All":
        filtered_df = df
    else:
        filtered_df = df[df["province"] == selected_province]

    # District options created from the filtered_df:
    district_options = ["All"] + sorted(filtered_df["district"].unique().tolist())
    # District drop down:
    selected_district = st.sidebar.selectbox("District", district_options)
    # Filtering:
    if selected_district != "All":
        filtered_df = filtered_df[filtered_df["district"] == selected_district]

    # Survey Round options created from the df:
    survey_round_options = ["All"] + sorted(filtered_df["survey_round"].unique().tolist())
    # Survey Rond Drop Down:
    selected_survey_round = st.sidebar.selectbox("Survey Round", survey_round_options)
    # Filtering:
    if selected_survey_round == "All":
        filtered_df = filtered_df
    else:
        filtered_df = filtered_df[filtered_df["survey_round"] == selected_survey_round]

    # Gender Options:
    gender_option = ["All"] + sorted(filtered_df["gender_head"].unique().tolist())
    # Gender drop down:
    selected_gender = st.sidebar.selectbox("Gender", gender_option)
    # Filtering:
    if selected_gender == "All":
        filtered_df = filtered_df

    else:
        filtered_df = filtered_df[filtered_df["gender_head"] == selected_gender]


    # Donor Options:
    donor_options = ["All"] + sorted(filtered_df["donor"].unique().tolist())
    # donor dropdown:
    selected_donor = st.sidebar.selectbox("Donor", donor_options)
    # Filtering:
    if selected_donor == "All":
        filtered_df = filtered_df
    else:
        filtered_df = filtered_df[filtered_df["donor"] == selected_donor]

    return filtered_df

