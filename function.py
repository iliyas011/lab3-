#1
def my_function(grams):
    ounces= 28.3495231 * grams
    return ounces

grams= int(input())
print("#1")
print(my_function(grams))
#2
def tem(F):
    C = (5/9)*(F-32)
    return C
F=int(input())
print("#2")
print(tem(F))
#3
def solve(numheads , numlegs):
    for chickens in range(numheads + 1 ):
        rabbits = numheads - chickens
        if 4 * rabbits + 2 * chickens == numlegs:
            return chickens , rabbits 
        
    return None 
        
    
numheads = 35 
numlegs = 94
r = solve(numheads , numlegs)
if r:
    chickens , rabbits  = r 
    print(f" #3 chickens = {chickens} and rabbits = {rabbits}"  )
else :
    print("#3 None")
    
        
#4
def prime(n):
    if n < 2 :
        return False 
    for i in range(2 , int(n ** 0.5)+1):
        if n % 2 == 0:
            return False
    return True
def f(numbers):
    return [num for num in numbers if prime(num)]
numbers = list(map(int, input().split()))
p = f(numbers)
print("#4 {p}")

#5
def g(s, step=0):
    if step == len(s):
        print("#5".join(s))
    for i in range(step, len(s)):
        s1 = [c for c in s]
        s1[step], s1[i] = s1[i], s1[step]
        g(s1, step + 1)

u = list(input())
g(u)


#6
def w(sentence):
    return " ".join(sentence.split()[::-1])

user_input = input()
print("#6")
print(w(user_input))

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print("#7")
print(has_33([1, 3, 3]))  
print(has_33([1, 3, 1, 3]))  
print(has_33([3, 1, 3])) 

#8
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:  
            code.pop(0)  
        if not code: 
            return True
    return False  

print("#8")
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  

#9
def sv(radius):
    return (4/3) * 3.14 * (radius ** 3)


radius = float(input())
print("#9")
print( sv(radius))


#10
def ue(lst):
    ul = []
    for item in lst:
        if item not in ul:
            ul.append(item)
    return ul
il= list(map(int, input().split()))
print("#10")
print( ue(il))

#11
def ip(word):

    cw = ''.join(char.lower() for char in word if char.isalnum())
    return cw == cw[::-1]


us = input()
if ip(us):
    print("#11 palindrome")
else:
    print("#11 not a palindrome")
    
#12
def hm(items1):
    for item2 in items1:
        print('*' * item2)
        
user_input = input("#12 : ")
num12 = list(map(int, user_input.split()))  
hm(num12)
    
#13
def gn():
    print("Hello! What is your name?")
    name = input()
    
    print(f"Well, {name}, think of a number between 1 and 20 (only you know it).")
    snumber = int(input("Enter the number you thought of (1-20) for the game to work: "))  
    
    gt = 0  
    while True:
        print("Take a guess.")
        gq = int(input()) 
        gt += 1  
        
        if gq < snumber:
            print("Your guess is too low.")
        elif gq > snumber:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed the number in {gt} guesses!")
            break  


gn()




    
    


