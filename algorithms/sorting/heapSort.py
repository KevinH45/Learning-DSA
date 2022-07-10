from data_structures.MaxHeap import MaxHeap

def heapSort(arr):

    maxHeap = MaxHeap()
    maxHeap.build_max_heap(arr)
    ls = []

    while maxHeap.heapSize>0:

        ls.append(maxHeap.find_max())
        maxHeap.swap(0,-1)
        maxHeap.heap.pop(-1)
        maxHeap.heapSize = len(maxHeap.heap)
        maxHeap.max_heapify(0)

    return ls