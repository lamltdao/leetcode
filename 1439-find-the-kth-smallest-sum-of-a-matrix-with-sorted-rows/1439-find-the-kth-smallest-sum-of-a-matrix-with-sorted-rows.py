from heapq import heapify, heappush, heappop
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        """
        Time: O(k * (log(min(200, n^m)) + m^2 * log(min(200, n^m)) ) = O(k * log(min(200, n^m) * (1 + m^2)) = O(k * log(min(200, n^m) * m^2)
        Space: O(min(200, n^m) * m)
        """
        nrow = len(mat)
        ncol = len(mat[0])
        tup = tuple([0 for _ in range(nrow)])
        arr_sum = sum(mat[i][0] for i in range(nrow))
        pq = [(arr_sum, tup)]
        heapify(pq)
        visited = set()
        visited.add(tup)
        while len(pq) > 0:
            summ, ar = heappop(pq)
            k -= 1
            if k == 0:
                return summ
            for i in range(len(ar)):
                if ar[i] + 1 < ncol:
                    new_arr = tuple([ar[j] if j != i else ar[j]+1 for j in range(len(ar))])
                    new_sum = summ - mat[i][ar[i]] + mat[i][new_arr[i]]
                    if new_arr not in visited:
                        visited.add(new_arr)
                        heappush(pq, (new_sum, new_arr))
        return -1