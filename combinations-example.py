# the question is how many different groups of 3 can you take
# from this list that are equal to 10

my_list = [1,2,3,4,5,6]

combinations = itertools.combinations(my_list, 3)
permutations = itertools.permutations(my_list, 3)

print([result for result in combinations if sum(result) == 10])

# the output is
# [(1,3,6), (1,4,5), (2,3,5)]

# if we place permuatitons instead of combinations

print([result for result in permutations if sum(result) == 10])

# the output is
# [(1,3,6),(1,4,5),(1,5,4),(1,6,3),(2,3,5),(2,5,3),(3,1,6),(3,2,5),(3,5,2),
# (3,6,1),(4,1,5),(4,5,1),(5,1,4),(5,2,3),(5,3,2),(5,4,1),(6,1,3),(6,3,1)]

# you can see that we get a lot more values and order matters

# this is the example where the order would matter ->
# a word matching game

word = 'sample'
my_letters = 'plmeas'

combinations = itertools.combinations(my_letters, 6)
permutations = itertools.permutations(my_letters, 6)

for p in permutations:
  # print p
  if ''.join(p) == word:
    print("Match!")
    break
else:
  print("No match!")
  
# can't find a match with combinations
# permutations should be used in this example

