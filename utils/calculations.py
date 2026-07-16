

# we calculate the total number of rows (households in the dataset):

def get_total_households(df):
    return len(df)

# we calculate the sum of unique provinces:

def get_total_provinces(df):
    return df["province"].nunique()

# we calculate the sum of total assistance:

def get_total_assistance(df):
    return df["assistance_value_usd"].sum()

# we calculate the average satisfaction:

def get_average_satisfaction(df):
    return df["satisfaction_level"].mean()