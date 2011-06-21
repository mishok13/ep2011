class SimpleHandler(sax.handler.ContentHandler):

    def __init__(self):
        ...
        self.ways = {}

    def startElement(self, name, attrs):
        if name == 'way':
            self.id = attrs['id']
            self.tags = {}
            self.geometry = []
        elif name == 'nd':
            self.geometry.append(attrs['ref'])

    def reset(self):
        self.id = None
        self.geometry = None
        self.tags = None

    def endElement(self, name):
        if name == 'way':
            self.way[self.id] = Way(self.id,
                                    self.geometry,
                                    self.tags)
            self.reset()
