# Memory Allocator

You are given an array of integers a, containing only 0s and 1s. These values correspond to blocks of memory, where a[i] = 0 means the i-th block of memory is free, and a[i] = 1 means the i-th block is allocated, ie. not free.

Your task is to perform two types of queries:

1. alloc X: Find the left-most interval of X consecutive free blocks of memory and mark these blocks as non-free (ie: find the first contiguous subarray of length X containing all 0s, and replace them all with 1s). If there are no areas with X consecutive free blocks, return -1; otherwise return the index of the first position of the allocated segment and assign an ID to the range, based on an atomic counter (the counter starts at 1 and is incremented on every successful alloc operation).

2. erase ID: Free blocks of memory, using the id of the range ID. Return the number of deleted blocks. If there is no such ID or the blocks with this ID have already been deleted, return -1.


The queries are given in the following format:
    queries is an array of 2-elements arrays;
    if queries[i][0] = 0 then this is an alloc type query, where X = queries[i][1];
    if queries[i][0] = 1 then this is an erase type query, where ID = queries[i][1].
    Return an array containing the results of all the queries.

**Example**

    a = [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0]
    queries = [[0, 2], [0, 1], [0, 1], [1, 2], [1, 4], [0, 4]]
    memoryAllocator(a, queries) = [2, 0, 4, 1, -1, -1].

**Example 2:**

    [0, 2] corresponds to alloc 2, there are the following free segments of size 2 - [2, 3], [3, 4], [7, 8], [8, 9], [11, 12], from which we take a left-most ([2, 3]) and return the start position of the segment, which is 2. We also assign ID = 1 to this segment. After this operation a = [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0].
    [0, 1] corresponds to alloc 1, after which a = [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0]. Return 0 since that is the starting index of the allocated memory. We also assign ID = 2 to this segment.
    [0, 1] corresponds to alloc 1, after which a = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0]. Return 4 since that is the starting index of the allocated memory. We also assign ID = 3 to this segment.
    [1, 2] corresponds to erase 2. The range with ID = 2 is [0, 0] (just the 0th element). After erasing the memory, a = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0]. Return 1 since there was 1 bit of memory erased.
    [1, 4] corresponds to erase 4. The current counter is equal to 3 (since there have been 3 successful allocations), so we return -1 since there is no range with ID = 4.
    [0, 4] corresponds to alloc 4. There is no segment of size 4 in which all blocks are free, so return -1. We also assign ID = 4 to this segment.


**Input/Output**

    [input] array.integer a
    An array of 0s and 1s representing bits of memory.
        Guaranteed constraints:
            1 ≤ a.length ≤ 300.

    [input] array.array.integer queries
        An array of 2-element arrays representing queries of the type alloc or erase.
        Guaranteed constraints:.
            2 ≤ queries.length ≤ 300,
            queries[i].length = 2,
            0 ≤ queries[i][0] ≤ 1,
            If queries[i][0] = 0, then 1 ≤ queries[i][1] ≤ a.length,
            If queries[i][0] = 1, then 1 ≤ queries[i][1] ≤ queries.length - 1.

    [output] array.integer
        Return the array in which ith element is equal to the answer of ith query.
