from config import Config
from typing import Optional, Dict

from abc import ABC, abstractmethod

class Question:
    def __init__(self, prompt: str, answer: str):
        self.prompt = prompt
        self.answer = answer
        
class SinglePromptQuestion(Question): 
    def __str__(self):
        return f"{self.prompt} -> {self.answer}"
           
    def __repr__(self):
        return f"{self.prompt} -> {self.answer}"
               
    def validate_answer(self):
        pass
    
class TwoPromptQuestion(Question):
    def __init__(self, prompt: str, secondary_prompt: str, answer: str):
        super().__init__(prompt, answer)
        self.secondary_prompt = secondary_prompt
       
    def __str__(self):
        return f"{self.prompt} ({self.secondary_prompt}) -> {self.answer}" 
    
    def __repr__(self):
        return f"{self.prompt} + ({self.secondary_prompt}) -> {self.answer}" 
      
       
    def validate_answer(self):
        pass    

    