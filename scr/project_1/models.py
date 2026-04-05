from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship


class Base(DeclarativeBase): pass


class Book(Base):
    __tablename__ = "book"   
    
    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))  
    author_id = Column(Integer, ForeignKey("author.author_id"))
    genre_id = Column(Integer, ForeignKey("genre.genre_id"))
    price = Column(Numeric) 
    amount = Column(Integer)
    
    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")


class Author(Base):
    __tablename__ = "author"
    
    author_id = Column(Integer, primary_key=True, index=True)
    name_author = Column(String(100))
    
    books = relationship("Book", back_populates="author")


class Genre(Base):
    __tablename__ = "genre"
    
    genre_id = Column(Integer, primary_key=True, index=True)
    name_genre = Column(String(50))
    
    books = relationship("Book", back_populates="genre")


class Buy(Base):
    __tablename__ = "buy" 
    
    buy_id = Column(Integer, primary_key=True, index=True)
    buy_description = Column(String(200))
    client_id = Column(Integer, ForeignKey("client.client_id"))
    
    client = relationship("Client", back_populates="buys")
    items = relationship("BuyBook", back_populates="buy")


class BuyBook(Base):
    __tablename__ = "buy_book"
    
    buy_book_id = Column(Integer, primary_key=True, index=True)
    buy_id = Column(Integer, ForeignKey("buy.buy_id"))
    book_id = Column(Integer, ForeignKey("book.book_id"))
    amount = Column(Integer)
    
    buy = relationship("Buy", back_populates="items")
    book = relationship("Book")


class Client(Base):
    __tablename__ = "client"
    
    client_id = Column(Integer, primary_key=True, index=True)
    name_client = Column(String(100))
    city_id = Column(Integer, ForeignKey("city.city_id"))
    
    city = relationship("City", back_populates="clients")
    buys = relationship("Buy", back_populates="client")


class City(Base):
    __tablename__ = "city"
    
    city_id = Column(Integer, primary_key=True, index=True)
    name_city = Column(String(100))
    days_delivery = Column(Integer)
    
    clients = relationship("Client", back_populates="city")


class BuyStep(Base):
    __tablename__ = "buy_step"
    
    buy_step_id = Column(Integer, primary_key=True, index=True)
    buy_id = Column(Integer, ForeignKey("buy.buy_id"))
    step_id = Column(Integer, ForeignKey("step.step_id"))
    date_step_beg = Column(Date)
    date_step_end = Column(Date)
    
    buy = relationship("Buy")
    step = relationship("Step")


class Step(Base):
    __tablename__ = "step"
    
    step_id = Column(Integer, primary_key=True, index=True)
    name_step = Column(String(50))
    