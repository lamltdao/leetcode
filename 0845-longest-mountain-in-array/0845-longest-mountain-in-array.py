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
            # currently increasing
            if is_inc == True:
                # still increasing
                if arr[i] > arr[i-1]:
                    num_inc += 1
                # change to decreasing. Update num_dec and is_inc. Keep is_inc the same
                elif arr[i] < arr[i-1]:
                    num_dec = 1
                    is_inc = False
                # equal. reset num_inc, num_dec to 0. Update is_inc
                else:
                    num_inc = num_dec = 0
                    is_inc = None
            # currently decreasing
            elif is_inc == False:
                # still decreasing
                if arr[i] < arr[i-1]:
                    num_dec += 1
                # change to increasing. Update num_inc and is_inc. Reset num_dec to 0, as the mountain is inc then dec, not dec then inc
                elif arr[i] > arr[i-1]:
                    num_inc = 1
                    is_inc = True
                    num_dec = 0 # reset
                else:
                    num_inc = num_dec = 0
                    is_inc = None
            # currently equal
            else:
                if arr[i] > arr[i-1]:
                    num_inc = 1
                    is_inc = True
                elif arr[i] < arr[i-1]:
                    num_dec = 1
                    is_inc = False
            # only consider if a mountain exists, i.e num_inc > 0 and num_dec > 0
            if num_inc > 0 and num_dec > 0:
                ans = max(ans, num_inc + num_dec+1)
        return ans
