import json
import csv



with open('dist_matrix.json')as f:
    distance_matrix=json.loads(f.read())


if __name__ == '__main__':
    default=0
    nonzero=0
    zero=0
    nan=0
    chk_dist=[[0]*5 for i in range(len(distance_matrix))]
    
    for i in range(len(distance_matrix)):
        default=0
        nonzero=0
        zero=0
        nan=0
        for j in range(len(distance_matrix)):
            if(distance_matrix[i][j] == 100000):
                default=default+1
            elif(distance_matrix[i][j]>0):
                nonzero=nonzero+1
            elif(distance_matrix[i][j]==0):
                zero=zero+1
            else:
                nan = nan + 1
        chk_dist[i][0]=default
        chk_dist[i][1]=nonzero
        chk_dist[i][2]=zero
        chk_dist[i][3]=nan
        chk_dist[i][4]=default+nonzero+zero+nan
        
    with open("output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(chk_dist)
                               

