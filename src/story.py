""" Story class file """

class Story(object):
    """ Describe a story.
    States, items, traits, class
    """

    def __init__(self):
        self.items = {}
        self.traits = {}
        self.classes = {}
        self.states = {}
        self.antonyms = {}


    def add_item(self, name, in_game_name, description):
        """Add an item to the story"""
        self.items[name] = {'name': in_game_name, 'description': description}


    def add_trait(self, name, in_game_name, description, antonym=None):
        """Add a trait, as well as the antonym if it's not None"""
        self.traits[name] = {'name': in_game_name, 'description': description}
        if antonym is not None:
            self.antonyms[antonym] = name


    def add_class(self, class_name, trait_value_dict):
        """Add a class, trait_value_dict is a dictionary 'trait' to 'value'"""
        self.classes[class_name] = {'traits': trait_value_dict}


    def add_state(self, name, state):
        """Add the state to the story, 'state' must be a State object"""
        self.states[name] = state


def load_story_from_json(json_content):
    """Return a Story object load from the json"""
    pass
