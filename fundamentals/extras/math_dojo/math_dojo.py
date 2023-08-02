class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for num in nums:
            self.result += num
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for num in nums:
            self.result -= num
        return self


# create an instance:
md = MathDojo()
# to test:
# x = md.add(2).add(2, 5, 1).subtract(3, 2).result
# print(x)
# should print 5
# run each of the methods a few more times and check the result!

y = md.add(5).add(3, 2, 8).add(5, 8, 3, 4).subtract(4, 2, 6).result
print(y)  # should print 26
