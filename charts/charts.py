import plotly.express as px
import pandas as pd

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



def assistance_by_ip (df):
    donor_count =(
        df.groupby("implementing_partner")["assistance_value_usd"]
        .sum()
        .reset_index()
    )

    fig = px.pie (
        donor_count,
        names = "implementing_partner",
        values= "assistance_value_usd",
        title="Assistance by Implementing Partner",

    )

    return fig


def assistance_by_sector (df):
    sector_count =(
        df.groupby("sector")["assistance_value_usd"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        sector_count,
        names = "sector",
        values= "assistance_value_usd",
        title="Assistance by Sector",
    )

    return fig


# ----------------------------------------------------
# Average Charts:
# ----------------------------------------------------
def average_satisfaction_by_province (df):
    satisfaction_count = (
        df.groupby("province")["satisfaction_level"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        satisfaction_count,
        x="province",
        y="satisfaction_level",
        title="Satisfaction by Province",
    )

    return fig

def average_hh_by_province(df):
    hh_count = (
        df.groupby("province")["household_size"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        hh_count,
        x="province",
        y="household_size",
        title="Household by Province",
    )

    return fig

def average_food_security_score_by_province (df):
    security_count = (
        df.groupby("province")["food_security_score"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        security_count,
        x="province",
        y="food_security_score",
        title="Food Security by Province",
    )

    return fig

def average_wash_access_score_by_province (df):
    wash_score_count = (
        df.groupby("province")["wash_access_score"]
        .mean()
        .reset_index()

    )

    fig = px.bar(
        wash_score_count,
        x="province",
        y="wash_access_score",
        title="Wash Access by Province",

    )

    return fig

# ----------------------------------------------------
# Trends Charts:
# ----------------------------------------------------

def assessments_by_month(df):

    df["assessment_date"] = pd.to_datetime(df["assessment_date"])

    df["month"] = df["assessment_date"].dt.to_period("M").astype(str)

    monthly_assessments = (
        df.groupby("month")
          .size()
          .reset_index(name="assessments")
    )

    fig = px.line(
        monthly_assessments,
        x="month",
        y="assessments",
        title="Household Assessments by Month",
        markers=True
    )

    return fig


def total_assistance_by_month(df):
    df["assessment_date"] = pd.to_datetime(df["assessment_date"])
    df["month"] = df["assessment_date"].dt.to_period("M").astype(str)

    total_monthly_assessments_value = (
        df.groupby("month")["assistance_value_usd"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        total_monthly_assessments_value,
        x="month",
        y="assistance_value_usd",
        title="Total Assistance by Month",
        markers=True
    )

    return fig


def avg_satisfaction_by_month(df):
    df["assessment_date"] = pd.to_datetime(df["assessment_date"])
    df["month"] = df["assessment_date"].dt.to_period("M").astype(str)

    satisfaction_by_month = (
        df.groupby("month")["satisfaction_level"]
        .mean()
        .reset_index()

    )

    fig  = px.line (
        satisfaction_by_month,
        x="month",
        y="satisfaction_level",
        title="Satisfaction by Month",
        markers=True

    )

    return fig