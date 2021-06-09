from abc import ABC, abstractmethod
from collections import Sequence
from typing import Dict, List
import random



class Sampler(ABC):
    @abstractmethod
    def sample(self, data: Sequence) -> Sequence:
        pass
    
class NoSampling(Sampler):
    def sample(self, data: Sequence) -> Sequence:
        return data
    
class RandomSampling(Sampler):
    def __init__(self, N):
        self._N = N
    
    @property
    def N(self):
        return self._N
        
    def sample(self, data: Sequence) -> Sequence:
        return random.choices(data, k=self.N)
    
class FirstNSampling(Sampler):
    def __init__(self, N):
        self._N = N
    
    @property
    def N(self):
        return self._N
    
    def sample(self, data: Sequence) -> Sequence:
        return data[:self.N]
    
class MatchSampler(Sampler):
    def __init__(self, to_match: Sequence):
        self._to_match = to_match
        
    @property
    def to_match(self):
        return self._to_match
        
    def sample(self, data: Sequence) -> Sequence:
        return [item for item in data if item in self.to_match]
            
    
class DisplayInterface(ABC):
    @abstractmethod
    def get_input(self, prompt: str):
        pass
    
    @abstractmethod
    def print(self, msg: str):
        pass

class ConsoleInterface(DisplayInterface):
    def get_input(self, prompt: str):
        return input(prompt)

    def print(self, msg: str):
        print(msg)


class Config:
    def __init__(self, exercise_sampler, question_sampler, prompt_sampler, interface):
        self.exercise_sampler = exercise_sampler
        self.question_sampler = question_sampler
        self.prompt_sampler = prompt_sampler
        self.interface = interface
    
    

