Source - 

```
https://gist.github.com/qrious-will/874578dc83674f47de7062198ae263f6
```

---


We'd like you to write some code to determine whether a maze is solvable and share it with us as a GitHub repo.

For this test, we ask you to solve the following programming problem:

```
Given a string of the form:

xx.exx
...xxx
.x....
xxxx..
x.x..s

Where:
- x indicates a wall,
- s indicates the start of the maze,
- e indicates the end of the maze,
Return a boolean to indicate whether the maze is solvable. You can only move up, down, left, or right.
```

If we were to call your code as a function, we would expect it to work something like this:

```
maze1 = """
xx.exx
...xxx
.x....
xxxx..
x.x..s
"""

solvable(maze1)
> True

maze2 = """
xs.x.e
...x..
"""

solvable(maze2)
> False
```

Additional Notes:

- Do write unit tests.
- Do include links to any references you used.
- Don't take much more than 2 hours.
- Don't use someone else's code to do the parsing or solving (we want to see how you do it!).
- Your solution will be judged based on its correctness, computational efficiency, and clarity. 
- Please use your own judgement to resolve any ambiguities and include a suitable explanation if necessary.
- We'd prefer your implementation to be written in Python; if you use a different language, please advise why you chose it.