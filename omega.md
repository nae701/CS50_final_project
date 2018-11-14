# Omega Directive

## Questions

6.1. Because in the best case scenario, where the list of size n is already sorted, selection sort still has to compare
the first entry with the next n-1 entries in order to find the first sorted element, the second entry with the next n-2 entries to
find the second sorted element, and so on. Although selection sort doesnt need to do any swaps since the list is ordered, it still
has to make approximately on the order of n^2  comparisons to check that the ordered list is actually ordered. This due to the implementation of the algorithm
since it takes This is not the same as bubble sort, which after comparing the first n pairs can determine that the list sorted.

6.2. In mergesort, regardless of how ordered the list is already (and so worst case and best case are the same)
you are always moving around n items in the list, each for a total of log n times. This is because you split the
original list into n sublists, halving the list each time, which means it takes us log n times to split our original
list into n sublists, and then we compare these n items at each level of halving, which results in a running time
on the order of n log n

6.3. Regardless of the string (of length n) passed to strlen, it will take approximately n steps in order to determine the
length of the string since it has to iteratre over all n chars in the string regardless. Since there is no best or worst case scenario
strlen is both O(n) and big omega(n), and thus must be big theta(n).

6.4. This is because in python, lists are objects with attributes. One of the attributes of a list happens to be its length.
Thus, when len() is called to act on a list, rather than calculating the length, it simply looks up in constant time, the value
of the attribute called length for that list. This look up time does not change with an increase in the size of the list n.

6.5. There may be an alpbaetically ordered array that is filled with all capital letters, such that at index 0 and 1, is A and B respectively.
Then isupper simply would go to the index of the array as specified by the ASCII value of the argument char subtract the ASCII value of "A", and if the ASCII value
of the element at that index is equal to the ASCII value of the argument char, isupper would return true. Since isupper is just indexing into array,
this always takes a constant amount of time, regardless of which char is the argument.

## Debrief


a. Lecture 2 notes

b. 90 minutes
