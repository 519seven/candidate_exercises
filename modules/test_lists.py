import random
#random.sample(range(1, 100), 3)

DIVISOR   = 150
LOW       = 1000
HIGH      = 2882
LIST_SIZE = 1082

def make_list():
    return ['{:0.2f}'.format(x/DIVISOR) for x in random.sample(range(LOW, HIGH), LIST_SIZE)] 

list_a = make_list() 
list_b = make_list() 