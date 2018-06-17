class Data(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next
        

class LinkedList(object):
    def __init__(self, *args):
        self.args = args
        self.tree = None
        self.lenth = 0
        self.num_iter = -1
        
        for v in args:
            self.add(v)


    def add(self, value):
        if self.lenth == 0:
            self.tree = Data(value, self.tree)
        else:
            self.enum(value)

        self.lenth += 1


    def enum(self, value, lenth=None, child=None):
        step = 1
        out = self.tree

        if not lenth:
            lenth = self.lenth
        
        while lenth >= step:
            if(step == lenth):
                out.next = Data(value, child)
                break
                
            step += 1
            out = out.next
        

    def get(self, index, obj=None):
        if index >= self.lenth:
            raise IndexError('index does not exist')

        step = 0
        out = self.tree
        
        while index >= step:
            if(step == index):
                if obj != None:
                    return out
                return out.value
                
            step += 1
            out = out.next


    def insert(self, index, value):
        if index >= self.lenth:
            self.add(value)
            return

        child = self.get(index, 1)
        self.enum(value, index, child)
        self.lenth += 1


    def remove(self, value):
        out = self.tree

        for k, v in enumerate(range(0, self.lenth, 1)):
            if out.value == value:
                child =  out.next
                out.value = child.value
                out.next = child.next
                self.lenth -= 1
                break

            out = out.next


    def remove_at(self, index):
        if index >= self.lenth:
            raise IndexError('index does not exist')

        out = self.tree

        for k, v in enumerate(range(0, self.lenth, 1)):
            if k == index:
                child = out.next
                this_value = out.value
                out.value = child.value
                out.next = child.next
                self.lenth -= 1
                return this_value

            out = out.next


    def clear(self):
        self.tree = None
        self.lenth = 0


    def contains(self, value):
        out = self.tree

        for k, v in enumerate(range(0, self.lenth, 1)):
            if out.value == value:
                return True
            out = out.next
        return False


    def len(self):
        return self.lenth


    def is_empty(self):
        if self.lenth == 0:
            return True
        return False


    def __iter__(self):
        return self


    def __next__(self):
        if self.num_iter >= self.lenth - 1:
            raise StopIteration
        self.num_iter += 1
        return self.get(self.num_iter)


class IndexError(Exception):
    pass
        
if __name__ == '__main__':
    ll = LinkedList(1, 2, 3, 4, 5)
    ll.add(6)
    ll.add(7)
    print(ll.get(6))
    ll.insert(7, 8)
    print(ll.get(7))
    ll.insert(9, 9)
    print(ll.get(8))
    ll.remove(2)
    print(ll.get(1))
    print(ll.remove_at(2))
    print(ll.get(2))
    ll.clear()
    ll.add(7)
    print(ll.get(0))
    print(ll.len())
    ll.clear()
    print(ll.is_empty())

    ll2 = LinkedList('item1', 'item2', 'item3')
    for item in ll2:
        print(item)