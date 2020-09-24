from fastapi import APIRouter
import json
import pandas as pd

router = APIRouter()

strains = pd.read_csv('data/strains.csv')

""" Return the data as JSON """
@router.get('/types')
async def types():

    sativa = []
    for i in range(strains.shape[0]):
        if 'Sativa' in strains.type.iloc[i]:
            sativa.append(strains.name.iloc[i])
    # Converting into Json
    sativa_json = json.dumps(sativa)

    indica = []
    for i in range(strains.shape[0]):
        if 'Indica' in strains.type.iloc[i]:
            indica.append(strains.name.iloc[i])
    # Converting into Json
    indica_json = json.dumps(indica)

    hybrid = []
    for i in range(strains.shape[0]):
        if 'Hybrid' in strains.type.iloc[i]:
            hybrid.append(strains.name.iloc[i])
    # Converting into Json
    hybrid_json = json.dumps(hybrid)


    return 'Sativa', sativa_json, 'Indica', indica_json, 'Hybrid', hybrid_json