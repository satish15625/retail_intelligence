from fastapi import FastAPI
from app.routes import load_data, process_data, insights

app = FastAPI(title="Retail Intelligence Engine")

# Register API routers
app.include_router(load_data.router)
app.include_router(process_data.router)
app.include_router(insights.router)
