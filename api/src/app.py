from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import account_router, invoice_router


app = FastAPI(
    title="FastAPI Gateway API",
    description="API Gateway for managing accounts, invoices, and credit cards",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(account_router.router)
app.include_router(invoice_router.router)



@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Gateway API"} 