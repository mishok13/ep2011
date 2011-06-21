class SimpleHandler(sax.handler.ContentHandler):

    def __init__(self):
        sax.handler.ContentHandler.__init__(self)
        self.id = None
        self.geometry = None
        self.nodes = {}

    def startElement(self, name, attrs):
        if name == 'node':
            self.id = attrs['id']
            self.tags = {}
            self.geometry = map(
                float, (attrs['lon'], attrs['lat']))
        elif name == 'tag':
            self.tags[attrs['k']] = attrs['v']

    def endElement(self, name):
        if name == 'node':
            self.nodes[self.id] = Node(self.id,
                                       self.geometry,
                                       self.tags)
            self.id = None
            self.geometry = None
            self.tags = None
