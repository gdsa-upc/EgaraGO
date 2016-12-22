import numpy as np
import time
#import sys
# Add the root path (the path above this one) to the pythonpath.
#sys.path.insert(0,"C:/Users/sergi/Desktop/ok")
from params import get_params

params = get_params()

print ("Number of clusters:", params['descriptor_size'])
print ("Descriptor type:",params['descriptor_type'])
print ("Keypoint detector:", params['keypoint_type'])
print ("Resize dimension:", params['max_size'])
print ("Distance metric:", params['distance_type'])


import get_features as GF
# Make sure that we are using training images only !
params['split'] = 'train'

t = time.time()
X, pca, scaler = GF.stack_features(params)

print ("Done. Time elapsed:", time.time() - t)
print (np.shape(X))

t = time.time()
GF.train_codebook(params,X)

print ("Done. Time elapsed:", time.time() - t)
t = time.time()
GF.get_features(params)

print ("Done. Time elapsed for training set:", time.time() - t)
# Switch to validation set
params['split'] = 'val'

t = time.time()
# Run again
GF.get_features(params)

print ("Done. Time elapsed for validation set:", time.time() - t)

from rank import *

t = time.time()
rank(params)

print ("Done. Time elapsed:", time.time() - t)

import eval_rankings as ER

ap_list, dict_ = ER.eval_rankings(params)

print ("Number of queries:", len(ap_list))
print ("Mean Average Precision", np.mean(ap_list)),

for id in dict_.keys():
    
    if not id == 'desconegut':
        # We divide by 10 because it's the number of images per class in the validation set.
        print id, dict_[id]/10

#query_id = '30630-5639-13175'
#ER.single_eval(params,query_id)

#query_id = '29429-11804-13780'
#ER.single_eval(params,query_id)

query_id = '11962-11431-11239'
ER.single_eval(params,query_id)

query_id = '3680-16272-2487'
ER.single_eval(params,query_id)
