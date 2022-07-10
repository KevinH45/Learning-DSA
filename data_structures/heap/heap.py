from copy import deepcopy

class MaxHeap:

    def __init__(self, heap=[]):

        self.heap = heap
        self.heapSize = len(self.heap)

    def find_left(self,i):
        return 2*i +1

    def find_right(self, i):
        return (2*i)+2

    def swap(self, i1, i2):
        tmp = self.heap[i1]
        self.heap[i1] = self.heap[i2]
        self.heap[i2] = tmp

    def max_heapify(self, i):
        
        if not self.heap:
            return

        left = self.find_left(i)
        right = self.find_right(i)


        # If left exists and its greater than its parent node, set it to the largest value (among left, right, and root)
        # Else, set the largest value to the root/parent
        if left<self.heapSize and self.heap[left]>self.heap[i]:
            largest = left
        else:
            largest = i
        
        # If right exists and its value is greater than the largest value, set the largest value to right
        if right<self.heapSize and self.heap[right]>self.heap[largest]:
            largest = right
        
        if largest!=i:
            self.swap(i,largest)
            self.max_heapify(largest)

    def build_max_heap(self, arr):
        n = len(arr)//2 - 1

        self.heap = deepcopy(arr)
        self.heapSize = len(arr)

        while n>=0:
            self.max_heapify(n)
            n-=1

    def find_max(self):
        if not self.heap:
            return None

        return self.heap[0]
    
    def extract_max(self):
        mx = self.heap.pop(0)
        
        # Heap is now jumbled mess, turn it back to max_heap
        self.build_max_heap(self.heap)

        return mx

    def edit_node(self, i, val):
        self.heap[i] = val
        self.build_max_heap(self.heap)

    def has_mhp(self):
        print(self.heap)

        def dfs(i):
            
            if i>=self.heapSize:
                return True
            
            left = self.find_left(i)
            right = self.find_right(i)
            parent = self.heap[i]


            print(i,left,right)
            

            # IF IN HEAP AND GREATER THAN PARENT
            if left<self.heapSize and self.heap[left]>parent:
                return False
                
            if right<self.heapSize and self.heap[right]>parent:
                return False
            
            return dfs(left) and dfs(right)

        return dfs(i=0)

class MinHeap:

    def __init__(self, heap=[]):

        self.heap = heap
        self.heapSize = len(self.heap)

    def find_left(self,i):
        return 2*i +1

    def find_right(self, i):
        return (2*i)+2

    def swap(self, i1, i2):
        tmp = self.heap[i1]
        self.heap[i1] = self.heap[i2]
        self.heap[i2] = tmp

    def min_heapify(self, i):
        
        if not self.heap:
            return

        left = self.find_left(i)
        right = self.find_right(i)


        if left<self.heapSize and self.heap[left]<self.heap[i]:
            smallest = left
        else:
            smallest = i

        if right<self.heapSize and self.heap[right]<self.heap[smallest]:
            smallest = right
        
        if smallest!=i:
            self.swap(i,smallest)
            self.min_heapify(smallest)

    def build_min_heap(self, arr):
        n = len(arr)//2 - 1

        self.heap = deepcopy(arr)
        self.heapSize = len(arr)

        while n>=0:
            self.min_heapify(n)
            n-=1

    def find_min(self):
        if not self.heap:
            return None

        return self.heap[0]
    
    def extract_min(self):
        mx = self.heap.pop(0)
        
        # Heap is now jumbled mess, turn it back to min_heap
        self.build_min_heap(self.heap)

        return mx

    def edit_node(self, i, val):
        self.heap[i] = val
        self.build_min_heap(self.heap)

    def has_mhp(self):
        print(self.heap)

        def dfs(i):
            
            if i>=self.heapSize:
                return True
            
            left = self.find_left(i)
            right = self.find_right(i)
            parent = self.heap[i]


            print(i,left,right)
            

            # IF IN HEAP AND LESS THAN PARENT
            if left<self.heapSize and self.heap[left]<parent:
                return False
                
            if right<self.heapSize and self.heap[right]<parent:
                return False
            
            return dfs(left) and dfs(right)

        return dfs(i=0)