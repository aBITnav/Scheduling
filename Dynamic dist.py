import json

with open('all_dist_matrix_new.json')as f:
    distance_matrix=json.loads(f.read())
with open('row.json')as f:
    rows=json.loads(f.read())
with open('column.json')as f:
    columns=json.loads(f.read())
with open('shift data/16 nov 14_45 ids.json') as f:
    ids=json.loads(f.read())

def calc_distance(source,destination):
    return distance_matrix[source][destination]['distance']


if __name__ == '__main__':
    matrix=[[0]*len(ids) for i in range(len(ids))]
   
    for i in range(len(ids)):
    	for j in range(len(ids)):
    		matrix[i][j]=calc_distance(ids[i],ids[j])
    with open('shift data/16 nov 14_45 dm.json','w') as f:
        f.write(json.dumps(matrix))
	
