#1
class StringProcessor:
    def init(self):
        self.text = "" 

    def getString(self):
        self.text = input()  

    def printString(self):
        print(self.text.upper())  


if __name__ == "__main__":
    processor = StringProcessor() 
    processor.getString()  
    processor.printString() 
    
#2
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length * self.length


if __name__ == "__main__":
    shape = Shape()
    print("Shape area:", shape.area())
    
    square = Square(5)
    print("Square area:", square.area())
    
#3
class Shape:
    def __init__(self):
        pass 
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

rectangle = Rectangle(5, 10)
print("Area:", rectangle.compute_area())  

#4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


p1 = Point(3, 4)
p2 = Point(6, 8)
p1.show()
p2.show()
print("Distance:", p1.dist(p2))

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal failed! Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: {self.balance}")

account = Account("John Doe", 100)
account.deposit(50)      
account.withdraw(30)      
account.withdraw(200)  

#6 

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))


print("Prime numbers:", prime_numbers)
   


    
