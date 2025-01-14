from app.models import Question
from config import db
# 모든 질문 가져오는 함수 (관리자)  
def get_all_questions():
    questions = Question.query.all()
    if questions:
        return [question.to_dict() for question in questions]
    return {"msg":"No Found Data"}

# 해당 질문 삭제하는 함수(관리자)
def delete_question(question_id):
    question = Question.query.get(question_id)
    if question:
        db.session.delete(question)
        db.session.commit()
        return {"msg": "Successfully Deleted Data"}
    return {'msg': 'No Data Founded'}
# 해당 질문 수정 함수(관리자)
def update_question(question_id,title,is_active,image_id):
    question = Question.query.filter_by(id = question_id).first()
    if not question:
        return {'msg': "No Data Found"}
    if title:   
        question.title = title
    if is_active is not None:
        question.is_active = is_active
    if image_id is not None:
        question.image_id = image_id
    db.session.commit()
    return question.to_dict()

    
# 해당 질문의 내용을 가져오는 함수
def get_question(question_id):
    question = Question.query.get(question_id)
    if not question:
        return{"msg":"No Data Found"}
    else:
        return question.to_dict()
    
# 잘문 게시 함수
def post_question(question_title, sqe,image_id):
    new_question = Question(
            title=question_title,
            sqe=sqe,
            image_id=image_id,
        )
    if new_question:
        db.session.add(new_question)
        db.session.commit()
        return new_question.to_dict()
# 질문 개수 확인
def count_questions():
    questions=Question.query.count()
    return {"total":questions}
