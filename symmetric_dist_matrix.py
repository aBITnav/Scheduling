import json
import csv

with open('dist_matrix.json')as f:
    distance_matrix=json.loads(f.read())
with open('row.json')as f:
    rows=json.loads(f.read())
with open('column.json')as f:
    columns=json.loads(f.read())

def calc_distance(source,destination):
    return distance_matrix[rows.index(source)][columns.index(destination)]
if __name__ == '__main__':
    l=len(columns)
    symmetric_dist_matrix=[[0]*l for i in range(l)]
    '''for i in range(l):
        for j in range(l):
            symmetric_dist_matrix[i][j]=calc_distance(columns[i],columns[j])
        with open('symmetric_dist_matrix.json','w') as f:
            f.write(json.dumps(symmetric_dist_matrix))
        with open('symmetric_dist_matrix.csv','w') as f:
            writer = csv.writer(f)
            writer.writerows(symmetric_dist_matrix)'''
                
                
	    
            
	
