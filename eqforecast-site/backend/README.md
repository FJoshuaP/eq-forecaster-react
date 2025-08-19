# Earthquake Forecasting API Backend

This is the FastAPI backend for the earthquake forecasting system. Currently, it provides the basic API structure with sample data.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Server
```bash
# Option 1: Using the run script
python run.py

# Option 2: Direct uvicorn command
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Access the API
- **API Base URL**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 📋 Available Endpoints

### Core Endpoints
- `GET /` - API information
- `GET /health` - Health check
- `GET /api/status` - Overall API status

### Data Endpoints
- `GET /api/regions` - Get Philippine regions
- `GET /api/earthquakes` - Get earthquake data (with filters)
- `GET /api/statistics` - Get statistical information
- `GET /api/model-info` - Get ML model information

## 🔧 Development Status

**Current Phase**: Basic API Structure ✅
- FastAPI server running
- Sample earthquake data
- Basic endpoints implemented
- CORS configured for frontend

**Next Phase**: ML Model Integration
- Implement Attention-LSTM model
- Add real PHIVOLCS data
- Implement prediction endpoints
- Add data validation

## 📊 Sample Data

The API currently uses sample earthquake data for development:
- 3 sample earthquakes in different regions
- 17 Philippine regions with metadata
- Basic filtering and statistics

## 🛠️ Project Structure

```
backend/
├── main.py              # Main FastAPI application
├── run.py               # Server startup script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🔮 Future Features

- [ ] Real PHIVOLCS data integration
- [ ] Attention-LSTM model implementation
- [ ] Earthquake magnitude prediction
- [ ] Confidence intervals and risk assessment
- [ ] Data validation and error handling
- [ ] Database integration
- [ ] Authentication and rate limiting

## 🐛 Troubleshooting

If you encounter issues:

1. **Port already in use**: Change the port in `run.py` or kill existing processes
2. **Import errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
3. **CORS issues**: Check that your frontend URL is in the allowed origins in `main.py`

## 📝 Notes

- This is a development setup with sample data
- The ML model is not yet implemented
- All endpoints return sample/placeholder data
- Designed to work with the React frontend in the parent directory