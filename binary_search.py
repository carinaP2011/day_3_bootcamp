class BinarySearch():
    def __init__(self,requiredlength=10,step=1):
        self.listitems=[x for x in range(0+step,requiredlength*step,step)]
        print(self.listitems)
        self.length=requiredlength
        #self.returndict=self.search(1)
        self.first=0
        self.last=self.length
        self.mid=(self.first+self.last)//2
        self.found=False
        self.counter=0
        self.dictvals=self.search(9)
    def search(self,val):
        #the binary search algorithm relies on having a sorted array of elements
        #return number of iterations and where the number was found
        while self.first<=self.last and not self.found:
            self.mid=(self.first+self.last)//2
            self.counter+=1
            if self.listitems[self.mid]==val:
                self.found = True
            else:
                if val<=self.listitems[self.mid]:
                    self.last=self.mid
                    self.search(val)#search the left half
                else:
                    self.first=self.mid
                    self.search(val)#search the right half

        return {'count':self.counter,'index':self.mid}
x=BinarySearch(20,2)
print(x.dictvals)
