from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Literal
from preprocessing.cleaning_data import preprocess
from predict.prediction import prediction
from fastapi.encoders import jsonable_encoder
import os

port = os.environ.get('PORT', 8000)
app = FastAPI(PORT = port)

class Item(BaseModel):
    area: int
    property_type: Literal['APARTMENT', 'HOUSE', 'OTHERS']
    rooms_number: int
    zip_code: int
    land_area: int | None
    garden: bool | None
    garden_area: int | None
    equipped_kitchen: bool | None
    swimming_pool: bool | None
    open_fire: bool | None
    terrace: bool | None
    terrace_area: int | None
    facades_number: int | None
    building_state: Literal["NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED", "TO REBUILD", None]


@app.get("/")
async def status_check():
  return "alive"

@app.get("/predict")
async def data_format():
  return ("Required fields are: area: int, property_type: str('APARTMENT', 'HOUSE', 'OTHERS'), rooms_number: int, zip_code: int. Optional filelds are: land_area: int, garden: bool, garden_area: int, equipped_kitchen: bool, swimming_pool: bool, open_fire: bool, terrace: bool, terrace_area: int, facades_number: int, building_state: str('NEW', 'GOOD', 'TO RENOVATE', 'JUST RENOVATED', 'TO REBUILD')")

@app.post("/predict")
async def make_prediction(data: Item = Body(embed=True)):
  json_input = jsonable_encoder(data)
  processed_input = preprocess(json_input)
  predicted_value = prediction(processed_input)
  return predicted_value