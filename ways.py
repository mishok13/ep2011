from shapely.geometry import LineString

nodes = {...} # dict of nodes, keyed by their ids

class Way(object):

    def __init__(self, id, refs, tags):
        self.id = id
        self.geometry = LineString(
            [(nodes[ref].x, nodes[ref].y)
             for ref in refs])
        self.tags = tags
