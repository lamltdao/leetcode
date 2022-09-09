class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        """
        hashmap content: [paths]
        """
        d = {}
        for p in paths:
            components = p.split(" ")
            directory = components[0] # without /
            for i in range(1, len(components)):
                file = components[i]
                file_name = []
                f_idx = 0
                while f_idx < len(file) and file[f_idx] != '(':
                    file_name.append(file[f_idx])
                    f_idx += 1
                file_name = ''.join(file_name)
                # f_idx points at (
                content = []
                while f_idx < len(file) and file[f_idx] != ')':
                    content.append(file[f_idx])
                    f_idx += 1
                content = ''.join(content)
                if content not in d:
                    d[content] = []
                d[content].append(directory+'/'+file_name)
        ans = []
        for content in d:
            if len(d[content]) > 1:
                ans.append(d[content])
        return ans
            