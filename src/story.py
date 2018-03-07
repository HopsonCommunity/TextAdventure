""" Story class file """

import json
from state import State
from typing import Dict

class Story(object):
    """ Describe a story.
    States, items, traits, class
    """

    def __init__(self):
        self.__reset()


    def __reset(self):
        """Clean up the structure"""
        pass


    def add_item(self, name: str, in_game_name: str, description: str):
        """Add an item to the story"""
        pass
        
    def add_trait(self, name: str, in_game_name: str, decription: str, antonym: str = None):
        """Add a trait, aswell as the antonym if it's not None"""
        pass


    def add_class(self, class_name: str, trait_value_dict: Dict[str, int]):
        """Add a class, trait_value_dict is a dictionary 'trait' to 'value'"""
        pass


    def add_state(self, name: str, state: State):
        """Add the state to the story, 'state' must be a State object"""
        pass


def load_story_from_json(json_content: json) -> Story:
    """Return a Story object load from the json"""
    pass
