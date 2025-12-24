from fastapi import FastAPI,HTTPException
from typing import Annotated,List
import uvicorn
from model import Contact,Createcontact,Updatecontact
from data_interactor import Queries


app = FastAPI()


contacts:list[Contact] = []

@app.get("/contacts")
def get_all_contacts() -> list[Contact]:
    contacts = Queries.get_all_contact()
    return contacts

@app.post("/contacts")
def create_new_contact(contact:Contact) -> dict:
    contacts = Queries.get_all_contact()
    contacts.append(contact)
    return {
            "messege":"the create new contact data work successsfully",
            "contact_id": contact.id
            }

@app.put("/contacts/{id}")
def update_existing_contact(id:int,contact:Contact) -> dict:
    contacts = Queries.get_all_contact()
    for updating in range(len(contacts)):
        if not contacts[updating].id == id:
            raise HTTPException(status_code=404, detail="ID not found")
        else:
            updating = contact 
            contacts.append(updating)
    return {"messege":"the updating work successsfully"}

@app.delete("/contacts/{id}")
def delete_contact() -> dict:
    contacts = Queries.get_all_contact()
    for removing in range(len(contacts)):
        if not contacts[removing].id == id:
            raise HTTPException(status_code=404, detail="ID not found")
        else:
            contacts.remove(contacts[removing])
    return {"messege":"the removing work successsfully"}



if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)