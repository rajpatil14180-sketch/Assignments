#TO CHECK THAT A STRING CONTAINS A CERTAIN SET OF CHARACTERS!!

str = input("Enter a string: ")

for i in str:
    if ('a' <= i <= 'z') or ('A' <= i <= 'Z') or ('0' <= i <= '9'):
        continue       
    else:
        print("INVALID")
        break

else:
    print("VALID")

