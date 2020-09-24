import logging, random, json, joblib, sklearn
import tokenize
from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field

example = 'I have a severe pain in the back'
log = logging.getLogger(__name__)
router = APIRouter()

strains = pd.read_csv('data/strains.csv')
list_of_strains = strains.name

predictor = joblib.load('app/api/model.joblib')
print('pickled model loaded')

class Strain(BaseModel):
    """Use this data model to parse the request body JSON."""

    ailment: str = Field(..., example="I am anxious. I like Sativa and earthy flavor.")
    # kind: str = Field(..., example='Hybrid')
    # effect: str = Field(..., example='Happy')
    # flavor: str = Field(..., example='Blueberry')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])


@router.post('/predict')
async def predict(strain: Strain):
    
    predict_strain = predictor.predict([strain.ailment])[0]
    
    # making a new df for our predicted value 
    y_pred_df = strains.loc[strains['name'] == predict_strain.upper()]
   
    description = y_pred_df.Description.to_json(orient='values')
    rating = float(y_pred_df.Rating)
    effects = y_pred_df.Effects.to_json(orient='values')
    flavors = y_pred_df.Flavor.to_json(orient='values')
    

    return {
        'prediction': predict_strain,
        'description': description,
        'rating': rating,
        'effects': effects,
        'flavors': flavors
    }