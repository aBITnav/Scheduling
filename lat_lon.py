from haversine import haversine
import json
import csv
with open('all_dist_matrix_new.json')as f:
    detail_matrix=json.loads(f.read())
    

with open('column.json')as f:
    columns=json.loads(f.read())


if __name__ == '__main__':
    latlon=[[0]*2 for i in range(len(columns))]
    haversine_matrix=[[0]*len(columns) for i in range(len(columns))]
    #0 -> latitude
    #1 -> Longitude
    dm=detail_matrix['514888']
    for i in range(len(columns)):
        latlon[i][0]=float(dm[columns[i]]['meta']['lat'])
        latlon[i][1]=float(dm[columns[i]]['meta']['lon'])
    for i in range(len(columns)):
        for j in range(len(columns)):
            haversine_matrix[i][j]=haversine((latlon[i][0],latlon[i][1]),(latlon[j][0],latlon[j][1]))*1000
    with open('latlon.json' , 'w')as f:
        f.write(json.dumps(latlon))
    with open('haversine_matrix.json' , 'w')as f:
        f.write(json.dumps(haversine_matrix))
    with open("haversine_matrix.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(haversine_matrix)
                                           
    
