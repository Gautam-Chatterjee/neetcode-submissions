class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        span = 1
        idx = len(self.stack)-1

        while idx >= 0 and self.stack[idx] <= price:
            span+=1
            idx-=1
        self.stack.append(price)
        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)