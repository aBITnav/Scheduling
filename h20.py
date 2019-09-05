from haversine import haversine
import json

with open('latlon.json') as f:
    latlon = json.loads(f.read())
if __name__ == '__main__':
    h2o = [0] * len(latlon)
    for i in range(len(latlon)):
        h2o[i] = round(haversine((12.8493202, 77.67812649999999), (latlon[i][0], latlon[i][1])) * 1300)
    with open('h2o.json', 'w') as f:
        f.write(json.dumps(h2o))
