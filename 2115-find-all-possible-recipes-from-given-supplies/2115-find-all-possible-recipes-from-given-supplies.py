class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        u to v: u needs v as an ingredient
        graph = {u: [v]}
        
        check if we can make u:
        dfs(u)
            
        """
        graph = {}
        for s in supplies:
            graph[s] = []
        for i in range(len(recipes)):
            r = recipes[i]
            graph[r] = ingredients[i]
        
        recur = set()
        def can_make(r):
            if r not in graph:
                return False
            if r in recur:
                return False
            recur.add(r)
            for ing in graph[r]:
                if not can_make(ing):
                    return False
            recur.remove(r)
            return True
        ans = []
        for r in recipes:
            if can_make(r):
                ans.append(r)
        return ans