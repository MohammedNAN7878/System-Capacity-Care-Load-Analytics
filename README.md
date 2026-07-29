# 📊 System Capacity & Care Load Analytics for Unaccompanied Children

## 📌 Overview

This project presents a **data-driven healthcare analytics framework** for monitoring system capacity and care load within the **Unaccompanied Alien Children (UAC) Program** administered by the **U.S. Department of Health and Human Services (HHS)**.

The dashboard analyzes daily operational data to provide insights into:

- 📈 Total system load
- 🔄 Inflow vs. outflow balance
- ⚠️ Capacity stress periods
- 📊 Backlog accumulation
- 🔮 Future care load forecasting

An interactive **Streamlit Dashboard** enables real-time monitoring, visualization, and decision support.

---

# 🎯 Objectives

## Primary Objectives

- Quantify daily and cumulative care load across CBP and HHS
- Identify periods of system stress and relief
- Analyze intake, transfers, and discharge trends

## Secondary Objectives

- Support healthcare staffing and shelter planning
- Improve operational awareness
- Enable data-driven humanitarian decision-making

---

# 📂 Dataset Description

The dataset contains daily records (2023–2025) of the UAC care pipeline.

| Column | Description |
|---------|-------------|
| Date | Reporting Date |
| Children Apprehended | Daily intake into CBP |
| Children in CBP Custody | Active CBP load |
| Children Transferred | Flow into HHS |
| Children in HHS Care | Active HHS load |
| Children Discharged | Sponsor placements |

---

# ⚙️ Methodology

## 1️⃣ Data Preprocessing

- Date conversion and sorting
- Missing value handling
- Logical validation
- Data integrity checks

## 2️⃣ Feature Engineering

Derived metrics include:

- Total System Load
- Net Daily Intake
- Growth Rate
- Cumulative Backlog
- Discharge Offset Ratio

## 3️⃣ Trend Analysis

- Daily trends
- Weekly trends
- Monthly trends
- Rolling averages
- Seasonal patterns

## 4️⃣ Forecasting

- 60-Day Forecast
- Prophet Time-Series Model
- Capacity Planning

---

# 📈 Key Performance Indicators (KPIs)

- Total Children Under Care
- Net Intake Pressure
- Backlog Accumulation
- Discharge Offset Ratio
- System Load Trend

---

# 📊 Dashboard Features

✅ Real-Time Monitoring

✅ Interactive Visualizations

✅ Forecasting

✅ KPI Cards

✅ Data Validation

✅ Daily / Weekly / Monthly Analysis

---

# 🛠 Technology Stack

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Prophet
- Scikit-Learn

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/Arqam-Shaikh/System-Capacity-Care-Load-Analytics.git
cd System-Capacity-Care-Load-Analytics
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

---

# 📁 Project Structure

```
System-Capacity-Care-Load-Analytics
│
├── assets/
├── data/
├── app.py
├── forecasting.py
├── metrics.py
├── preprocessing.py
├── requirements.txt
└── README.md
```

---

# 🌟 Features

- Interactive Dashboard
- Healthcare Capacity Analytics
- Time-Series Forecasting
- Data Validation
- KPI Monitoring
- Responsive UI

---

# 🤝 Acknowledgement

This project was developed as part of the **Unified Mentor Internship Program** using healthcare analytics use cases inspired by the **U.S. Department of Health and Human Services (HHS)**.

---

# 🌐 Live Demo

### 🚀 Streamlit Application

https://system-capacity-care-load-analytics-c6cgxbhdbv4rz6v9y9fnnm.streamlit.app/

---

# 💻 GitHub Repository

https://github.com/Arqam-Shaikh/System-Capacity-Care-Load-Analytics

---

# 👨‍💻 Developer

## Arqam Shaikh

**Data Analytics | Machine Learning | Python Developer**

### GitHub

https://github.com/Arqam-Shaikh

### LinkedIn

https://www.linkedin.com/in/arqam-shaikh-5196b4313/

For queries or collaboration, feel free to connect.

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Thank you for visiting this project!