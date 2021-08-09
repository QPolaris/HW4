from . import db

class Company(db.Model):
    def __repr__(self):
        return '<Company %r>' % self.company
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False) # company name
    email = db.Column(db.String(100), nullable=False) # company email
    phone_number = db.Column(db.Integer, nullable=False) # company phone number
    address = db.Column(db.String(280), nullable=False) # company address