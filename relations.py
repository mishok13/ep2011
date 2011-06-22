from shapely.geometry import MultiPolygon, MultiLineString, ...

ways = {...} # dict of ways, with ids as keys

class Relation(object):

    def __init__(self, id, members, tags):
        self.id = id
        self.tags = tags
        if tags['type'] == 'multipolygon':
            outer = [ways[member['ref']]
                     for member in members
                     if member['role'] == 'outer']
            inner = [ways[member['ref']]
                     for member in members
                     if member['role'] == 'inner']
            self.geometry = MultiPolygon([(outer, inner)])
