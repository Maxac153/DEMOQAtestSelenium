from enum import Enum


class Endpoints(Enum):
    # Book Store
    GET_BOOKS = "/BookStore/v1/Books"
    CREATE_BOOKS = "/BookStore/v1/Books"
    DELETE_BOOKS = "/BookStore/v1/Books"
    GET_BOOK = "/BookStore/v1/Book"
    DELETE_BOOK = "/BookStore/v1/Book"
    UPDATE_BOOKS = "/BookStore/v1/Books/"
