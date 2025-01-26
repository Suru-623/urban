import uvicorn
from services.saveimg import saveimg
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to specific frontend origins for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Basic route to test the connection
@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI backend!"}


# Post route to accept data from the frontend
@app.post("/image-details")
async def get_image_details(req: Request):
    data = await req.json()
    print(data)
    lng = data['lng']
    lat = data['lat']
    
    return saveimg(lng, lat),


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    
    
    # const staticMapUrl = `https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/static/${lng},${lat},15,0/600x400?access_token=${mapboxgl.accessToken}&attribution=false&logo=false&marker=${lng},${lat};`;
#  uvicorn main:app --reload