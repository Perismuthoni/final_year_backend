# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from enum import unique
from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

# Define a User model
class User(Base):

    __tablename__ = 'auth_user'
    usr_id = db.column(db.bigint, unique= True)
    usr_name    = db.Column(db.String(128),  nullable=False)
    usr_username    = db.Column(db.String(128),  nullable=False)
    usr_email    = db.Column(db.String(128),  nullable=False, unique=True)
    usr_password = db.Column(db.String(192),  nullable=False)
    usr_role     = db.Column(db.SmallInteger, nullable=False)
    usr_status   = db.Column(db.SmallInteger, nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password):

        self.name     = name
        self.email    = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)  
class business(Base):
    __tablename__ = 'business'
    bsn_name   = db.Column(db.string(128), nullable=False)
    bsn_location = db.Column(db.string(128))
    bsn_longitude = db.column(db.integer)
    bsn_latittude = db.column(db.integer)
    bsn_registration_date = db.Column(db.DateTime)
    bsn_owner_id = db.Column(db.bigint, db.ForeignKey('usr.id'))    

    class delivery(Base):
        __tablename__ = 'delivery'
    d_id = db.Column(db.integer, primary_key=True)
    d_name   = db.Column(db.string(128),db.ForeignKey('usr_name'), nullable=False, )
    d_registration_date = db.Column(db.DateTime)
    d_owner_id = db.Column(db.bigint, db.ForeignKey('usr.id'))

        