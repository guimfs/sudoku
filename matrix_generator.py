import random as rd

lv_base_matrix = 3

lv_number_of_matrix = lv_base_matrix**2

ll_matrix = []

def f_randomlist(self,):
    lv_randomlist = rd.sample(range(1,9))
    return lv_randomlist

for i in range(len(lv_number_of_matrix)):
    ll_row = f_randomlist

