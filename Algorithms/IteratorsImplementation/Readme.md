# Iterators Implementation

Write an Iterator class that has the following behavior:

    Accepts a list of strings as input to its constructor
    Has the following methods
        next(): string
        The first call returns the first element of the input list, the second call the second element, and so on. If there isn’t an element for the call, it throws an error.
        hasNext(): boolean
        Returns true if calling next would successfully return an element, otherwise false.

For example your class should behave as follows:
    iterator = new Iterator([‘a’, ‘b’, ‘c’]);
    iterator.hasNext();  // returns true
    iterator.next();  // returns ‘a’

    iterator.hasNext();  // returns true
    iterator.next();  // returns ‘b’

    iterator.hasNext();  // returns true
    iterator.next();  // returns ‘c’

    iterator.hasNext();  // returns false
    iterator.next();  // throws an Error.

------------------------------------------------
Write an InterleavingIterator class that has the following behavior:

    Implements the Iterator interface:
        next(): string
    Returns the next element in the iteration.
        hasNext(): boolean
    Returns true if the iteration has more elements.
Has a constructor that accepts a list of iterators as input.
Repeated calls to InterleavingIterator.next() must round-robin interleave the results of calls to next on iterators from the input list.

For example, suppose you have the following list of iterators: [ iteratorA, iteratorB, iteratorC ], with the following respective iterations:

iteratorA: a, b, c
iteratorB: z,
iteratorC: 1, 2, 3

Your InterleavingIterator class should accept that list of iterators and repeated calls to next should produce the following iteration: