from datetime import date
from pydantic import (
    BaseModel, Field, validator)


class NotificationSchema(BaseModel):
    
    title : str = Field(
        ..., title = "Title") 
    content : str = Field(
        ..., title = "Content")
    date : date = Field(
        ..., title = "Date")
    
    
    @validator("title")
    def validate_title(cls, value : str):
        
        if len(value) <= 2:
            raise ValueError("Invalid notification title.")
        
        return value
    
    
    @validator("content")
    def validate_content(cls, value : str):
        space_count = len(value.split(" "))
        
        if len(space_count) <= 5:
            raise ValueError("Invalid notification content.")
        
        return value