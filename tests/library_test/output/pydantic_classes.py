from datetime import datetime, date
from typing import List, Set
from pydantic import BaseModel

############################################
#
# The classes are defined here
#
############################################

class LibraryCreate(BaseModel):
    address: str
    name: str

 

class BookCreate(BaseModel):
    title: str
    pages: int
    release: datetime
    authors_id: List[int]
    library_id: int

 

class AuthorCreate(BaseModel):
    name: str
    email: str
    books_id: List[int]

 

