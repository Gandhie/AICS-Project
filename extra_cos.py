import pickle
from scipy.spatial.distance import cosine

def make_file(dist_lst, filename):
    """Gets cosine distance measures for a list of vectors and saves list of measures to file."""
    vecs = dist_lst

    prep_cos = [cosine(u, v) for i, u in enumerate(vecs) for j, v in enumerate(vecs) if i > j]

    handle = filename

    with open(handle, 'wb') as outfile:
        pickle.dump(prep_cos, outfile, pickle.HIGHEST_PROTOCOL)

# Loads dictionary from file, as saved in Jupyter Notebook.
with open('11d_vecs.pkl', 'rb') as loadfile:
    prep_bbox_11d_vecs = pickle.load(loadfile)

# Checks length of the value list for the preposition (key) "under" and divides it in half (with rounding) to split the list in half to get around MemoryError.
print(len(prep_bbox_11d_vecs["under"]))
half = round(len(prep_bbox_11d_vecs["under"]) / 2)

part_one = prep_bbox_11d_vecs["under"][:half]
part_two = prep_bbox_11d_vecs["under"][half:]

# Checks length of both half-lists together, to compare to full list length above.
print(len(part_one), "+", len(part_two), "=", (len(part_one) + len(part_two)))

# Runs function for both halves.
make_file(part_one, "under_list_p1.pkl")
print("Done with Part 1 of under.")

make_file(part_two, "under_list_p2.pkl")
print("Done with Part 2 of under.")
