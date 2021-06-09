# Local imports
from question import Question
from samplers import Sampler, NoSampling, FirstNSampling, RandomSampling

# Standard library imports
import random
from abc import ABC, abstractmethod
from typing import Optional, List

# Third party imports
import yaml


class Exercise(ABC):
    """Interface for the definition of quiz exercises"""    
    def __init__(self, 
                 available_questions: Optional[List[Question]] = None, 
                 question_sampler: Sampler = NoSampling()):
        self.available_questions = available_questions
        self.question_sampler = question_sampler
        self.questions = []
        
    def __str__(self):
        return "\n".join([str(question) for question in self.questions])
    
    def load_from_yaml(self, path: str):
        """Sample questions loaded from a yaml file

        Args:
            path (str): Path to the yaml file
        """        
        with open(path, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        self.available_questions = data["questions"]
        self.questions = self.sample_questions()
        
    def shuffle_questions(self):
        random.shuffle(self.questions)
        
    @abstractmethod
    def sample_questions(self):
        pass
 
 
class SinglePromptExercise(Exercise):
    
    def sample_questions(self):
        sampled_questions = self.question_sampler.sample(self.available_questions)
        return [
            Question(prompts=[question["prompt"]], answer=question["answer"]) 
            for question in sampled_questions
        ]

                
class TwoPromptExercise(Exercise):
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
                    Question(
                        prompts=[question["prompt"], prompt],
                        answer=question[prompt]
                    )
                )
                        
        return output  
    

       
class TranslationExercise(SinglePromptExercise):
    pass
        
class FillInTheBlanksExercise(SinglePromptExercise):
    pass
        
class CaseExercise(TwoPromptExercise):
    secondary_prompts = ["accusative", "locative"]
    
class ConjugationExercise(Exercise):
    pronouns = ["ja", "ti", "on", "mi", "vi", "oni"]
    tenses = ["present"]
    
    def __init__(self, 
                 available_questions = None, 
                 question_sampler = NoSampling(), 
                 tense_sampler: Sampler = FirstNSampling(1),
                 pronoun_sampler: Sampler = NoSampling()):
        super().__init__(available_questions, question_sampler)
        self.tense_sampler = tense_sampler
        self.pronoun_sampler = pronoun_sampler
        
    def sample_questions(self):
        sampled_questions = self.question_sampler.sample(self.available_questions)
        
        output = []
        for question in sampled_questions:
            tenses = [key for key in question.keys() if key in self.tenses]
            sampled_tenses = self.tense_sampler.sample(tenses)
            
            for tense in sampled_tenses:
                pronouns = [key for key in question[tense].keys() if key in self.pronouns]
                sampled_pronouns = self.pronoun_sampler.sample(pronouns)
                
                for pronoun in sampled_pronouns:
                    output.append(
                        Question(
                            prompts=[question["prompt"], tense, pronoun], 
                            answer=question[tense][pronoun]
                        )
                    )
                        
        return output          
        
     
        
    