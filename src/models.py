import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er


Base = declarative_base()

# association table son para relacionar dos tablas con dos keys
# association object si quieres relacionar dos tablas con datos iguales y diferentes

association_table = Table('Follower', Base.metadata,
    Column('user_from_id', ForeignKey('user.id'), primary_key=True),
    Column('user_to_id', ForeignKey('user.id'), primary_key=True)
)

class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    firstname = Column(String(120), nullable=False)
    lastname = Column(String(120),  nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    comment = relationship('Comment')
    post = relationship('Post')
    follower = relationship('Follower')

   
    


    #  def to_dict(self): 
    #     return {'<User %r>' % self.username} 

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    Comment_text = Column(String(80), nullable=True )
    user_id = Column(String(120), ForeignKey('user.id')) 
    post_id= Column(String(120), ForeignKey('post.id'))

    

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(120), ForeignKey('user.id'))
    comment = relationship('Comment')
    media = relationship('Media')


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type_media= Column(String(120), unique=True)
    url = Column(String(80), unique=True)
    post_id = Column(String(80), ForeignKey('post.id'))
    



   

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e