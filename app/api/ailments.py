from fastapi import APIRouter
import json
import pandas as pd

router = APIRouter()

strains = pd.read_csv('data/strains.csv')

""" Return the data as JSON """
@router.get('/ailments')
async def ailments():

    depression = []
    for i in range(strains.shape[0]):
        if 'Depression' in strains.ailment.iloc[i]:
            depression.append(strains.name.iloc[i])
    # converting into json 
    depression_json = json.dumps(depression)

    pain = []
    for i in range(strains.shape[0]):
        if 'Pain' in strains.ailment.iloc[i]:
            pain.append(strains.name.iloc[i])
    # converting into json 
    pain_json = json.dumps(pain)

    insomnia = []
    for i in range(strains.shape[0]):
        if 'Insomnia' in strains.ailment.iloc[i]:
            insomnia.append(strains.name.iloc[i])
    # converting into json 
    insomnia_json = json.dumps(insomnia)

    stress = []
    for i in range(strains.shape[0]):
        if 'Stress' in strains.ailment.iloc[i]:
            stress.append(strains.name.iloc[i])
    # converting into json 
    stress_json = json.dumps(stress)

    lack_of_appetite = []
    for i in range(strains.shape[0]):
        if 'Lack of Appetite' in strains.ailment.iloc[i]:
            lack_of_appetite.append(strains.name.iloc[i])
    # converting into json 
    lack_of_appetite_json = json.dumps(lack_of_appetite)

    muscle_spasms = []
    for i in range(strains.shape[0]):
        if 'Muscle Spasms' in strains.ailment.iloc[i]:
            muscle_spasms.append(strains.name.iloc[i])
    # converting into json 
    muscle_spasms_json = json.dumps(muscle_spasms)

    nausea = []
    for i in range(strains.shape[0]):
        if 'Nausea' in strains.ailment.iloc[i]:
            nausea.append(strains.name.iloc[i])
    # converting into json 
    nausea_json = json.dumps(nausea)

    inflammation = []
    for i in range(strains.shape[0]):
        if 'Inflammation' in strains.ailment.iloc[i]:
            inflammation.append(strains.name.iloc[i])
    # converting into json 
    inflammation_json = json.dumps(inflammation)


    return 'Depression', depression_json, 'Pain', pain_json, 'Insomnia', insomnia_json,\
        'Stress', stress_json, 'Lack of Appetite', lack_of_appetite_json, \
        'Muscle Spasms', muscle_spasms_json, 'Inflammation', inflammation_json, \
        'Nausea', nausea_json

    