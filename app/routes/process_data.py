from fastapi import APIRouter
from app.models import store
from app.utils import clean_data

router = APIRouter()

@router.post("/process-data")
def process_data():
    if store.raw_data is None:
        return {"error": "Data not loaded."}

    before = len(store.raw_data)
    store.cleaned_data = clean_data(store.raw_data)
    after = len(store.cleaned_data)

    return {
        "message": "Data cleaned successfully.",
        "before_rows": before,
        "after_rows": after
    }
