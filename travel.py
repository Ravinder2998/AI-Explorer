import ssl
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

# Ensure SSL module is available
try:
    ssl.create_default_context()
except AttributeError:
    print("Warning: SSL module is not properly configured.")

app = FastAPI()

class TravelRequest(BaseModel):
    budget: str
    duration: int
    destination: str
    start_date: date
    preferences: str = "No preferences provided"

def generate_itinerary(travel_request: TravelRequest):
    itinerary = f"""
    Travel Itinerary:
    Destination: {travel_request.destination}
    Budget: {travel_request.budget}
    Duration: {travel_request.duration} days
    Start Date: {travel_request.start_date}
    Preferences: {travel_request.preferences}

    Day 1: Explore the city center and visit top attractions.
    Day 2: Experience local cuisine and hidden gems.
    Day 3: Adventure activities or cultural experiences.
    Day 4: Relaxing day with nature or spa retreat.
    Day 5: Final shopping and departure.
    """
    return {"itinerary": itinerary}

@app.post("/generate-itinerary/")
def generate(travel_request: TravelRequest):
    return generate_itinerary(travel_request)
