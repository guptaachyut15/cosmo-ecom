from fastapi import Depends
from fastapi.security import HTTPBearer


security = HTTPBearer()


def has_access(credentials=Depends(security)):
    """
    Code to check bearer token
    """
