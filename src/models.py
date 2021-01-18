from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    address = db.Column(db.String(60), nullable=False)
    stage = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "email": self.email,
            "phone":self.phone,
            "address":self.address,
            "stage":self.stage

            # do not serialize the password, its a security breach
        }