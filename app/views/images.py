from models import Image
from config import db


def get_image(questions):
    images = Image.query.filter_by(Image.questions.contains(questions)).all()
    if images:
        return [image.to_dict() for image in images]
    else: 
        return {"msg":"No Data Found"}
def post_image(questions, url, type):
    new_image = Image(questions=questions, url=url,type=type)
    if new_image:
        db.session.add(new_image)
        db.session.commit()
        return new_image.to_dict()
    else:
        return {"msg":"No Data Found"}
    