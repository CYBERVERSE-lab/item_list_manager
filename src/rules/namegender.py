from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.namegender import NameGender
from bson import ObjectId


def get_collection_grocery_data(request: Request):
    return request.app.db['grocery_data']  # Specify the collection name

def getNameAndGender(request: Request, name: str):
    # Getting the collection
    collection = get_collection_grocery_data(request)
    
    # Querying the collection for the user with the given name
    user = collection.find_one({"first_name": name}, {"_id": 0, "first_name": 1, "last_name": 1, "gender": 1})
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    # Returning the result
    return user

def updateFirstName(request: Request, first_name: str, new_first_name: str):
    # Getting the collection
    collection = get_collection_grocery_data(request)
    
    # Querying the collection for the user with the given name
    user = collection.find_one({"first_name": first_name})
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    # Updating the user's first name
    collection.update_one({"first_name": first_name}, {"$set": {"first_name": new_first_name}})
    
    # Returning the updated user
    return collection.find_one({"first_name": new_first_name}, {"_id": 0, "first_name": 1, "last_name": 1, "gender": 1})

def updateLastName(request: Request, last_name: str, new_last_name: str):
    # Getting the collection
    collection = get_collection_grocery_data(request)
    
    # Querying the collection for the user with the given name
    user = collection.find_one({"last_name": last_name})
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    # Updating the user's first name
    collection.update_one({"last_name": last_name}, {"$set": {"last_name": new_last_name}})
    
    # Returning the updated user
    return collection.find_one({"last_name": new_last_name}, {"_id": 0, "first_name": 1, "last_name": 1, "gender": 1})

def updateGender(request: Request, gender: str, new_gender: str):
    # Getting the collection
    collection = get_collection_grocery_data(request)
    
    # Querying the collection for the user with the given name
    user = collection.find_one({"gender": gender})
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    # Updating the user's first name
    collection.update_one({"gender": gender}, {"$set": {"gender": new_gender}})
    
    # Returning the updated user
    return collection.find_one({"gender": new_gender}, {"_id": 0, "first_name": 1, "last_name": 1, "gender": 1})