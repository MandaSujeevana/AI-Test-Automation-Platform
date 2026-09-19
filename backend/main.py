from fastapi import FastAPI
from pydantic import BaseModel

# Create the FastAPI application instance
app = FastAPI(title="AI-Powered Test Automation Platform")


# Define a Pydantic model for request data validation
class User(BaseModel):
    name: str
    email: str


@app.get("/")
def read_root():
    """Root endpoint returning a project identification message."""
    return {"message": "Welcome to the AI-Powered Test Automation Platform API"}


@app.get("/health")
def health_check():
    """Health check endpoint to verify backend service status."""
    return {"status": "healthy"}


@app.post("/users")
def create_user(user: User):
    """POST endpoint to create a new user."""
    return {
        "message": "User created successfully",
        "user": {
            "name": user.name,
            "email": user.email,
        },
    }
