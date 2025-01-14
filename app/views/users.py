from flask import request
from app.models import User 
from config import db

#관리자
#전체 유저 데이터 조회 함수(관리자)
def get_all_users():
    users = User.query.all()
    return [user.to_dict() for user in users]

def update_user(user_id, username, age, gender, email):
    user = User.query.get(user_id)
    if user:
        if username:
            user.name = username
        if age:
            user.age = age
        if gender:
            user.gender = gender
        if email:
            user.email = email
        db.session.commit()
        return user.to_dict()
    return {"msg:Not Found User Data"}
# 유저 삭제
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        return {"msg": "Successfully delete data"}
    return {"msg":"Not Found Data"}
    
# 유저
#생성함수
def create_user(username, email, age, gender):
    if not all([username, email, age, gender]):
        return {"message": "모든 필드를 입력해주세요."}

    # 이름 중복 확인
    existing_user = User.query.filter_by(name=username).first()
    if existing_user:
        return {"message": "이미 존재하는 계정입니다."}

    # 새로운 유저 생성
    new_user = User(name=username, email=email, age=age, gender=gender)
    db.session.add(new_user)
    db.session.commit()

    return {
        "message": f"{new_user.name}님 회원가입을 축하합니다.",
        "user_id": new_user.id,
    }

#특정유저조회함수   
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        return user.to_dict()
    return {"msg" : "Not found"}