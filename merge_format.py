"""
Module: merge_format
Description: Formats merged pool clusters and attaches location dicts.
"""
import json

def main():
    """Main execution block formatting pool merges."""
    with open('merge.json') as f:
        merge = json.loads(f.read())
    with open('column.json') as f:
        ids = json.loads(f.read())
    with open('latlon.json') as f:
        latlon = json.loads(f.read())

    data = []
    for i in range(len(merge)):
        a = []
        for j in range(len(merge[i])):
            l = {'lat': 0, 'lon': 0}
            l['lat'] = latlon[merge[i][j]][0]
            l['lon'] = latlon[merge[i][j]][1]
            a.append(l)
        data.append(a)
    
    with open('all_emp_output.json', 'w') as f:
        f.write(json.dumps(data))

if __name__ == '__main__':
    main()
