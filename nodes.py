from shapely.geometry import Point

def convert_tags(tags):
    return {tag['k']: tag['v'] for tag in tags}

class Node(object):

    def __init__(self, id, lon, lat, tags):
        self.id = id
        self.geometry = Point(lon, lat)
        self.tags = tags
