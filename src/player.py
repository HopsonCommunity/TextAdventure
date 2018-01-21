""" Player class file """

class Player(object):
    """Describe the player, his inventory, traits, position and history"""

    def __init__(self, state=None):
        self.state = state
        self.items = {}
        self.traits = {}
        self.history = {}


    def save_to(self, filename):
        """Save the inventory, state, stats and history of the player to the file.
        Can be loaded with 'load_player_from' later"""
        pass


    def set_state(self, state):
        """Set the player's position to 'state'"""
        self.state = state


    def get_state(self):
        """Return the current player's state"""
        return self.state


    def set_traits(self, traits):
        """Set all traits in `traits` (dictionary name to value)"""
        for trait, value in traits.items():
            self.traits[trait] = value


    def update_traits(self, traits):
        """Update the players traits to reflect the parameter traits. (Adds to the previous value)"""
        for trait, value in traits.items():
            self.traits[trait] = self.traits.get(trait, 0) + value


    def has_traits(self, traits):
        """Return true if the player has all traits in parameter traits (equal or more)"""
        for trait, value in traits.items():
            if self.traits.get(trait, 0) < value:
                return False
            return True


    def update_items(self, items: dict):
        """Update the players inventory to reflect the parameter items. (Adds to the previous value)"""
        for item, count in items.items():
            self.items[item] = max(self.items.get(item, 0) + count, 0)  # clamps value to zero if result is negative


    def has_items(self, items: dict):
        """Return true if the player has at least number of items specified in parameter items"""
        for item, count in items.items():
            if self.items.get(item, 0) < count:
                return False
        return True


    def set_history(self, history: dict):
        """Set the history 'name' to 'value', it must be a boolean"""
        for story, value in history.items():
            self.history[story] = value


    def has_history(self, history: dict):
        """Return true if all values in player history and in parameter are equal"""
        for story, value in history.items():
            if self.history.get(story, 0) != value:
                return False
            return True


def load_player_from(content):
    """Return a Player object load from the save file"""
    pass
