import json

def make_symmetric(matrix):
       for i in range(len(matrix)):
              for j in range(len(matrix[i])):
                     if matrix[i][j] != matrix[j][i]:
                            matrix[i][j] = matrix[j][i] = (matrix[i][j] + matrix[j][i])/2
       return matrix

if __name__ == '__main__':
    
    
    with open('dist_matrix.json')as f:
        distance_matrix = json.loads(f.read())
    dm=[[]]*(len(distance_matrix))
    with open('row.json')as f:
        rows=json.loads(f.read())
    with open('column.json')as f:
        columns=json.loads(f.read())
    for i in range(len(distance_matrix)):
           for j in range(len(distance_matrix)):
                  if distance_matrix[j][i] == 0:
                         dm[i]=distance_matrix[j]
    with open('symmetry.json', 'w') as f:
        f.write(json.dumps(dm))
    
    
    
