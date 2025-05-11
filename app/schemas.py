from pydantic import BaseModel

class ShipmentData(BaseModel):
    Warehouse_block: int
    Mode_of_Shipment: int
    Customer_care_calls: int
    Customer_rating: int
    Cost_of_the_Product: float
    Prior_purchases: int
    Product_importance: int
    Gender: int
    Discount_offered: float
    Weight_in_gms: float

class Prediction(BaseModel):
    on_time: bool
