class Way:

    def __init__(self, id, refs, tags):
        self.id = id
        self.geometry = [nodes[ref] for ref in refs]
        self.tags = {tag['k']: tag['v'] for tag in tags}
