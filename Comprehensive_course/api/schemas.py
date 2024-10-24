import os

import motor.motor_asyncio
from dotenv import load_dotenv
from pydantic import BaseModel, Field, EmailStr, ConfigDict
from pydantic.functional_validators import BeforeValidator


from typing import Optional
from typing_extensions import Annotated
from bson import ObjectId


load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"))

db = client.blog_api

# mongo uses BSON and fastapi uses JSON
PyObjectId = Annotated[str, BeforeValidator(str)]


class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    email: EmailStr =  Field(...)
    password: str = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed = True,
        json_encoders={ObjectId: str},
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "jdoe@example.com",
                "password": "secret_code"
            }
        }
    )

class UserResponse(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    email: EmailStr =  Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed = True,
        json_encoders={ObjectId: str},
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "jdoe@example.com",
            }
        }
    )


class TokenData(BaseModel):
    id: str | None = None

class PasswordReset(BaseModel):
    email: EmailStr