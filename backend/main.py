from fastapi import FastAPI, Depends

app = FastAPI()

items_db = [
    {"id": 1, "name": "Apple"},
    {"id": 2, "name": "Banana"},
    {"id": 3, "name": "Pineapple"},
    {"id": 4, "name": "Grapes"},
]

@app.get("/items")
def get_items(q: str | None = None):
    if q:
        filtered = [item for item in items_db if q.lower() in item["name"].lower()]
        return filtered
    return items_db


def get_exchange_rate():
    """
    Dependency que devuelve la tasa USD → COP.
    En la vida real podrías conectarte a una API externa aquí.
    """
    return 4000


@app.get("/price/{usd}")
def get_price(usd: float, rate: float = Depends(get_exchange_rate)):
    return {
        "usd": usd,
        "rate": rate,
        "cop": usd * rate
    }
