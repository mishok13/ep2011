import mapnik

map = mapnik.Map(1000, 1000)
mapnik.load_map(map, "style.xml")
bbox = mapnik.Envelope(mapnik.Coord(-180.0, -90.0),
                       mapnik.Coord(180.0, 90.0))
map.zoom_to_box(bbox)
mapnik.render_to_file(map, 'map.png', 'png')
