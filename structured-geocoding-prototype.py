def geocode(**query):
    boundary = world
    for key in ['country', 'zip', 'city',
                'street', 'housenumber']:
        try:
            value = query[key]
            boundary = find(key, value, boundary)
        except KeyError:
            continue
    return boundary

def find(key, value, boundary):
    for tags, geometry in data:
        if geometry in boundary and\
               tags.get(key) == value:
            return geometry
