# Local imports
from samplers import Sampler
from interfaces import DisplayInterface

# Standard library imports

# Third party imports


class Config:
    def __init__(self, 
                 exercise_sampler: Sampler, 
                 question_sampler: Sampler, 
                 prompt_sampler: Sampler, 
                 pronoun_sampler: Sampler,
                 interface: DisplayInterface):
        self.exercise_sampler = exercise_sampler
        self.question_sampler = question_sampler
        self.prompt_sampler = prompt_sampler
        self.pronoun_sampler = pronoun_sampler
        self.interface = interface