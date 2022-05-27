- First parse numbers as well as operators and put them into an array called components
- Use a helper function (n1,n2,op) that evaluates n1 op n2, where op is +, -, or *
- Create a function (components, startIdx, endIdx) that returns an array of all possible results
- Then, for i in range(startIdx+1, endIdx):
        if components[i] is an operator:
            arr_1 = f(components, startIdx, i-1)
            arr_2 = f(components, i+1, endIdx)
            for n1 in arr_1:
                for n2 in arr_2:
                    final_ans.append(helper(n1,n2,components[i]))