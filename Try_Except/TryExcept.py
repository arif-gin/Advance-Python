# try:
#     open("this.txt",'r')
# except Exception as e:
#     print(e)
# print("Program is running")

while (True):

    print("press q to quit")
    a = input("Enter a number:")
    if a == 'q':
        break
    try:
        a = int(a)
        if a > 6:
            print("You entered a number greater than 6")

    except Exception as e:
        print(f"Your input result in an error {e}")

print("thanks for playing this game")
