"""
CTEC 121
Esther Pisano
Module 2 Programming Assignment
Applying what we have learned so far.
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""


def main():
    '''
# Section 1
    print("\n\n")
    # My string example
    MyPet = input("Enter a favorite animal or pet: ")
    print(MyPet)

    print("\n\n")
    # My integer example
    AnnualSalary = int(input("Enter your yearly salary: $"))
    print("$", AnnualSalary)

    print("\n\n")
    # My float example
    PieLeft = float(
        input("Enter how much of the pie is left (decimals are okay):"))
    print(PieLeft, "%")

# Section 2
    print("\n\n")
    # My end= example
    print("e.pisano", end='@')
    print("students.clark.edu")
    print("\n\n")
    '''

    import math
    '''
    # My sep= example
    n = eval(input("Enter any number here:"))
    print(3, n, 5, sep="+")
    total = (3 + n + 5)
    print("total:", total)

    print("\n\n")
# Section 5
    # My simultaneous assignment example
    i, ii = eval(input("Enter two numbers separated by a comma: "))
    print(i, ii)
    print()

    # My integer arithmetic examplesl
    print(5/2)
    print(5 % 2)
    print("\n\n")

    # My definite loops
    numbers = [1, 2, 3]
    for number in numbers:
        print(number)
    for i in range(0, 10):
        print(i)
    for i in range(11, 26, 3):
        print(i)
    '''
    '''
    # My use of math.n
    print(math.pi)
    print(math.sqrt(4))
    print(math.ceil(3.7))
    print(math.floor(3.3))
    print(3**2)
    print(3**3)
   
    a, b, c, d, e = input("Input five numbers seperated by a space:").split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    print(a+b+c+d+e)
    print(a**2 + b**2 + c**2 + d**2 + e**2)


# BONUS
    r = eval(input("input a number here:"))
    print((4/3) * math.pi * r ** 3)
    
    print("\n\n\n\n\n")

    r = eval(input("input a number here:"))
    A = (4 * math.pi * r**2)
    print(A)
    

    x1 = eval(input("x1: "))
    x2 = eval(input("x2: "))
    y1 = eval(input("y1: "))
    y2 = eval(input("y2: "))
    slope = (y2-y1)/(x2-x1)
    print("\n")
    print("Answer:", slope)
    

    a = eval(input("a: "))
    b = eval(input("b: "))
    c = eval(input("c: "))
    s = (a+b+c)/2
    print("Answer:", s)
    '''
    a = eval(input("a: "))
    b = eval(input("b: "))
    c = eval(input("c: "))
    s = (a+b+c)/2
    print(s)
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Answer:", A)


main()
