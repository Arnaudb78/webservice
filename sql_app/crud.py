from sqlalchemy.orm import Session  # Import de la Session pour la gestion des transactions avec la base de données
from . import models, schemas  # Import des modules locaux contenant les modèles SQLAlchemy et les schémas Pydantic


def get_artists(db: Session, skip: int = 0, limit: int = 100):
    """
    Fonction pour récupérer tous les artistes de la base de données.

    :param db: Session de base de données
    :param skip: Nombre d'artistes à sauter (pour la pagination)
    :param limit: Limite du nombre d'artistes à récupérer (pour la pagination)
    :return: Liste des artistes récupérés
    """
    return db.query(models.Artiste).offset(skip).limit(limit).all()



def create_artist(db: Session, artist: schemas.ArtisteCreate):
    """
    Fonction pour créer un nouvel artiste dans la base de données.

    :param db: Session de base de données
    :param artist: Données de l'artiste à créer
    :return: L'artiste créé
    """
    db_artist = models.Artiste(**artist.dict())  # Crée une instance de l'artiste à partir des données reçues
    db.add(db_artist)  # Ajoute l'artiste à la session de base de données
    db.commit()  # Valide la transaction dans la base de données
    db.refresh(db_artist)  # Rafraîchit l'objet artiste avec les valeurs de la base de données
    return (artist.dict())  # Renvoie l'artiste créé


def get_artist(db: Session, artist_id: int):
    """
    Fonction pour récupérer un artiste par ID dans la base de données.

    :param db: Session de base de données
    :param artist_id: ID de l'artiste à récupérer
    :return: L'artiste récupéré ou None s'il n'existe pas
    """
    return db.query(models.Artiste).filter(models.Artiste.id == artist_id).first()


def update_artist(db: Session, artist: schemas.ArtisteUpdate, db_artist: models.Artiste):
    """
    Fonction pour mettre à jour les détails d'un artiste dans la base de données.

    :param db: Session de base de données
    :param artist: Données de mise à jour de l'artiste
    :param db_artist: Artiste à mettre à jour
    :return: L'artiste mis à jour
    """
    for var, value in vars(artist).items():  # Parcourt chaque attribut de l'objet artiste reçu
        if value is not None:  # Vérifie si la valeur de l'attribut est non nulle
            setattr(db_artist, var, value)  # Met à jour l'attribut correspondant de l'artiste dans la base de données
    db.commit()  # Valide la transaction dans la base de données
    db.refresh(db_artist)  # Rafraîchit l'objet artiste avec les valeurs de la base de données
    return (artist.dict())  # Renvoie l'artiste mis à jour


def delete_artist(db: Session, db_artist: models.Artiste):
    """
    Fonction pour supprimer un artiste de la base de données.

    :param db: Session de base de données
    :param db_artist: Artiste à supprimer
    :return: L'artiste supprimé
    """
    db.delete(db_artist)  # Supprime l'artiste de la session de base de données
    db.commit()  # Valide la transaction dans la base de données
    return db_artist.dict() # Renvoie l'artiste supprimé


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return (user.dict())


def update_user(db: Session, user: schemas.UserUpdate, db_user: models.User):
    for var, value in vars(user).items():
        if value is not None:
            setattr(db_user, var, value)
    db.commit()
    db.refresh(db_user)
    return (user.dict())


def delete_user(db: Session, db_user: models.User):
    db.delete(db_user)
    db.commit()
    return (db_user.dict())


def find_artist_by_name(db: Session, artist_name: str):
    return db.query(models.Artiste).filter(models.Artiste.nom == artist_name).first()
