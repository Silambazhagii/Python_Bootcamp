try:
    num = int(input("Enter a num:"))
    print(10/num)

except ZeroDivisionError:
    print("OOPS")
    
finally:
    print("This runs no matter what.")