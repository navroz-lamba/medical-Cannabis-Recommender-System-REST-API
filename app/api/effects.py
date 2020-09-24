from fastapi import APIRouter
import json
import pandas as pd

router = APIRouter()

strains = pd.read_csv('data/strains.csv')

""" Return the data as JSON """
@router.get('/effects')
async def effects():

    relaxed = []
    for i in range(strains.shape[0]):
        if 'Relaxed' in strains.effects.iloc[i]:
            relaxed.append(strains.name.iloc[i])
    # converting into json 
    relaxed_json = json.dumps(relaxed)

    happy = []
    for i in range(strains.shape[0]):
        if 'Happy' in strains.effects.iloc[i]:
            happy.append(strains.name.iloc[i])
    # converting into json 
    happy_json = json.dumps(happy)

    euphoric = []
    for i in range(strains.shape[0]):
        if 'Euphoric' in strains.effects.iloc[i]:
            euphoric.append(strains.name.iloc[i])
    # converting into json 
    euphoric_json = json.dumps(euphoric)

    uplifted = []
    for i in range(strains.shape[0]):
        if 'Uplifted' in strains.effects.iloc[i]:
            uplifted.append(strains.name.iloc[i])
    # converting into json 
    uplifted_json = json.dumps(uplifted)

    sleepy = []
    for i in range(strains.shape[0]):
        if 'Sleepy' in strains.effects.iloc[i]:
            sleepy.append(strains.name.iloc[i])
    # converting into json 
    sleepy_json = json.dumps(sleepy)

    dry_mouth = []
    for i in range(strains.shape[0]):
        if 'Dry Mouth' in strains.effects.iloc[i]:
            dry_mouth.append(strains.name.iloc[i])
    # converting into json 
    dry_mouth_json = json.dumps(dry_mouth)

    focused = []
    for i in range(strains.shape[0]):
        if 'Focused' in strains.effects.iloc[i]:
            focused.append(strains.name.iloc[i])
    # converting into json 
    focused_json = json.dumps(focused)

    energetic = []
    for i in range(strains.shape[0]):
        if 'Energetic' in strains.effects.iloc[i]:
            energetic.append(strains.name.iloc[i])
    # converting into json 
    energetic_json = json.dumps(energetic)

    paranoid = []
    for i in range(strains.shape[0]):
        if 'Paranoid' in strains.effects.iloc[i]:
            paranoid.append(strains.name.iloc[i])
    # converting into json 
    paranoid_json = json.dumps(paranoid)

    anxious = []
    for i in range(strains.shape[0]):
        if 'Anxious' in strains.effects.iloc[i]:
            anxious.append(strains.name.iloc[i])
    # converting into json 
    anxious_json = json.dumps(anxious)

    hungry = []
    for i in range(strains.shape[0]):
        if 'Hungry' in strains.effects.iloc[i]:
            hungry.append(strains.name.iloc[i])
    # converting into json 
    hungry_json = json.dumps(hungry)

    talkative = []
    for i in range(strains.shape[0]):
        if 'Talkative' in strains.effects.iloc[i]:
            talkative.append(strains.name.iloc[i])
    # converting into json 
    talkative_json = json.dumps(talkative)

    creative = []
    for i in range(strains.shape[0]):
        if 'Creative' in strains.effects.iloc[i]:
            creative.append(strains.name.iloc[i])
    # converting into json 
    creative_json = json.dumps(creative)


    return 'Relaxed', relaxed_json, 'Happy', happy_json, 'Euphoric', euphoric_json,\
        'Uplifted', uplifted_json, 'Sleepy', sleepy_json, 'Dry Mouth', dry_mouth_json, \
        'Focused', focused_json, 'Energetic', energetic_json, 'Paranoid', paranoid_json, \
        'Anxious', anxious_json, 'Hungry', hungry_json, 'Talkative', talkative_json, \
        'Creative', creative_json