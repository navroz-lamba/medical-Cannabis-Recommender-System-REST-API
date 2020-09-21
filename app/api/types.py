from fastapi import APIRouter
import json
import pandas as pd

router = APIRouter()

strain = pd.read_csv('data/strains.csv')

""" Return the data as JSON """
@router.get('/types')
async def types():

    sativa = []
    for i in range(strain.shape[0]):
        if 'Sativa' in strain.type.iloc[i]:
            sativa.append(strain.name.iloc[i])
    # Converting into Json
    sativa_json = json.dumps(sativa)

    indica = []
    for i in range(strain.shape[0]):
        if 'Indica' in strain.type.iloc[i]:
            indica.append(strain.name.iloc[i])
    # Converting into Json
    indica_json = json.dumps(indica)

    hybrid = []
    for i in range(strain.shape[0]):
        if 'Hybrid' in strain.type.iloc[i]:
            hybrid.append(strain.name.iloc[i])
    # Converting into Json
    hybrid_json = json.dumps(hybrid)


    return 'Sativa', sativa_json, 'Indica', indica_json, 'Hybrid', hybrid_json