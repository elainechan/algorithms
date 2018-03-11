## Notes

### Divide and Conquer
- **Steps**:
	1. _Divide_ the problem into a number of subproblems that are smaller instances of the same problem.
	2. _Conquer_ the subproblems by solving them _recursively_. If the subproblem sizes are small enough, however, just solve the subproblems in a straightforward manner.
	3. _Combine_ the solutions to the subproblems into the solution for the original problem.

### Dynamic Programming
- Similar to _Divide and Conquer_ with a typical focus on _optimization_
- _Memoize_: solves each subsubproblem just once and then saves its answer in a table, thereby avoiding the work of recomputing the answer every time it solves each subsubproblem.
- **Steps**:
	1. Characterize the structure of an optimal solution.
	2. Recursively define the value of an optimal solution.
	3. Compute the value of an optimal solution, typically in a bottom-upf ashion.
	4. Construct an optimal solution from computed information.

### Greedy Algorithms
- always makes the choice that looks best at the moment
- it makes a locally optimal choice in the hope that this choice will lead to a globally optimal solution

--------
## Code Jam
- [past problems](https://code.google.com/codejam/past-contests)
- [quick start guide](https://code.google.com/codejam/resources/quickstart-guide#io-tutorial)

## Solving Strategies
- [common constraints](https://www.hiredintech.com/the-common-constraints-handout.pdf)
- [engineering approach, model of thinking](http://decuqa.tumblr.com/post/140338241671/how-does-google-evaluate-analytical-thinking)
- [steps to tackle a problem](http://www.jessicayung.com/how-to-tackle-programming-problems-google-code-jam-2017-qualification-round-problem-a/)
- [solving toy problems](https://docs.google.com/document/d/1KlU7nxRKiicGSsMN89mog06GozqfYlyh0L3DRC3WYFk/edit)
- [quora answer](https://www.quora.com/What-is-a-good-way-to-prepare-for-Google-Code-Jam)

## Implementations Tips
- `import collections` when working with data structures
- Stacks and queues - use `deque` or `list` (list is faster, deque more powerful)
- Union find - use `set`
- Fenwick tree, prefix sum - code manually
- Do learn to implement:
	- Pascal Triangle
	- Priority Queue/heap

## Resources
- [Stanford intro to programming contests](http://web.stanford.edu/class/cs97si/)
- [USCAO Olympiads](http://train.usaco.org/usacogate?a=e2IlxKa7a9I)
- [Peking Online Judge](http://poj.org/)