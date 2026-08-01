"""
Module: final_output
Description: Exports merge assignment output to JSON.
"""
import json
import csv
import pandas as pd

def main():
    """Main execution block to export merged employee locations."""
    with open('merge.json') as f:
        clust = json.loads(f.read())
    with open('column.json') as f:
        ids = json.loads(f.read())
    with open('latlon.json') as f:
        latlon = json.loads(f.read())

    data = [[0] * 2 for i in range(len(ids))]
    k = 0
    for i in range(len(clust)):
        c = 1
        for j in clust[i]:
            data[k][0] = latlon[j][0]
            data[k][1] = latlon[j][1]
            c = c + 1
            k = k + 1

    with open('all_emp_output.json', 'w') as f:
        f.write(json.dumps(data))

if __name__ == '__main__':
    main()
