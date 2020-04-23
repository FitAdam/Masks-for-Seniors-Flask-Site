from mask_site import db
from datetime import datetime

class order(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(20))
    surname = db.Column("surname", db.String(20))
    email = db.Column("email", db.String(120))
    address = db.Column("address",db.String(60))
    address_2 = db.Column("address_2",db.String(60))
    post_code = db.Column("post_code",db.String(60))
    quantity = db.Column("quantity",db.String(10))
    date_posted = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    def __init__(self, name, surname, email, address, address_2, post_code, quantity):
        self.name = name
        self.surname = surname
        self.email = email
        self.address = address
        self.address_2 = address_2
        self.post_code = post_code
        self.quantity = quantity
        