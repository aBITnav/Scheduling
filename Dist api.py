"""
Module: Dist api
Description: Extracts smaller distance matrix mappings from a larger detail matrix.
"""
import json
from pydash import objects

def make_small(matrix, key):
    """Reduces the matrix to include only the specified key (e.g. 'distance')."""
    return [[objects.get(t, key)  for _,t in v.items()] for _,v in matrix.items()]

def get_id(matrix):
    """Returns the list of keys from the matrix as a list."""
    return [list(matrix.keys())[t] for t in range(len(matrix))]

def get_col(matrix):
    """Returns the keys of the matrix."""
    return list(matrix.keys())

def main():
    """Main execution function to load data and write smaller mapping files."""
    # RUNTIME FOR 10K data POINTS IS 20 Sec
    with open('all_dist_matrix_new.json') as f:
        detail_matrix = json.loads(f.read())

    dist_matrix = make_small(detail_matrix, 'distance')
    row = get_id(detail_matrix) # from
    column = get_col(detail_matrix["514888"]) # to

    with open('dist_matrix.json', 'w') as f:
        f.write(json.dumps(dist_matrix))
    with open('row.json', 'w') as f:
        f.write(json.dumps(row))
    with open('column.json', 'w') as f:
        f.write(json.dumps(column))

if __name__ == '__main__':
    main()
