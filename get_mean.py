import numpy as np
import pickle

with open('above_list.pkl', 'rb') as load1:
    above_dists = pickle.load(load1)

with open('below_list.pkl', 'rb') as load2:
    below_dists = pickle.load(load2)

with open('over_list.pkl', 'rb') as load3:
    over_dists = pickle.load(load3)

with open('under_list_p1.pkl', 'rb') as load4:
    under_list1 = pickle.load(load4)

with open('under_list_p2.pkl', 'rb') as load5:
    under_list2 = pickle.load(load5)

under_dists = under_list1 + under_list2

print(len(under_dists), len(under_list1), len(under_list2))

above_mean = np.mean(above_dists)
below_mean = np.mean(below_dists)
over_mean = np.mean(over_dists)
under_mean = np.mean(under_dists)

print(above_mean, below_mean, over_mean, under_mean)
