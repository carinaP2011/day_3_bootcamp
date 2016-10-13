class BinarySearch():
    def __init__(self,a=10,b=1):
        self.listitems=[x for x in range(0,a,b)]
        self.length=a
        self.firstitem=0
        self.lastitem=self.length
        self.mid=self.firstitem +self.lastitem//2
        self.found=False
        self.counter=0
        self.dictvals=self.search(1)
    def binary_search(self,mylist):

        while self.firstitem  <= self.lastitem and not self.found:
            self.mid=self.firstitem+self.lastitem//2
            self.counter+=1
            if self.listitems[self.mid]==val:
                self.found = True
            else:
                if val<=self.listitems[self.mid]:
                    self.lastitem=self.mid
                    self.search(mylist)
                else:
                    self.firstitem=self.mid
                    self.search(mylist)

        return {'count':self.counter,'index':self.mid}
x=binary_search
print(x.dictvals)

import unittest
