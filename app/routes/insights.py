from fastapi import APIRouter
from app.models import store


router = APIRouter(prefix="/insights")

@router.get("/daily-revenue")
def daily_revenue(ship_state: str = None, category: str = None):
    if store.cleaned_data is None:
        return {"error": "Data not processed."}
    
    df = store.cleaned_data.copy()
    if ship_state:
        df = df[df['ship-state'].str.upper() == ship_state.upper()]
    if category:
        df = df[df['Category'].str.lower() == category.lower()]

    df['Date'] = df['Date'].dt.date
    result = df.groupby('Date')['Amount'].sum().reset_index()
    return result.to_dict(orient="records")



@router.get("/top-skus")
def top_skus(month: str, N: int = 5):
    if store.cleaned_data is None:
        return {"error": "Data not processed."}
    
    df = store.cleaned_data.copy()
    df['Month'] = df['Date'].dt.to_period('M')
    df = df[df['Month'].astype(str) == month]

    result = df.groupby('SKU')['Amount'].sum().nlargest(N).reset_index()
    return result.to_dict(orient="records")



@router.get("/asp-order-count")
def asp_order_count():
    if store.cleaned_data is None:
        return {"error": "Data not processed."}

    df = store.cleaned_data
    grouped = df.groupby('SKU').agg(
        total_revenue=('Amount', 'sum'),
        total_orders=('Order ID', 'nunique'),
        quantity=('Qty', 'sum')
    )
    grouped['ASP'] = grouped['total_revenue'] / grouped['quantity']
    return grouped.reset_index()[['SKU', 'ASP', 'total_orders']].to_dict(orient='records')

