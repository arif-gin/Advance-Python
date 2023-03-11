try:
    a=int(input("Enter a number:"))
    c=1/a
    print(c)

except ValueError as e:
    print("Exception1 occured ve")
    print(e)

except ZeroDivisionError as e:
    print("Exception2 occured zde")
    print(e)
print("thanks for using this code")


# def increment(num):
#     try:
#         return int(num)+1
#     except:
#         raise ValueError("This is not good-aarif")
# a=increment('ff 34')
# print(a)
