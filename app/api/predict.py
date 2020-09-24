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

    ailment: str = Field(..., example="I have nausea and i would like an earthy flavor.")
    # kind: str = Field(..., example='Hybrid')
    # effect: str = Field(..., example='Happy')
    # flavor: str = Field(..., example='Blueberry')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])


@router.post('/predict')
async def predict(strain: Strain):
    
    # predict_strain = predictor.predict(strain.to_df())[0]
    predict_strain = predictor.predict([strain.ailment])[0]
    
    # making a new df for our predicted value 
    # y_pred_df = strains.loc[strains['name'] == predict_strain[0].upper()]
   
    # # description = y_pred_df.Description.to_string(index=False)
    # description = y_pred_df.Description.to_json(orient='values')
    # rating = float(y_pred_df.Rating)
    # effects = y_pred_df.Effects.to_json(orient='values')
    # flavors = y_pred_df.Flavor.to_json(orient='values')
    

    return {
        'prediction': predict_strain,
        # 'description': description,
        # 'rating': rating,
        # 'effects': effects,
        # 'flavors': flavors
    }

# import logging, random, json, joblib, sklearn
# import tokenize
# from fastapi import APIRouter
# import pandas as pd
# from pydantic import BaseModel, Field

# # example = 'I am anxious'
# log = logging.getLogger(__name__)
# router = APIRouter()

# strains = pd.read_csv('data/strains.csv')
# list_of_strains = strains.name

# model = joblib.load('app/api/model.joblib')
# print('pickled model loaded')

# class Strain(BaseModel):
#     """Use this data model to parse the request body JSON."""

#     ailment: str
#     # kind: str = Field(..., example='Hybrid')
#     # effect: str = Field(..., example='Happy')
#     # flavor: str = Field(..., example='Blueberry')

#     def to_dict(self):
#         """Convert pydantic object to pandas dataframe with 1 row."""
#         return list(self)


# @router.post('/predict')
# async def predict():
#     example = 'I have nausea and I would like an Indica flower'
#     # dict_strain = strain.to_dict()
#     # new_data = ",".join([value for value in dict_strain.values()])
#     predict_strain = model.predict([example])[0]
#     # predict_strain = predictor.predict([strain])
    
#     # # making a new df for our predicted value 
#     # y_pred_df = strains.loc[strains['name'] == predict_strain.upper()]
   
#     # # # description = y_pred_df.Description.to_string(index=False)
#     # description = y_pred_df.Description.to_json(orient='values')
#     # rating = float(y_pred_df.Rating)
#     # effects = y_pred_df.Effects.to_json(orient='values')
#     # flavors = y_pred_df.Flavor.to_json(orient='values')
    

#     return {
#         'prediction': predict_strain,
#         # 'description': description,
#         # 'rating': rating,
#         # 'effects': effects,
#         # 'flavors': flavors
#     }

# import logging, random, json, joblib, sklearn
# import tokenize
# from fastapi import APIRouter
# import pandas as pd
# from pydantic import BaseModel, Field

# # example = 'I am anxious'
# log = logging.getLogger(__name__)
# router = APIRouter()

# strains = pd.read_csv('data/strains.csv')
# list_of_strains = strains.name

# model = joblib.load('app/api/model.joblib')
# print('pickled model loaded')

# class Strain(BaseModel):
#     """Use this data model to parse the request body JSON."""

#     ailment: str
#     # kind: str = Field(..., example='Hybrid')
#     # effect: str = Field(..., example='Happy')
#     # flavor: str = Field(..., example='Blueberry')

#     def to_list(self):
#         """Convert pydantic object to pandas dataframe with 1 row."""
#         return [self]


# @router.post('/predict')
# async def predict(strain:Strain):

#     predict_strain = model.predict(strain.to_list())[0]
    
#     # predict_strain = predictor.predict([strain])
    
#     # # making a new df for our predicted value 
#     # y_pred_df = strains.loc[strains['name'] == predict_strain.upper()]
   
#     # # # description = y_pred_df.Description.to_string(index=False)
#     # description = y_pred_df.Description.to_json(orient='values')
#     # rating = float(y_pred_df.Rating)
#     # effects = y_pred_df.Effects.to_json(orient='values')
#     # flavors = y_pred_df.Flavor.to_json(orient='values')
    

#     return {
#         'prediction': predict_strain,
#         # 'description': description,
#         # 'rating': rating,
#         # 'effects': effects,
#         # 'flavors': flavors
#     }