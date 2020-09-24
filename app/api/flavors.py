from fastapi import APIRouter
import json
import pandas as pd

router = APIRouter()

strains = pd.read_csv('data/strains.csv')

""" Return the data as JSON """
@router.get('/flavors')
async def flavors():

    citrus = []
    for i in range(strains.shape[0]):
        if 'Citrus' in strains.flavor.iloc[i]:
            citrus.append(strains.name.iloc[i])
    # Converting into Json
    citrus_json = json.dumps(citrus)

    sweet = []
    for i in range(strains.shape[0]):
        if 'Sweet' in strains.flavor.iloc[i]:
            sweet.append(strains.name.iloc[i])
    # Converting into Json
    sweet_json = json.dumps(sweet)

    earthy = []
    for i in range(strains.shape[0]):
        if 'Earthy' in strains.flavor.iloc[i]:
            earthy.append(strains.name.iloc[i])
    # Converting into Json
    earthy_json = json.dumps(earthy)

    pine= []
    for i in range(strains.shape[0]):
        if 'Pine' in strains.flavor.iloc[i]:
            pine.append(strains.name.iloc[i])
    # Converting into Json
    pine_json = json.dumps(pine)

    skunk= []
    for i in range(strains.shape[0]):
        if 'Skunk' in strains.flavor.iloc[i]:
            skunk.append(strains.name.iloc[i])
    # Converting into Json
    skunk_json = json.dumps(skunk)

    berry= []
    for i in range(strains.shape[0]):
        if 'Berry' in strains.flavor.iloc[i]:
            berry.append(strains.name.iloc[i])
    # Converting into Json
    berry_json = json.dumps(berry)

    lemon= []
    for i in range(strains.shape[0]):
        if 'Lemon' in strains.flavor.iloc[i]:
            lemon.append(strains.name.iloc[i])
    # Converting into Json
    lemon_json = json.dumps(lemon)

    lime= []
    for i in range(strains.shape[0]):
        if 'Lime' in strains.flavor.iloc[i]:
            lime.append(strains.name.iloc[i])
    # Converting into Json
    lime_json = json.dumps(lime)

    blueberry= []
    for i in range(strains.shape[0]):
        if 'Blueberry' in strains.flavor.iloc[i]:
            blueberry.append(strains.name.iloc[i])
    # Converting into Json
    blueberry_json = json.dumps(blueberry)

    strawberry= []
    for i in range(strains.shape[0]):
        if 'Strawberry' in strains.flavor.iloc[i]:
            strawberry.append(strains.name.iloc[i])
    # Converting into Json
    strawberry_json = json.dumps(strawberry)

    mango= []
    for i in range(strains.shape[0]):
        if 'Mango' in strains.flavor.iloc[i]:
            mango.append(strains.name.iloc[i])
    # Converting into Json
    mango_json = json.dumps(mango)

    rose= []
    for i in range(strains.shape[0]):
        if 'Rose' in strains.flavor.iloc[i]:
            rose.append(strains.name.iloc[i])
    # Converting into Json
    rose_json = json.dumps(rose)

    pepper= []
    for i in range(strains.shape[0]):
        if 'Pepper' in strains.flavor.iloc[i]:
            pepper.append(strains.name.iloc[i])
    # Converting into Json
    pepper_json = json.dumps(pepper)


    return 'Citrus', citrus_json, 'Sweet', sweet_json, 'Earthy', earthy_json, \
    'Pine', pine_json, 'Skunk', skunk_json, 'Berry', berry_json, \
    'Lemon', lemon_json, 'Lime', lime_json, 'Blueberry', blueberry_json, \
    'Strawberry', strawberry_json, 'Mango', mango_json, 'Rose', rose_json, \
    'Pepper', pepper_json





    





