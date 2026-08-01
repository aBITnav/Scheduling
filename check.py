"""
Module: check
Description: Simple script to read and print the distance matrix as a DataFrame.
"""
import json
import csv
import pandas as pd

def main():
    """Main block to load and display the distance matrix."""
    with open('dist_matrix.json') as f:
        data = json.loads(f.read())
    with open('column.json') as f:
        ids = json.loads(f.read())
    with open('row.json') as f:
        rows = json.loads(f.read())

    df = pd.DataFrame(data, columns=ids, index=rows)
    df = df[rows]
    print(df)

if __name__ == '__main__':
    main()
