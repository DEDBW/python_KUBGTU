import osmium as o
from collections import Counter

OSM_FILENAME = '11.osm'

class ParkingCounterHandler(o.SimpleHandler):
    def __init__(self):
        super().__init__()
        self.parking_counts = Counter()

    def process_element(self, element):
        tags = element.tags
        if tags.get('amenity') == 'parking':
            parking_type = tags.get('parking', 'не указан')
            self.parking_counts[parking_type] += 1

    def node(self, n):
        self.process_element(n)

    def way(self, w):
        self.process_element(w)

    def relation(self, r):
        self.process_element(r)

handler = ParkingCounterHandler()

handler.apply_file(OSM_FILENAME, locations=False)

print("--- Количество парковок по типам ---")
if handler.parking_counts:
    for park_type, count in handler.parking_counts.most_common():
        print(f"- {park_type}: {count}")
else:
    print("Парковки не найдены.")