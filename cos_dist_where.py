import pickle
from scipy.spatial.distance import cosine

# Loads the dictionary of prepositions and their vectors from file, as saved in the Jupyter Notebook.
with open('11d_vecs.pkl', 'rb') as loadfile:
    prep_bbox_11d_vecs = pickle.load(loadfile)

prepositions = ['over', 'above', 'below', 'under']

# Gets all cosine distance scores for each preposition and saves the list of scores to file.
# This was applied to the three first prepositions (above, below, over), but the last (under) was too large and required its own workaround script.
for p in prep_bbox_11d_vecs:
    vecs = prep_bbox_11d_vecs[p]

    prep_cos = [cosine(u, v) for i, u in enumerate(vecs) for j, v in enumerate(vecs) if i > j]

    lst_filename = p + "_list.pkl"

    with open(lst_filename, 'wb') as outfile:
        pickle.dump(prep_cos, outfile, pickle.HIGHEST_PROTOCOL)

    # Progress indication print, with example results.
    print("Done with:", p)
