### Algorithms & Sorts: 

1. [Binary search](https://github.com/hakloi/python_portfolio/blob/main/practice/algorithms/binary_search.py) - 
 is an algorithm with _O(log n)_ time that is used to find the position of an item in a sorted array. 
2. [Selection sort - ascending/descending](https://github.com/hakloi/python_portfolio/blob/main/practice/algorithms/selection_sort.py) -
is an algorithm _O(n^2)_ that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.
3. [Recursion](https://github.com/hakloi/python_portfolio/blob/main/practice/algorithms/recursion.py) -  is when a function calls itself. Also it uses stack. The stack is a simple data structure. Recursion is __VERY IMPORTANT__ for functional language like Haskell that doesn't have a loop.
4. [Quicksort](https://github.com/hakloi/python_portfolio/blob/main/practice/algorithms/quicksort.py) - 
is a sorting algorithm with O(n*log n) time.
5. [Merge sort]() - 
the constant in Big O notation can matter sometimes. That’s why quicksort is faster than merge sort

__Graphs__ are data structures used to represent "connections" between pairs of elements.

__Deque__ or a "double-ended queue" is a data structure that supports operations at both ends (i.e. enqueuing and dequeuing) elements in a queue. To add an element at the _beginning_ of the deque, we use the _deque.appendleft_ method, and to add an element at the _end_ of the deque, we use the _deque.appendright_ method. 

6. [Breadth-first search (BFS)](https://github.com/hakloi/python_portfolio/blob/main/practice/algorithms/breadth_first_search.py) -
is a different kind of search algorithm: one that runs on graphs. To implement BFS we use a _queue_.  Breadth-first search will find you the path with the fewest segments.
7. [Depth-first search (DFS)]() - 
the algorithm begins at the root node and then it explores each branch before backtracking. It is implemented using _stacks_. \
8. [Dijkstra’s algorithm](https://github.com/hakloi/python_portfolio/blob/main/practice/algorithms/Dijkstras.py) -
only works with directed acyclic graphs, called _DAGs_ for short. __You can’t use Dijkstra’s algorithm if you have negative-weight edges.__
9. [Bellman-Ford algorithm]() - 

__Sets__ - are like lists, except sets can’t have duplicates. Also set has some interesting operations on sets, like union, intersection, and diference.

10. [Greedy Algorithm]() -
optimize locally, hoping to end up with a global optimum. They are easy to write and fast to run, so they make good approximation algorithms.

__Hash tables__ are a powerful data structure because they’re so fast and  they let you model data in a diferent way. It has really fast search, insert, and delete.

__Queue__ - is a FIFO data structure (First In, First Out). There are two only operations - _enqueue_ and _dequeue_.

__Stack__ - is a LIFO data structure (Last In, First Out).

### NP-complete problems: have no known fast solution!
1. [Travelling Salesperson]()

2. [Max clique problem]() 

3. [Graph coloring problem]()
