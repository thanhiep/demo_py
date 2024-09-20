import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from decouple import config
from datetime import datetime, timedelta

JWT_SECRET = config("secret")
ACCESS_TOKEN_EXP = int(config("access_token_exp"))

JWT_ALGORITHM = config("algorithm")

REF_JWT_SECRET = config("ref_secret")
REFRESH_TOKEN_EXP = int(config("refresh_token_exp"))

SEVEN_DAYS_FROM_SECONDS = 7 * 24 * 60 * 60

def create_token(data: dict):
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXP)
    payload = {"data": data, "exp": expires}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token


def create_token_ref(data: dict):
    expires = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXP)
    payload = {"data": data, "exp": expires}
    token = jwt.encode(payload, REF_JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token


def decode_token(token: str):
    try:
        token_decode = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])   
        return token_decode
    
    except ExpiredSignatureError:
        return {"ExpiredToken": "Token has expired"}
    
    except InvalidTokenError:
        return {"InvalidToken": "Invalid token"}
    
    except Exception as e:
        return {"Error": str(e)}


def decode_token_ref(token: str):
    try:
        token_decode = jwt.decode(token, REF_JWT_SECRET, algorithms=[JWT_ALGORITHM]) 
        return token_decode
    
    except ExpiredSignatureError:
        return {"ExpiredToken": "Token has expired"}
    
    except InvalidTokenError:
        return {"InvalidToken": "Invalid token"}
    
    except Exception as e:
        return {"Error": str(e)}