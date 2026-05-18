from fastapi import FastAPI
from app.routers import auth, users, places, wishlists, trips, reviews

app = FastAPI(title="TravelGuide")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(places.router)
app.include_router(wishlists.router)
app.include_router(trips.router)
app.include_router(reviews.router)


@app.get("/")
async def root():
    return {"message": "TravelGuide API is running"}