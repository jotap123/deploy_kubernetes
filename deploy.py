import os
import uvicorn
import pandas as pd
from fastapi import FastAPI
from house_pricing import Pricing

app = FastAPI()
model = pd.read_pickle(os.getcwd() + os.path.abspath('/../models/house_model.pkl'))


@app.get('/')
async def index():
    return {"message":"Hello World"}


@app.post('/predict')
async def predict_house_prices(data:Pricing):
    cols = model.feature_names_in_
    data = data.dict()
    df = pd.DataFrame([list(data.values())], columns=cols)

    features_list = df.values.tolist()
    prediction = int(model.predict(features_list)[0].round())

    return {'prediction': f'House is worth approximately ${prediction}'}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)