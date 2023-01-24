#camrenn wallace-rivera
#

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    


def isPalindrome(s,word):

    for i in word:

        s.push(i)

    newWord=""

    while not s.isEmpty():

        newWord+=s.pop()

    return newWord==word


def main():

    s=Stack()
    
    print(isPalindrome(s,"duck"))
    
    print(isPalindrome(s,"radar"))


main()


