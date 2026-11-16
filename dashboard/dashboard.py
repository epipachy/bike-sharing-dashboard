
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)


DATA_PATH = Path(__file__).parent / "main_data.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df['date'] = pd.to_datetime(df['date'])
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("File main_data.csv tidak ditemukan!")
    st.stop()


st.title("🚲 Bike Sharing Dashboard")
st.markdown(
    "Explore bike-sharing rental patterns based on "
    "time, season, weather, and user characteristics."
)

st.divider()

st.sidebar.header("Dashboard Filters")

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(df['date'].min().date(), df['date'].max().date()),
    min_value=df['date'].min().date(),
    max_value=df['date'].max().date()
)

season_options = ["All"] + sorted(
    df['season_name'].dropna().unique().tolist()
)

selected_season = st.sidebar.selectbox(
    "Select Season",
    season_options
)

weather_options = ["All"] + sorted(
    df['weather_name'].dropna().unique().tolist()
)

selected_weather = st.sidebar.selectbox(
    "Select Weather",
    weather_options
)

if len(date_range) == 2:
    start_date, end_date = date_range

    filtered_df = df[
        (df['date'].dt.date >= start_date) &
        (df['date'].dt.date <= end_date)
    ].copy()
else:
    filtered_df = df.copy()

if selected_season != "All":
    filtered_df = filtered_df[
        filtered_df['season_name'] == selected_season
    ]

if selected_weather != "All":
    filtered_df = filtered_df[
        filtered_df['weather_name'] == selected_weather
    ]


st.subheader("Key Performance Indicators")

if filtered_df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

total_rentals = filtered_df['total_rentals'].sum()
total_casual = filtered_df['casual'].sum()
total_registered = filtered_df['registered'].sum()
average_rentals = filtered_df['total_rentals'].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Rentals",
    f"{total_rentals:,.0f}"
)

col2.metric(
    "Average Rentals / Hour",
    f"{average_rentals:,.1f}"
)

col3.metric(
    "Casual Users",
    f"{total_casual:,.0f}"
)

col4.metric(
    "Registered Users",
    f"{total_registered:,.0f}"
)

st.divider()


st.subheader("Daily Bike Rental Trends")

daily_data = (
    filtered_df.groupby('date')['total_rentals']
    .sum()
    .reset_index()
)

fig_daily = px.line(
    daily_data,
    x='date',
    y='total_rentals',
    title="Total Bike Rentals Over Time",
    labels={
        'date': 'Date',
        'total_rentals': 'Total Rentals'
    },
    markers=True
)

st.plotly_chart(fig_daily, use_container_width=True)


st.subheader("Hourly Rental Patterns")

hourly_data = (
    filtered_df.groupby('hour')['total_rentals']
    .sum()
    .reset_index()
)

fig_hourly = px.bar(
    hourly_data,
    x='hour',
    y='total_rentals',
    title="Total Bike Rentals by Hour",
    labels={
        'hour': 'Hour of Day',
        'total_rentals': 'Total Rentals'
    }
)

st.plotly_chart(fig_hourly, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    season_data = (
        filtered_df.groupby('season_name')['total_rentals']
        .sum()
        .reset_index()
    )

    fig_season = px.bar(
        season_data,
        x='season_name',
        y='total_rentals',
        title="Bike Rentals by Season",
        labels={
            'season_name': 'Season',
            'total_rentals': 'Total Rentals'
        }
    )

    st.plotly_chart(fig_season, use_container_width=True)

with col2:
    weather_data = (
        filtered_df.groupby('weather_name')['total_rentals']
        .sum()
        .reset_index()
    )

    fig_weather = px.bar(
        weather_data,
        x='weather_name',
        y='total_rentals',
        title="Bike Rentals by Weather",
        labels={
            'weather_name': 'Weather',
            'total_rentals': 'Total Rentals'
        }
    )

    st.plotly_chart(fig_weather, use_container_width=True)

st.subheader("Rental Distribution by User Type")

user_data = pd.DataFrame({
    'User Type': ['Casual', 'Registered'],
    'Total Rentals': [total_casual, total_registered]
})

fig_users = px.pie(
    user_data,
    names='User Type',
    values='Total Rentals',
    title="Casual vs Registered Users",
    hole=0.4
)

st.plotly_chart(fig_users, use_container_width=True)

st.divider()

st.caption(
    "Bike Sharing Dashboard | Data Analysis Project"
)
