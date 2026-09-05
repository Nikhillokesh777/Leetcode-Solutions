class StockSpanner:

    def __init__(self):
        self.stack=[]
        

    def next(self, price: int) -> int:
        val = 1
        data =price
        while self.stack and self.stack[-1][0]<=data:
            val += self.stack.pop()[1]
        self.stack.append((data,val))
        return val        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)