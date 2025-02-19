from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ✅ Enable CORS so the frontend can send requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains (or specify your frontend URL)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Define a Pydantic model for `POST` request data
class IPData(BaseModel):
    ip: str
    country: str
    city: str
    isp: str
    latitude: float
    longitude: float
    browser: str

# ✅ Allow both `GET` and `POST`
@app.get("/login")
async def login_get():
    """For testing via browser or curl (GET method)"""
    return {"message": "Please send data using POST method"}

@app.post("/login")
async def login_post(ip_data: IPData):
    """Receives public IP & location data from frontend (POST)"""
    return {
        "IP Address": ip_data.ip,
        "Location": {
            "Country": ip_data.country,
            "City": ip_data.city,
            "ISP": ip_data.isp,
            "Latitude": ip_data.latitude,
            "Longitude": ip_data.longitude
        },
        "Browser": ip_data.browser
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3039, reload=True)
