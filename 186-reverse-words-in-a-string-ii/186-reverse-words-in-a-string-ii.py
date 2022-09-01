class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        c1:
            mark the left most word by 2 ptr, then shifting other chars to the left, moving that word at the current end
            O(len(s)^2)
        c2: 
        - reverse s 
        - reverse each word in reversed s
        """
        s.reverse()
        i = 0
        while i < len(s) and s[i] != ' ':
            j = i + 1
            while j < len(s) and s[j] != ' ':
                j += 1
            # reverse i:j
            s[i:j] = s[i:j][::-1]
            i = j+1
        
            
        