from models import Answer
from config import db

# 모든 답변을 가져오는 기능(관리자)
def get_all_answer():
    answers = Answer.query.all()
    if not answers:
        return {"msg": "No Found Data"}
    return [answer.to_dict() for answer in answers]

# 해당 답변 삭제 쿼리 (관리자)
def delete_answer(answer_id):
    answer = Answer.query.filter_by(id = answer_id).all()
    
    if not answer:
        return {'msg': 'No Found Data'}
    db.session.delete(answer)
    db.session.commit()
    
    return {"msg": "Successfully Deleted Data"}
    

# 특정 사용자 및 선택지의 답변 정보를 가져오는 기능
def get_answer(user_id, choice_id):
    answers = Answer.query.filter_by(user_id=user_id, choice_id=choice_id).all()
    if not answers:
        return {"msg":"No Found Data"}
    return [answer.to_dict() for answer in answers]

# 답변 등록
def post_answer(user_id, choice_id):
    new_answer = Answer(user_id=user_id, choice_id=choice_id)
    db.session.add(new_answer)
    db.session.commit()
    return new_answer.to_dict()