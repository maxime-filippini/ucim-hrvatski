from config import Config, RandomSampling, NoSampling, ConsoleInterface
from exercise import TranslationExercise, ConjugationExercise, CaseExercise

from typing import List
import yaml
import random
from pathlib import Path


# Question file, always structure as a list of dicts
# For a conjugation question, sample in the list, then sample within keys that are not the prompt. The key is a prompt element, the value the expected answer.


# Process
# Read from yaml
# Sample from yaml
# Build question objects


class Quiz:
    def __init__(self, config: Config):
        self._config = config

    @property
    def config(self):
        return self._config   
    
    def create_exercises_from_yaml(self, paths: List[str]):
        # Create exercises using the sampler inside the config.
        # Pass the question sampler to the relevant exercises based on themes
        sampler = self.config.exercise_sampler
        
        sampled_paths = sampler.sample(paths)
        
        self.exercises = []
        for path in sampled_paths:
            path = Path(path)
            
            if path.name.startswith("cases"):
                exercise = CaseExercise(
                    question_sampler=self.config.question_sampler,
                    prompt_sampler=self.config.prompt_sampler,
                )
            
            elif path.name.startswith("translation"):
                exercise = TranslationExercise(
                    question_sampler=self.config.question_sampler
                )
                
            elif path.name.startswith("conjugation"):
                exercise = ConjugationExercise(
                    question_sampler=self.config.question_sampler,
                    prompt_sampler=self.config.prompt_sampler,
                )
                
            else: 
                exercise = None
                
            if exercise:
                exercise.load_from_yaml(path=path)
                exercise.shuffle_questions()
                self.exercises.append(exercise)
            
    def shuffle_exercises(self):
        random.shuffle(self.exercises)
        
        
    
    
        
if __name__ == "__main__":
    paths = ["data/cases.yaml", "data/conjugation.yaml"]
    config = Config(
        exercise_sampler=RandomSampling(2),
        question_sampler=NoSampling(), 
        prompt_sampler=RandomSampling(1),
        interface=ConsoleInterface(),
    )
    
    quiz = Quiz(config=config)
    quiz.create_exercises_from_yaml(paths)
    
    print(quiz.exercises[0])