import json
import csv
import pandas as pd

with open('merge.json') as f:
    clust=json.loads(f.read())
with open('column.json') as f:
    ids=json.loads(f.read())
with open('latlon.json') as f:
    latlon=json.loads(f.read())

if __name__=='__main__':
    data=[[0]*2 for i in range(len(ids))]
    k=0
    for i in range(len(clust)):
        c=1
        for j in clust[i]:
            #data[k][0]=ids[j]
            #data[k][1]=j
            data[k][0]=latlon[j][0]
            data[k][1]=latlon[j][1]
            #data[k][4]=i+1
            #data[k][5]=c
            c=c+1
            k=k+1

    with open('all_emp_output.json','w') as f:
        f.write(json.dumps(data))
    '''csv=pd.DataFrame(data,columns=['Employee','Sl.No','Lat','Lon','Pool','Order'])
    with open("clust_analysis.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(csv)
    csv.to_csv('merge_lsis.csv')'''
    
        
