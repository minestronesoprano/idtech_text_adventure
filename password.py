def passes():
    print("THIS IS THE REAL STORY")


def failed():
    print("THIS IS THE fake STORY")


passed = False
password = input("Enter the password")

while not passed:
    if password == "123":
        passed = True
        passes()
        break
    else:
        failed()
        password = input()


