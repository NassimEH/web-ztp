from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from env import FRONTEND_URL
from routers import device, template, dhcp

app = FastAPI()

# Configuration CORS
app.add_middleware(CORSMiddleware, allow_origins=[FRONTEND_URL], allow_credentials=True)

# Inclusion des routes
app.include_router(device.router)
app.include_router(template.router)
app.include_router(dhcp.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
