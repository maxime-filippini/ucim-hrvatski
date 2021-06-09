# Local imports

# Standard library imports
from abc import ABC, abstractmethod
from typing import List

# Third party imports


class Question:
    def __init__(self, prompts: List[str], answer: str):
        self.prompts = prompts
        self.answer = answer
        
    def __str__(self):
        prompts = self.prompts[0] + " " + " + ".join([f"({p})" for p in self.prompts[1:]])
        return f"{prompts}"
           
    def __repr__(self):
        return self.__str__()       
        
    def validate_answer(self):
        pass
    