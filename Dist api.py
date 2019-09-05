import json
from pydash import objects
def make_small(matrix, key):
    return [[objects.get(t, key)  for _,t in v.items()] for _,v in matrix.items()]
def id(matrix):
    return [list(matrix.keys())[t] for t in range(len(matrix))]
def col(matrix):
    return list(matrix.keys())

    
#RUNTIME FOR 10K data POINTS IS 20 Sec

if __name__ == '__main__':
    with open('all_dist_matrix_new.json')as f:
        detail_matrix=json.loads(f.read())
    dist_matrix=make_small(detail_matrix,'distance')
    row=id(detail_matrix) #from
    column=col(detail_matrix["514888"]) #to
    with open('dist_matrix.json', 'w') as f:
        f.write(json.dumps(dist_matrix))
    with open('row.json', 'w') as f:
        f.write(json.dumps(row))
    with open('column.json', 'w') as f:
        f.write(json.dumps(column))

    
