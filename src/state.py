""" State class file """

class State(object):
    """ Describe a State """

    def __init__(self, title, description, is_end):
        self.assets = {}
        self.title = title
        self.description = description
        self.end = is_end


    def set_music(self, music):
        """Set the music state to 'music'"""
        self.assets['music'] = music


    def set_background(self, background):
        """Set the background state to 'background'"""
        self.assets['background'] = background


    def add_sprite(self, sprite, position_x, position_y, scale):
        """Add a new sprite 'sprite' to the state at position and scale specified"""
        if 'sprites' not in self.assets:
            self.assets['sprites'] = []
        self.assets['sprites'].append({
            'sprite': sprite,
            'position': (position_x, position_y),
            'scale': scale
        })


    def add_option(self, label, next_state, required, acquired):
        """Add an option, required and acquired are a dictonary with key 'items', 'history', 'stats'
        Each of them are a dictionary name to value"""
        pass


    def get_title(self):
        """Return the title"""
        return self.title


    def get_description(self):
        """Return the description"""
        return self.description


    def get_assets(self):
        """Return the assets used.
        This is a dictionary with key "music", "background", and "sprites".
        The last one is an array of sprite, position and scale"""
        return self.assets.copy()


    def is_end(self):
        """Return true if it's an end state, false otherwise"""
        return self.end


    def get_option_count(self):
        """Return the nuber of option in this state"""
        pass


    def get_option(self, index):
        """Return the option at 'index'"""
        pass


def load_state_from_json(json_content):
    """Return a State object load from the json"""
    pass
