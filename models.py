from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey, Table 
from sqlalchemy.orm import  relationship
from main import db

from datetime import datetime 

class users(db.Model):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(String(64))
    display_name = Column(String(64))
    insert_time = Column(DateTime(), default=datetime.now)

    def __init__(self , userid, display_name):
        self.userid = userid
        self.display_name = display_name

    def new_user(self):
        user = db.session.query(users.userid==self.userid).first()
        print(self)
        if not user:
            db.session.add(users(self.userid, self.display_name))
            db.session.commit()
            print("Done!")
        else:
            print ("{} has already existed.".format(self.userid))

    def __repr__(self):
        return '%r' % (self.userid)

class Sche(db.Model):
    __tablename__ = 'sche'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String(4), nullable=False, default='0101')
    time = Column(String(4), nullable=False, default='0000')
    title = Column(String(80), nullable=False)
    dest = Column(String(20), nullable=False)
    location = Column(String(100), nullable=False)
    MoreInfo = Column(String(300))


db.create_all()
