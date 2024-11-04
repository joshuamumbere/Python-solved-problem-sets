# In this file i will implement lambda with filter, map and reduce functions

# Given that am using an input list given below
input_list =[2,3,4,5,6,7]

# I now want to use the map function to square each list item
map_answer = map(lambda x: x**2, input_list)
print(list(map_answer))

# I now want to use the filter function to filter out the even numbers
filter_answer = filter(lambda x: x%2==0, input_list)
print(list(filter_answer))

# I now want to use the reduce function to sum up all the list items
from functools import reduce
reduce_answer = reduce(lambda x,y: x+y , input_list)
print(reduce_answer)
