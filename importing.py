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
        self.nodes = {}
        self.ways = {}
        self.relations = {}
        self.current = None


    def startElement(self, name, attrs):
        if name == 'node':
            self.id = attrs['id']
            self.current = (float(attrs['lat']), float(attrs['lon'])), []
        elif name in ('way', 'relation'):
            self.id = attrs['id']
            self.current = [], []
        elif name == 'tag':
            self.current[1].append((attrs['k'], attrs['v']))
        elif name == 'nd':
            self.current[0].append(attrs['ref'])
        elif name == 'member':
            self.current[0].append(attrs)
        else:
            print name, dict(attrs)


    def endElement(self, name):
        try:
            container = {'node': self.nodes,
                         'way': self.ways,
                         'relation': self.relations}[name]
            container[self.id] = self.current
        except KeyError:
            pass



def main(args):
    handler = OSMHandler()
    sax.parse(args.input, handler)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='?', default=sys.stdin,
                        type=argparse.FileType('r'))
    main(parser.parse_args())
