txt = "SIMPLE CALCULATOR"
align = txt.center(20)
print(align)

no1 = float(input("Enter first number: "))
op = input("Enter arithmetic operator : ")
no2 = float(input("Enter second number: "))


if op == "+":
    print(no1 + no2)
elif op == "-":
    print(no1 - no2)
elif op == "*":
    print(no1 * no2)
elif op == "/":
    print(no1/no2)
elif op =="**":
    print(no1**no2)
else:
    print("Invalid choice....")
