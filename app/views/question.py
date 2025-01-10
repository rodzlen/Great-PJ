from models import Question
from config import db
# 해당 질문 제목의 내용을 가져오는 함수
def get_question(question_title):
    questions = Question.query.filter_by(title=question_title).all()
    if not questions:
        return{"msg":"No Data Found"}
    else:
        return [question.to_dict() for question in questions]
    
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

