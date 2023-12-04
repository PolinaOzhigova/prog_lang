from .ploc import Ploc
from .iloc import Iloc

class SpecialDict(dict):
    def __init__(self, values=None):
        if values is None:
            values = {}
        super().__init__(values)
        self.iloc = Iloc(self)
        self.ploc = Ploc(self)