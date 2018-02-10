from __init__ import db

class Fish(db.Model):
    __tablename__ = 'fish'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    feed_name = db.Column(db.String, db.ForeignKey('feed.name'))

    def __init__(self,name):
        self.name = name


class Feed(db.Model):

    __tablename__ = 'feed'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    impact = db.Column(db.String(80), nullable=False)
    fish = db.relationship("Fish", order_by="Fish.id", cascade="all, delete-orphan")
    supplier= db.relationship("Supplier", order_by="Supplier.id", cascade="all, delete-orphan")

    def __init__(self, name):
        self.name = name


class Supplier(db.Model):
    
    __tablename__ = 'supplier'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    telephone = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False) # bug
    feed_id = db.Column(db.Integer, db.ForeignKey('feed.id'))

    def __init__(self, name):
        self.name = name
