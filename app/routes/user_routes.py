from flask import request 
from flask.views import MethodView
from flask_smorest import Blueprint
from app.views import question, images,users,choices,answers

# user 관련
# answer Api
answer_blp = Blueprint('answers',__name__)

class AnswerApi(MethodView):
    # def get(self,answer_id=None):
    #     return answers.get_answer(answer_id==answer_id)

    def post(self):
        new_answer = request.json
        return answers.post_answer(user_id=new_answer['user_id'],choice_id=new_answer['choice_id'])
    
    # def delete(self, answer_id=None):
    #     return answers.delete_answer(answer_id=answer_id)
            
        
        

# choice Api
choice_blp = Blueprint('choices',__name__)

class ChoiceApi(MethodView):
    def get(self,question_id=None):
        return choices.get_choice(question_id=question_id)
    
    # def post(self):
    #     new_choice = request.json
    #     return choices.post_choice(question_id=new_choice['question_id'],content=new_choice['content'],sqe=new_choice['sqe'])
    # def delete(self,choice_id=None):
    #     return choices.delete_choice(choice_id=choice_id)
    
    # def put(self,choice_id=None):
    #     new_choice = request.json
    #     return choices.update_choice(choice_id=choice_id,content=new_choice['content'], is_active=new_choice['is_active'], sqe=new_choice['sqe'] )

#image API
image_blp = Blueprint('images',__name__,url_prefix='/image')
class ImageApi(MethodView):
    
    def get(self):
        return images.get_image()


#질문 API
question_blp = Blueprint('questions',__name__)

class QuestionApi(MethodView):
    
    def get(self,question_id=None):
        if question_id:
            return question.get_question(question_id=question_id)
        return question.count_questions()
        
    
    # def post(self):
    #     data = request.json
    #     if data:
    #         title = data['title']
    #         sqe = data['sqe']
    #         image_id = data['image_id']
    #         return question.post_question(question_title=title,image_id=image_id,sqe=sqe)
    #     else:
    #         return {'msg':"No Data Found"}
        
    # def put(self,question_id=None):
    #     new_question = request.json
    #     return question.update_question(question_id=question_id,title=new_question['title'],is_active=new_question['is_active'],image_id=new_question['image_id'])
        
    # def delete(self,question_id=None):
    #     return question.delete_question(question_id)

# 회원 API
user_blp = Blueprint('users',__name__)


class UserApi(MethodView):    
    # 회원 가입시 유저 정보 저장
    def post(self):
        new_data = request.json
        return users.create_user(username=new_data['name'],email=new_data['email'],age=new_data['age'],gender=new_data['gender'])

# MethodView를 Blueprint에 등록 
# image_blp.add_url_rule('/<int:image_id>',view_func=ImageApi.as_view('image'))
image_blp.add_url_rule('/main',view_func=ImageApi.as_view('image'))

# question_blp.add_url_rule('/', view_func=QuestionApi.as_view('questions'))
question_blp.add_url_rule('/question/<int:question_id>', view_func=QuestionApi.as_view('question'))
question_blp.add_url_rule('/questions/count', view_func=QuestionApi.as_view('question'))

user_blp.add_url_rule('/signup',view_func=UserApi.as_view('users'),methods=["POST"])

# choice_blp.add_url_rule('/',view_func=ChoiceApi.as_view('choices'))
choice_blp.add_url_rule('/choice/<int:question_id>',view_func=ChoiceApi.as_view('choice'))

answer_blp.add_url_rule('/submit',view_func=AnswerApi.as_view('answers'))
# answer_blp.add_url_rule('/<int:answer_id>',view_func=AnswerApi.as_view('answer'))