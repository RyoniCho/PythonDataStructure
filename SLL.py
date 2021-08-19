

class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
       

    pass


class SLL:
    def __init__(self) -> None:
        self.head=None
        self.length=0
        pass
    def Insert(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            currentNode=self.head
            while True:
                if currentNode.next ==None:
                    currentNode.next=newNode
                    break
                else:
                    currentNode=currentNode.next
        
        self.length+=1


        
        
        pass
    def RemoveAtIndex(self,index):
        
        if index>=self.length or index<0:
            return

        if self.head ==None:
            return
        #if Index is Head
        if index==0:
            self.head=self.head.next
        else:
            currentNode=self.head.next
            prevNode=self.head
            currentIndex=1
            while True:
                if currentIndex==index:
                    prevNode.next=currentNode.next
                    break

                prevNode=currentNode
                currentNode=currentNode.next
                currentIndex+=1


        pass
    def RemoveAtValue(self,data):
        if self.head ==None:
            return
       
        currentNode=self.head
        # if Value is HeadData
        if currentNode.data==data:
            self.head=currentNode.next
            return
        else:

            while True:
                prevNode=currentNode
                currentNode=currentNode.next
                if currentNode ==None:
                    break

                if currentNode.data==data:
                    prevNode.next=currentNode.next
                    break
           
        pass

    def Print(self):
        if self.head==None:
            return
        
        currentNode=self.head
        while True:
            print(currentNode.data)
            
            if currentNode.next==None:
                break

            currentNode=currentNode.next

            
        pass
    def Clear(self):
        self.head=None
        self.length=0
        pass


sll=SLL()

sll.Insert(44)
sll.Insert(55)
sll.Insert(53)
sll.Insert(2)
sll.Insert(5)

sll.Print()
print("="*40)

sll.RemoveAtIndex(3)

sll.RemoveAtValue(44)
sll.RemoveAtValue(53)
sll.RemoveAtValue(0)
sll.Print()
sll.Clear()
print("After clear")
sll.Print()
