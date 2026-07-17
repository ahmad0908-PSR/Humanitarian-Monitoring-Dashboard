import plotly.express as px

# ----------------------------------------------------
# Distribution Charts:
# ----------------------------------------------------
def households_by_province(df):

    province_count = (
        df.groupby("province")
        .size()
        .reset_index(name="households")

    )

    fig = px.bar(
        province_count,
        x="province",
        y="households",
        title="Households by Province",
    )

    return fig


def households_by_gender(df):
    gender_count = (
        df.groupby("gender_head")
        .size()
        .reset_index(name="households")

    )

    fig = px.bar(
        gender_count,
        x="gender_head",
        y="households",
        title="Households by Gender",
    )

    return fig


def households_by_sector(df):
    sector_count = (
        df.groupby("sector")
        .size()
        .reset_index(name="households")

    )

    fig = px.bar (
        sector_count,
        x="sector",
        y="households",
        title="Households by Sector",
    )

    return fig

def households_by_survey_round(df):
    survey_round_count = (
        df.groupby("survey_round")
        .size()
        .reset_index(name="households")
    )

    fig = px.bar (
        survey_round_count,
        x="survey_round",
        y="households",
        title="Households by Survey Rounds",

    )

    return fig



# ----------------------------------------------------
# Totals Charts:
# ----------------------------------------------------
def assistance_by_province(df):
    assistance_sum = (
        df.groupby("province")["assistance_value_usd"]
        .sum()
        .reset_index()

    )

    fig = px.pie (
        assistance_sum,
        names = "province",
        values= "assistance_value_usd",
        title="Assistance by Province",
        hole=0.5,
    )

    return fig


