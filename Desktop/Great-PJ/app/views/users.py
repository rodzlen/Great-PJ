from flask import jsonify
from models import User 
from config import db

#생성함수
def create_user(username, email, age, gender):
    new_user = User(username=username, email=email, age=age, gender=gender)
    db.session.add(new_user)
    db.session.commit()
    
    return new_user.to_dict()


#전체 유저 데이터 조회 함수

def get_users():
    users = User.query.all()
    return [user.to_dict() for user in users]



 #특정유저조회함수   
def get_user(user_id):
    user = User.query.filter_by(user_id).all()
    if user:
        return user.to_dict()
    return {"msg" : "Not found"}