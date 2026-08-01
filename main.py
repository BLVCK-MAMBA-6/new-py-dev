"""
Core API Initialization Module
Author: Adeyemo Favour Olakunle
Description: Base configuration for FastAPI application and database client.
"""

import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client

# Initialize Application
app = FastAPI(
    title="Data Inference Pipeline",
    description="Backend routing for analytics and AI workflows.",
    version="1.0.0"
)

# Initialize Supabase Client
SUPABASE_URL = os.environ.get("SUPABASE_URL", "your-supabase-url")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "your-supabase-key")

try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
except Exception as e:
    print(f"Database initialization failed: {e}")

class HealthCheck(BaseModel):
    status: str
    version: str

@app.get("/", response_model=HealthCheck)
async def system_status():
    """
    Verifies that the server is active and receiving requests.
    """
    return HealthCheck(status="Operational", version="1.0.0")

@app.get("/api/v1/ping")
async def ping_database():
    """
    Checks the connection to the Supabase backend.
    """
    if not SUPABASE_URL or SUPABASE_URL == "your-supabase-url":
        raise HTTPException(status_code=503, detail="Database credentials not configured!")
    return {"message": "Database connection established!"}
