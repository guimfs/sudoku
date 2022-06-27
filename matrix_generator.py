import random as rd
import itertools as it
from unittest import case

lv_base_matrix = 3

lv_number_of_matrix = lv_base_matrix**2

lv_range_of_numbers = range(1,lv_number_of_matrix + 1)

ll_matrix = []

#generates randomlist from a list of valid numbers
def f_randomlist(valid_numbers):
    ll_random_list = rd.sample(valid_numbers, (valid_numbers.stop - 1))

    return ll_random_list


#create list with rows of matrix and the values
ll_rows = []
ll_column = []
ll_exclude = []
for i in range(lv_number_of_matrix):
    ll_row = f_randomlist(lv_range_of_numbers)
    ll_column.append
    ll_rows.append(ll_row)

#create list conaining all columns elements
ll_columns = []
for i in range(len(ll_rows[i])):
    ll_column = []
    for j in range(len(ll_rows)):
        ll_column.append(ll_rows[j][i])
    ll_columns.append(ll_column)

ld_repeat_elements = {}
#Identifies elements that are equal in the columns
for i in range(len(ll_rows[i])):
    for j in range(len(ll_rows)):
        if i < (len(ll_rows[i])) - 2:
            if ll_rows[i][j] == ll_rows[i+1][j]:
#                ld_repeat_elements["element ",j, "line ",i, " and ", i+1] = ll_rows[i][j]

                print("line", i, "element ", j, "equal to line", i+1)

print("End")