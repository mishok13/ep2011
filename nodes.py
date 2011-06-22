from shapely.geometry import Point

class Node(object):

    def __init__(self, id, lonlat, tags):
        self.id = id
        self.geometry = Point(projection(*lonlat))
        self.tags = tags
