from collections import Sequence
from typing import Optional, List
from question import Question, SinglePromptQuestion, TwoPromptQuestion
from config import Sampler, NoSampling, FirstNSampling, RandomSampling
import yaml
import random

class Exercise:
    def __init__(self, 
                 available_questions: Optional[List[Question]] = None, 
                 question_sampler: Sampler = NoSampling()):
        self.available_questions = available_questions
        self.question_sampler = question_sampler
        self.questions = []
        
    def __str__(self):
        return "\n".join([str(question) for question in self.questions])
    
    def load_from_yaml(self, path: str):
        with open(path, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        self.available_questions = data["questions"]
        self.questions = self.sample_questions()
        
    def shuffle_questions(self):
        random.shuffle(self.questions)
 
 
class SinglePromptExercise(Exercise):
    
    def sample_questions(self):
        sampled_questions = self.question_sampler.sample(self.available_questions)
        return [
            SinglePromptQuestion(prompt=question["prompt"], answer=question["answer"]) 
            for question in sampled_questions
        ]

                
class MultiPromptExercise(Exercise):
    secondary_prompts = []
    
    def __init__(self, available_questions = None, question_sampler = NoSampling(), prompt_sampler: Sampler = FirstNSampling(1)):
        super().__init__(available_questions, question_sampler)
        self.prompt_sampler = prompt_sampler
        
    def sample_questions(self):
        sampled_questions = self.question_sampler.sample(self.available_questions)
        output = []
        for question in sampled_questions:
            secondary_prompts = [key for key in question.keys() if key in self.secondary_prompts]
            sampled_prompts = self.prompt_sampler.sample(secondary_prompts)
    
            for prompt in sampled_prompts:
                output.append(
                    TwoPromptQuestion(
                        prompt=question["prompt"], 
                        secondary_prompt=prompt, 
                        answer=question[prompt]
                    )
                )
                        
        return output       
    
        
                
class TranslationExercise(SinglePromptExercise):
    question_class = SinglePromptQuestion


class ConjugationExercise(MultiPromptExercise):
    secondary_prompts = ["ja", "ti", "on", "mi", "vi", "oni"]
        

class CaseExercise(MultiPromptExercise):
    secondary_prompts = ["accusative", "locative"]
    
                    
                    
if __name__ == "__main__":
    all_questions = [
        {
            "prompt": "htjeti",
            "ja": "hocu",
            "ti": "hoces",
            "on": "hoce",
        }
    ]
    
    q_sampler = FirstNSampling(1)
    prompt_sampler = RandomSampling(2)
    exercise = ConjugationExercise(
        available_questions=all_questions, 
        question_sampler=q_sampler, 
        prompt_sampler=prompt_sampler
    )
    
    print(exercise.sample_questions())
    print(exercise.sample_questions())
    print(exercise.sample_questions())
    print(exercise.sample_questions())
        
    