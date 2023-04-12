class Solution:
    def simplifyPath(self, path: str) -> str:
        can_path = []
        i = 0
        while i < len(path):
            if path[i] == '/':
                # read all /s
                while i < len(path) and path[i] == '/':
                    i += 1
            else: # get the path
                word_list = []
                while i < len(path) and path[i] != '/':
                    word_list.append(path[i])
                    i += 1
                w = ''.join(word_list)
                if w == '..':
                    if len(can_path) > 0:
                        can_path.pop()
                elif w != '.':
                    can_path.append(w)
        if len(can_path) == 0:
            return '/'
        ans = []
        for p in can_path:
            ans.append('/'+p)
        return ''.join(ans)
                