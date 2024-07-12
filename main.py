from uvicorn import run

from src.utils.env import Env

if __name__ == "__main__":
    run("src.server:app", host="127.0.0.1", port=Env.PORT, reload=True)
