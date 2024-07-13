from decouple import config
from dataclasses import dataclass


@dataclass
class Env:
    # Get tokens and keys from env.

    # MongoDB Config
    MDB_SRV = config("MDB_SRV")
    DB_NAME = config("DB_NAME")
    CSRF_KEY = config("CSRF_KEY")
    DEV = config("DEV", cast=bool)
    LITESTAR_PORT = config("LITESTAR_PORT", cast=int)
    LITESTAR_HOST = config("LITESTAR_HOST")
