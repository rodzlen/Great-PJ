from flask import Blueprint,request
from flask.views import MethodView
from app.views import question, images,users

#질문 API
question_blp = Blueprint('question',__name__,url_prefix='/questions')

class QuestionApi(MethodView):
    
    def get(self):
        return question.get_all_questions()
    
    def post(self):
        data = request.json
        if data:
            title = data['title']
            sqe = data['sqe']
            image_id = data['image_id']
            url = data['url']
            type = data['type']
            images.post_image(url=url,type=type)
            question.post_question(question_title=title,image_id=image_id,sqe=sqe)
        else:
            return {'msg':"No Data Found"}


# 회원 API
user_blp = Blueprint('users',__name__,url_prefix='/users')


class UserApi(MethodView):
    # 전체 유저 조회
    def get(self,user_id=None):
        if user_id:
            return users.get_user(user_id)
        else:    
            return users.get_users()
    
    def post(self):
        new_data = request.json
        # 필수 필드 체크
        if not all(key in new_data for key in ['username', 'email', 'age', 'gender']):
            return {'msg': 'Missing required fields'}, 400
        users.create_user(username=new_data['username'],email=new_data['email'],age=new_data['age'],gender=new_data['gender'])
        return {'msg': 'User Created Successfully'}, 201

# MethodView를 Blueprint에 등록
question_blp.add_url_rule('/', view_func=QuestionApi.as_view('questions'))
user_blp.add_url_rule('/',view_func=UserApi.as_view('users'))
user_blp.add_url_rule('/<int:user_id>',view_func=UserApi.as_view('user'))