import itertools

my_list = [1,2,3]

combinations = itertools.combinations(my_list, 3)
for c in combinations:
  print(c)

# will print (1,2,3) because this is already a group of three

combinations = itertools.combinations(my_list, 2)
for c in combinations:
  print(c)
  
# will print (1,2) (1,3) (2,3) the order doesn't matter

# it is permutations where the order does matter

permutations = itertools.permutations(my_list, 2)
for p in permutations:
  print(p)
  
# will print (1,2) (1,3) (2,1) (2,3) (3,1) (3,2)
