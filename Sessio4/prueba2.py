# -*- coding: utf-8 -*-
import numpy as np
from get_params import get_params
from build_database import build_database
from get_features import get_features
from rank import rank
from eval_rankings import eval_rankings
import warnings
warnings.filterwarnings("ignore")

#Extraccio dels parametres
params=get_params()
#Creacio de la base de dades
params['split']='train'
build_database(params)
params['split']='val'
build_database(params)
#Extraccio de les características
get_features(params)
#Calcul del ranking
rank(params)
#Evaluacio del ranking
ap_list=eval_rankings(params)
print "-Llista de Average Precission: "
print ap_list
print "\n"
print "-Mean Average Precission: "
print np.mean(ap_list)
