from app.models import Answer,User,Choices
from config import db
from flask import request

# 모든 답변을 가져오는 기능(관리자)
def get_all_answer():
    answers = Answer.query.all()
    if not answers:
        return {"msg": "No Found Data"}
    return [answer.to_dict() for answer in answers]

# 해당 답변 삭제 쿼리 (관리자)
def delete_answer(answer_id):
    answer = Answer.query.get(answer_id)
    
    if not answer:
        return {'msg': 'No Found Data'}
    db.session.delete(answer)
    db.session.commit()
    
    return {"msg": "Successfully Deleted Data"}
    

# 특정 사용자 및 선택지의 답변 정보를 가져오는 기능
def get_answer(answer_id):
    answer = Answer.query.join(User,).join(Choices).filter_by(id=answer_id).first()
    if not answer:
        return {"msg":"No Found Data"}
    return answer.to_dict()

# 답변 등록
def post_answer(new_answers):
    for new_answer in new_answers:
        user_id = new_answer.get("userId")
        choice_id = new_answer.get("choiceId")
        new_answer = Answer(user_id=user_id, choice_id=choice_id)
        db.session.add(new_answer)
        db.session.commit()

    return {"message":f"User: {new_answer.user_id}'s answers Success Create"}
    

# 답변 업데이트 필요성?