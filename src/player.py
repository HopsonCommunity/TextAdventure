""" Player class file """

from collections import defaultdict
from state import State
from typing import Dict

class Player(object):
    """Describe the player, his inventory, traits, position and history"""

    def __init__(self, state=None):
        self.state = state
        self.items = defaultdict(lambda: 0)
        self.traits = defaultdict(lambda: 0)
        self.history = defaultdict(lambda: False)


    def save_to(self, filename: str):
        """Save the inventory, state, stats and history of the player to the file.
        Can be loaded with 'load_player_from' later"""
        pass


    def set_state(self, state: str):
        """Set the player's position to 'state'"""
        self.state = state


    def get_state(self) -> str:
        """Return the current player's state"""
        return self.state


    def set_traits(self, traits: Dict[str, int]):
        """Set all traits in `traits` (dictionary name to value)"""
        for trait, value in traits.items():
            self.traits[trait] = value


    def update_traits(self, traits: Dict[str, int]):
        """Update the players traits to reflect the parameter traits. (Adds to the previous value)"""
        for trait, value in traits.items():
            self.traits[trait] += value


    def has_traits(self, traits: Dict[str, int]) -> bool:
        """Return true if the player has all traits in parameter traits (equal or more)"""
        return all(
            self.traits.get(trait, 0) > value 
            for trait, value in traits.items())


    def update_items(self, items: dict):
        """Update the players inventory to reflect the parameter items. (Adds to the previous value)"""
        for item, count in items.items():
            self.items[item] = max(self.items[item] + count, 0)  # clamps value to zero if result is negative


    def has_items(self, items: dict) -> bool:
        """Return true if the player has at least number of items specified in parameter items"""
        return all(
            self.items.get(item, 0) > count 
            for item, count in items.items())


    def set_history(self, history: dict):
        """Set the history 'name' to 'value', it must be a boolean"""
        for story, value in history.items():
            self.history[story] = value


    def has_history(self, history: dict) -> bool:
        """Return true if all values in player history and in parameter are equal"""
        return all(
            self.history.get(story, False) == value 
            for story, value in history.items())


def load_player_from(content):
    """Return a Player object load from the save file"""
    pass
