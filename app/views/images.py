from app.models import Image,Question
from config import db
# 모든 이미지들을 가져오기(관리자)
def get_all_images():
    images = Image.query.all()
    if not images:
        return {"msg": "No Data Found"}
    return [image.to_dict() for image in images]
# 햐당 이미지 조회
def get_image():
    image = Image.query.filter_by(type='main').first()
    if image:
        return {"image":image.url}
    return {"msg":"Not Found Image Data"}
# 이미지 등록
def post_image( url, type):
    new_image = Image(url=url,type=type)
    
    db.session.add(new_image)
    db.session.commit()
    return new_image.to_dict()
# 이미지 수정
def update_image(image_id,url,type):
    image = Image.query.filter_by(id=image_id).first()
    image.url=url
    image.type=type
    db.session.commit()
    return image.to_dict()

# 이미지 삭제 
def delete_image(image_id):
    image = Image.query.filter_by(id = image_id).first()
    if image:
        db.session.delete(image)
        db.session.commit()
        return {"msg":"Successfully Deleted Image"}
    return {"msg":"Not Found Image Data"}
    