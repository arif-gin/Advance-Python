try:
    i=int(input("Enter a number:"))
    c=1/i
except Exception as e:
    print(e)
else:
    print("We were successful")

try:
    i=int(input("Enter a number:"))
    c=1/i
except Exception as e:
    print(e)
    exit()
finally:
    print("We were done")

print("Thanks for using the program")
