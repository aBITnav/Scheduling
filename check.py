import json
import csv
import pandas as pd

with open('dist_matrix.json') as f:
    data=json.loads(f.read())
with open('column.json') as f:
    ids=json.loads(f.read())
with open('row.json') as f:
    rows=json.loads(f.read())

if __name__=='__main__':
    csv=pd.DataFrame(data,columns=ids,index=rows)
    csv=csv[rows]
    print(csv)
