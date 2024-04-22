import paramath

list_one = [-5,1,22,3,34,5,6,7,8,9,12,55,11,99]
list_two = [-5,1,22,3,34,5,6,7,10,44,12,12,9]

my_data = paramath.Table(list_one, list_two)

graph = my_data.points()

print(graph)