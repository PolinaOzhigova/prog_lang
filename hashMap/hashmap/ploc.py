class PlocException(Exception):
    pass


class Ploc(dict):
    def __init__(self, special_dict: dict):
        super().__init__()
        self.special_dict = special_dict

    @staticmethod
    def compare(key, operation, value) -> bool:
        comparison = {
            "=": key == value,
            "<": key < value,
            ">": key > value,
            "<=": key <= value,
            ">=": key >= value,
            "<>": key != value,
        }
        return comparison.get(operation, False)

    @staticmethod
    def check_condition(operation, digit) -> bool:
        valid_operations = ["=", "<", ">", "<=", ">=", "<>"]
        return operation in valid_operations and digit.isdigit()

    @staticmethod
    def parse_condition(_condition):
        conditions_list = []

        for condition_str in "".join(_condition.split()).split(","):
            condition = {"operation": "", "value": ""}
            for char in condition_str:
                if char in ("<", ">", "="):
                    condition["operation"] += char
                elif char.isdigit():
                    condition["value"] += char
                elif char == ",":
                    if Ploc.check_condition(condition["operation"], condition["value"]):
                        condition["value"] = float(condition["value"])
                        conditions_list.append(condition)
                    else:
                        raise PlocException("Invalid condition")
                    condition = {"operation": "", "value": ""}
            if Ploc.check_condition(condition["operation"], condition["value"]):
                condition["value"] = float(condition["value"])
                conditions_list.append(condition)
            else:
                raise PlocException("Invalid condition")

        return conditions_list

    @staticmethod
    def parse_key(_key):
        values = []
        key = _key[1:-1] if _key[0] == '(' else _key
        key = "".join(key.split()).split(',')

        if len(key) == 1 and key[0].isdigit():
            values.append(float(key[0]))
        else:
            values = [float(k) for k in key if k.isdigit()]

        return values

    def __getitem__(self, condition):
        if not isinstance(condition, str):
            raise PlocException("Invalid condition")

        parsed_conditions = self.parse_condition(condition)
        selected = "{"

        for key_str, value in self.special_dict.items():
            key_values = self.parse_key(key_str)

            if len(key_values) != len(parsed_conditions):
                continue

            if all(
                self.compare(key, operation, value)
                for key, operation, value in zip(key_values, (c["operation"] for c in parsed_conditions), (c["value"] for c in parsed_conditions))
            ):
                selected += f", {key_str} = {value}" if len(selected) > 1 else f"{key_str} = {value}"

        selected += "}"
        return selected