from config import db
from app.models import Choices, Question

# 모든 선택을 가져오기(관리자)
def get_all_choice():
    choices = Choices.query.all()
    if not choices:
        return {"msg":"No Found choices Data"}
    return [choice.to_dict() for choice in choices]

# 해당 선택지 업데이트 쿼리
def update_choice(choice_id, content,is_active,sqe):
    choice = Choices.query.filter_by(id = choice_id).first()
    if content is not None:
        choice.content=content
    if is_active is not None:
        choice.is_actice= is_active
    if sqe is not None:
        choice.sqe = sqe
    db.session.commit()
    return {"msg":"Successfully Update Data","choice":choice.to_dict()}
    

# 해당 선택지 삭제 쿼리
def delete_choice(choice_id):
    choice = Choices.query.filter_by(id=choice_id).first()
    if choice is None:
        return {"mag": "No Found Data"}
    db.session.delete(choice)
    db.session.commit()
    return {"msg": "Successfully Deleted Data"}
# 해당 선택지 가져오기
def get_choice(question_id):
    choices = Choices.query.filter_by(question_id = question_id).all()
    if not choices:
        return {"msg":"No Data Found"}
    return [choice.to_dict() for choice in choices]

# 선택지 등록하기
def post_choice(question_id, content,sqe):
    # 파라미터 값 확인
    if not question_id or not content or not sqe:
        return {"msg": "Missing required fields: question_id, content, or sqe"}
    new_choice = Choices(question_id=question_id,content= content, sqe=sqe)
    db.session.add(new_choice)
    db.session.commit()
    return new_choice.to_dict()