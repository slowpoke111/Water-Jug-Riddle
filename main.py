from Graph import *
 
start = Node(0,0)
g = Graph(start)

print('Running Greedy Search...')
path, num_states = g.greedySearch()
print('Number of States Searched: ' + str(num_states))
print('Solution: ')
for node in path:
  print(node)
print()

print('Running A* Search...')
path, num_states = g.a_star()
print('Number of States Searched: ' + str(num_states))
print('Solution: ')
for node in path:
  print(node)
print()

        
