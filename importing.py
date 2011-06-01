#!/usr/bin/env python


from xml import sax
import argparse
from shapely import geometry
import sys



class OSMHandler(sax.handler.ContentHandler):


    def __init__(self):
        sax.handler.ContentHandler.__init__(self)
        self.id = None
        self.geometry = None
        self.tags = []
        self.nodes = {}
        self.nds = []
        self.ways = {}


    def startElement(self, name, attrs):
        if name == 'node':
            self.id = attrs['id']
            self.geometry = float(attrs['lat']), float(attrs['lon'])
        elif name == 'tag':
            self.tags.append((attrs['k'], attrs['v']))
        elif name == 'way':
            self.id = attrs['id']
        elif name == 'nd':
            self.nds.append(self.nodes[attrs['ref']])
        elif name == 'relation':
            self.id = attrs['id']

        else:
            print name, dict(attrs)


    def endElement(self, name):
        if name == 'tag' or name == 'nd':
            return
        elif name == 'node':
            self.nodes[self.id] = self.geometry, self.tags
            self.id = None
            self.geometry = None
            self.tags = []
        elif name == 'way':
            self.ways[self.id] = (self.nds, self.tags)
            self.id = None
            self.tags = []
            self.nds = []
        else:
            print name



def main(args):
    handler = OSMHandler()
    sax.parse(args.input, handler)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='?', default=sys.stdin,
                        type=argparse.FileType('r'))
    main(parser.parse_args())
