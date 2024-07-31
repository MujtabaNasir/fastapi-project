from fastapi import FastAPI
import uvicorn
from mujtaba_charm.utils.sample import hello
import logging 

app = FastAPI()

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
logger = logging.getLogger(__name__)


@app.get("/hello")
async def get_hello():
    """
    Prints a greeting message.

    Returns:
        dict: A dictionary containing a greeting message.
    """
    logger.info("Handling /hello request")
    message = hello()
    logger.info(f"Returning message: {message}")
    return {"message": message}

@app.get("/hello/{name}")
async def get_hello(name):
    """
    Prints a string greeting the name entered as parameter. If no name
    provided, it greets the world.

    Returns:
        dict: A dictionary containing a greeting message along with the name entered by the user.
    """
    logger.info(f"Handling /hello/{name} request")
    message = hello(name)
    logger.info(f"Returning message: {message}")
    return {"message": message}


@app.get("/health")
async def health_check():
    """
    Returns the health check status of the API.
    """
    logger.info("Handling /health request")
    return {"status": "ok"}

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)