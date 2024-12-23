try:
    number=int(input("Enter the number"))
    print("The number is ", number)
except ValueError as ex:
    print("Exception",ex)