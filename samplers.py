# Local imports

# Standard library imports
import random
from collections import Sequence
from abc import ABC, abstractmethod

# Third party imports


class Sampler(ABC):
    """Interface for samplers"""    
    @abstractmethod
    def sample(self, data: Sequence) -> Sequence:
        pass
    
    
class NoSampling(Sampler):
    """Returns the original sequence"""    
    def sample(self, data: Sequence) -> Sequence:
        return data
    
    
class RandomSampling(Sampler):
    """Returns a sequence of length N of randomly picked items of the original sequence"""    
    def __init__(self, N):
        self._N = N
    
    @property
    def N(self):
        return self._N
        
    def sample(self, data: Sequence) -> Sequence:
        return random.choices(data, k=self.N)
    
    
class FirstNSampling(Sampler):
    """Returns a sequence of the first N elements of the original sequence"""    
    def __init__(self, N):
        self._N = N
    
    @property
    def N(self):
        return self._N
    
    def sample(self, data: Sequence) -> Sequence:
        return data[:self.N]
    
    
class MatchSampler(Sampler):
    """Returns a sequence of the elements of the original sequence found in another sequence"""    
    
    def __init__(self, to_match: Sequence):
        self._to_match = to_match
        
    @property
    def to_match(self):
        return self._to_match
        
    def sample(self, data: Sequence) -> Sequence:
        return [item for item in data if item in self.to_match]