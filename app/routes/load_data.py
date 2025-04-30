from fastapi import APIRouter
from app.models import store
import pandas as pd

router = APIRouter()

@router.get('/')
def home():
    return "Home"
@router.post("/load-data")
def load_data():
    try:
        df = pd.read_csv("data/Amazon Sale Report.csv")
        store.raw_data = df
        return {"message": f"Data loaded successfully with {len(df)} records."}
    except Exception as e:
        return {"error": str(e)}
