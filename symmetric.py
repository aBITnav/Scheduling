"""
Module: symmetric
Description: Converts asymmetric distance data to a symmetric representation.
"""
import json

def make_symmetric(matrix):
    """Averages distance mappings to enforce bidirectionality (symmetry)."""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != matrix[j][i]:
                matrix[i][j] = matrix[j][i] = (matrix[i][j] + matrix[j][i]) / 2
    return matrix

def main():
    """Main execution block enforcing symmetry on distance maps."""
    with open('dist_matrix.json') as f:
        distance_matrix = json.loads(f.read())

    dm = [[]] * len(distance_matrix)

    with open('row.json') as f:
        rows = json.loads(f.read())
    with open('column.json') as f:
        columns = json.loads(f.read())

    for i in range(len(distance_matrix)):
        for j in range(len(distance_matrix)):
            if distance_matrix[j][i] == 0:
                dm[i] = distance_matrix[j]

    with open('symmetry.json', 'w') as f:
        f.write(json.dumps(dm))

if __name__ == '__main__':
    main()
