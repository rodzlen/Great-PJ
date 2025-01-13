from app.models import Image,Question
from config import db
# 모든 이미지들을 가져오기(관리자)
def get_all_images():
    images = Image.query.all()
    if not images:
        return {"msg": "No Data Found"}
    return [image.to_dict() for image in images]
    
# 해당 question_title의 모든 image 조회
def get_image(question_title):
    images = db.session.query(Image).join(Question).filter(Question.title == question_title).all()
    if not images:
        return {"msg":"No Data Found"}
    return [image.to_dict() for image in images]

def post_image( url, type):
    new_image = Image(url=url,type=type)
    
    db.session.add(new_image)
    db.session.commit()
    return new_image.to_dict()
    