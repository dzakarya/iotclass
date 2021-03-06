from pydantic import BaseModel
from .http_response import HTTPResponseWrapper,ErrorMessage

class GetValue(BaseModel):
    value : int

class ResponseGetValue(HTTPResponseWrapper):
    data: GetValue = None
    meta: ErrorMessage = None

class GetLightValue(BaseModel):
    zone1 : int
    zone2 : int

class ResponseGetLightValue(ResponseGetValue):
    data: GetLightValue = None
    meta: ErrorMessage = None