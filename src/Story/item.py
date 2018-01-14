""" This file contains the Item class """

class Item:
    """Describe a Story Item. Contains an in-game name and a description"""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_name(self):
        """Returns the in-game name of the item"""
        return self.name

    def get_description(self):
        """Returns the description of the item"""
        return self.description
