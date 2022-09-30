class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # dict {domain: # of visit}
        # for each cpdomain, extract each domain, update dict
        d = {}
        for cpd in cpdomains:
            arr = cpd.split(" ")
            num_visit, domain = int(arr[0]), arr[1]
            domain_arr = domain.split(".")
            tmp_d = ""
            for i in range(len(domain_arr)-1, -1,-1):
                if tmp_d == "":
                    tmp_d = domain_arr[i]
                else:
                    tmp_d = domain_arr[i] + "." + tmp_d
                if tmp_d not in d:
                    d[tmp_d] = 0
                d[tmp_d] += num_visit
        ans = []
        for domain in d.keys():
            ans.append(str(d[domain]) + " " + domain)
        return ans
        