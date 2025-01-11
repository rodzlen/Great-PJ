from config import db
from models import Choices, Question

# 모든 선택을 가져오기(관리자)
def get_all_choice():
    choices = Choices.query.all()
    if not choices:
        return {"msg":"No Found choices Data"}
    return [choice.to_dict() for choice in choices]

# 해당 질문의 선택지들 가져오기
def get_choice(question_id):
    choices = Choices.query.filter(question_id = question_id).all()
    if not choices:
        return {"msg":"No Data Found"}
    return [choice.to_dict() for choice in choices]

# 해당 질문의 선택지 등록하기
def post_choice(question_id, content,sqe):
    # 파라미터 값 확인
    if not question_id or not content or not sqe:
        return {"msg": "Missing required fields: question_id, content, or sqe"}
    new_choice = Choices(question_id=question_id,content= content, sqe=sqe)
    db.session.add(new_choice)
    db.session.commit()
    return new_choice.to_dict()