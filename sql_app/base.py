from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Fichier utiliser pour définir l'accès à la base de données
# pip install mysql-connector-python
# pip install sqlalchemy

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://myuser:myuserpassword@localhost/mydatabase"

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
