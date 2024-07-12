from decouple import config
from dataclasses import dataclass


@dataclass
class Env:
    # Get tokens and keys from env.

    # MongoDB Config
    MDB_SRV = config("MDB_SRV")
    DB_NAME = config("DB_NAME")
    CSRF_KEY = config("CSRF_KEY")
    PORT = config("PORT", cast=int)
