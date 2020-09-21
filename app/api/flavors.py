from fastapi import APIRouter
import json
import pandas as pd

router = APIRouter()

strain = pd.read_csv('data/strains.csv')

""" Return the data as JSON """
@router.get('/flavors')
async def flavors():

    citrus = []
    for i in range(strain.shape[0]):
        if 'Citrus' in strain.flavor.iloc[i]:
            citrus.append(strain.name.iloc[i])
    # Converting into Json
    citrus_json = json.dumps(citrus)

    sweet = []
    for i in range(strain.shape[0]):
        if 'Sweet' in strain.flavor.iloc[i]:
            sweet.append(strain.name.iloc[i])
    # Converting into Json
    sweet_json = json.dumps(sweet)

    earthy = []
    for i in range(strain.shape[0]):
        if 'Earthy' in strain.flavor.iloc[i]:
            earthy.append(strain.name.iloc[i])
    # Converting into Json
    earthy_json = json.dumps(earthy)

    pine= []
    for i in range(strain.shape[0]):
        if 'Pine' in strain.flavor.iloc[i]:
            pine.append(strain.name.iloc[i])
    # Converting into Json
    pine_json = json.dumps(pine)

    skunk= []
    for i in range(strain.shape[0]):
        if 'Skunk' in strain.flavor.iloc[i]:
            skunk.append(strain.name.iloc[i])
    # Converting into Json
    skunk_json = json.dumps(skunk)

    berry= []
    for i in range(strain.shape[0]):
        if 'Berry' in strain.flavor.iloc[i]:
            berry.append(strain.name.iloc[i])
    # Converting into Json
    berry_json = json.dumps(berry)

    lemon= []
    for i in range(strain.shape[0]):
        if 'Lemon' in strain.flavor.iloc[i]:
            lemon.append(strain.name.iloc[i])
    # Converting into Json
    lemon_json = json.dumps(lemon)

    lime= []
    for i in range(strain.shape[0]):
        if 'Lime' in strain.flavor.iloc[i]:
            lime.append(strain.name.iloc[i])
    # Converting into Json
    lime_json = json.dumps(lime)

    blueberry= []
    for i in range(strain.shape[0]):
        if 'Blueberry' in strain.flavor.iloc[i]:
            blueberry.append(strain.name.iloc[i])
    # Converting into Json
    blueberry_json = json.dumps(blueberry)

    strawberry= []
    for i in range(strain.shape[0]):
        if 'Strawberry' in strain.flavor.iloc[i]:
            strawberry.append(strain.name.iloc[i])
    # Converting into Json
    strawberry_json = json.dumps(strawberry)

    mango= []
    for i in range(strain.shape[0]):
        if 'Mango' in strain.flavor.iloc[i]:
            mango.append(strain.name.iloc[i])
    # Converting into Json
    mango_json = json.dumps(mango)

    rose= []
    for i in range(strain.shape[0]):
        if 'Rose' in strain.flavor.iloc[i]:
            rose.append(strain.name.iloc[i])
    # Converting into Json
    rose_json = json.dumps(rose)

    pepper= []
    for i in range(strain.shape[0]):
        if 'Pepper' in strain.flavor.iloc[i]:
            pepper.append(strain.name.iloc[i])
    # Converting into Json
    pepper_json = json.dumps(pepper)


    return 'Citrus', citrus_json, 'Sweet', sweet_json, 'Earthy', earthy_json, \
    'Pine', pine_json, 'Skunk', skunk_json, 'Berry', berry_json, \
    'Lemon', lemon_json, 'Lime', lime_json, 'Blueberry', blueberry_json, \
    'Strawberry', strawberry_json, 'Mango', mango_json, 'Rose', rose_json, \
    'Pepper', pepper_json





    





