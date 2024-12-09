import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False, unique=True)

    favorites = relationship('Favorite', back_populates='user')

class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(String(50), nullable=False)
    mass = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    skin_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    birth_year = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)


    specie_id = Column(Integer, ForeignKey('specie.id'))
    specie = relationship('Specie', back_populates='characters')

    homeworld_id = Column(Integer, ForeignKey('planet.id'))
    homeworld = relationship('Planet', back_populates='residents')

    favorites = relationship('Favorite', back_populates='character')

# Tabla 'Planet'
class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(String(50), nullable=False)
    rotation_period = Column(String(50), nullable=False)
    orbital_period = Column(String(50), nullable=False)
    gravity = Column(String(50), nullable=False)
    population = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    surface_water = Column(String(50), nullable=False)

    residents = relationship('Character', back_populates='homeworld')

    favorites = relationship('Favorite', back_populates='planet')

# Tabla 'Specie'
class Specie(Base):
    __tablename__ = 'specie'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    classification = Column(String(50), nullable=False)
    designation = Column(String(50), nullable=False)
    average_height = Column(String(50), nullable=False)
    average_lifespan = Column(String(50), nullable=False)
    hair_colors = Column(String(50), nullable=False)
    skin_colors = Column(String(50), nullable=False)
    eye_colors = Column(String(50), nullable=False)
    language = Column(String(50), nullable=False)
    description = Column(String(250), nullable=False)

    characters = relationship('Character', back_populates='specie')

    favorites = relationship('Favorite', back_populates='specie')

class Starship(Base):
    __tablename__ = 'starship'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    starship_class = Column(String(50), nullable=False)
    manufacturer = Column(String(50), nullable=False)
    cost_in_credits = Column(String(50), nullable=False)
    length = Column(String(50), nullable=False)
    crew = Column(String(50), nullable=False)
    passengers = Column(String(50), nullable=False)
    max_atmosphering_speed = Column(String(50), nullable=False)
    hyperdrive_rating = Column(String(50), nullable=False)
    MGLT = Column(String(50), nullable=False)
    cargo_capacity = Column(String(50), nullable=False)
    description = Column(String(250), nullable=False)

    favorites = relationship('Favorite', back_populates='starship')

class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    vehicle_class = Column(String(50), nullable=False)
    manufacturer = Column(String(50), nullable=False)
    cost_in_credits = Column(String(50), nullable=False)
    length = Column(String(50), nullable=False)
    crew = Column(String(50), nullable=False)
    passengers = Column(String(50), nullable=False)
    max_atmosphering_speed = Column(String(50), nullable=False)
    cargo_capacity = Column(String(50), nullable=False)
    consumables = Column(String(50), nullable=False)
    description = Column(String(250), nullable=False)

    favorites = relationship('Favorite', back_populates='vehicle')

class Favorite(Base):
    __tablename__ = 'favorite'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)
    starship_id = Column(Integer, ForeignKey('starship.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    specie_id = Column(Integer, ForeignKey('specie.id'), nullable=True)

    user = relationship('User', back_populates='favorites')
    character = relationship('Character', back_populates='favorites')
    vehicle = relationship('Vehicle', back_populates='favorites')
    starship = relationship('Starship', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')
    specie = relationship('Specie', back_populates='favorites')

    def to_dict(self):
        return {}

render_er(Base, 'diagram.png')