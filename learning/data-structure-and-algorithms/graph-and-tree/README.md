Graph can be represented as 
* Adjacency matrix
* Adjacency list

other representation is
* incident matrix
* Incident list

1. Adjacancy matrix

  * 2-d size VxV matrix
  * removing an edge takes O(1) time ( ex. M[1][2] = 0 )
  * Queries for an edge existance is also O(1)
  
  * Require more space O(V**2)
  * Addition of new vertex cost O(V**2) 


 
2. Adjacancy list
  * Uses array of linked list
  * Size of array is equal to number of vertices 
  * Saves space O(|V| + |E|), worst case O(V**2)
  * Addition of new vertex is easy 
  * 

  * Queries to find edge between two vertices is O(V)
 



Traversal :: -

1. Breadth first search ( Similar to Level order traversal of tree)
  * To avoid cyclic travesal use boolean array of visited nodes
  * we use queue for breadth first search 

  * When you encounter  a new vertices
  * mark vertices visited in boolean array of visited vertices
  * queue the vertices
  * remove next element from queue 
  * perform above steps again
  * Time complexity is O(V+E)
  * Applications :: 
     * Shortest path in graph
     * Web crawler
     * Social Network 
     * Cycle detection
     * To test if graph is bipartite
     * To broadcast in network
     * Ford Folkerson algorithms

2. Depth first search 

  * To avoid cyclic traversal use boolean array of visited vertices
  * we use stack for depth first search ( recursively using stack, or Iteratively using stack )
  * Rest of the process is similar to Breadth first search
  * Time complexity is O(V+E)
  * Applications ::
     * Cycle detection 
     * Connected components
     * Topology soting
     


