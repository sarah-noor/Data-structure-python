"""
LIFO -> Last in, first out

1. push
2. pop
3. display
4. isEmpty()
5. isFull()

"""

class Stack():
    """docstring for ClassName"""
    def __init__(self):
        super(Stack, self).__init__()
        self.TOP = -1
        self.MAX_LEN = 100
        self.mystack = []


    # Checking the stack 
    def isFull(self):
        if self.TOP == self.MAX_LEN:
            return True
        else:
            return False

    # function that check the stack that is empty or not
    def isEmpty(self):
        if self.TOP == -1:
            return True
        else:
            return False

    # a function that take a value and insert in the stack
    def push(self, value):
        if self.isFull():
            print("Stack is full !")
        else:
            self.TOP +=1
            self.mystack.append(value)

    # Function that remove the last inserted element
    def pop(self):

        if self.isEmpty():
            print("Stack is empty")
        else:
            self.TOP -=1

    # Desplay the elements stored in the stack
    def display(self):
        
        try:
            for value in self.mystack:
                print(value)
        except:
            print("Error")

if __name__ == "__main__":
    stack = Stack()
    stack.pop()
    stack.push(4)
    stack.display()