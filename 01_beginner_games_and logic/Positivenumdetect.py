a = int (input ("Enter first number:"))
b = int(input ("Enter second number:"))

if a > 0 and b > 0:
    print("a and b are both positive")
elif a > 0 or b > 0:
    print("Only one is positive")
else:
    print("neither is positive")
    