import turtle
q=turtle.Turtle()
q.speed(0)

def double():
    number=int(input("Enter a number and I will double it.: "))
    print(number*2)
    even_odd(number)

def even_odd(number):
    if number % 2 == 0:
        print("Your number is even.")
    else:
        print("Your number is odd.")
    square()

def square():
    length=int(input("Enter a length for your square.: "))
    for i in range(4):
        q.forward(length)
        q.right(90)
        
double()
