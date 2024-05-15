from pydantic import BaseModel
from typing import List, Optional
from pydantic import BaseModel, EmailStr
from datetime import date

# Créer les class dont vous avez besoin dans votre API


# Schéma Pydantic pour représenter les données d'un artiste lors de la récupération
class Artiste(BaseModel):
    id: int
    nom: str
    prenom: str | None  = None
    nationalite: Optional[str] = None
    genre: str
    biographie: Optional[str] = None


# Schéma Pydantic pour représenter les données d'un artiste lors de la création
class ArtisteCreate(BaseModel):
    id: int
    nom: str
    prenom : str | None  = None
    nationalite: Optional[str] = None
    genre: str
    biographie: Optional[str] = None


# Schéma Pydantic pour représenter les données de mise à jour d'un artiste
class ArtisteUpdate(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    nationalite: Optional[str] = None
    genre: Optional[str] = None
    biographie: Optional[str] = None


# Schéma Pydantic pour représenter les données d'un utilisateur lors de la récupération
class User(BaseModel):
    id: int
    nom: str
    prenom:  Optional[str] = None
    birthday: date
    email: str
    address: Optional[str] = None


class UserCreate(BaseModel):
    id: int
    nom: str
    prenom:  Optional[str] = None
    birthday: Optional[date] = None
    email: EmailStr
    address: Optional[str] = None


class UserUpdate(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    birthday: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
