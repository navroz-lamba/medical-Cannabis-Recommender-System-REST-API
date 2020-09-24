import pandas as pd
from fastapi import APIRouter
import json

router = APIRouter()

strains = pd.read_csv('data/strains.csv')
results = strains.to_json(orient="index")


@router.get('/data')
async def data():
    """
    Return cannabis data as json
    """
    return results
