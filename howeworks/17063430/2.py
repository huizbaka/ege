from itertools import permutations

roads = "15 17 18 24 27 28 34 35 37 42 43 47 51 53 56 65 68 71 72 73 74 81 82 86"
map_data = "АБ АГ АЕ БА БГ БВ ВБ ВД ВИ ГА ГБ ГЕ ДВ ДЖ ЕА ЕГ ЕЖ ЖЕ ЖД ЖИ ИВ ИЖ"

def road(distances, connections):
    d = set(connections.replace(' ', ''))
    for arr in permutations(d):
        t = distances
        for idx, city in enumerate(arr):
            t = t.replace(str(idx + 1), city)
        if set(connections.split()) == set(t.split()):
            return arr

for length in roads.split():
    test_roads = roads.replace(length, '').replace(length[::-1], '')
    result = road(test_roads, map_data)
    if result:
        print(length)
        break