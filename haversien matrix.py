"""
Module: haversien matrix
Description: Reduces the detail matrix down to only haversine distance values.
"""
import json
from pydash import objects

def make_small(matrix, key):
    """Reduces the matrix to a matrix of specific values."""
    return [[objects.get(t, key)  for _, t in v.items()] for _, v in matrix.items()]

def main():
    """Main execution logic to write the simplified haversine matrix."""
    # RUNTIME FOR 10K data POINTS IS 20 Sec
    with open('all_dist_matrix_new.json') as f:
        detail_matrix = json.loads(f.read())

    dist_matrix = make_small(detail_matrix, 'haversine')
    
    with open('haversine_matrix.json', 'w') as f:
        f.write(json.dumps(dist_matrix))

if __name__ == '__main__':
    main()
