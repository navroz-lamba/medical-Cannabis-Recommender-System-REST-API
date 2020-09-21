from fastapi import APIRouter
import json
import pandas as pd

router = APIRouter()

strain = pd.read_csv('data/strains.csv')

""" Return the data as JSON """
@router.get('/effects')
async def effects():

    relaxed = []
    for i in range(strain.shape[0]):
        if 'Relaxed' in strain.effects.iloc[i]:
            relaxed.append(strain.name.iloc[i])
    # converting into json 
    relaxed_json = json.dumps(relaxed)

    happy = []
    for i in range(strain.shape[0]):
        if 'Happy' in strain.effects.iloc[i]:
            happy.append(strain.name.iloc[i])
    # converting into json 
    happy_json = json.dumps(happy)

    euphoric = []
    for i in range(strain.shape[0]):
        if 'Euphoric' in strain.effects.iloc[i]:
            euphoric.append(strain.name.iloc[i])
    # converting into json 
    euphoric_json = json.dumps(euphoric)

    uplifted = []
    for i in range(strain.shape[0]):
        if 'Uplifted' in strain.effects.iloc[i]:
            uplifted.append(strain.name.iloc[i])
    # converting into json 
    uplifted_json = json.dumps(uplifted)

    sleepy = []
    for i in range(strain.shape[0]):
        if 'Sleepy' in strain.effects.iloc[i]:
            sleepy.append(strain.name.iloc[i])
    # converting into json 
    sleepy_json = json.dumps(sleepy)

    dry_mouth = []
    for i in range(strain.shape[0]):
        if 'Dry Mouth' in strain.effects.iloc[i]:
            dry_mouth.append(strain.name.iloc[i])
    # converting into json 
    dry_mouth_json = json.dumps(dry_mouth)

    focused = []
    for i in range(strain.shape[0]):
        if 'Focused' in strain.effects.iloc[i]:
            focused.append(strain.name.iloc[i])
    # converting into json 
    focused_json = json.dumps(focused)

    energetic = []
    for i in range(strain.shape[0]):
        if 'Energetic' in strain.effects.iloc[i]:
            energetic.append(strain.name.iloc[i])
    # converting into json 
    energetic_json = json.dumps(energetic)

    paranoid = []
    for i in range(strain.shape[0]):
        if 'Paranoid' in strain.effects.iloc[i]:
            paranoid.append(strain.name.iloc[i])
    # converting into json 
    paranoid_json = json.dumps(paranoid)

    anxious = []
    for i in range(strain.shape[0]):
        if 'Anxious' in strain.effects.iloc[i]:
            anxious.append(strain.name.iloc[i])
    # converting into json 
    anxious_json = json.dumps(anxious)

    hungry = []
    for i in range(strain.shape[0]):
        if 'Hungry' in strain.effects.iloc[i]:
            hungry.append(strain.name.iloc[i])
    # converting into json 
    hungry_json = json.dumps(hungry)

    talkative = []
    for i in range(strain.shape[0]):
        if 'Talkative' in strain.effects.iloc[i]:
            talkative.append(strain.name.iloc[i])
    # converting into json 
    talkative_json = json.dumps(talkative)

    creative = []
    for i in range(strain.shape[0]):
        if 'Creative' in strain.effects.iloc[i]:
            creative.append(strain.name.iloc[i])
    # converting into json 
    creative_json = json.dumps(creative)


    return 'Relaxed', relaxed_json, 'Happy', happy_json, 'Euphoric', euphoric_json,\
        'Uplifted', uplifted_json, 'Sleepy', sleepy_json, 'Dry Mouth', dry_mouth_json, \
        'Focused', focused_json, 'Energetic', energetic_json, 'Paranoid', paranoid_json, \
        'Anxious', anxious_json, 'Hungry', hungry_json, 'Talkative', talkative_json, \
        'Creative', creative_json