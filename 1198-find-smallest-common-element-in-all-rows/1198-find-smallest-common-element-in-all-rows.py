class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        intersect = set(mat[0])
        for i in range(1,len(mat)):
            intersect = intersect.intersection(set(mat[i]))
        return min(intersect) if len(intersect) > 0 else -1