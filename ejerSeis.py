import math

class Circle():
    def __init__(self, radius=None):
        self.radius = radius or 1

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = val
        self._diameter = self._radius * 2
        self._area = math.pi * (self._radius ** 2)

    @property
    def diameter(self):
        return self._diameter
    @diameter.setter
    def diameter(self, val):
        if val < 0:
            raise ValueError('Diameter cannot be negative')
        self._diameter = val
        self._radius = self._diameter / 2
        self._area = math.pi * (self._radius ** 2)

    @property
    def area(self):
        return self._area
    @area.setter
    def area(self, val):
        if val:
            raise AttributeError("can't set attribute")

    def __str__(self):
        return 'The circle has a radius of {}, a diameter of {} and an area of {}'.format(self._radius, self._diameter, round(self._area, 2))
