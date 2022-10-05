class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        m = max(damage)
        return sum(damage) - m + max(m - armor, 0) + 1