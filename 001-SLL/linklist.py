class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next


class SLL:
    def __init__(self,start=None):
        self.start = start

    def is_empty(self):
        return self.start==None

    def insert_at_start(self,data):
        n = Node(data,self.start)
        self.start = n

    def insert_at_last(self,data):
        n = Node(data)

        if self.is_empty():
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n

    def inser_after(self,value,data):
        
        temp = self.start
        while temp is not None:
            if temp.item == value:
                n = Node(data,temp.next)
                temp.next = n
                break

            temp = temp.next
        

    











    def __iter__(self):
        return SLLIterator(self.start)

class SLLIterator:
    def __init__(self,start):
        self.current=start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
        



mylist=SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.inser_after(30,40)



for x in mylist:
    print(x,end=' ')

print()