"""
Module: Dynamic dist
Description: Calculates and dynamically outputs distances based on shift IDs.
"""
import json

def calc_distance(distance_matrix, source, destination):
    """Calculates the specific distance between a source and a destination ID."""
    return distance_matrix[source][destination]['distance']

def main():
    """Main execution block to compute the specific distance matrix."""
    with open('all_dist_matrix_new.json') as f:
        distance_matrix = json.loads(f.read())
    with open('row.json') as f:
        rows = json.loads(f.read())
    with open('column.json') as f:
        columns = json.loads(f.read())
    with open('shift data/16 nov 14_45 ids.json') as f:
        ids = json.loads(f.read())

    matrix = [[0] * len(ids) for i in range(len(ids))]
   
    for i in range(len(ids)):
        for j in range(len(ids)):
            matrix[i][j] = calc_distance(distance_matrix, ids[i], ids[j])

    with open('shift data/16 nov 14_45 dm.json', 'w') as f:
        f.write(json.dumps(matrix))

if __name__ == '__main__':
    main()
