import streamlit as st
import pandas as pd
from datetime import date
import os

st.title("Daily Reporting App")

# Initialize CSV file
CSV_FILE = "daily_reports.csv"

# Form inputs
with st.form("report_form"):
    st.subheader("Daily Reporting")
    report_date = st.date_input("Date", date.today())
    pu_code = st.text_input("PU Code")
    ffs_present = st.number_input("Number of FFs present", min_value=0)

    st.subheader("Training Record")
    farmer_sessions = st.number_input("Number of Farmers training sessions conducted", min_value=0)
    farmers_participated = st.number_input("Number of Farmers participated in sessions", min_value=0)
    worker_sessions = st.number_input("Number of Workers (Men) training sessions conducted", min_value=0)
    workers_participated = st.number_input("Number of Workers participated in sessions", min_value=0)

    st.subheader("Adoption Data")
    adoption_data = st.number_input("Number of Farmers adoption data updated on app", min_value=0)

    st.subheader("Capacity Building Records")
    month = st.text_input("Month")
    training_sessions_updated = st.number_input("Number of Training sessions updated on app", min_value=0)

    st.subheader("FFB Data")
    ffb_data = st.number_input("Number farmers FFB data checked and updated", min_value=0)

    st.subheader("Picking Data")
    picking_info = st.number_input("Number of farmers picking information updated", min_value=0)
    harvested_area = st.number_input("Harvested Cotton Area", min_value=0.0)
    seed_cotton = st.number_input("Total seed cotton harvested (KGs)", min_value=0.0)

    st.subheader("Other Activities")
    activity1 = st.text_input("Activity 1")
    activity2 = st.text_input("Activity 2")
    activity3 = st.text_input("Activity 3")

    submitted = st.form_submit_button("Submit Report")

if submitted:
    data = {
        "Date": [report_date],
        "PU Code": [pu_code],
        "FFs Present": [ffs_present],
        "Farmer Sessions": [farmer_sessions],
        "Farmers Participated": [farmers_participated],
        "Worker Sessions": [worker_sessions],
        "Workers Participated": [workers_participated],
        "Adoption Data": [adoption_data],
        "Month": [month],
        "Training Sessions Updated": [training_sessions_updated],
        "FFB Data": [ffb_data],
        "Picking Info": [picking_info],
        "Harvested Area": [harvested_area],
        "Seed Cotton": [seed_cotton],
        "Activity1": [activity1],
        "Activity2": [activity2],
        "Activity3": [activity3]
    }
    df = pd.DataFrame(data)
    if os.path.exists(CSV_FILE):
        df.to_csv(CSV_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(CSV_FILE, index=False)
    st.success("Report submitted successfully!")

# Show existing data
if os.path.exists(CSV_FILE):
    st.subheader("Submitted Reports")
    st.dataframe(pd.read_csv(CSV_FILE))
