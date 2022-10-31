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
        dp_l = [0 for _ in range(n)]
        dp_r = [0 for _ in range(n)]
        ans = [None for _ in range(n)]
        INF = n
        i = 0
        while i < n:
            if dominoes[i] == "R":
                dp_r[i] = INF
                j = 1
                while i+j < n and dominoes[i+j] != "R":
                    dp_r[i+j] = INF-j
                    if dominoes[i+j] == "L":
                        j += 1
                        break
                    j += 1
                i += j
            else:
                i += 1
        i = n-1
        while i >= 0:
            if dominoes[i] == "L":
                dp_l[i] = INF
                j = 1
                while i-j >= 0 and dominoes[i-j] != "L":
                    dp_l[i-j] = INF-j
                    if dominoes[i-j] == "R":
                        j += 1
                        break
                    j += 1
                i -= j
            else:
                i -= 1
        # print(dp_l)
        # print(dp_r)
        for i in range(n):
            if dp_l[i] < dp_r[i]:
                ans[i] = "R"
            elif dp_l[i] > dp_r[i]:
                ans[i] = "L"
            else:
                ans[i] = "."
        return ''.join(ans)
                
                