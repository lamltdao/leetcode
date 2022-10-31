class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0 for _ in range(n)]
        tmp_force = 0
        for i in range(n):
            if dominoes[i] == "R":
                tmp_force = n
            elif dominoes[i] == "L":
                tmp_force = 0
            else:
                tmp_force = max(tmp_force-1, 0) # can't be neg
            forces[i] += tmp_force
        for i in range(n-1, -1, -1):
            if dominoes[i] == "L":
                tmp_force = n
            elif dominoes[i] == "R":
                tmp_force = 0
            else:
                tmp_force = max(tmp_force-1, 0) # can't be neg
            forces[i] -= tmp_force
        for i in range(len(forces)):
            if forces[i] > 0:
                forces[i] = "R"
            elif forces[i] < 0:
                forces[i] = "L"
            else:
                forces[i] = "."
        return ''.join(forces)