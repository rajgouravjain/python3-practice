Graph Representation 
=

Edge list
-

Adjacency matric
-

Adjacency list
-

1. list of list
1. dict of dict ( with edge weigth)
1. use default dict (ex. of BFS in GFG)


1. Array of Nodes. Each node is pointing to Linkedlist of incindent node with weight
1. Node as object containing dict of incident node and weight.

Breath first Search
-
Breath first search requires::
1. Array of boolean for visited node
1. A queue for ordering the nodes touched by during visit
1. A graph

Breath first search works on loop on queue and visited nodes, 
if queue has members keep visiting it. If all nodes are visited and queue 
is empty. teminate the loop.

Depth first search 
-

Depth first search can be implemented two ways 

#### Similar to Breath first search (Iterative depth first search)
This method requires::
1. array of booleans for visited nodes
2. A Stack to  keep  track of nodes which are touched upon\
 but not visited
3. A graph object

#### Recusion using dynamic programming
This method requries::
1. Utility fuction which takes a vertex and array of visited nodes. 
visited node will call Recursion on utility fuction to visit, connected nodes.


