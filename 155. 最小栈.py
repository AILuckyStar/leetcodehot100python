class MinStack:
    def __init__(self):
        self.stk=[]
        self.minstk=[float("inf")]
    def push(self,x):
        self.stk.append(x)
        self.minstk.append(min(x,self.minstk[-1]))
    def pop(self):
        self.stk.pop()
        self.minstk.pop()
    def top(self):
        return self.stk[-1]
    def getMin(self):
        return self.minstk[-1]
#貌似真考，不难记
