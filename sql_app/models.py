from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .base import Base  # Import de la classe Base à partir de votre fichier database.py


# Fichier permettant de définir les class utilisées dans la BDD
# Classe représentant la table tb_artiste
class Artiste(Base):
    __tablename__ = "tb_artiste"  # Nom de la table dans la base de données

    id = Column(Integer, primary_key=True, name="at_id")  # Colonne pour l'ID de l'artiste
    nom = Column(String(50), nullable=False, name="at_nom")  # Colonne pour le nom de l'artiste
    prenom = Column(String(50), name="at_prenom")  # Colonne pour le prénom de l'artiste
    nationalite = Column(String(100), name="at_nationalite")  # Colonne pour la nationalité de l'artiste
    genre = Column(String(50), nullable=False, name="at_genre")  # Colonne pour le genre musical de l'artiste
    biographie = Column(Text, name="at_biographie")  # Colonne pour la biographie de l'artiste


# Classe représentant la table tb_user
class User(Base):
    __tablename__ = "tb_user"  # Nom de la table dans la base de données

    id = Column(Integer, primary_key=True, name="us_id")  # Colonne pour l'ID de l'utilisateur
    nom = Column(String(50), nullable=False, name="us_nom")  # Colonne pour le nom de l'utilisateur
    prenom = Column(String(100), name="us_prenom")  # Colonne pour le prénom de l'utilisateur
    birthday = Column(Date, name="us_birthday")  # Colonne pour la date de naissance de l'utilisateur
    email = Column(String(100), nullable=False, unique=True, name="us_email")  # Colonne pour l'email de l'utilisateur
    address = Column(String(100), name="us_address")  # Colonne pour l'adresse de l'utilisateur


# Classe représentant la table tb_label
class Label(Base):
    __tablename__ = "tb_label"  # Nom de la table dans la base de données

    id = Column(Integer, primary_key=True, name="lb_id")  # Colonne pour l'ID du label
    nom = Column(String(50), nullable=False, name="lb_nom")  # Colonne pour le nom du label
    pays = Column(String(50), name="lb_pays")  # Colonne pour le pays du label
    date_de_creation = Column(Date, name="lb_DateDeCreation")  # Colonne pour la date de création du label


# Classe représentant la table tb_album
class Album(Base):
    __tablename__ = "tb_album"  # Nom de la table dans la base de données

    id = Column(Integer, primary_key=True, name="ab_id")  # Colonne pour l'ID de l'album
    id_artiste = Column(Integer, ForeignKey("tb_artiste.at_id"), name="ab_id_artiste")  # Colonne pour l'ID de l'artiste associé à l'album
    titre = Column(String(100), nullable=False, name="ab_titre")  # Colonne pour le titre de l'album
    annee = Column(Integer, nullable=False, name="ab_annee")  # Colonne pour l'année de l'album

    artiste = relationship("Artiste")  # Relation avec la classe Artiste


# Classe représentant la table tb_song
class Song(Base):
    __tablename__ = "tb_song"  # Nom de la table dans la base de données

    id = Column(Integer, primary_key=True, name="sg_id")  # Colonne pour l'ID de la chanson
    id_album = Column(Integer, ForeignKey("tb_album.ab_id"), name="sg_id_album")  # Colonne pour l'ID de l'album associé à la chanson
    titre = Column(String(50), nullable=False, name="sg_titre")  # Colonne pour le titre de la chanson
    date_de_sortie = Column(Date, nullable=False, name="sg_DateDeSortie")  # Colonne pour la date de sortie de la chanson

    album = relationship("Album")  # Relation avec la classe Album


# Classe représentant la table tb_playlist
class Playlist(Base):
    __tablename__ = "tb_playlist"  # Nom de la table dans la base de données

    id = Column(Integer, primary_key=True, name="pl_id")  # Colonne pour l'ID de la playlist
    id_user = Column(Integer, ForeignKey("tb_user.us_id"), name="pl_id_user")  # Colonne pour l'ID de l'utilisateur associé à la playlist
    titre = Column(String(50), nullable=False, name="pl_titre")  # Colonne pour le titre de la playlist
    description = Column(Text, name="pl_description")  # Colonne pour la description de la playlist

    user = relationship("User")  # Relation avec la classe User


# Classe représentant la table tb_collaborer
class Collaborer(Base):
    __tablename__ = "tb_collaborer"  # Nom de la table dans la base de données

    id_artiste = Column(Integer, ForeignKey("tb_artiste.at_id"), primary_key=True, name="cl_id_artiste")  # Colonne pour l'ID de l'artiste
    id_song = Column(Integer, ForeignKey("tb_song.sg_id"), primary_key=True, name="cl_id_song")  # Colonne pour l'ID de la chanson


# Classe représentant la table tb_suivre
class Suivre(Base):
    __tablename__ = "tb_suivre"  # Nom de la table dans la base de données

    id_artiste = Column(Integer, ForeignKey("tb_artiste.at_id"), primary_key=True, name="su_id_artiste")  # Colonne pour l'ID de l'artiste
    id_user = Column(Integer, ForeignKey("tb_user.us_id"), primary_key=True, name="su_id_user")  # Colonne pour l'ID de l'utilisateur


# Classe représentant la table tb_affilier
class Affilier(Base):
    __tablename__ = "tb_affilier"  # Nom de la table dans la base de données

    id_artiste = Column(Integer, ForeignKey("tb_artiste.at_id"), primary_key=True, name="af_id_artiste")  # Colonne pour l'ID de l'artiste
    id_label = Column(Integer, ForeignKey("tb_label.lb_id"), primary_key=True, name="af_id_label")  # Colonne pour l'ID du label


# Classe représentant la table tb_partager
class Partager(Base):
    __tablename__ = "tb_partager"  # Nom de la table dans la base de données

    id_user = Column(Integer, ForeignKey("tb_user.us_id"), primary_key=True, name="pa_id_user")  # Colonne pour l'ID de l'utilisateur
    id_playlist = Column(Integer, ForeignKey("tb_playlist.pl_id"), primary_key=True, name="pa_id_playlist")  # Colonne pour l'ID de la playlist


# Classe représentant la table tb_detenir
class Detenir(Base):
    __tablename__ = "tb_detenir"  # Nom de la table dans la base de données

    id_song = Column(Integer, ForeignKey("tb_song.sg_id"), primary_key=True, name="de_id_song")  # Colonne pour l'ID de la chanson
    id_playlist = Column(Integer, ForeignKey("tb_playlist.pl_id"), primary_key=True, name="de_id_playlist")  # Colonne pour l'ID de la playlist
