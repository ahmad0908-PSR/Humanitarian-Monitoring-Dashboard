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

    return filtered_df

