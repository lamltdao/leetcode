class StockPrice:
    def __init__(self):
        self.latest_timestamp = None
        self.latest_price = None
        self.price = {} # time: price
        # note heapify only O(n)
        # pq {timestamp}, compared by price[timestamp]. price is updated => run heapify
        self.min_h = []
        self.max_h = []
        heapify(self.min_h)
        heapify(self.max_h)
        """
        update: O(n)
        current: O(1)
        max,min: O(log)
        """
    def update(self, timestamp: int, price: int) -> None:
        self.price[timestamp] = price
        heappush(self.min_h, (price, timestamp))
        heappush(self.max_h, (-price, timestamp))
        if self.latest_timestamp is None or timestamp >= self.latest_timestamp:
            self.latest_timestamp = timestamp
            self.latest_price = price
        
    def current(self) -> int:
        return self.latest_price

    def maximum(self) -> int:
        while True:
            max_ts_price, max_ts = heappop(self.max_h)
            max_ts_price = -max_ts_price
            if max_ts_price == self.price[max_ts]:
                heappush(self.max_h, (-max_ts_price, max_ts))
                return max_ts_price
        return None

    def minimum(self) -> int:
        while True:
            min_ts_price, min_ts = heappop(self.min_h)
            if min_ts_price == self.price[min_ts]:
                heappush(self.min_h, (min_ts_price, min_ts))
                return min_ts_price
        return None
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()