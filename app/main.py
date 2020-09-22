from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import predict, data, effects, ailments, flavors, types, ratings

app = FastAPI(
    title='MED CAB DS API',
    description='Recommend medical cannabis strain based on User input.',
    version='0.1',
    docs_url='/',
)

app.include_router(predict.router)
app.include_router(data.router)
app.include_router(effects.router)
app.include_router(ailments.router)
app.include_router(flavors.router)
app.include_router(types.router)
app.include_router(ratings.router)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex='https?://.*',
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
