from abc import ABC, abstractmethod
from collections import Sequence
from question import Question

class QuestionDatabase(ABC):
    @abstractmethod
    def build_questions(self):
        pass
    
class UserDefinedQuestionDatabase(QuestionDatabase):
    def build_questions(self, questions: Sequence[Question]):
        self.questions = questions

class YamlQuestionDatabase(QuestionDatabase):
    def build_questions(self, path: str):
        pass
