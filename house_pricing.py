from pydantic import BaseModel


class Pricing(BaseModel):
    median_local_price: float
    house_size_factor: float
    acre_lot_factor: float
    bed_per_1000sf: float
    bath_per_1000sf: float
