class Data(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next
        

class LinkedList(object):
    def __init__(self, *args):
        self.args = args
        self.tree = None
        self.len = 0
        
        for v in args:
            self.add(v)
        
        
    def add(self, value):
        if self.len == 0:
            self.tree = Data(value, self.tree)
        else:
            self.tree = Data(value, self.enum())
        
        self.len += 1
        
    
    def enum(self):
        step = 0;
        out = self.tree
        
        while self.len >= step:
            if(step == self.len):
                return out
                
            step += 1
            out = out.next
        
        
    def get(self, index):
        step = 0;
        out = self.tree
        
        while index >= step:
            if(step == index):
                return out.value
                
            step += 1
            out = out.next
        
if __name__ == '__main__':
    ll = LinkedList(1, 2, 3, 4, 5)
    ll.add(6)
    ll.add(7)
    print(ll.get(0))
