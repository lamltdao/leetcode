from heapq import heapify, heappush, heappop
class MedianFinder:

    def __init__(self):
        """
        1,3,4,6
        7
        
        2 heaps: k ele
        max heap: store min k//2 el
        min heap: store max k//2 el
        findMed: log(m) + log(n)
        Invariant: min_heap ==  max_heap or min_heap == max_heap+1 min_heap+1 >= max_heap
        """
        self.min_heap = []
        heapify(self.min_heap)
        self.max_heap = []
        heapify(self.max_heap)

    def addNum(self, num: int) -> None:
        # move 
        heappush(self.min_heap, num)
        # Reorder
        if len(self.min_heap) > 0 and len(self.max_heap) > 0:
            min_of_max = heappop(self.min_heap)
            max_of_min = -heappop(self.max_heap)
            if min_of_max < max_of_min:
                heappush(self.min_heap, max_of_min)
                heappush(self.max_heap, -min_of_max)
            else:
                heappush(self.min_heap, min_of_max)
                heappush(self.max_heap, -max_of_min)
        # Keep the invariant
        while len(self.min_heap) > 0 and len(self.min_heap) > len(self.max_heap) + 1:
            heappush(self.max_heap, -heappop(self.min_heap))
        while len(self.max_heap) > 0 and len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))

    def findMedian(self) -> float:
        count = len(self.min_heap) + len(self.max_heap)
        if count & 1: # odd
            med = heappop(self.min_heap)
            heappush(self.min_heap, med)
            return med
        else:
            med1 = heappop(self.min_heap)
            med2 = -heappop(self.max_heap)
            heappush(self.min_heap, med1)
            heappush(self.max_heap, -med2)
            return (med1+med2) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()