import streamlit as st
import pandas as pd
from analyzer import *
from rules import *
from data_generator import generate_cloud_data

st.set_page_config(page_title="Cloud FinOps Dashboard", layout="wide")

st.title("Cloud FinOps Analyzer")
if st.button("Generate New Cloud Data"):
    generate_cloud_data()
    st.success("New cloud data generated. Refresh dashboard.")
df = load_data()

col1,col2,col3 = st.columns(3)

col1.metric("Total Cost", "$"+str(total_cost(df)))
col2.metric("Total Resources", len(df))
col3.metric("Idle Resources", len(idle_resources(df)))

st.subheader("Cost by Service")
st.bar_chart(service_cost(df))

st.subheader("Daily Cloud Spend")
st.line_chart(daily_cost(df))

st.subheader("Idle Resources")
st.write(idle_resources(df))

st.subheader("Optimization Suggestions")
suggestions = detect_idle(df)
if suggestions:
    suggestions_df = pd.DataFrame(suggestions)
    st.table(suggestions_df)
else:
    st.write("No optimization suggestions found")

st.subheader("Cost Anomaly Detection")
spikes = detect_cost_spike(df)
if spikes:
    spikes_df = pd.DataFrame(spikes)
    st.table(spikes_df)
else:
    st.success("No cost anomalies detected")