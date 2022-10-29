from heapq import heapify, heappush, heappop
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        sort trips by (trip[1], trip[2])
        pq (to, num_pass) min heap
        when at idx i
            pop (to, num_pass), cur_pass -= num_pass from pq as long as to < i
            if adding passenger at idx i does not exceed capa => update pq and cur_pass
            else:
                return False
        
        return True
        Time: O(nlogn), Space: O(n) for pq
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