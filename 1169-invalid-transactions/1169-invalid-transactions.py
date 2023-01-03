class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        {name: [(time, amount, city)]}
        """
        mapping = {}
        for t in transactions:
            name, time, amount, city = t.split(',')
            time = int(time)
            amount = int(amount)
            if name not in mapping:
                mapping[name] = []
            mapping[name].append((time, amount, city))
        invalid_trans = []
        for n in mapping.keys():
            for i in range(len(mapping[n])):
                time,amount,city = mapping[n][i]
                if amount > 1000:
                    invalid_trans.append(','.join([n, str(time), str(amount), city]))
                    continue
                for j in range(len(mapping[n])):
                    if j == i:
                        continue
                    time_j = mapping[n][j][0]
                    city_j = mapping[n][j][2]
                    if city != city_j and abs(time-time_j) <= 60:
                        invalid_trans.append(','.join([n, str(time), str(amount), city]))
                        break
        return invalid_trans