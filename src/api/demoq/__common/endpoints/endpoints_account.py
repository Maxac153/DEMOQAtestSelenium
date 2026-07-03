from enum import Enum


class EndpointsAccount(Enum):
    # Account
    AUTHORIZED = "/Account/v1/Authorized"
    GENERATE_TOKEN = "/Account/v1/GenerateToken"
    CREATE_USER = "/Account/v1/User"
    DELETE_USER = "/Account/v1/User/"
    GET_USER = "/Account/v1/User/"
