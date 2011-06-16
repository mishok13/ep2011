from shapely.geometry import Point

class SimpleHandler(sax.handler.ContentHandler):

    def __init__(self):
        sax.handler.ContentHandler.__init__(self)
        self.id = None
        self.geometry = None

    def startElement(self, name, attrs):
        if name == 'node':
            self.id = attrs['id']
            self.geometry = Point(float(attrs['lon'],
                                        attrs['lat']))
