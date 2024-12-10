import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key = True)
    from_id = Column(Integer, ForeignKey('users.id'))
    from_user = Column(Integer, ForeignKey('users.id'))
    to_id = relationship('Users', foreign_keys=[from_id], backref= 'follower')
    to_user = relationship('Users', foreign_keys=[from_id], backref= 'following')

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    full_name = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    born_date = Column(Integer, nullable = False)
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship('Location', backref= 'users')

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "born_date": self.born_date
        }
    

class Posts(Base):
     __tablename__ = 'posts'
     id = Column(Integer, primary_key = True)
     title = Column(String, nullable = False)
     content = Column(String, nullable = False)
     user_id = Column(Integer, ForeignKey('users.id'))
     user = relationship('Users', backref = 'posts')
     location_id = Column(Integer, ForeignKey('location.id'))
     location = relationship('Location', backref= 'posts')

     def to_dict(self):
         return {
             "id": self.id,
             "title": self.title,
             "content": self.content
         }

class Comments(Base):
     __tablename__ = 'comments'
     id = Column(Integer, primary_key = True)
     content = Column(String, nullable = False)
     user_id = Column(Integer, ForeignKey('users.id'))
     user = relationship('Users', backref = 'comments')
     post_id = Column(Integer, ForeignKey('posts.id'))
     post = relationship('Posts', backref = 'comments' )

     def to_dict(self):
         return {
             "id": self.id,
             "content": self.content
         }
class Medias(Base):
     __tablename__ = 'medias'
     id = Column(Integer, primary_key = True)
     src = Column(String, nullable = False)
     post_id = Column(Integer, ForeignKey('posts.id'))
     post = relationship('Posts', backref = 'medias' )

     def to_dict(self):
         return {
             "id": self.id,
             "src": self.src
         }
     
class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    address = Column(String, nullable = True) 

    def to_dict(self):
         return {
             "id": self.id,
             "src": self.name,
             "address": self.address
         }

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
