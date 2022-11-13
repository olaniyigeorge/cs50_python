expression= input("Expression: ")

broken_up_expression= expression.split(" ")

""" if len(broken_up_expression) != 3:
    print("Expression not formatted properly.") """


if broken_up_expression[1] == "+":
    print(float(broken_up_expression[0]) + float(broken_up_expression[2]))
elif broken_up_expression[1] == "-":
    print(float(broken_up_expression[0]) - float(broken_up_expression[2]))
elif broken_up_expression[1] == "*":
    print(float(broken_up_expression[0]) * float(broken_up_expression[2]))
elif broken_up_expression[1] == "/":
    print(float(broken_up_expression[0]) / float(broken_up_expression[2]))
#else: 
    #print("Type in a valid arithmetic sign")
    