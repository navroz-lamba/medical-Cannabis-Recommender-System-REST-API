import logging
import random
import json
from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field

log = logging.getLogger(__name__)
router = APIRouter()

strains = pd.read_csv('data/strains.csv')
list_of_strains = strains.name

class Strain(BaseModel):
    """Use this data model to parse the request body JSON."""

    kind: str = Field(..., example='Hybrid')
    ailment: str = Field(..., example='Insomnia')
    effect: str = Field(..., example='Happy')
    flavor: str = Field(..., example='Blueberry')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame(self)


@router.post('/predict')
async def predict(strain: Strain):
    """
    Make random baseline prediction for classification problem 🔮

    ### Request Body
   
    - `kind`: str
    - `ailment`: str
    - `effect`: str
     -`flavor`: str

    ### Response
    - `prediction`: string, at random
    """

    # X_new = strain.to_df()
    # log.info(X_new)

    y_pred = random.choice(list_of_strains)
    # making a new df for our predicted value 
    y_pred_df = strains.loc[strains['name'] == y_pred]

    # description = y_pred_df.Description.to_string(index=False)
    description = y_pred_df.Description.to_json(orient='values')
    rating = float(y_pred_df.Rating)
    

    return {
        'prediction': y_pred,
        'description': description,
        'rating': rating
    }
