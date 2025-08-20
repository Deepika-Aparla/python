def tri(a,b,c):
    if (a+b>c) and (b+c>a) and (a+c>b):
        print("can form a triangle")
        if a == b == c:
            print("equilatoral triangle")
        elif a == b or b == c or c == a:
            print("isosceles triangle")
        elif (a**2)+(b**2) == (c**2) or (b**2)+(c**2) == (a**2) or (c**2)+(a**2) == (b**2):
            print("right angle triangle")
        else:
            print("scalene triangle")
    else:
        print("cannot form a triangle")

a=float(input("enter the first side"))
b=float(input("enter the second side"))
c=float(input("enter the third side"))
tri(a,b,c)

