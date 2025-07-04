# ✈️ Airline Booking Demand Web App

A Python Flask web application that simulates and visualizes airline booking demand between major airports using dynamic charts.

## 🔥 Features

- 📈 **Monthly Demand Trend** — enter origin and destination airports to see a line chart of 6-month simulated booking demand.
- 📊 **Top 5 Busiest Routes** — view popular routes with highest demand as a bar chart.
- 🎨 Responsive UI using Chart.js and CSS.
- 🚀 Built using Flask, HTML5, JS, and Python (with simulated data).
  
## 💻 Technologies Used

- Flask (Python Web Framework)
- HTML5 + CSS3
- JavaScript + Chart.js
- Jinja2 Templating

## 🧠 How It Works

1. Enter any airport code in the form (e.g., `DEL`, `BOM`)
2. App simulates monthly demand using Python backend.
3. Displays:
   - Line Chart: Monthly demand for the route
   - Bar Chart: Top 5 busiest routes

## 📷 Screenshots

![App Screenshot](screenshots/airline_chart_1.png)
![Top Routes](screenshots/airline_chart_2.png)

## 🚀 Run Locally

```bash
git clone https://github.com/your-username/airline-demand-app.git
cd airline-demand-app
pip install -r requirements.txt
python app.py
