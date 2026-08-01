"""
Module: test
Description: Validates that elements having real-world distances equal to 0 also have 0 haversine distance.
"""
import json

def main():
    """Main testing logic."""
    with open('haversine_matrix.json') as f:
        haversien_matrix = json.loads(f.read())
    with open('dist_matrix.json') as f:
        distance_matrix = json.loads(f.read())

    with open('row.json') as f:
        rows = json.loads(f.read())
    with open('column.json') as f:
        columns = json.loads(f.read())

    for i in range(len(distance_matrix)):
        for j in range(len(distance_matrix)):
            if ((distance_matrix[i][j] == 0) and haversien_matrix[i][j] != 0):
                print(i, j, "Haversine:", haversien_matrix[i][j])

if __name__ == '__main__':
    main()
