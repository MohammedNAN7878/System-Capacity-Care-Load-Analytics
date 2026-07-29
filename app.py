import streamlit as st
import pandas as pd
import plotly.express as px
import os

from preprocessing import load_and_structure_data, validate_data
from metrics import compute_metrics
from forecasting import forecast_load


# Page Configuration
st.set_page_config(
    page_title="UAC Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# CSS Styling
st.markdown("""
<style>
.stApp { background-color: #F4F7FB; }
.block-container { padding-top: 1rem; padding-bottom: 2rem; }
h1 { color: #0A3D62; font-weight: 700; }
h2, h3 { color: #003366; font-weight: 600; }
section[data-testid="stSidebar"] { background-color: #0A3D62; color: white; }
section[data-testid="stSidebar"] label { color: #FFFFFF !important; }
section[data-testid="stSidebar"] div[data-testid="stCheckbox"] label { color: #EAF4FF !important; font-weight: 600; }
section[data-testid="stSidebar"] .stSelectbox label { color: #FFFFFF !important; }
section[data-testid="stSidebar"] .stDateInput label { color: white; }
section[data-testid="stSidebar"] h2 { color: white; }
section[data-testid="stSidebar"] div[data-baseweb="select"] span { color: black !important; }
section[data-testid="stSidebar"] div[data-baseweb="select"] > div { background-color: white !important; color: black !important; }
div[role="listbox"] div { color: black !important; }
section[data-testid="stSidebar"] input { color: black !important; background-color: white !important; }
section[data-testid="stSidebar"] h3 { color: #FFFFFF !important; font-weight: 700; }
[data-testid="metric-container"] { background: white; border-radius: 16px; padding: 20px; box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08); border-left: 6px solid #0A3D62; }
[data-testid="stMetricLabel"] { justify-content: center; }
button[role="tab"] { font-weight: 600; color: #0A3D62; }
button[role="tab"][aria-selected="true"] { border-bottom: 3px solid #0A3D62; color: #003366; }
.stPlotlyChart { background-color: white; padding: 10px; border-radius: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.06); }
@media (max-width: 768px) { h1 { font-size: 22px !important; } h2 { font-size: 18px !important; } .block-container { padding: 1rem !important; } [data-testid="metric-container"] { padding: 12px !important; } }
footer { visibility: hidden; }
section[data-testid="stSidebar"] div[data-testid="stCheckbox"] p { color: #EAF4FF !important; font-weight: 600 !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background-color:#0A3D62; padding:18px; border-radius:14px; color:white; text-align:center; font-size:18px; font-weight:500; margin-top:25px; margin-bottom:15px; box-shadow: 0 6px 18px rgba(0,0,0,0.08);">
    🌍 Real-Time Care System Capacity Monitoring & Forecasting
</div>
""", unsafe_allow_html=True)

# Header Section
col_logo, col_title = st.columns([1, 4], gap="small")

with col_logo:
    logo1_path = os.path.join("assets", "unified_mentor_logo_2.png")
    logo2_path = os.path.join("assets", "hhs_logo.png")
    if os.path.exists(logo1_path):
        st.image(logo1_path, width=200)
    if os.path.exists(logo2_path):
        st.image(logo2_path, width=160)

with col_title:
    st.title("UAC Analytics Dashboard")
    st.markdown("""
    **Developed By:** Arqam Shaikh  
    **Data Source:** U.S. Department of Health & Human Services (HHS)
    """)

st.markdown("---")

# Load & Process Data
df = load_and_structure_data("data/HHS_Unaccompanied_Alien_Children_Program.csv")
df = validate_data(df)
df = compute_metrics(df)

# Sidebar Filters
st.sidebar.markdown("## 📌 Dashboard Controls")
st.sidebar.markdown("---")

start_date = st.sidebar.date_input("Start Date", df.index.min())
end_date = st.sidebar.date_input("End Date", df.index.max())

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Metric Toggles")

show_system_load = st.sidebar.checkbox("Total System Load", True)
show_cbp_hhs = st.sidebar.checkbox("CBP vs HHS Comparison", True)
show_intake_backlog = st.sidebar.checkbox("Net Intake & Backlog", True)

st.sidebar.markdown("---")
st.sidebar.markdown("### ⏱ Time Granularity")

granularity = st.sidebar.selectbox(
    "Select Time Aggregation",
    ["Daily", "Weekly", "Monthly"]
)

filtered_df = df.loc[start_date:end_date]
if granularity == "Weekly":
    filtered_df = filtered_df.resample("W").mean()
elif granularity == "Monthly":
    filtered_df = filtered_df.resample("M").mean()

# Tabs Layout
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Dashboard",
    "📈 Forecast",
    "✅ Validation",
    "ℹ️ About"
])

# TAB 1 — DASHBOARD
with tab1:
    st.markdown("## 📌 Key System Metrics Overview")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    col1.metric("Total Children Under Care", f"{int(filtered_df['Total_System_Load'].iloc[-1]):,}")
    col2.metric("Net Intake Pressure", f"{int(filtered_df['Net_Intake'].iloc[-1]):,}")
    col3.metric("Backlog Accumulation", f"{int(filtered_df['Cumulative_Backlog'].iloc[-1]):,}")
    col4.metric("Discharge Offset Ratio", round(filtered_df['Discharge_Offset_Ratio'].mean(), 2))

    st.markdown("---")

    if show_system_load:
        st.subheader("📈 Total System Load Over Time")
        fig = px.line(filtered_df, y='Total_System_Load', color_discrete_sequence=["#0A3D62"])
        fig.update_layout(height=500, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig, use_container_width=True)

    if show_cbp_hhs:
        st.subheader("📊 CBP vs HHS Load Comparison")
        fig2 = px.line(filtered_df, y=['CBP_Custody', 'HHS_Care'], color_discrete_sequence=["#1B9CFC", "#F39C12"])
        fig2.update_layout(height=500, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig2, use_container_width=True)

    if show_intake_backlog:
        st.subheader("📉 Net Intake & Backlog Trend")
        fig3 = px.line(filtered_df, y=['Net_Intake', 'Cumulative_Backlog'], color_discrete_sequence=["#E74C3C", "#2ECC71"])
        fig3.update_layout(height=500, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig3, use_container_width=True)

# TAB 2 — FORECAST
with tab2:
    st.subheader("🔮 60-Day Forecast of Total System Load")
    forecast = forecast_load(df)
    fig4 = px.line(forecast, x='ds', y='yhat', title='Forecasted Total System Load', color_discrete_sequence=["#8E44AD"])
    st.plotly_chart(fig4, use_container_width=True)
    st.markdown("""
    **Forecast Details:**
    - 60-day predictive model using Facebook Prophet
    - Captures seasonal trends and historical patterns
    - Helps with capacity planning and resource allocation
    """)

# TAB 3 — VALIDATION
with tab3:
    st.subheader("🛡 Data Validation Summary")
    transfer_issues = df['Transfer_Validation'].sum()
    discharge_issues = df['Discharge_Validation'].sum()
    col1, col2 = st.columns(2)
    col1.metric("Transfer Validation Checks Passed", int(transfer_issues))
    col2.metric("Discharge Validation Checks Passed", int(discharge_issues))
    st.markdown("""
    **Validation Logic Applied:**
    - ✅ Transfers must not exceed children in CBP custody
    - ✅ Discharges must not exceed children in HHS care
    - ✅ Data integrity checks for all metrics
    - ✅ Outlier detection and anomaly flagging
    """)

# TAB 4 — ABOUT PROJECT
with tab4:
    st.subheader("📋 About This Dashboard")
    st.markdown("""
    ### Project Overview
    This interactive analytics dashboard provides real-time insights into the 
    **U.S. Unaccompanied Alien Children (UAC) Care System** operated by the 
    Department of Health & Human Services (HHS).
    
    ### Key Features
    ✅ **Real-Time Monitoring** - Track system capacity and care load  
    ✅ **Predictive Analytics** - 60-day forecasts using machine learning  
    ✅ **Data Validation** - Automated integrity checks on all metrics  
    ✅ **Multi-Timeframe Analysis** - Daily, Weekly, and Monthly views  
    ✅ **Interactive Visualizations** - Drill down into specific metrics  
    
    ### Technology Stack
    🐍 **Python** | 📊 **Pandas** | 📈 **Plotly** | 🔮 **Prophet**  
    🚀 **Streamlit** | 🤖 **Scikit-Learn** | ☁️ **Cloud Deployment**
    """)

    st.markdown("---")
    st.markdown("""
    ### 👨‍💻 Developer
    **Arqam Shaikh**  
    Data Analytics & Machine Learning Engineer  
    [GitHub](https://github.com/Arqam-Shaikh) | [LinkedIn](https://linkedin.com/in/arqam-shaikh)
    
    ### 📊 Data Source
    U.S. Department of Health & Human Services (HHS)  
    Unaccompanied Alien Children Program Dataset
    """)

# Footer
st.markdown("---")

footer = """
<div style='text-align:center; font-size:13px; color:gray; line-height:1.8;'>

<strong>🌐 System Capacity & Care Load Analytics Dashboard</strong><br>
<strong>Developed by Arqam Shaikh</strong><br>
Data Source: U.S. Department of Health & Human Services (HHS)<br><br>

<a href='https://system-capacity-care-load-analytics-c6cgxbhdbv4rz6v9y9fnnm.streamlit.app/'
target='_blank'
style='color:#0A3D62; text-decoration:none;'>
<strong>🚀 Live Dashboard</strong>
</a>

&nbsp; | &nbsp;

<a href='https://github.com/Arqam-Shaikh/System-Capacity-Care-Load-Analytics'
target='_blank'
style='color:#0A3D62; text-decoration:none;'>
<strong>💻 GitHub Repository</strong>
</a>

<br><br>

<strong>Built With</strong><br>
Python • Streamlit • Plotly • Prophet • Pandas • Scikit-Learn

<br><br>

<strong>Internship</strong><br>
Unified Mentor Internship Program

<br><br>

<strong>📬 Connect with Me</strong><br>

<a href='https://github.com/Arqam-Shaikh' target='_blank'>GitHub</a>
&nbsp; | &nbsp;
<a href='https://www.linkedin.com/in/arqam-shaikh-5196b4313/' target='_blank'>LinkedIn</a>

<br><br>

⭐ Thank you for visiting this dashboard!

</div>
"""

st.markdown(footer, unsafe_allow_html=True)