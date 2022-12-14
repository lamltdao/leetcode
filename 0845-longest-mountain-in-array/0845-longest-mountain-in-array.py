class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        """
        1 pass, O(1) space
        """
        if len(arr) < 3:
            return 0
        num_inc = num_dec = 0
        is_inc = True
        if arr[1] > arr[0]:
            num_inc = 1
        elif arr[1] < arr[0]:
            num_dec = 1
            is_inc = False
        else:
            is_inc = None
        ans = 0
        for i in range(2, len(arr)):
            if is_inc == True:
                if arr[i] > arr[i-1]:
                    num_inc += 1
                elif arr[i] < arr[i-1]:
                    num_dec = 1
                    is_inc = False
                else:
                    num_inc = num_dec = 0
                    is_inc = None
            elif is_inc == False:
                if arr[i] < arr[i-1]:
                    num_dec += 1
                elif arr[i] > arr[i-1]:
                    num_inc = 1
                    is_inc = True
                    num_dec = 0 # reset
                else:
                    num_inc = num_dec = 0
                    is_inc = None
            else:
                if arr[i] > arr[i-1]:
                    num_inc = 1
                    is_inc = True
                elif arr[i] < arr[i-1]:
                    num_dec = 1
                    is_inc = False
            if num_inc > 0 and num_dec > 0:
                ans = max(ans, num_inc + num_dec+1)
        return ans
