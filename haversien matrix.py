import json
from pydash import objects
def make_small(matrix, key):
    return [[objects.get(t, key)  for _,t in v.items()] for _,v in matrix.items()]


    
#RUNTIME FOR 10K data POINTS IS 20 Sec

if __name__ == '__main__':
    with open('all_dist_matrix_new.json')as f:
        detail_matrix=json.loads(f.read())
    dist_matrix=make_small(detail_matrix,'haversine')
    with open('haversine_matrix.json', 'w') as f:
        f.write(json.dumps(dist_matrix))
    
