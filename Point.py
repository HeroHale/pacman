import pygame

class Point():
    def __init__(self, coords):
        self.points = []
        self.x = coords[0]
        self.y = coords[1]
    def set_connections(self, connections):
        self.points = connections
        for point in connections:
            point.points.append(self)
    def get_valid_directions(self):
        for connection in self.points:
            pass
