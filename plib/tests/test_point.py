import pytest 
from plib import Point 
 
@pytest.fixture
def points():
    return Point(0, 0), Point(2, 0)

class TestPoint: 
    def test_creation(self): 
        Point(1, 2) 

        with pytest.raises(TypeError): 
            Point(1, "a")

    def test_addition(self, points):
        p1, p2 = points
        assert p1 + p2 == Point(2, 0)

    def test_substract(self, points):
        p1, p2 = points
        assert p1 - p2 == Point(-2, 0)
    
    @pytest.mark.parametrize(
        "p1, p2, distance",
        [(Point(0, 0), Point(0, 10), 10),
        (Point(0, 0), Point(10, 0), 10),
        (Point(0, 0), Point(10, 10), 14.14),]
    )
    def test_all_axis(self, p1, p2, distance):
        assert p1.distance(p2) == pytest.approx(distance, 0.1)
    #pytest.approx задает точность