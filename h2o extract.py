import json

with open('h2o.json') as f:
    h2o=json.loads(f.read())
with open ('column.json') as f:
    allids=json.loads(f.read())
with open('shift data/16 nov 14_45 ids.json') as f:
    shiftids=json.loads(f.read())
if __name__=='__main__':
    shifth2o=[0]*len(shiftids)
    for i in range(len(shiftids)):
        shifth2o[i]=h2o[allids.index(shiftids[i])]
    with open('shift data/16 nov 14_45 h2o.json','w') as f:
        f.write(json.dumps(shifth2o))
