import pickle
from scipy.spatial.distance import cosine
import numpy as np

# Loads the dictionary of prepositions and their vectors (visual features) from file, as saved in the Jupyter Notebook.
with open('vis_vecs.pkl', 'rb') as loadfile:
    prep_vis_feat = pickle.load(loadfile)

prepositions = ['over', 'above', 'below', 'under']

joint_vis_feat = {
    p: []
    for p in prepositions
}

# Creates concatenated vectors pairwise from the target and landmark vector lists and saves the joint vectors to file.
for p in prep_vis_feat:

    targets = prep_vis_feat[p]['target']
    landmarks = prep_vis_feat[p]['landmark']
    joint_vecs = [np.concatenate((target,landmark), axis=None) for target,landmark in zip(targets,landmarks)]
    joint_vis_feat[p] = joint_vecs

for p in joint_vis_feat:
    print(p, len(joint_vis_feat[p]), joint_vis_feat[p][0].shape)

filename = "joint_what_vecs.pkl"

with open(filename, 'wb') as outfile:
    pickle.dump(joint_vis_feat, outfile, pickle.HIGHEST_PROTOCOL)

print("Saved joint vector dict to file.")
