import time
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

REF_JWT_SECRET = config("ref_secret")

SEVEN_DAYS_IN_SECONDS = 7 * 24 * 60 * 60

def token_response(token: str):
    return {"access token": token}


def create_token(userID: str):
    payload = {"userID": userID, "expires": time.time() + 600}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def create_token_ref(userID: str):
    payload = {"userID": userID, "expires": time.time() + SEVEN_DAYS_IN_SECONDS}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decode_token(token:str):
    try:
        token_decode = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return token_decode if token_decode["expires"] >= time.time() else None
    except:
        return {}