from user import User
from threading import Lock
from question import Question
from answer import Answer
from tag import Tag
from typing import Dict

class StackOverflow:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls.users : Dict[int, User] = {}
                cls.users: Dict[int, User] = {}
                cls.questions: Dict[int, Question] = {}
                cls.answers: Dict[int, Answer] = {}
                cls.tags: Dict[str, Tag] = {}
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def create_user(self, username, mail):
        user_id = len(self.users) + 1
        user = User(username, user_id, mail)
        self.users[user_id] = user
        return user

    def ask_question(self, user, title, content, tags):
        question = user.ask_question(title, content, tags)
        self.questions[question.id] = question
        for tag in question.tags:
            self.tags.setdefault(tag.name, tag)
        return question

    def answer_question(self, user, question, content):
        answer = user.answer_question(question, content)
        self.answers[answer.id] = answer
        return answer

    def add_comment(self, user, commentable,  content):
        return user.comment_on(commentable, content)

    def vote_question(self, user, question, value):
        question.vote(user, value)

    def vote_answer(self, user, answer, value):
        answer.vote(user, value)

    def accept_answer(self, answer):
        answer.accept()

    def search_questions(self, query):
        return [q for q in self.questions.values() if
                query.lower() in q.title.lower() or
                query.lower() in q.content.lower() or
                any(query.lower() == tag.name.lower() for tag in q.tags)]

    def get_questions_by_user(self, user):
        return user.questions

    def get_user(self, user_id):
        return self.users.get(user_id)

    def get_question(self, question_id):
        return self.questions.get(question_id)

    def get_answer(self, answer_id):
        return self.answers.get(answer_id)

    def get_tag(self, name: str):
        return self.tags.get(name)