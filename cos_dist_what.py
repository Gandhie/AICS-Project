import pickle
from scipy.spatial.distance import cosine
import numpy as np

# Loads the dictionary of prepositions and their vectors (visual features) from file, as saved in the Jupyter Notebook.
with open('vis_vecs.pkl', 'rb') as loadfile:
    prep_vis_feat = pickle.load(loadfile)

prepositions = ['over', 'above', 'below', 'under']

# Gets cosine distance measures for target and landmarks separately in lists, which are then assigned as the values of their respective label in a dictionary which is saved to file.
for p in prep_vis_feat:
    targ_vecs = prep_vis_feat[p]['target']
    landm_vecs = prep_vis_feat[p]['landmark']

    prep_targ_cos = [cosine(u, v) for i, u in enumerate(targ_vecs) for j, v in enumerate(targ_vecs) if i > j]
    prep_landm_cos = [cosine(u, v) for i, u in enumerate(landm_vecs) for j, v in enumerate(landm_vecs) if i > j]

    prep_cos_dict = {}
    prep_cos_dict['target'] = prep_targ_cos
    prep_cos_dict['landmark'] = prep_landm_cos

    lst_filename = p + "_what_dict.pkl"

    with open(lst_filename, 'wb') as outfile:
        pickle.dump(prep_cos_dict, outfile, pickle.HIGHEST_PROTOCOL)

    # Progress indication print, with example results.
    print("Done with:", p)
