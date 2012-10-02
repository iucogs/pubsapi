from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

import seppubs.config

# Create the database engine from config file
url = seppubs.config.get('sqlalchemy', 'url')
engine = create_engine(url, echo=False, pool_recycle=30) 

# configure the declarative syntax base
Base = declarative_base()
Base.metadata.bind = engine

# configure the default Session
Session = sessionmaker(bind=engine)
session = Session()

author_of = Table('author_of', Base.metadata,
    Column('author_id', Integer, ForeignKey('authors.author_id')),
    Column('citation_id', Integer, ForeignKey('citations.citation_id')),
    Column('poisiton_num', Integer)
    )

class Author(Base):
    __tablename__ = 'authors'

    author_id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    verified = Column(Boolean)

    def __init__(firstname, lastname, verified=False):
        self.firstname = firstname
        self.lastname = lastname
        self.verified = verified

    def __repr__(self):
        return "<Author %d: %s %s>" %\
            (self.author_id, self.firstname, self.lastname)

class Citation(Base):
    __tablename__ = 'citations'
    __table_args__ = {'autoload' : True}

    citation_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))

    authors = relationship("Author", secondary=author_of, backref='citations') 

    def __repr__(self):
        return "<Citation %d: %s (%s)>" %\
            (self.citation_id, self.title, self.year)

member_of_collection = Table('member_of_collection', Base.metadata,
    Column('collection_id', Integer, ForeignKey('collections.collection_id')),
    Column('citation_id', Integer, ForeignKey('citations.citation_id'))
    )

class Collection(Base):
    __tablename__ = 'collections'
    __table_args__ = {'autoload' : True}
    
    collection_id = Column(Integer, primary_key=True)
    collection_name = Column(String)
   
    # TODO: Fix bug so that owners are actually referenced by user_id
    # user_id = Column(Integer, ForeignKey('users.id'))

    citations = relationship("Citation", secondary=member_of_collection)

    def __repr__(self):
        return "<Collection %d: %s (%s)>" %\
            (self.collection_id, self.collection_name, self.owner)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    lastname = Column(String)
    firstname = Column(String)
    admin = Column(Boolean)
    cogs = Column(Boolean)

    def __repr__(self):
        return "<User %d: %s>" %\
            (self.id, self.username)

