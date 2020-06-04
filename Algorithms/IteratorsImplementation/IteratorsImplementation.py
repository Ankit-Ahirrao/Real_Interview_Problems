
class Iterator:
	def __init__(self, arr_str):
		self.it = it(arr_str)
		self.next = next(self.it, None)

	def next(self):
		if self.next == None:
			# Exception here
			return;
		cur_next = self.next
		self.next = next(self.it, None)
		return cur_next

	def hasNext(self):
		return self.next != None


from collections import deque

class interLeavingIterator:
	def __init__(self, arr_it):
		self.it_list = self.filter(arr_it)

	def filter(self, iterators):
		filtered_arr = deque()
		for iterator in iterators:
			if iterator.hasnext():
				filtered_arr.append(iterator)
		return filtered_arr
	
	def hasNext(self):
		return len(it_list) > 0
	
	def next(self):
		if not self.hasNext():
			# Exception here
			return
		next_it = self.it_list.popleft()
		element = next_it.next()
		if next_it.hasNext():
			self.it_list.append(next_it)
		return element
		

Write or describe an InterleavingListIterator class that implements the ListIterator interface and accepts as input a list of ListIterators. ListIterator adds a previous() and hasPrevious() methods to the Iterator interface. For all input ListIterators hasPrevious evaluates to false. Can you maintain the same complexity profile of InterleavingIterator?

iteratorA: a, b, c
iteratorB: z,
iteratorC: 1, 2, 3

 a, z, 1, b, 2, c, 3

3, 1, 3



3: [A, C]
1: [B]
