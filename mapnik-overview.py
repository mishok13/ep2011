import mapnik

map = mapnik.Map(0, 0)
mapnik.load_map(map, "style.xml")
image = mapnik.Image(1000, 1000)
mapnik.render(image, map)
with open('map.png', 'w') as out:
    out.write(image.tostring('png8'))
