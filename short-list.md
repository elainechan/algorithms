# Algorithms and Data Structures (Short)

## Map Reduce Filter
- [JavaScript](https://gist.github.com/alexhawkins/28aaf610a3e76d8b8264)

## Math
[slides](http://web.stanford.edu/class/cs97si/02-mathematics.pdf)
### Algebra
- [ ] Sum of powers
	- [Explanation](https://www.maa.org/press/periodicals/convergence/sums-of-powers-of-positive-integers-introduction)
- [x] Fast exponentiation - [repl](https://repl.it/@elainechan/fast-exponential)
- [ ] Recursive computation of a**n
- [ ] [Gaussian elimination](https://math.oregonstate.edu/home/programs/undergrad/CalculusQuestStudyGuides/vcalc/gauss/gauss.html), [Numpy](https://stackoverflow.com/questions/6789927/is-there-a-python-module-to-solve-linear-equations)
	- [ ] System of linear equations
	- [ ] Invert a matrix
	- [ ] Find the rank of a matrix
	- [ ] Compute determinant of matrix
### Number Theory
- [ ] Greatest common divisor/factor
- Euclidian Algorithm
	- [ ] Congruence & Modulo Operation
	- [ ] Multiplicative Inverse
	- [ ] Extended Euclidean Algorithm
- [ ] Chinese Remainder Theorem
### Combinatronics
- [ ] Binomial Coefficients
- [ ] Fibonacci Sequence
- [ ] Closed Form
### Geometry
- [ ] 2D Vector Operations
- [ ] Line-line intersection
- [ ] Circumcircle of a Triangle
- [ ] Area of a Triangle
- [ ] Area of a Simple Polygon

## Data Structures
[list](http://web.stanford.edu/class/cs97si/03-data-structures.pdf)
### Stack and Queue
- Stack: LIFO
- Constant-time:
	– `Push(x)`: inserts `x` into the stack
	– `Pop()`: removes the newest item
	– `Top()`: returns the newest item
- Have a large enough array `s[]` and a counter `k`, which starts
at zero
	– `Push(x)`: set `s[k] = x` and increment `k` by 1
	– `Pop()`: decrement `k` by 1
	– `Top()`: returns `s[k - 1]` (error if `k` is zero)
- Queue: FIFO, constant-time:
	– `Enqueue(x)`: inserts `x` into the queue
	– `Dequeue()`: removes the oldest item
	– `Front()`: returns the oldest item
### Heap and Priority Queue
- Priority Queue:
	– Insert(x, p): inserts x into the PQ, whose priority is p
	– RemoveTop(): removes the element with the highest priority
	– Top(): returns the element with the highest priority
- Heap:
- Complete binary tree with the heap property
	– The value of a node ≥ values of its children
	- The root node has the maximum value
	– Constant-time `top()` operation
### Union-Find Structure
Supports efficiently:
	– Find(x): returns the “representative” of the set that x belongs
	– Union(x, y): merges two sets that contain x and y
### Binary Search Tree (BST)
- For each node:
	– value of v >= values in v’s left subtree
	– value of v <= values in v’s right subtree
- Supports three operations:
	– Insert(x): inserts a node with value x
	– Delete(x): deletes a node with value x, if there is any
	– Find(x): returns the node with value x, if there is any
- Extensions:
	– Count(x): counts the number of nodes with value less than or equal to x
	– GetNext(x): returns the smallest node with value >= x
### Fenwick Tree
Supports very useful interval operations:
	– `Set(k, x)` : sets the value of kth item equal to `x`
	– `Sum(k)`: computes the sum of items `1, ..., k` (prefix sum)
		- Note: sum of items `i, ..., j` = `Sum(j) − Sum(i − 1)`
- `O(log n)` time using `O(n)` space
### Lowest Common Ancestor (LCA)
- Input: a rooted tree and a bunch of node pairs
- Output: lowest (deepest) common ancestors of the given pairs of nodes
- Goal: preprocessing the tree in O(n log n) time in order to answer each LCA query in `O(log n)` time