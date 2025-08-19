#!/usr/bin/env python3
"""
Simple script to run the FastAPI earthquake forecasting backend
"""

import uvicorn

if __name__ == "__main__":
    print("🚀 Starting Earthquake Forecasting API Backend...")
    print("📍 API will be available at: http://localhost:8000")
    print("📚 API documentation at: http://localhost:8000/docs")
    print("🔍 Health check at: http://localhost:8000/health")
    print("\nPress Ctrl+C to stop the server\n")
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )