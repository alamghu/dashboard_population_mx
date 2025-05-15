#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import io
import geopandas as gpd
import numpy as np
import json
import plotly.graph_objects as go
import plotly.io as pio
import altair_viewer as altviewer
import logging


# Page configuration
st.set_page_config(
    page_title="End to End Tracker",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

#######################
# Sample Data Preparation
data = [
    {'Well ID': 'Well-1', 'Process Step': 'Handover UWO to GGO', 'Start Date': '2025-05-01', 'End Date': '2025-05-03', 'Status': 'Completed', 'KPI': 3},
    {'Well ID': 'Well-1', 'Process Step': 'SCMT Execution', 'Start Date': '2025-05-04', 'End Date': '2025-05-06', 'Status': 'Ongoing', 'KPI': 2},
    {'Well ID': 'Well-1', 'Process Step': 'Mechanical Completion', 'Start Date': '2025-05-07', 'End Date': '2025-05-10', 'Status': 'Pending', 'KPI': 5},
    {'Well ID': 'Well-2', 'Process Step': 'Handover UWO to GGO', 'Start Date': '2025-05-01', 'End Date': '2025-05-02', 'Status': 'Completed', 'KPI': 1},
    {'Well ID': 'Well-2', 'Process Step': 'SCMT Execution', 'Start Date': '2025-05-03', 'End Date': '2025-05-05', 'Status': 'Ongoing', 'KPI': 4}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Sidebar Filters
st.sidebar.title("Well and Process Filters")
selected_well = st.sidebar.selectbox("Select Well ID", df['Well ID'].unique())
selected_status = st.sidebar.selectbox("Select Process Status", df['Status'].unique())

# Filter Data
filtered_df = df[(df['Well ID'] == selected_well) & (df['Status'] == selected_status)]

# Dashboard Title
st.title("Well Process Tracking Dashboard")

# Display Data
st.subheader("Filtered Data")
st.write(filtered_df)

# Visualization
st.subheader("KPI Analysis")
fig = px.bar(filtered_df, x='Process Step', y='KPI', color='Status', title=f"KPI Analysis for {selected_well}")
st.plotly_chart(fig)
