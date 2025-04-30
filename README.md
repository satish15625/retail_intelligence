### Project Setup for run 
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

cd retail_intelligence
pip install -r requirements.txt

uvicorn app.main:app --reload



# 🛒 Retail Intelligence Engine – FastAPI Project

This project is a modular Python backend application using **FastAPI**, built for extracting insights from Amazon sales data through REST API endpoints.

---

## 🚀 Features

- Load and clean raw Amazon sales CSV
- Filter and aggregate daily revenue
- Identify top-performing SKUs
- Calculate average selling price (ASP) and order count
- Optional: Top categories by revenue

---

## 📦 Setup Instructions

### 1. Clone and Install Dependencies

```bash
git clone https://github.com/<your-username>/retail-intelligence-engine.git
cd retail-intelligence-engine
pip install -r requirements.txt


retail-intelligence/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── utils.py
│   └── routes/
│       ├── load_data.py
│       ├── process_data.py
│       └── insights.py
├── data/
│   └── Amazon Sale Report.csv
├── requirements.txt
├── README.md
└── api_test_endpoints.xlsx



Running the App
uvicorn app.main:app --reload
Visit: http://127.0.0.1:8000/docs for interactive Swagger UI.


API Endpoints Summary

Method	Endpoint	Description
POST	/load-data	Load the Amazon sales CSV file into memory
POST	/process-data	Clean and preprocess the data
GET	/insights/daily-revenue	Get daily revenue by date, state, or category
GET	/insights/top-skus	Get top SKUs by revenue or quantity
GET	/insights/asp-order-count	Calculate ASP and order count by SKU/category
GET	/insights/top-categories	(Optional) Get top N categories by revenue
