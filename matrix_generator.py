import random as rd
import itertools as it

lv_base_matrix = 3

lv_number_of_matrix = lv_base_matrix**2

lv_range_of_numbers = range(1,10)

ll_matrix = []

#generates randomlist from a list of valid numbers
def f_randomlist(valid_numbers, *args):
    ll_random_list = rd.sample(valid_numbers, (valid_numbers.stop - 1))
    return ll_random_list

#create list with rows of matrix and the values
ll_rows = []
for i in range(lv_number_of_matrix):
    ll_row = f_randomlist(lv_range_of_numbers)
    ll_rows.append(ll_row)

#Identifies elements that are equal in the columns
for i in range(len(ll_rows[i])):
    for j in range(len(ll_rows)):
        if i < (len(ll_rows[i])) - 2:
            if ll_rows[i][j] == ll_rows[i+1][j]:
                print("line", i, "element ", j, "equal to line", i+1)



    #if i > 0:
        #for j in range(len(ll_row)):
            #while ll_rows[i-1][j] == ll_rows[i][j]:
                #fazer reorganizar a lista
                #trocar o invalido com o ultimo com o ultimo
                #lv_invalid_numb = ll_rows[i][j]
                    #move element to end of list
                 #   ll_rows[i].append(ll_rows[i].pop(ll_rows[i].index(ll_rows[i][j])))
                    #move elemenet to begin of list
#                    ll_teste = ll_rows[i][1:]
#                    ll_teste.remove(ll_teste[6])
#                    ll_rows[i] = ll_rows[i][-2:-1] + ll_teste
                    # ultimo elemento -> ll_rows[i][len(ll_rows[i])-1]
                

#                ll_row = f_randomlist(lv_range_of_numbers)
#                ll_rows.append(ll_row)



print("End")