""" Player class file """

class Player(object):
    """Describe the player, his inventory, traits, position and history"""

    def __init__(self, state=None):
        self.state = state
        self.items = {}

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

    def set_trait(self, name, value):
        """Set the trait to 'value'"""
        pass

    def add_to_trait(self, name, value):
        """Add 'value' to 'trait'"""
        pass

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

    def set_history(self, name, value):
        """Set the history 'name' to 'value', it must be a boolean"""
        pass

    def has_history(self, name):
        """Return true if the history 'name' has been previously set"""
        pass

def load_player_from(content):
    """Return a Player object load from the save file"""
    pass
