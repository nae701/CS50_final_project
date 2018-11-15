# Song that Never Ends

## Questions

8.1. RecursionError: maximum recursion depth exceeded while calling a Python object

8.2. See `song.c`.

8.3. Segmentation fault

8.4. Each time the function sing() is called, it takes up some more space in the stack. Eventually, since it is being recursively
called indefinitely, the stack runs out of memory to store the sing() functions, which causes a "stack overflow". Since the stack
runs out of memory to use, C returns a segmentation fault indicating that there is a memory problem.

8.5. See `song.py`.

8.6. In that algorithm, David flipped to the middle of the book and discarded the half he did not need. He then
begins the algorithm over again by flipping to the middle of the remaining pages, and removed the unwanted pages. He
repeats the same steps until he finds Mike Smith. Within David's algorithm, he is "calling the function recursively" since after every few steps
he simply repeats the same process, which makes the algorithm recursive. More specifically he does step 1, step 2, and then step 3 is
of the algorithm is to go back to step 1.

## Debrief

a. Lecture 3 notes

b. 30 minutes
