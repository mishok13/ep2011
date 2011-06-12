class Node:

    def __init__(self, id, lat, lon, tags):
        self.id = id
        self.geometry = lat, lon
        self.tags = {tag['k']: tag['v'] for tag in tags}
