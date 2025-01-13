from flask import request
from flask_smorest import Blueprint
from flask.views import MethodView
from app.views import question,images,users,choices,answers








# 관리자 다 할 수 있음
# answer Api
answer_blp_admin = Blueprint('admin_answers',__name__,url_prefix='/admin/answers')

class AnswerApi(MethodView):
    def get(self,answer_id=None):
        if answer_id:
            return answers.get_answer(answer_id==answer_id)
        return answers.get_all_answer()
    def post(self):
        new_answer = request.json
        return answers.post_answer(user_id=new_answer['user_id'],choice_id=new_answer['choice_id'])
    
    def delete(self, answer_id=None):
        return answers.delete_answer(answer_id=answer_id)
            
        
        

# choice Api
choice_blp_admin = Blueprint('admin_choices',__name__,url_prefix='/admin/choices')

class ChoiceApi(MethodView):
    def get(self,choice_id=None):
        if choice_id:
            return choices.get_choice(choice_id)
        return choices.get_all_choice()
    
    def post(self):
        new_choice = request.json
        if new_choice:
            return choices.post_choice(question_id=new_choice['question_id'],content=new_choice['content'],sqe=new_choice['sqe'])
        return {"msg":"Not Found Request Data"}
    def delete(self,choice_id=None):
        return choices.delete_choice(choice_id=choice_id)
    def put(self,choice_id=None):
        new_choice = request.json
        return choices.update_choice(choice_id=choice_id,content=new_choice['content'], is_active=new_choice['is_active'], sqe=new_choice['sqe'] )

#image API
image_blp_admin = Blueprint('admin_images',__name__,url_prefix='/admin/images')
class ImageApi(MethodView):
    
    def get(self,image_id=None):
        if image_id:
            return images.get_image(image_id=image_id)
        return images.get_all_images()
    
    def post(self):
        new_image = request.json
        
        if new_image:
            return images.post_image(url=new_image['url'],type=new_image['type'])
        else:
            return {'msg':"Not Found Request Data"}
    def put(self,image_id=None):
        data = request.json
        url = data['url']
        type= data['type']
        return images.update_image(url=url,type=type,image_id=image_id)
    def delete(self,image_id=None):
        return images.delete_image(image_id=image_id)


#질문 API
question_blp_admin = Blueprint('admin_questions',__name__,url_prefix='/admin/questions')

class QuestionApi(MethodView):
    
    def get(self,question_id=None):
        if question_id:
            return question.get_question(question_id=question_id)
        return question.get_all_questions()
    
    def post(self):
        data = request.json
        if data:
            title = data['title']
            sqe = data['sqe']
            image_id = data['image_id']
            return question.post_question(question_title=title,image_id=image_id,sqe=sqe)
        else:
            return {'msg':"No Data Found"}
        
    def put(self,question_id=None):
        new_question = request.json
        return question.update_question(question_id=question_id,title=new_question['title'],is_active=new_question['is_active'],image_id=new_question['image_id'])
        
    def delete(self,question_id=None):
        return question.delete_question(question_id)

# 회원 API
user_blp_admin = Blueprint('admin_users',__name__,url_prefix='/admin/users')


class UserApi(MethodView):
    # 전체 유저 조회
    def get(self,user_id=None):
        if user_id:
            return users.get_user(user_id)
        else:    
            return users.get_users()
    
    def post(self):
        new_data = request.json        
        return users.create_user(username=new_data['username'],email=new_data['email'],age=new_data['age'],gender=new_data['gender'])
    
    def put(self,user_id):
        update_user = request.json
        return users.update_user(user_id=user_id,username=update_user['username'],age=update_user['age'],gender=update_user['gender'],email=update_user['email'])
    
    def delete(self,user_id):
        return users.delete_user(user_id=user_id)

# MethodView를 Blueprint에 등록
image_blp_admin.add_url_rule('/',view_func=ImageApi.as_view('images_admin'))
image_blp_admin.add_url_rule('/<int:image_id>',view_func=ImageApi.as_view('image_admin'))

question_blp_admin.add_url_rule('/', view_func=QuestionApi.as_view('questions_admin'))
question_blp_admin.add_url_rule('/<int:question_id>', view_func=QuestionApi.as_view('question_admin'))

user_blp_admin.add_url_rule('/',view_func=UserApi.as_view('users_admin'))
user_blp_admin.add_url_rule('/<int:user_id>',view_func=UserApi.as_view('user_admin'))

choice_blp_admin.add_url_rule('/',view_func=ChoiceApi.as_view('choices_admin'))
choice_blp_admin.add_url_rule('/<int:choice_id>',view_func=ChoiceApi.as_view('choice_admin'))

answer_blp_admin.add_url_rule('/<int:answer_id>',view_func=AnswerApi.as_view('answer_admin'))
answer_blp_admin.add_url_rule('/',view_func=AnswerApi.as_view('answers_admin'))