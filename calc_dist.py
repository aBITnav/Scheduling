"""
Module: calc_dist
Description: Generates a symmetric distance matrix from the larger detail matrix.
"""
import json

def calc_distance(distance_matrix, source, destination):
    """Calculates the specific distance between a source and a destination ID."""
    return distance_matrix[source][destination]['distance']

def main():
    """Main logic to build the symmetric distance matrix."""
    with open('all_dist_matrix_new.json') as f:
        distance_matrix = json.loads(f.read())
    with open('row.json') as f:
        rows = json.loads(f.read())
    with open('column.json') as f:
        columns = json.loads(f.read())

    l = len(columns)
    symmetric_matrix = [[0] * l for i in range(l)]
    for i in range(l):
        for j in range(l):
            symmetric_matrix[i][j] = calc_distance(distance_matrix, columns[i], columns[j])
            
    with open('symmetric_dist_matrix.json', 'w') as f:
        f.write(json.dumps(symmetric_matrix))

if __name__ == '__main__':
    main()
