""" Player class file """

class Player(object):
    """Describe the player, his inventory, traits, position and history"""

    def __init__(self, state):
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

    def set_trait(self, name, value):
        """Set the trait to 'value'"""
        pass

    def add_to_trait(self, name, value):
        """Add 'value' to 'trait'"""
        pass

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
