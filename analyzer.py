import pandas as pd

def load_data():
    df = pd.read_csv("data/cloud_cost.csv")
    return df

def total_cost(df):
    return df["cost"].sum()

def service_cost(df):
    return df.groupby("service")["cost"].sum()

def idle_resources(df):
    return df[df["cpu_usage"] < 5]

def daily_cost(df):
    return df.groupby("day")["cost"].sum()