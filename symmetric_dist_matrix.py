"""
Module: symmetric_dist_matrix
Description: Outputs the structured symmetric distance matrix format.
"""
import json
import csv

def calc_distance(distance_matrix, rows, columns, source, destination):
    """Calculates the specific distance based on index maps."""
    return distance_matrix[rows.index(source)][columns.index(destination)]

def main():
    """Main logic to build the symmetric matrix."""
    with open('dist_matrix.json') as f:
        distance_matrix = json.loads(f.read())
    with open('row.json') as f:
        rows = json.loads(f.read())
    with open('column.json') as f:
        columns = json.loads(f.read())

    l = len(columns)
    symmetric_dist_matrix = [[0] * l for i in range(l)]

    # Logic to build the matrix is commented out in original file:
    # for i in range(l):
    #     for j in range(l):
    #         symmetric_dist_matrix[i][j]=calc_distance(distance_matrix, rows, columns, columns[i], columns[j])
    #     with open('symmetric_dist_matrix.json','w') as f:
    #         f.write(json.dumps(symmetric_dist_matrix))
    #     with open('symmetric_dist_matrix.csv','w') as f:
    #         writer = csv.writer(f)
    #         writer.writerows(symmetric_dist_matrix)

if __name__ == '__main__':
    main()
