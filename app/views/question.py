from models import Question
from config import db

# 모든 질문 가져오는 함수 (관리자)  
def get_all_questions():
    questions = Question.query.all()
    if questions:
        return [question.to_dict() for question in questions]
    return {"msg":"No Found Data"}

# 해당 질문 삭제하는 함수(관리자)
def delete_question(question_id):
    question = Question.query.filter_by(id = question_id).first()
    if question:
        db.session.delete(question)
        db.session.commit()
        return {"msg": "Successfully Deleted Data"}
    return {'msg': 'No Data Founded'}
# 질문 수정 함수(관리자)
def update_question(question_id,title,is_active):
    question = Question.query.filter_by(id = question_id).all()
    if not question:
        return {'msg': "No Data Found"}
    if title:   
        question.title = title
    if is_active is not None:
        question.is_active = is_active
    db.session.commit()
    return {'msg':"Successfully Updated Data"}

    

# 해당 질문 제목의 내용을 가져오는 함수
def get_question(question_title):
    questions = Question.query.filter_by(title=question_title).all()
    if not questions:
        return{"msg":"No Data Found"}
    else:
        return [question.to_dict() for question in questions]
# 잘문 게시 함수
def post_question(question_title, is_active,sqe,image_id):
    new_question = Question(
            title=question_title,
            is_active=is_active,
            sqe=sqe,
            image_id=image_id,
        )
    if new_question:
        db.session.add(new_question)
        db.session.commit()
        return new_question.to_dict()

