from pydantic import BaseModel,Field
from typing import Annotated,List


class Contact(BaseModel):
    id:int | None = None
    first_name:Annotated[str,Field(max_length=50)]
    last_name:Annotated[str,Field(max_length=50)]
    phone_number:Annotated[str,Field(max_length=20)]

class Createcontact(BaseModel):
    first_name:Annotated[str,Field(max_length=50)]
    last_name:Annotated[str,Field(max_length=50)]
    phone_number:Annotated[str,Field(max_length=20)]

class Updatecontact(BaseModel):
    first_name:Annotated[str,Field(max_length=50)]
    last_name:Annotated[str,Field(max_length=50)]
    phone_number:Annotated[str,Field(max_length=20)]