"""
Module: test dump
Description: Dumps analytics about matrix distance completeness to a CSV.
"""
import json
import csv

def main():
    """Main execution block processing matrix sparsity."""
    with open('dist_matrix.json') as f:
        distance_matrix = json.loads(f.read())

    chk_dist = [[0] * 5 for i in range(len(distance_matrix))]
    
    for i in range(len(distance_matrix)):
        default = 0
        nonzero = 0
        zero = 0
        nan = 0
        for j in range(len(distance_matrix)):
            if (distance_matrix[i][j] == 100000):
                default = default + 1
            elif (distance_matrix[i][j] > 0):
                nonzero = nonzero + 1
            elif (distance_matrix[i][j] == 0):
                zero = zero + 1
            else:
                nan = nan + 1
        chk_dist[i][0] = default
        chk_dist[i][1] = nonzero
        chk_dist[i][2] = zero
        chk_dist[i][3] = nan
        chk_dist[i][4] = default + nonzero + zero + nan
        
    with open("output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(chk_dist)

if __name__ == '__main__':
    main()
