from fastapi.testclient import TestClient # type: ignore
from app.app import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={
        "Warehouse_block": 1,
        "Mode_of_Shipment": 0,
        "Customer_care_calls": 2,
        "Customer_rating": 4,
        "Cost_of_the_Product": 150,
        "Prior_purchases": 3,
        "Product_importance": 1,
        "Gender": 0,
        "Discount_offered": 10,
        "Weight_in_gms": 3000
    })
    assert response.status_code == 200
    assert "on_time" in response.json()
