import json
import math

class Point:
    def __init__(self, x, y): 
        if (isinstance(x, (int, float)) and isinstance(y, (int, float))): 
            self.x = x 
            self.y = y 
        else: 
            raise TypeError("Invalid point type")

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return Point(self.x == other.x, self.y == other.y)

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)
    
    def is_zero(self):
        return self.x == 0 and self.y == 0

    def to_json(self):
        return json.dumps({'x': self.x, 'y': self.y})

    @classmethod
    def from_json(a, json_str):
        data = json.loads(json_str)
        return a(data['x'], data['y'])

    def __str__(self):
        return f"Point({self.x}, {self.y})"