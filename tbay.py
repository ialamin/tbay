from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship




class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=True)
    
    #relationship to items = many items/user
    items = relationship("Item", backref="user")
    #relationship to bids = many bids/user
    bids = relationship("Bid", backref="user")


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
    #relationship to user = many items/user
    user_id = Column(Integer, ForeignKey('user.id'),
                             nullable=False)
    #relationship to bid = many bids/item
    bids = relationship("Bid", backref="item")
    
                            
class Bid(Base):
    __tablename__ = "bids"
    
    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    
    #relationship to user = many bids/user
    user_id = Column(Integer, ForeignKey('user.id'),
                             nullable=False)
    #relationship to items = many bids/item
    item_id = Column(Integer, ForeignKey('item.id'),
                             nullable=False)
    
    
    
    
Base.metadata.drop_all(engine)

    
Base.metadata.create_all(engine)


john = User(name="John")
bill = User(name="Bill")
pam = User(name="Pam")
baseball = Item(name="baseball", user=john)
print("Made it this far")



session.add_all([john, bill, pam])
session.commit()








