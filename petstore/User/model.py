
import os
import sys
from sqlalchemy.exc import SQLAlchemyError
sys.path.append(os.getcwd() + '/..')
from petstore.app import db
from sqlalchemy.orm import sessionmaker, relationship

#Order_Pet = db.Table('Order_Pet', db.metadata,
#    db.Column('order_id', db.Integer, db.ForeignKey('Order.id')),
#    db.Column('pet_id', db.Integer, db.ForeignKey('Pet.id'))
#)

class Order(db.Model):
    __tablename__ = 'Order'
    id = db.Column(db.Integer(), primary_key=True)
    petId =  db.Column(db.Integer, db.ForeignKey('Pet.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    shipDate = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), nullable=False)
    complete = db.Column(db.Boolean, nullable=False)
    pet = relationship("Pet", back_populates="order")

#    Pet = db.relationship("Pet", back_populates="Order")
#   pet = db.relationship('Pet', secondary=Order_Pet, backref=db.backref('Order', lazy='dynamic'), lazy='dynamic')

Pet_Order = db.Table('Pet_Order', db.metadata,
    db.Column('pet_id', db.Integer, db.ForeignKey('Pet.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('Category.id'))
)

Pet_Tag = db.Table('Pet_Tag', db.metadata,
    db.Column('pet_id', db.Integer, db.ForeignKey('Pet.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('Tag.id'))
)


class Pet(db.Model):
    __tablename__ = 'Pet'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    category = relationship('Category', backref="Pet",secondary=Pet_Order,  lazy=True )
    photoUrls = db.Column(db.String(120), nullable=False)
    tags = relationship('Tag', backref='Pet',secondary=Pet_Tag, lazy=True)
    status = db.Column(db.String(120), nullable=False)
  #  Order = db.relationship('Order', back_populates='Pet', lazy=True)    
    order = relationship("Order", back_populates="pet" ,lazy='dynamic', primaryjoin="Pet.id == Order.petId")
    

class Category(db.Model):
    __tablename__ = 'Category'
    id = db.Column(db.Integer(), primary_key=True)
    name= db.Column(db.String(120), nullable=False)
   # pet = relationship("Pet", back_populates="category" , primaryjoin="Pet.category == Category.id ")




class Tag(db.Model):
    __tablename__ = 'Tag'
    id = db.Column(db.Integer(), primary_key=True)
    name= db.Column(db.String(120), nullable=False)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    firstName = db.Column(db.String(120), nullable=False)
    lastName = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    userStatus = db.Column(db.Integer, nullable=False)

Customer_Address = db.Table('Customer_Address', db.metadata,
    db.Column('customer_id', db.Integer, db.ForeignKey('Customer.id')),
    db.Column('address_id', db.Integer, db.ForeignKey('Address.id'))
)


class Customer(db.Model):
    __tablename__ = 'Customer'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    address = relationship('Address', backref='Customer',secondary=Customer_Address, lazy=True)

class Address(db.Model):
    __tablename__ = 'Address'
    id= db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    zip = db.Column(db.String(120), nullable=False)

