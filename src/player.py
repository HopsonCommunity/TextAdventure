""" Player class file """

class Player(object):
    """Describe the player, his inventory, traits, position and history"""

    def __init__(self, state):
        self.traits = {}
        pass

    def save_to(self, filename):
        """Save the inventory, state, stats and history of the player to the file.
        Can be loaded with 'load_player_from' later"""
        pass

    def set_state(self, state):
        """Set the player's position to 'state'"""
        pass

    def get_state(self):
        """Return the current player's state"""
        pass

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

    def add_items(self, items):
        """Add all items in 'items' (dictionary name to value) in the player's inventory"""
        pass

    def has_items(self, items):
        """Return true if the player has all items in 'items' (dictionary name to value)"""
        pass

    def remove_items(self, items):
        """Remove all items of 'items' (dictionary name to value)"""
        pass

    def set_history(self, name, value):
        """Set the history 'name' to 'value', it must be a boolean"""
        pass

    def has_history(self, name):
        """Return true if the history 'name' has been previously set"""
        pass

def load_player_from(content):
    """Return a Player object load from the save file"""
    pass
