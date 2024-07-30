from fastapi import FastAPI
from mujtaba_charm.utils.sample import hello

app = FastAPI()

@app.get("/hello")
async def get_hello():
    """
    Prints a greeting message.

    Returns:
        dict: A dictionary containing a greeting message.
    """
    return {"message": hello()}

@app.get("/hello/{name}")
async def get_hello(name):
    """
    Prints a string greeting the name entered as parameter. If no name
    provided, it greets the world.

    Returns:
        dict: A dictionary containing a greeting message along with the name entered by the user.
    """
    return {"message": hello(name)}

@app.get("/health")
async def health_check():
    """
    Returns the health check status of the API.
    """
    return {"status": "ok"}
