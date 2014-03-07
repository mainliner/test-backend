from app import db
import datetime



class User(db.Model):
    __tablename__='user'
    userid=db.Column(db.Integer,primary_key=True)
    udid=db.Column(db.String(70),unique=True)
    language=db.Column(db.String(70),unique=True)
    push=db.Column(db.Boolean, default=0)
    last=db.Column(db.DateTime, default=datetime.date.today())
    token=db.Column(db.String(100))
    def __init__(self, udid=None,language=None,push=None,last=None,token=None):
        self.udid=udid
        self.language=language
        self.push=push
        self.token=token
        self.last=datetime.date.today()
    def __repr__(self):
        return '<User %s>' % self.username


