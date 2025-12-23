from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import Annotated,List
import uvicorn

app = FastAPI()



class Contact(BaseModel):
    id:int | None = None
    first_name:Annotated[str,Field(max_length=50)]
    last_name:Annotated[str,Field(max_length=50)]
    phone_number:Annotated[str,Field(max_length=20)]

contacts:list[Contact] = []

@app.get("/contacts")
def get_all_contacts() -> list:
    return contacts

@app.post("/contacts")
def create_new_contact(contact:Contact):
    contacts.append(contact)
    return {"messege":"the create new contact data work successsfully",
            "contact_id": contact.id
            }

@app.put("/contacts/{id}")
def update_existing_contact(id,contact:Contact):
    for updating in contacts:
        if not updating.id == id:
            raise HTTPException(status_code=404, detail="ID not found")
        else:
            contacts.append(contact)
    return {"messege":"the updating work successsfully"}

@app.delete("/contacts/{id}")
def delete_contact():
    for removing in contacts:
        if not removing.id == id:
            raise HTTPException(status_code=404, detail="ID not found")
        else:
            contacts.remove(removing)
    return {"messege":"the removing work successsfully"}



if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)