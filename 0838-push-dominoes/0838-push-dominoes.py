class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        dp_l[i] = 1 means being pushed left
        dp_r ... right
        right:
            loop from left to right
                if dom[i] == R
                    dp_r[i] = INF
                    j = 1
                    while arr[i+j] != "R":
                        dp_r[i+j] = INF-j
                        j += 1
        same for left
        
        for each dominos:
            if dp_l[i] > dp_r[i]:
                => L
            elif <:
                => R
            else:
                => .
                
            ".L.R...LR..L.."
        dp_l 
        INF-1,INF,0,INF-4,INF-3,INF-2,INF-1,INF,INF-3,INF-2,INF-1,INF,0,0
        dp_r 
        0,0,0,INF,INF-1,INF-2,INF-3,INF-4,INF,INF-1,INF-2,INF-3, 0, 0
        
        [L,L,0,R,R,0,L,L,R,R,L,L,0,0]
        """
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