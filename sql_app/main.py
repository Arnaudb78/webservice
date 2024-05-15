from fastapi import Depends, FastAPI, HTTPException  # Import des composants nécessaires de FastAPI
from sqlalchemy.orm import Session  # Import de Session pour la gestion des transactions avec la base de données
from typing import List  # Import pour définir le type List

from . import crud, models, schemas  # Import des modules locaux
from .base import SessionLocal, engine  # Import de la session de base de données et du moteur SQLAlchemy

models.Base.metadata.create_all(bind=engine)  # Création des tables dans la base de données si elles n'existent pas déjà

app = FastAPI()  # Création de l'instance de l'application FastAPI


# Fonction pour obtenir une session de base de données
def get_db():
    db = SessionLocal()  # Crée une session de base de données
    try:
        yield db  # Renvoie la session de base de données pour utilisation dans une fonction de gestionnaire de route
    finally:
        db.close()  # Ferme la session de base de données après son utilisation pour libérer les ressources


# Opération pour obtenir tous les artistes
@app.get("/artists/", response_model=List[schemas.Artiste])  # Définit une route GET pour récupérer tous les artistes
def read_artists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # skip et limit sont des paramètres de requête pour la pagination
    artists = crud.get_artists(db, skip=skip, limit=limit)  # Appelle la fonction pour récupérer tous les artistes
    print(artists)
    return artists  # Renvoie la liste des artistes



# Opération pour créer un nouvel artiste
@app.post("/artists/", response_model=schemas.Artiste)  # Définit une route POST pour créer un nouvel artiste
def create_artist(artist: schemas.ArtisteCreate, db: Session = Depends(get_db)):
    # artist est le corps de la requête, contenant les données du nouvel artiste
    return crud.create_artist(db=db, artist=artist)  # Appelle la fonction pour créer un nouvel artiste


# Opération pour obtenir les détails d'un artiste par ID
@app.get("/artists/{artist_id}/", response_model=schemas.Artiste)  # Définit une route GET pour récupérer un artiste par ID
def read_artist(artist_id: int, db: Session = Depends(get_db)):
    # artist_id est un paramètre de chemin dans l'URL, spécifiant l'ID de l'artiste à récupérer
    db_artist = crud.get_artist(db, artist_id=artist_id)  # Appelle la fonction pour récupérer un artiste par ID
    if db_artist is None:  # Vérifie si l'artiste existe
        raise HTTPException(status_code=404, detail="Artist not found")  # Renvoie une erreur 404 si l'artiste n'existe pas
    return db_artist  # Renvoie les détails de l'artiste


# Opération pour mettre à jour les détails d'un artiste par ID
@app.put("/artists/{artist_id}/", response_model=schemas.Artiste)  # Définit une route PUT pour mettre à jour un artiste par ID
def update_artist(artist_id: int, artist: schemas.ArtisteUpdate, db: Session = Depends(get_db)):
    # artist_id est un paramètre de chemin dans l'URL, spécifiant l'ID de l'artiste à mettre à jour
    db_artist = crud.get_artist(db, artist_id=artist_id)  # Appelle la fonction pour récupérer un artiste par ID
    if db_artist is None:  # Vérifie si l'artiste existe
        raise HTTPException(status_code=404, detail="Artist not found")  # Renvoie une erreur 404 si l'artiste n'existe pas
    return crud.update_artist(db=db, artist=artist, db_artist=db_artist)  # Appelle la fonction pour mettre à jour un artiste


# Opération pour supprimer un artiste par ID
@app.delete("/artists/{artist_id}/", response_model=schemas.Artiste)  # Définit une route DELETE pour supprimer un artiste par ID
def delete_artist(artist_id: int, db: Session = Depends(get_db)):
    # artist_id est un paramètre de chemin dans l'URL, spécifiant l'ID de l'artiste à supprimer
    db_artist = crud.get_artist(db, artist_id=artist_id)  # Appelle la fonction pour récupérer un artiste par ID
    if db_artist is None:  # Vérifie si l'artiste existe
        raise HTTPException(status_code=404, detail="Artist not found")  # Renvoie une erreur 404 si l'artiste n'existe pas
    return crud.delete_artist(db=db, db_artist=db_artist)  # Appelle la fonction pour supprimer un artiste


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}/", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.put("/users/{user_id}/", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db=db, user=user, db_user=db_user)


@app.delete("/users/{user_id}/", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, db_user=db_user)


@app.get("/search/artists/{query}", response_model=schemas.Artiste)
def get_user_by_name(artist_name: str, db: Session = Depends(get_db)):
    db_artists = crud.find_artist_by_name(db, artist_name=artist_name)
    if db_artists is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    return db_artists
