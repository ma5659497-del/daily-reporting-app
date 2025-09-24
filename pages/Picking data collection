import streamlit as st
import pandas as pd
import os

st.title("Farmer Data Collection")

# Excel file to store data
DATA_FILE = "farmer_data.xlsx"

# Load existing data if file exists
if os.path.exists(DATA_FILE):
    df = pd.read_excel(DATA_FILE)
else:
    df = pd.DataFrame(columns=[
        "PP","PU Code","LG/Hub Code","Village","MF Code","Farmer Name","Father Name",
        "Farmer CNIC","Gender","Contact Number","Farmer DOB - Year","Education",
        "Farmer Date of joining","Sowing Date","Active/Inactive","Farmer Status","Farmer Continuity",
        "Total cultivable Land (ha)","Total Land under Cotton Production (ha)","Average Yield (kg/ha)",
        "Seed Cotton Sold 1 (KGs)","Date of Selling 1","Buyer Name 1","Buyer Contact 1",
        "Seed Cotton Sold 2 (KGs)","Date of Selling 2","Buyer Name 2","Buyer Contact 2",
        "Seed Cotton Sold 3 (KGs)","Date of Selling 3","Buyer Name 3","Buyer Contact 3",
        "Seed Cotton Sold 4 (KGs)","Date of Selling 4","Buyer Name 4","Buyer Contact 4",
        "Seed Cotton Sold 5 (KGs)","Date of Selling 5","Buyer Name 5","Buyer Contact 5",
        "Seed Cotton Sold 6 (KGs)","Date of Selling 6","Buyer Name 6","Buyer Contact 6",
        "Total Quantity Sold (KGs)"
    ])

with st.form("farmer_form", clear_on_submit=True):
    st.subheader("Basic Information")
    col1, col2, col3 = st.columns(3)
    with col1:
        pp = st.text_input("PP")
        pu_code = st.text_input("PU Code")
        lg_code = st.text_input("LG/Hub Code")
        village = st.text_input("Village")
        mf_code = st.text_input("MF Code")
    with col2:
        farmer_name = st.text_input("Farmer Name")
        father_name = st.text_input("Father Name")
        cnic = st.text_input("Farmer CNIC")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        contact = st.text_input("Contact Number")
    with col3:
        dob_year = st.number_input("Farmer DOB - Year", min_value=1900, max_value=2100, step=1)
        education = st.text_input("Education")
        joining_date = st.date_input("Farmer Date of Joining")
        sowing_date = st.date_input("Sowing Date")
        active = st.selectbox("Active/Inactive", ["Active", "Inactive"])
        status = st.text_input("Farmer Status")
        continuity = st.text_input("Farmer Continuity")

    st.subheader("Land & Yield Information")
    cultivable_land = st.number_input("Total cultivable Land (ha)", min_value=0.0, step=0.1)
    cotton_land = st.number_input("Total Land under Cotton Production (ha)", min_value=0.0, step=0.1)
    avg_yield = st.number_input("Average Yield (kg/ha)", min_value=0.0, step=1.0)

    st.subheader("Seed Cotton Transactions")
    transactions = []
    total_sold = 0
    for i in range(1, 7):
        st.markdown(f"**Transaction {i}**")
        sold = st.number_input(f"Seed Cotton Sold {i} (KGs)", min_value=0.0, step=1.0)
        date = st.date_input(f"Date of Selling {i}", key=f"date{i}")
        buyer = st.text_input(f"Buyer Name {i}", key=f"buyer{i}")
        buyer_contact = st.text_input(f"Buyer Contact {i}", key=f"buyer_contact{i}")
        transactions.extend([sold, date, buyer, buyer_contact])
        total_sold += sold

    submitted = st.form_submit_button("Save Farmer Data")

if submitted:
    new_row = {
        "PP": pp, "PU Code": pu_code, "LG/Hub Code": lg_code, "Village": village, "MF Code": mf_code,
        "Farmer Name": farmer_name, "Father Name": father_name, "Farmer CNIC": cnic,
        "Gender": gender, "Contact Number": contact, "Farmer DOB - Year": dob_year,
        "Education": education, "Farmer Date of joining": joining_date, "Sowing Date": sowing_date,
        "Active/Inactive": active, "Farmer Status": status, "Farmer Continuity": continuity,
        "Total cultivable Land (ha)": cultivable_land, "Total Land under Cotton Production (ha)": cotton_land,
        "Average Yield (kg/ha)": avg_yield,
        "Seed Cotton Sold 1 (KGs)": transactions[0], "Date of Selling 1": transactions[1],
        "Buyer Name 1": transactions[2], "Buyer Contact 1": transactions[3],
        "Seed Cotton Sold 2 (KGs)": transactions[4], "Date of Selling 2": transactions[5],
        "Buyer Name 2": transactions[6], "Buyer Contact 2": transactions[7],
        "Seed Cotton Sold 3 (KGs)": transactions[8], "Date of Selling 3": transactions[9],
        "Buyer Name 3": transactions[10], "Buyer Contact 3": transactions[11],
        "Seed Cotton Sold 4 (KGs)": transactions[12], "Date of Selling 4": transactions[13],
        "Buyer Name 4": transactions[14], "Buyer Contact 4": transactions[15],
        "Seed Cotton Sold 5 (KGs)": transactions[16], "Date of Selling 5": transactions[17],
        "Buyer Name 5": transactions[18], "Buyer Contact 5": transactions[19],
        "Seed Cotton Sold 6 (KGs)": transactions[20], "Date of Selling 6": transactions[21],
        "Buyer Name 6": transactions[22], "Buyer Contact 6": transactions[23],
        "Total Quantity Sold (KGs)": total_sold
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_excel(DATA_FILE, index=False)

    st.success(f"✅ Farmer data saved for {farmer_name}")

st.subheader("📋 Saved Farmer Records")
st.dataframe(df)
