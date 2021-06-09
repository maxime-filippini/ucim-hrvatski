# Local imports

# Standard library imports
from abc import ABC, abstractmethod

# Third party imports


class DisplayInterface(ABC):
    """Interface for the display interface of the app"""    
    @abstractmethod
    def get_input(self, prompt: str):
        pass
    
    @abstractmethod
    def print(self, msg: str):
        pass


class ConsoleInterface(DisplayInterface):
    """Implementation of the console interface for the app"""  
    separator = "-"*80
    newline = "\n"
      
    def get_input(self, prompt: str):
        return input(prompt + " => ")

    def print(self, msg: str):
        print(msg)