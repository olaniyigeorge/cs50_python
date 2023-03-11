import sys


class Jar:
    def __init__(self, capacity=12):

        if capacity == abs(capacity):
            self._capacity = capacity
        else:
            #return None
            raise ValueError("Capacity shouldn't be a negative number")
        
        self._size = 0


    def __str__(self):
        return f"{self.size * '🍪'}"


    def deposit(self, n):
        '''
        '''
        if n != abs(n):
            #return None
            raise ValueError("Input a positive number")
        if self.size + n > self.capacity:
            #return None
            raise ValueError("Deposit too high")
        else:
            self._size = self.size + n
            return self.size
            
        
    def withdraw(self, n):
        if n != abs(n):
            #return None
            raise ValueError("Input a positive number")
        if self.size - n < 0:
            #return None
            raise ValueError("You are trying to withdraw more than available")
        else:
            self._size = self.size - n
            return self.size

    

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
        


def main():
    j= Jar(10)

    print(j)
    print(j.size)
    print(j.capacity)

    print(j.deposit(-5))
    print(j.withdraw(2))
    print(j.size)


 
if __name__ == "__main__":
    main()