class MaxHeap():
    def __init__(self, size):
        # Create a heap with the initial capacity given by size.
        self.lastIndex = -1 #denoting empty heap
        self.array = [-1] * size  # array of size containing -1 denoting node not being used
        pass

    def insert(self, data):
        # Insert an item in to the heap.
        # This method should be able to handle items above and beyond the initial capacity
        if self.lastIndex is -1:
            self.array[1] = data
            self.lastIndex = 1
        else:
            self.lastIndex += 1
            self.array[self.lastIndex] = data
        if self.lastIndex > 3:
            parentNew = self.lastIndex//2
            # bottom up heapify
            for i in range(parentNew, 0, -1):
                self.heapify(i)
        else:
            self.heapify(1)
        pass

    def heapify(self, position):
        largest = position
        left = 2 * position
        right = 2 * position + 1
        length = self.lastIndex
        arr = self.array
        check1 = False
        check2 = False
        if left <= length and arr[position] < arr[left]:
            largest = left
            check1 = True
        if right <= length and arr[position] < arr[right]:
            largest = right
            check2 = True
        if check1 and check2:
            if arr[left] > arr[right]:
                largest = left
        if largest != position:
            arr[position], arr[largest] = arr[largest], arr[position]
            self.heapify(largest)
        pass

    def extractMax(self):
        # Return the largest item in the heap, but ensure that the heap property is maintained
        largestItem = self.array[1]
        self.array[1] = self.array[self.lastIndex]
        mid = self.lastIndex//2
        self.lastIndex -= 1
        # top down heapify
        for i in range(1, mid+1):
            self.heapify(i)        
        return largestItem
        pass

    def __len__(self):
        # Return the number of items currently in the heap
        if self.lastIndex is -1:
            return 0
        else:
            return self.lastIndex
        pass

    def getData(self):
        # Return the current heap as an array that does not use the first value
        return self.array[0:self.lastIndex+1]
        pass
