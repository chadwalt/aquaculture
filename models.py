from app import db

class Fish(db.Model):
    __tablename__ = 'fish'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(80), nullable=False)
    feed_name = db.Column(Integer, ForeignKey=(Feed.name))

    def __init__(self,name):
        self.name = name


class Feed(db.Model):

    __tablename__ = 'feed'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(80), nullable=False)
    impact = db.Column(String(80), nullable=False)
    fish = relationship("Fish",order_by="Fish.id", cascade="all, delete-orphan")
    supplier= relationship("Supplier",order_by="Supplier.id", cascade="all, delete-orphan")

    def __init__(self, name):
        self.name = name


class Supplier(db.Model):
    
    __tablename__ = 'supplier'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(80), nullable=False)
    telephone = db.Column(String(80), nullable=False)
    price = db.Column(Integer, nullable=False) # bug
    feed_id = db.Column(Integer, ForeignKey=(Feed.id))

    def __init__(self, name):
        self.name = name
