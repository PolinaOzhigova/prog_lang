class IlocException(Exception):
    pass

class Iloc(dict):

    def __init__(self, special_dict: dict):
        super().__init__()
        self.special_dict = special_dict

    def __getitem__(self, item_index):
        if not isinstance(item_index, int) or item_index >= len(self.special_dict) or item_index < 0:
            raise IlocException("Invalid index")
        else:
            sorted_indices = sorted(self.special_dict.keys())
            return self.special_dict[sorted_indices[item_index]]