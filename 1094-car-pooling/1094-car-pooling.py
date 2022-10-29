from heapq import heapify, heappush, heappop
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        sort trips by (trip[1], trip[2])
        pq (to, num_pass)
        when at idx i
        check each (to, num_pass) in deque. if to < i, cur_pass -= num_pass
        
        [,[9,1,7],[4,2,4],[9,3,4], [7,4,5]]
23

        1: 9
        2: 13
        3: 22
        4: 
        """
        trips.sort(key=lambda arr: (arr[1], arr[2]))
        pq = []
        heapify(pq)
        cur_pass = 0
        for i in range(len(trips)):
            num_pass, f, t = trips[i][0], trips[i][1], trips[i][2]
            # drop passenger off
            while len(pq) > 0:
                to, n_p = heappop(pq)
                if to <= f:
                    cur_pass -= n_p
                else:
                    heappush(pq, (to, n_p))
                    break
            # add passenger
            if cur_pass + num_pass > capacity:
                return False
            cur_pass += num_pass
            heappush(pq, (t, num_pass))
        return True