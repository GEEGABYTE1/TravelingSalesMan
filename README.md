# TravelingSalesMan 🚶🏻‍♂️📫
Greedy Algorithm that outputs the most cost-efficient path to visit all places.

# Algorithm 📟

Assuming that the mailman has to go places `[a, b, c, d]`, with certain costs to travel a path (for ex, travelling from point `a` to point `d` costs $5), this algorithm computes the the most cost-efficient path.

We start off by setting all the places as `unvisited` places, because we actually have not traversed them yet. We then get a `current_vertex` by random since we want our algorithm to compute every possible case, which in this case, would be *4!*. We then compare it's edges and their weights.

We get the edge with the smallest weight (assuming that it's the cheapest), and we set that as the `current_vertex` after adding it to the `final_path`, which will ber returned at the end. 

To keep track of all the visited vertices, for every time a `current_vertex` updates, we make sure that the dictionary that keeps track of both unvisited and visited vertices updates as the `current_vertex` becomes it's chepeast edge. 

This algorithm will keep doing this until all the vertices have been visited. 

*There are multiple conditional statements to make sure that the algorithm checks the vertices and their statuses (visited or not) at each stage of the solution (meaning after comparing the edges, finding the cheapest edge, and after adding it to the final path), which is the algorithm's optimal substructure property.*

# More Information 

Time Complexity: `O(no. vertices + no.edges)` 

This algorithm works for all solutions and any no. of vertices. 

Made in Python 🐍
